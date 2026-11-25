"""Kiểm số CP1 (Người 2): tính độc lập với lab13.py để đối chiếu A1–A4.
Chạy trong src/: python kiem_so.py. Số từ cột _simulated là giả lập.
"""
import pandas as pd

runs = pd.read_csv('logix_runs.csv')
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

# A1 · tính trực tiếp bằng tổng chuỗi, không dùng công thức đóng, để kiểm chéo
def e_lan_chay(p, k):  # sum_{i=1..k} P(cần tới lần i) = sum (1-p)^(i-1)
    return sum((1 - p) ** (i - 1) for i in range(1, k + 1))

a1 = [e_lan_chay(0.8, 2), e_lan_chay(0.8, 10_000), e_lan_chay(0.8, 3) / (1 - 0.2 ** 3)]
assert all(abs(x - y) < 1e-9 for x, y in zip(a1, [1.20, 1.25, 1.25])), a1
print('A1:', [round(x, 2) for x in a1])

# A2 · cộng tay từng khoản
def tinh(rq):
    r = runs[runs.request_id.isin(rq.request_id)]
    token = (r.tokens_in * 26 / 1000 + r.tokens_out * 130 / 1000)
    tool = r.tool_calls * 15
    xem = rq.phut_xem_lai_simulated.sum() * 2000
    lam = rq.phut_lam_lai_simulated.sum() * 2000
    tong = token.sum() + tool.sum() + xem + lam
    tc = (rq.ket_qua == 'thanh_cong').sum()
    return dict(token=token.sum(), tool=tool.sum(), so_tool=r.tool_calls.sum(),
                lan2_3=(token + tool)[r.attempt > 1].sum(),
                phut_xem=rq.phut_xem_lai_simulated.sum(), xem=xem,
                phut_lam=rq.phut_lam_lai_simulated.sum(), lam=lam,
                tong=tong, tc=tc, cps=tong / tc, lan_chay=len(r),
                hoa_don=(token.sum() + tool.sum()) / len(rq))

g = tinh(reqs)
print('\nA2')
for k, v in g.items():
    print(f'  {k:10s} {v:>14,.1f}')
print(f'  gấp {g["cps"] / g["hoa_don"]:.1f} lần hoá đơn; làm lại {g["lam"] / g["tong"]:.1%}, '
      f'xem lại {g["xem"] / g["tong"]:.1%}, giờ nhân viên {(g["xem"] + g["lam"]) / g["tong"]:.1%}')
khong_tc = (reqs.ket_qua != 'thanh_cong').sum()
print(f'  cả hệ thống/yêu cầu: {(g["tong"] + khong_tc * 12000) / len(reqs):,.0f} đ ({khong_tc} ca không thành công)')

print('\nA3  loai       n   tỉ lệ TC  lần chạy/yc   cps      ×12000')
for loai, rq in reqs.groupby('loai'):
    t = tinh(rq)
    print(f'    {loai:9s} {len(rq):4d}  {t["tc"] / len(rq):7.1%}  {t["lan_chay"] / len(rq):8.2f}  '
          f'{t["cps"]:8,.0f}  {t["cps"] / 12000:5.2f}×')

ok_theo_lan = runs.merge(reqs[['request_id', 'loai']]).assign(ok=lambda d: d.status == 'ok') \
    .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
print('\n  Tỉ lệ ok theo lần thử:\n', (ok_theo_lan * 100).round(1))

# A4 · phạm vi noi_dia + hang_nang, cộng 40 triệu/tháng
pv = tinh(reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])])
print('\nA4')
for ten, kl in [('45.000 yc/tháng', 45_000), ('một nửa', 22_500)]:
    tc_thang = kl * pv['tc'] / len(reqs)
    co_dinh = 40_000_000 / tc_thang
    print(f'  {ten:16s} TC/tháng {tc_thang:8,.0f}  cố định/việc {co_dinh:6,.0f}  '
          f'cps+cố định {pv["cps"] + co_dinh:6,.0f}  {(pv["cps"] + co_dinh) / 12000:.2f}×')
print(f'  (cps trong phạm vi chưa cộng cố định: {pv["cps"]:,.0f} đ, {pv["tc"]} việc thành công)')


# ---------- CP2 · B · tính độc lập, không gọi mo_hinh ----------
def cps_b(gia_vao=26, gia_ra=130, he_xem=1.0, he_lam=1.0, luong=2000, k=None):
    """Trả (tổng trợ lý, số thành công, cps). k = giới hạn số lần chạy."""
    r = runs if k is None else runs[runs.attempt <= k]
    giu = reqs if k is None else reqs[reqs.so_lan_chay <= k]  # vượt k: chuyển nhân viên, 0 phút
    tong = ((r.tokens_in * gia_vao + r.tokens_out * gia_ra) / 1000 + r.tool_calls * 15).sum() \
        + giu.phut_xem_lai_simulated.sum() * luong * he_xem \
        + giu.phut_lam_lai_simulated.sum() * luong * he_lam
    tc = (giu.ket_qua == 'thanh_cong').sum()
    return tong, tc, tong / tc

goc = cps_b()[2]
kb = {
    'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260), 'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
    'Xem lại gấp đôi': dict(he_xem=2), 'Xem lại giảm một nửa': dict(he_xem=0.5),
    'Làm lại gấp đôi': dict(he_lam=2), 'Làm lại giảm một nửa': dict(he_lam=0.5),
    'Lương tăng 25%': dict(luong=2500), 'Tối đa 2 lần chạy': dict(k=2), 'Chỉ 1 lần chạy': dict(k=1),
}
print(f'\nB1  gốc {goc:,.0f} đ')
pct = {}
for ten, kw in kb.items():
    c = cps_b(**kw)[2]
    pct[ten] = (c / goc - 1) * 100
    print(f'  {ten:24s} {c:7,.0f}  {pct[ten]:+6.1f}%')
for a in ('Giá token', 'Xem lại', 'Làm lại'):  # giảm nửa = −½ gấp đôi
    assert abs(pct[f'{a} giảm một nửa'] + pct[f'{a} gấp đôi'] / 2) < 1e-6, a
print('  Tự kiểm tra: giảm một nửa = −½ gấp đôi: ĐẠT')

c2 = cps_b(gia_vao=52, gia_ra=260, he_xem=2)[2]
print(f'\nB2  token×2 + xem lại×2: {c2:,.0f} đ ({(c2 / goc - 1) * 100:+.1f}%), '
      f'tổng riêng {pct["Giá token gấp đôi"] + pct["Xem lại gấp đôi"]:+.1f}%')

print('\nB3  k  tổng trợ lý   không TC   cả hệ thống     cps')
for k in (1, 2, 3):
    tong, tc, c = cps_b(k=k)
    ktc = len(reqs) - tc
    print(f'    {k}  {tong:11,.0f}  {ktc:6d}  {tong + ktc * 12000:12,.0f}  {c:6,.0f}')
