# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-HuuDuyenBL-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- Số thành viên: 3
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |     Phạm Lý Ngọc Đức   |      |       |        | Người 1: code, tính toán và kiểm tra kỹ thuật |
|   2 |      Nguyễn Huy Tấn  |      |       |        | Người 2: kiểm số, kế hoạch pilot, gắn nhãn 1 |
|   3 |      Vũ Lương Duy  |      |       |        | Người 3: chỉ số, tổng hợp hồ sơ, gắn nhãn 2 |

Người 1–3 tương ứng với STT trong bảng thành viên. Điền thông tin cá nhân trước khi nộp. Nhóm phân công kiêm nhiệm các vai của lab cho 3 thành viên.

## Phân công theo checkpoint

Các giờ dưới đây là lịch mẫu tại lớp, điều chỉnh theo thông báo của coach.

| Checkpoint | Người 1 | Người 2 | Người 3 |
| --- | --- | --- | --- |
| Chuẩn bị · 14:00–14:10 | Cài môi trường, chạy thử `src/lab13.py`. | Đọc công thức, chuẩn bị kiểm số. | Điền thông tin `TEAM.md`, kiểm tra các mẫu báo cáo. |
| CP1 · A · 14:10–14:53 | Viết 3 hàm A1 và `mo_hinh`; tính A2, A3, A4. | Kiểm tra A1, tính tay ít nhất 1 khoản chi phí; đối chiếu output và điền các bảng A trong `report/team/bang_chi_phi.md`. | Chuẩn bị `report/team/ho_so_launch_v0.md`; ghi kết luận về phạm vi từ A3 và chi phí cố định A4. |
| CP2 · B · 14:53–15:20 | Chạy 9 kịch bản B1, kịch bản kết hợp B2, giới hạn chạy B3 và xem lại 100% B4. | Kiểm tra phần trăm thay đổi và chi phí cả hệ thống; điền B1–B3 trong `report/team/bang_chi_phi.md`. | Đối chiếu B4, điền kết luận; ghi rủi ro kinh tế và cập nhật hồ sơ. |
| CP3 · C · 15:35–16:08 | Hoàn thiện A–B còn thiếu; chuẩn bị công thức và dữ liệu D1. | Gắn nhãn độc lập 20 ca với vai người gắn nhãn 1; sau đó cùng Người 3 so nhãn và hoàn thiện `report/team/bang_loi.md`. | Gắn nhãn độc lập 20 ca với vai người gắn nhãn 2; sau đó ghi đồng thuận, quy tắc phân biệt và bảng khắc phục cùng Người 2. |
| CP4 · D · 16:08–16:36 | Hỗ trợ và kiểm tra code D1; tính tỉ lệ mở lại hiện tại. | Trực tiếp viết code tính đủ 5 câu D1; điền cách chia, D2, cỡ mẫu và đánh đổi trong `report/team/pilot_plan.yaml`. | Soạn luật dừng, rollback và vai trò phụ trách trong kế hoạch pilot; đối chiếu với A–B. |
| CP5 · E · 16:36–17:00 | Tính 3 chỉ số E1, cung cấp output để kiểm tra. | Kiểm tra công thức chỉ số, event và ít nhất 2 rủi ro kinh tế; rà soát kế hoạch pilot. | Hoàn thiện `report/team/chi_so.md` và hồ sơ launch đủ 7 mục; ghi đề xuất đã được cả nhóm thống nhất. |
| Duyệt chéo · 17:00–17:45 | Trình bày chi phí, trả lời câu hỏi A–B; tham gia đánh giá nhóm bạn. | Trình bày cỡ mẫu, thiết kế pilot và luật dừng; tham gia đánh giá nhóm bạn. | Tổng hợp nhận xét và ghi `report/team/phieu_cham.md` khi nhóm làm hội đồng. |
| Đóng gói · 17:45–18:00 | Kiểm tra code, chuẩn bị commit và push. | Chạy lại code trên máy mình; kiểm tra YAML và checklist nộp. | Hoàn thiện `report/team/group_report.md`; kiểm tra đủ file và thông tin đóng góp. |

## Điều kiện hoàn thành checkpoint

| Checkpoint | Sản phẩm cần kiểm tra |
| --- | --- |
| CP1 | A1 đạt cả 3 phép thử (1,20 · 1,25 · 1,25); A2 đủ 9 dòng, A3 đủ 4 loại; có bảng A4. |
| CP2 | B1 đủ 9 kịch bản; B2 có kịch bản kết hợp và xếp hạng; B3, B4 có kết luận bằng số. |
| CP3 | Có 2 bộ nhãn độc lập cho 20 ca, tỉ lệ đồng thuận và quy tắc xử lý bất đồng; bảng khắc phục đủ 5 loại lỗi. Mục tiêu đồng thuận ít nhất 16/20 ca. |
| CP4 | D1 đủ 5 câu, D2 đủ 5 câu; YAML đọc được, đủ trường, không còn chỗ cần điền; ít nhất 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ. |
| CP5 | Có 3 chỉ số tính thử và 2 chỉ số tự đề xuất; ít nhất 6 event có `trace_id`, 2 dòng rủi ro; hồ sơ đủ 7 mục và đề xuất cuối. |

## Nguyên tắc phối hợp

- CP3: Người 2 và Người 3 gắn nhãn riêng trong 8 phút, không trao đổi trước khi so nhãn. Giữ nguyên hai bộ nhãn ban đầu sau khi so; ghi nhãn thống nhất ở cột riêng.
- Sau giải lao, Người 2 trực tiếp chạy lại mô hình chi phí và viết phần D1 với Người 1 hỗ trợ, để ít nhất 2 người tự tay tính được chi phí.
- Mọi số trong báo cáo phải có nguồn từ code của nhóm hoặc cách tính tay được ghi rõ; kết quả phụ thuộc cột `_simulated` phải ghi nhãn `simulated`.
- Mỗi file do người phụ trách cập nhật; báo trước khi sửa cùng file để tránh xung đột. Các kết luận và đề xuất cuối được cả nhóm kiểm tra.
- Chỉ điền kết quả gắn nhãn, duyệt chéo và đóng góp thực tế sau khi đã thực hiện.
- Mỗi thành viên tự viết báo cáo cá nhân, ghi công cụ AI và cách tự kiểm tra; tự nộp link repo nhóm trên LMS.
- Hạn nộp theo `SUBMISSION.md`: trước 23:59 GMT+7 ngày lab, trừ thông báo gia hạn của coach.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
