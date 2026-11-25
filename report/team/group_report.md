# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: HuuDuyenBL
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN và bảo vệ trước hội đồng Gate 2a. Cả nhóm chia 3 người: Người 1 viết code và tính toán, Người 2 kiểm số độc lập, kế hoạch pilot và gắn nhãn 1, Người 3 chỉ số, hồ sơ và gắn nhãn 2. Mỗi số của Người 1 được Người 2 tính lại bằng `src/kiem_so.py`.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- A, B: `src/lab13.py`, `report/team/bang_chi_phi.md` (A1 đạt 1,20 · 1,25 · 1,25; A2–A4, B1–B4).
- C: `report/team/bang_loi.md` (hai bộ nhãn độc lập, đồng thuận 17/20, bảng khắc phục 5 ca).
- D: `src/lab13.py` và `report/team/pilot_plan.yaml` (D1 đã chạy đạt kiểm tra 1.251, 859, 299; chọn 20 nhân viên mỗi nhóm, mức chênh 6 điểm, DE 6,96).
- E: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- Chi phí mỗi việc thành công 4.472 đ, gấp 16,3× hoá đơn token chia số yêu cầu; cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated].
- Pilot thu hẹp về `noi_dia` (0,22×) và `hang_nang` (0,69×); loại `quoc_te` (1,88×) và `doi_tac` (0,85×) [simulated].
- Yếu tố nhạy nhất: số ca làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%); xem lại 100% còn 0,98×–1,03× [simulated].
- Chỉ số đợt chạy thử: chính 82,83%, dùng 27,12%, an toàn 4,25%.
- Đề xuất cuối: **Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, 4 điều kiện có người phụ trách và ngày kiểm tra (xem `ho_so_launch_v0.md`). Kết quả duyệt chéo: chưa có.

## 5. Khó khăn và cách xử lý

- Dễ quên giờ nhân viên và chi phí cố định khi so với 12.000 đ: đã tính cả hệ thống và cộng cố định riêng.
- Hai bộ nhãn khác nhau ở 3 ca 6, 12, 17: thống nhất theo nguyên nhân gốc và ghi quy tắc phân biệt.
- Cỡ mẫu pilot: 40 nhân viên không đủ cho mức chênh 5 điểm; kế hoạch chọn 6 điểm, cần 299 yêu cầu/nhân viên và ghi rõ power khoảng 0,64 nếu tác động thật chỉ 5 điểm.
- Khi ghép CP4, tôi (Phạm Lý Ngọc Đức) gặp conflict do hai người cùng thêm code vào cuối `src/lab13.py`. Tôi giữ D1 của Người 2 và hàm tỉ lệ mở lại của mình, bỏ phần in trùng rồi chạy lại toàn bộ chương trình; commit xử lý là `6d0d673`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

Trong phần việc của tôi (Phạm Lý Ngọc Đức), tôi viết code A1–A4, B1–B4, tính tỉ lệ mở lại CP4, xử lý conflict khi ghép D1 và bổ sung ba chỉ số E1. Bằng chứng là các commit `7f611b5`, `3dc007e`, `3b46844`, `6d0d673`, `bc104f2` trong lịch sử `src/lab13.py`.

## 7. Hạn chế và hướng cải thiện

- Phần lớn con số phụ thuộc cột `_simulated`; cần thay bằng phút đo thật sau tuần đầu của pilot.
- Chưa có nhóm đối chứng trong đợt chạy thử nên không kết luận trợ lý nâng chỉ số.
- Ngưỡng chi phí 8.000 đ/việc trong luật dừng là suy ra từ dữ liệu mẫu, cần xác nhận.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, `NormalIndPower`
