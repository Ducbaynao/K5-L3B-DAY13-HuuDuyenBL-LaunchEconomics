"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs thuộc reqs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def in_a2(runs, reqs):
    """In bảng A2 (9 dòng) và các chỉ số đối chiếu so với nhân viên tự làm."""
    ket_qua = mo_hinh(runs, reqs)
    tong_tool_calls = runs['tool_calls'].sum()
    phut_xem_lai = reqs['phut_xem_lai_simulated'].sum()
    phut_lam_lai = reqs['phut_lam_lai_simulated'].sum()
    khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
    ca_he_thong_moi_yc = (ket_qua['tong'] + khong_thanh_cong * BASELINE) / len(reqs)

    print('\n=== A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    print(f"{'token':16s} {ket_qua['token']:>14,.0f}")
    print(f"{'tool':16s} {ket_qua['tool']:>14,.0f}  ({tong_tool_calls:,} lan goi)")
    print(f"{'chay_lai':16s} {ket_qua['chay_lai']:>14,.0f}")
    print(f"{'xem_lai [simulated]':22s} {ket_qua['xem_lai']:>14,.0f}  ({phut_xem_lai:,.0f} phut)")
    print(f"{'lam_lai [simulated]':22s} {ket_qua['lam_lai']:>14,.0f}  ({phut_lam_lai:,.0f} phut)")
    print(f"{'tong [simulated]':22s} {ket_qua['tong']:>14,.0f}")
    print(f"{'thanh_cong':16s} {ket_qua['thanh_cong']:>14,.0f}")
    print(f"{'cps [simulated]':22s} {ket_qua['cps']:>14,.0f}")
    print(f"{'hoa_don_moi_yc':16s} {ket_qua['hoa_don_moi_yc']:>14,.1f}")
    print(
        f"[simulated] Gap hoa don: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f}x | "
        f"Ty trong lam_lai: {ket_qua['lam_lai'] / ket_qua['tong'] * 100:.1f}% | "
        f"xem_lai: {ket_qua['xem_lai'] / ket_qua['tong'] * 100:.1f}%"
    )
    print(
        f"Chi phi ca he thong [simulated]: {ca_he_thong_moi_yc:,.0f} d/yc "
        f"({ca_he_thong_moi_yc / BASELINE:.2f}x cua {BASELINE:,} d; "
        f"cong {khong_thanh_cong} ca khong thanh cong x {BASELINE:,} d)"
    )
    return ket_qua


def in_a3(runs, reqs):
    """In bảng A3 theo từng loại yêu cầu và tỉ lệ status == 'ok' theo loại và attempt."""
    print('\n=== A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    cac_loai = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
    for loai in cac_loai:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        so_yc = len(sub)
        ty_le_tc = kq['thanh_cong'] / so_yc * 100
        lan_chay_yc = sub['so_lan_chay'].mean()
        so_voi_baseline = kq['cps'] / BASELINE
        print(
            f"{loai:10s} | yc={so_yc:4d} | tc={ty_le_tc:5.1f}% | "
            f"chay/yc={lan_chay_yc:4.2f} | cps[simulated]={kq['cps']:>7,.0f} d | "
            f"vs_12k={so_voi_baseline:.2f}x"
        )

    print('\n=== A3 · TỈ LỆ STATUS == OK THEO LOẠI VÀ ATTEMPT ===')
    bang_ok = (
        runs.merge(reqs[['request_id', 'loai']], on='request_id')
        .assign(ok=lambda d: d['status'] == 'ok')
        .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
        .reindex(cac_loai)
    )
    print((bang_ok * 100).round(1).to_string())


def in_a4(runs, reqs, chi_phi_co_dinh=40_000_000, khoi_luong_thang=45_000):
    """Tính chi phí cố định phân bổ cho phạm vi noi_dia + hang_nang ở quy mô đầy đủ và 1/2 khối lượng."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    ty_le_tc_trong_mau = kq_pv['thanh_cong'] / len(reqs)

    print('\n=== A4 · CHI PHÍ CỐ ĐỊNH (PHẠM VI noi_dia + hang_nang) ===')
    print(
        f"Pham vi co {len(pham_vi)} yc, trong do {kq_pv['thanh_cong']} thanh cong "
        f"({kq_pv['thanh_cong'] / len(pham_vi) * 100:.2f}% trong pham vi)."
    )
    print(
        f"Ti le viec thanh cong trong pham vi tren TOAN BO mau: "
        f"{kq_pv['thanh_cong']}/{len(reqs)} = {ty_le_tc_trong_mau * 100:.2f}% "
        f"(dung de quy doi tu tong luong yc toan cong ty). "
        f"Tong[simulated]={kq_pv['tong']:,.0f} d, cps[simulated]={kq_pv['cps']:,.0f} d"
    )
    for nhan, he_so in [('Quy mo day du (45.000 yc/thang)', 1.0), ('Mot nua khoi luong (22.500 yc/thang)', 0.5)]:
        kl = khoi_luong_thang * he_so
        viec_tc_thang = kl * ty_le_tc_trong_mau
        co_dinh_moi_viec = chi_phi_co_dinh / viec_tc_thang
        tong_cps = kq_pv['cps'] + co_dinh_moi_viec
        print(
            f"{nhan:38s} | viec_tc={viec_tc_thang:>8,.0f} | "
            f"co_dinh={co_dinh_moi_viec:>6,.0f} d | "
            f"tong_cps[simulated]={tong_cps:>6,.0f} d ({tong_cps / BASELINE:.2f}x)"
        )


def in_b1(runs, reqs):
    """In bảng độ nhạy B1 cho 9 kịch bản đơn lẻ."""
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Gia token gap doi': dict(gia_vao=52, gia_ra=260),
        'Gia token giam mot nua': dict(gia_vao=13, gia_ra=65),
        'Xem lai gap doi': dict(he_so_xem_lai=2),
        'Xem lai giam mot nua': dict(he_so_xem_lai=0.5),
        'Lam lai gap doi': dict(he_so_lam_lai=2),
        'Lam lai giam mot nua': dict(he_so_lam_lai=0.5),
        'Luong tang 25%': dict(luong_phut=2500),
        'Toi da 2 lan chay': dict(max_lan_chay=2),
        'Chi 1 lan chay': dict(max_lan_chay=1),
    }
    print('\n=== B1 · BẢNG ĐỘ NHẠY (9 KỊCH BẢN) ===')
    print(f"{'Goc (A2) [simulated]':28s} {goc:>8,.0f} d")
    ket_qua_b1 = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1) * 100
        ket_qua_b1[ten] = (cps, pct)
        print(f"{ten + ' [simulated]':28s} {cps:>8,.0f} d ({pct:+6.1f}%)")
    return goc, ket_qua_b1


def in_b2(runs, reqs, goc, ket_qua_b1):
    """In B2: kết hợp giá token gấp đôi + xem lại gấp đôi và xếp hạng 3 yếu tố mạnh nhất."""
    cps_ket_hop = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    pct_ket_hop = (cps_ket_hop / goc - 1) * 100
    pct_tok2 = ket_qua_b1['Gia token gap doi'][1]
    pct_xem2 = ket_qua_b1['Xem lai gap doi'][1]

    print('\n=== B2 · KẾT HỢP VÀ XẾP HẠNG YẾU TỐ ===')
    print(
        f"Ket hop (token x2 + xem lai x2) [simulated]: {cps_ket_hop:,.0f} d ({pct_ket_hop:+.1f}%) | "
        f"Tong 2 tac dong rieng: {pct_tok2:+.1f}% + {pct_xem2:+.1f}% = {pct_tok2 + pct_xem2:+.1f}%"
    )
    print(
        "[simulated] Xep hang theo muc thay doi CPS trong cac kich ban B1 da thu: "
        f"1. So ca lam lai ({ket_qua_b1['Lam lai gap doi'][1]:+.1f}% / {ket_qua_b1['Lam lai giam mot nua'][1]:+.1f}%), "
        f"2. Ti le xem lai ({ket_qua_b1['Xem lai gap doi'][1]:+.1f}% / {ket_qua_b1['Xem lai giam mot nua'][1]:+.1f}%), "
        f"3. Luong nhan vien ({ket_qua_b1['Luong tang 25%'][1]:+.1f}% khi +25%)."
    )


def in_b3(runs, reqs):
    """In B3: so sánh giới hạn 1, 2, 3 lần chạy theo tổng chi phí hệ thống và CPS."""
    print('\n=== B3 · SO SÁNH GIỚI HẠN 1, 2, 3 LẦN CHẠY ===')
    cac_muc = []
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        ca_he_thong = kq['tong'] + khong_tc * BASELINE
        cac_muc.append((k, kq['tong'], khong_tc, ca_he_thong, kq['cps']))
        print(
            f"Gioi han {k} lan | tong[simulated]={kq['tong']:>10,.0f} d | "
            f"khong_tc={khong_tc:>3d} | ca_he_thong[simulated]={ca_he_thong:>10,.0f} d | "
            f"cps[simulated]={kq['cps']:>6,.0f} d"
        )
    re_nhat_ht = min(cac_muc, key=lambda x: x[3])
    thap_nhat_cps = min(cac_muc, key=lambda x: x[4])
    print(
        f"Re nhat cho cong ty (ca he thong): {re_nhat_ht[0]} lan ({re_nhat_ht[3]:,.0f} d [simulated]); "
        f"CPS thap nhat: {thap_nhat_cps[0]} lan ({thap_nhat_cps[4]:,.0f} d [simulated]). "
        f"Trung nhau: {'Co' if re_nhat_ht[0] == thap_nhat_cps[0] else 'Khong'}."
    )


def in_b4(runs, reqs):
    """In B4: xem lại 100% yêu cầu trong phạm vi noi_dia + hang_nang."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ok_ids = set(runs.loc[runs['status'] == 'ok', 'request_id'])
    so_co_ok = int(pham_vi['request_id'].isin(ok_ids).sum())
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    so_thanh_cong = int((pham_vi['ket_qua'] == 'thanh_cong').sum())

    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    chi_phi_agent = (
        runs_pv['tokens_in'] / 1000 * GIA_VAO
        + runs_pv['tokens_out'] / 1000 * GIA_RA
        + runs_pv['tool_calls'] * GIA_TOOL
    ).sum()

    xem_lai_100 = so_co_ok * 5 * LUONG_PHUT
    all_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    tb_lam_lai = all_lam_lai.mean()
    med_lam_lai = all_lam_lai.median()

    print('\n=== B4 · XEM LẠI 100% (PHẠM VI noi_dia + hang_nang) ===')
    print(
        f"Pham vi: {len(pham_vi)} yc | co >=1 lan ok: {so_co_ok} | "
        f"lam_lai: {so_lam_lai} | thanh_cong: {so_thanh_cong} | "
        f"token+tool: {chi_phi_agent:,.0f} d | xem_lai_100 (5p/ca ok) [simulated]: {xem_lai_100:,.0f} d"
    )
    print(
        f"Thoi gian lam lai gia lap trong mau (toan bo ca lam_lai): "
        f"trung binh {tb_lam_lai:.1f} phut/ca, trung vi {med_lam_lai:.1f} phut/ca [simulated]."
    )
    print("B4 giu nguyen 900 viec thanh cong theo du lieu mau; chua cong chi phi co dinh "
          "va phan nhan vien tiep nhan yeu cau khong thanh cong.")
    for nhan, phut_lam_lai in [('Gia dinh de (9 phut/ca)', 9.0), (f'Trung binh du lieu ({tb_lam_lai:.1f} phut/ca)', tb_lam_lai)]:
        lam_lai_cost = so_lam_lai * phut_lam_lai * LUONG_PHUT
        tong = chi_phi_agent + xem_lai_100 + lam_lai_cost
        cps = tong / so_thanh_cong
        hoa_von_xem = (so_thanh_cong * BASELINE - chi_phi_agent - lam_lai_cost) / (so_co_ok * LUONG_PHUT)
        print(
            f"{nhan:34s} | lam_lai[simulated]={lam_lai_cost:>9,.0f} d | "
            f"tong[simulated]={tong:>10,.0f} d | cps[simulated]={cps:>6,.0f} d ({cps / BASELINE:.2f}x) | "
            f"hoa von CPS xem lai <= {hoa_von_xem:.1f} phut [simulated]"
        )
        print(
            f"[simulated] CPS {'thap' if cps < BASELINE else 'cao'} hon baseline "
            f"{abs(cps / BASELINE - 1) * 100:.1f}%; "
            f"{'gan nhu khong con tiet kiem' if cps < BASELINE else 'vuot baseline'} "
            "khi xem lai 100%."
        )


def in_ty_le_mo_lai(reqs):
    """Tính số ca mở lại, tổng yêu cầu và tỉ lệ mo_lai_trong_7_ngay trên toàn mẫu và phạm vi pilot."""
    print('\n=== CP4 (NGƯỜI 1) · TỈ LỆ MỞ LẠI TRONG 7 NGÀY ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    for nhan, df in [('Toan mau', reqs), ('Pham vi (noi_dia + hang_nang)', pham_vi)]:
        so_mo_lai = int((df['mo_lai_trong_7_ngay'] == 1).sum())
        tong_yc = len(df)
        ty_le = df['mo_lai_trong_7_ngay'].mean() * 100
        print(f"{nhan:32s}: {so_mo_lai}/{tong_yc:,} = {ty_le:.2f}%")


# ---------- Nhiệm vụ D1 · Cỡ mẫu (Người 2) ----------
from statistics import NormalDist


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức trong docs/du_lieu_va_cong_thuc.md)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def power_hai_ti_le(p1, p2, n, alpha=0.05):
    """Power khi mỗi nhóm có n mẫu hiệu dụng (đảo công thức co_mau)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    pb = (p1 + p2) / 2
    z = (abs(p2 - p1) * math.sqrt(n) - za * math.sqrt(2 * pb * (1 - pb))) / math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return NormalDist().cdf(z)


def in_d1(baseline=0.70, icc=0.02, so_nhan_vien=40):
    print('\n=== D1 · CỠ MẪU (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    n5 = co_mau(baseline, baseline + 0.05)
    print(f"a) Chia theo yeu cau: {n5:,} yc moi nhom")

    m = 75
    de = 1 + (m - 1) * icc
    n_b = math.ceil(n5 * de)
    nv_b = math.ceil(n_b / m)
    print(f"b) Theo nhan vien, m={m}: DE={de:.2f}, n={n_b:,} moi nhom -> {nv_b} nguoi/nhom, "
          f"tong {2 * nv_b} > {so_nhan_vien}: {'du' if 2 * nv_b <= so_nhan_vien else 'KHONG du nguoi'}")

    tran_c = 20 / icc
    print(f"c) 20 nhan vien/nhom: n hieu dung toi da c/ICC = {tran_c:,.0f} "
          f"{'>=' if tran_c >= n5 else '<'} {n5:,}: {'dat' if tran_c >= n5 else 'KHONG dat'}")
    print(f"d) 6 depot/nhom: n hieu dung toi da = {6 / icc:,.0f}")

    n6 = co_mau(baseline, baseline + 0.06)
    # 20m / (1 + (m-1)·ICC) >= n6  ->  m >= n6·(1-ICC) / (20 - n6·ICC)
    m_e = math.ceil(n6 * (1 - icc) / (20 - n6 * icc))
    de_e = 1 + (m_e - 1) * icc
    print(f"e) Muc chenh 6 diem: {n6:,} moi nhom; 20 nguoi/nhom -> m >= {m_e} yc moi nguoi (DE={de_e:.2f})")
    print(f"   Danh doi: neu tac dong that chi 5 diem, power voi n={n6} chi con "
          f"{power_hai_ti_le(baseline, baseline + 0.05, n6):.2f}")
    return dict(n5=n5, n6=n6, m_e=m_e, de_e=de_e)




def in_e1(reqs):
    """Tính và in 3 chỉ số E1 trên mẫu chạy thử (dữ liệu giả lập, không có nhóm đối chứng)."""
    tong_yc = len(reqs)
    chinh_tu = int(((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum())
    chinh_tl = chinh_tu / tong_yc * 100

    xem = reqs[reqs['duoc_xem_lai'] == 1]
    xem_mau = len(xem)
    dung_tu = int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())
    dung_tl = dung_tu / xem_mau * 100

    an_toan_tu = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    an_toan_tl = an_toan_tu / tong_yc * 100

    print('\n=== E1 · BA CHỈ SỐ MẪU CHẠY THỬ (GIẢ LẬP, KHÔNG ĐỐI CHỨNG) ===')
    print(f"Chi so chinh (dong <=24h & khong mo lai 7 ngay): {chinh_tu}/{tong_yc:,} = {chinh_tl:.2f}%")
    print(f"Chi so dung - bo qua goi y (sua + bo / duoc xem lai): {dung_tu}/{xem_mau:,} = {dung_tl:.2f}%")
    print(f"Chi so an toan - mo lai trong 7 ngay: {an_toan_tu}/{tong_yc:,} = {an_toan_tl:.2f}%")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_a2(runs, reqs)
    in_a3(runs, reqs)
    in_a4(runs, reqs)
    goc_cps, ket_qua_b1 = in_b1(runs, reqs)
    in_b2(runs, reqs, goc_cps, ket_qua_b1)
    in_b3(runs, reqs)
    in_b4(runs, reqs)
    d1 = in_d1()
    assert (d1['n5'], d1['n6'], d1['m_e']) == (1251, 859, 299), d1  # số đối chiếu D1
    in_ty_le_mo_lai(reqs)
    in_e1(reqs)
