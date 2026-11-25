# Báo cáo cá nhân — Nguyễn Huy Tấn-2A202603925

## 1. Thông tin thành viên

- Họ tên: Nguyễn Huy Tấn
- MSSV: 2A202603925
- Email:
- Vai trong nhóm: Người 2 — người kiểm số, người gắn nhãn 1, phụ trách kế hoạch pilot (D1)

## 2. Phần việc phụ trách

Người 2: kiểm số A–B độc lập với code của Người 1 và điền `bang_chi_phi.md` (A1–A4, B1–B3); gắn nhãn 1 ở CP3; viết code D1 và điền `pilot_plan.yaml` ở CP4; rà công thức chỉ số và rủi ro ở CP5.

## 3. Đóng góp cụ thể

- CP1: viết `src/kiem_so.py` tính lại A1–A4 không dùng `mo_hinh`. Tính tay khoản token trên cả 1.624 lần chạy = 245.585 đ; mẫu số 978 việc thành công. Khớp `lab13.py` của Người 1: 4.472 đ/việc thành công, gấp 16,3 lần hoá đơn 274,7 đ [simulated].
- CP2: thêm phần B vào `kiem_so.py`, có tự kiểm tra "giảm một nửa = −½ gấp đôi". Điền B1 (9 kịch bản), B2 (6.543 đ, +46,3%; xếp hạng làm lại > xem lại > lương) và B3 (giới hạn 2 lần rẻ nhất cho công ty, 6.901.220 đ) [simulated]. Đối chiếu khớp output B của Người 1.
- CP3: gắn nhãn độc lập 20 ca (người gắn nhãn 1). So với Người 3: đồng thuận 17/20 = 85%, lệch ở ca 6, 12, 17; ghi quy tắc phân biệt cho 3 ca lệch.
- CP4: viết `co_mau`, `power_hai_ti_le`, `in_d1` trong `src/lab13.py`. D1: a) 1.251/nhóm; b) DE 2,48, cần 84 người > 40; c) tối đa 1.000 < 1.251; d) tối đa 300; e) m ≥ 299 yêu cầu mỗi người (DE 6,96). Chọn chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm (power 0,64 nếu tác động thật là 5 điểm). Điền D2, đánh đổi và các trường còn `?` trong `pilot_plan.yaml`; cập nhật mục 5, 6 của `ho_so_launch_v0.md`.

## 4. Bằng chứng

- PR đã merge vào `main`: #2 (CP1, commit `5716c28`), #3 (CP2, `83738a1`), #6 (CP3, `d817d05`), #7 (CP4, `0c7b048`).
- File: `src/kiem_so.py`, `src/lab13.py` (phần D1), `report/team/bang_chi_phi.md` (A1–B3), `report/team/bang_loi.md` (cột nhãn người 1, đồng thuận, quy tắc), `report/team/pilot_plan.yaml`.
- Kiểm tra: `python kiem_so.py` và `python lab13.py` chạy hết; `yaml.safe_load` đọc được `pilot_plan.yaml`, ngoài chú thích không còn `?`; `grep` từ cấm theo checklist không in gì.

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề và hướng dẫn, viết `kiem_so.py`, code D1, điền các bảng và YAML, thao tác git (nhánh, commit, PR). Tôi tự kiểm tra bằng cách chạy lại hai script, so từng con số với output của Người 1 và với số đối chiếu trong hướng dẫn (lệch không quá 2%), kiểm tra YAML bằng `yaml.safe_load`.
- CP3: tôi tự gắn nhãn 20 ca. Công cụ AI dùng để trích nội dung 20 ca từ đề, điền nhãn của tôi vào `bang_loi.md`, so với nhãn của Người 3 và tính tỉ lệ đồng thuận.
- Ngày bắt đầu pilot 2026-12-07 và ngày quyết định 2027-01-11 là giả định do công cụ AI đề xuất, nhóm cần xác nhận.

## 6. Tự đánh giá

- Làm tốt: kiểm số độc lập bằng cách tính khác với `mo_hinh`, mọi số A–D khớp đáp án; số simulated đều có nhãn; nêu rõ đánh đổi bất lợi của pilot (power 0,64).
- Chưa tốt: lệch nhãn với Người 3 ở 3 ca (6, 12, 17), chủ yếu do nhầm giữa Hệ thống và Ngầm; phụ thuộc nhiều vào công cụ AI ở phần viết code.
- Còn lại: trình bày D1 và luật dừng khi duyệt chéo; chạy lại code trên máy mình trước khi nộp.
