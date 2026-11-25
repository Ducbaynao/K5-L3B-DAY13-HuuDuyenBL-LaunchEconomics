# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: HuuDuyenBL · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công, gấp 16,3× hoá đơn token chia số yêu cầu (274,7 đ). Trong phạm vi `noi_dia` + `hang_nang`: 3.414 đ, cộng cố định 40 triệu đ/tháng thành 4.599 đ (0,38×) ở 45.000 yêu cầu/tháng, 5.784 đ (0,48×) nếu còn một nửa khối lượng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8% khi gấp đôi) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1% khi tăng 25%). Giá token chỉ ±5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]. Thu hẹp `noi_dia` + `hang_nang`: 0,22× và 0,69×; loại `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×). Số bất lợi: xem lại 100% còn 0,98×–1,03× [simulated] | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính 82,83% (994/1.200) · Dùng, bỏ qua gợi ý 27,12% (48/177) · An toàn, mở lại 7 ngày 4,25% (51/1.200). Đây là số của đợt chạy thử, chưa có nhóm đối chứng; 10 event có `trace_id` (xem `chi_so.md`) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập, đồng thuận 17/20 = 85% (ca lệch 6, 12, 17 đã có quy tắc); 20 ca: 4 do người dùng, 5 hệ thống, 4 ngữ cảnh, 4 giới hạn, 3 ngầm; bảng khắc phục 5 ca đủ năm loại, mỗi dòng có event/ngưỡng và một vai trò (xem `bang_loi.md`) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20 (20 cụm mỗi nhóm), ngẫu nhiên phân tầng theo depot. 5 điểm cần 1.251/nhóm nhưng 20 người chỉ đạt tối đa 1.000 → chấp nhận mức chênh 6 điểm: 859/nhóm, ≥ 299 yêu cầu mỗi nhân viên, DE 6,96. Số bất lợi: power chỉ 0,64 nếu tác động thật là 5 điểm. 3 luật dừng (an toàn, chi phí, mức dùng); quyết định 2027-01-11 (xem `pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,8%) · xem lại 100% kéo dài: 11.743 đ (0,98×) · khối lượng còn một nửa: cố định +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

### Đề xuất của nhóm

- Lý do: trong phạm vi, chi phí mỗi việc thành công là 0,22× (`noi_dia`) và 0,69× (`hang_nang`) so với 12.000 đ, cộng cố định 40 triệu đ/tháng vẫn 0,38× [simulated]; đã loại `quoc_te` (1,88×) và `doi_tac` (0,85×); có 3 luật dừng và rollback 30 phút.
- Con số bất lợi và cách xử lý: xem lại 100% chỉ còn 0,98×–1,03× [simulated] → điều kiện 4; pilot chỉ phát hiện được mức chênh 6 điểm, power 0,64 nếu tác động thật là 5 điểm → điều kiện 2; chi phí nhân viên đang là số giả lập → điều kiện 3.

| # | Điều kiện | Người phụ trách | Ngày kiểm tra |
| --: | --- | --- | --- |
| 1 | Sửa khoá chống trùng và đối soát sổ cái mỗi giờ (ca 7, 20), ngưỡng 0 ca hoàn trùng | Kỹ sư trưởng agent | Trước 2026-12-07 |
| 2 | Ký chấp nhận mức chênh 6 điểm (power 0,64 ở mức 5 điểm) | Giám đốc vận hành LogiX-VN | Trước 2026-12-07 |
| 3 | Bật đủ 10 event có `trace_id`; thay phút xem lại, làm lại simulated bằng phút đo thật | PM trợ lý hoàn phí | 2026-12-14 (hết tuần 1) |
| 4 | Kế hoạch giảm xem lại theo bậc, mỗi lần xem lại ≤ 5 phút (hoà vốn B4: 5,1 phút) | Trưởng nhóm CSKH | 2026-12-21 (hết bước rollout 0,25) |

Nếu đến 2026-12-07 chưa xong điều kiện 1 và 2 thì lùi ngày bắt đầu, không chạy pilot.

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang` (chia theo nhân viên 20 + 20, bắt đầu 2026-12-07, quyết định 2027-01-11).
