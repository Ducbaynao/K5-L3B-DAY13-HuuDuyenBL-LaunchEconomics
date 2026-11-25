# Báo cáo cá nhân — Vũ Lương Duy-2A202603945

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Vũ Lương Duy
- MSSV: 2A202603945
- Email:
- Vai trong nhóm: Người 3 — chỉ số, tổng hợp hồ sơ, người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

Người 3: chỉ số, tổng hợp hồ sơ launch v0, gắn nhãn 2 (CP3), luật dừng và rollback (CP4), `chi_so.md`, `group_report.md`.

## 3. Đóng góp cụ thể

- CP3: gắn nhãn 20 ca lỗi; đồng thuận với Người 2 là 17/20 = 85%, lệch ở ca 6, 12, 17; soạn bảng khắc phục 5 ca đủ 5 loại, mỗi dòng có cách phát hiện đo được và một vai trò phụ trách.
- CP2: điền kết luận B4 (xem lại 100% cho 11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút; simulated).
- CP5: `chi_so.md` (chỉ số chính 82,83%, dùng 27,12%, an toàn 4,25%; 10 event có `trace_id`; 3 dòng rủi ro) và `ho_so_launch_v0.md` (7 mục).
- CP4: 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, rollback, owner, scope trong `pilot_plan.yaml`. Phần D1 (cỡ mẫu) do Người 2.

## 4. Bằng chứng

- Nhánh `nguoi3/cp3-gan-nhan`, PR #5 đã merge vào `main`.
- File: `report/team/bang_loi.md`, `chi_so.md`, `ho_so_launch_v0.md`, `pilot_plan.yaml`, `bang_chi_phi.md` (mục B4).
- Con số tự tính: ba chỉ số E1 tính từ `logix_requests.csv` (994/1.200, 48/177, 51/1.200).

## 5. Công cụ AI đã dùng

- Claude Code: hỗ trợ đọc đề, soạn các file hồ sơ, tính thử chỉ số, git (nhánh, commit, push). Tôi tự kiểm tra bằng cách chạy lại `src/lab13.py` và đối chiếu A1–B4 với bảng đáp án trong hướng dẫn, kiểm tra YAML bằng `yaml.safe_load`, và `grep` không còn `?` hay từ cấm.
- Lưu ý khi gắn nhãn CP3: hướng dẫn chi tiết có bảng nhãn tham khảo mà công cụ AI đã đọc trước khi gợi ý nhãn, nên bộ nhãn của tôi chưa phải hoàn toàn độc lập; tôi đã đọc lại 20 ca và đối chiếu từng nhãn trước khi chấp nhận.

## 6. Tự đánh giá

- Làm tốt: số liệu khớp đáp án, mọi số simulated có nhãn, vai trò phụ trách là một vai trò cụ thể.
- Chưa tốt: nhãn CP3 chưa độc lập hoàn toàn (xem mục 5); ngưỡng chi phí 8.000 đ/việc là mình tự suy từ 3.414 đ và 4.599 đ, cần nhóm xác nhận.
- Còn lại: `phieu_cham.md` chỉ điền sau duyệt chéo; đề xuất cuối cần cả nhóm thống nhất.
