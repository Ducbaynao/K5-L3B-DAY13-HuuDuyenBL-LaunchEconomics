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


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_a2(runs, reqs)
    in_a3(runs, reqs)
    in_a4(runs, reqs)
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
