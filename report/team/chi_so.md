# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được nhân viên mở bằng trợ lý | số yêu cầu có `agent_suggestion_shown` ÷ số yêu cầu của nhóm can thiệp, theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | số đơn có `so_tien_da_hoan` ≠ `so_tien_dung` ÷ số đơn kiểm mẫu (100 đơn/tuần) | Không cần tính |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng. Ba số trên lấy từ `logix_requests.csv`, tính bằng pandas với `keep_default_na=False`; không dựa vào cột `_simulated`.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | giu/sua/bo, phut_xem_lai (đo thật), trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

**Kiểm tra chéo:** mỗi chỉ số dưới đây tính được từ event trong danh sách.

- Chỉ số chính: `ticket_closed` (closed_at so với thời điểm `refund_request_created` ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, nối bằng `trace_id`.
- Chỉ số dùng (bỏ qua gợi ý): `staff_review_decision` với quyết định `sua` hoặc `bo`, chia số yêu cầu có `agent_suggestion_shown`.
- Chỉ số an toàn (lỗi lọt đến khách): `ticket_reopened` chia số `ticket_closed`.
- Chỉ số dùng tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` của nhóm can thiệp (thuộc tính `arm`).
- Chỉ số an toàn tự đề xuất: `audit_sample_checked` so sánh `so_tien_da_hoan` với `so_tien_dung`.
- Chi phí mỗi việc thành công: `agent_run_completed` (token, tool), `staff_review_decision` và `staff_rework_completed` (phút đo thật thay cho phút simulated).

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`), toàn bộ có phần simulated.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ/việc thành công [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi `noi_dia` + `hang_nang`, 48/982) | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× so với 12.000 đ (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated] | % yêu cầu được xem lại còn > 50% cuối bước rollout 0,25 (đợt chạy thử: 14,75%, 177/1.200) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa, tổng 5.784 đ = 0,48× [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
