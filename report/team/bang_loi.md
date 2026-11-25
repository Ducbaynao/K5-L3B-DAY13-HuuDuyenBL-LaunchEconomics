# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Huy Tấn · Người gắn nhãn 2: Vũ Lương Duy (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | _(Tấn điền)_ | Do người dùng | | |
| 2 | _(Tấn điền)_ | Hệ thống | | |
| 3 | _(Tấn điền)_ | Ngữ cảnh | | |
| 4 | _(Tấn điền)_ | Giới hạn hệ thống | | |
| 5 | _(Tấn điền)_ | Ngầm | | |
| 6 | _(Tấn điền)_ | Do người dùng | | |
| 7 | _(Tấn điền)_ | Hệ thống | | |
| 8 | _(Tấn điền)_ | Hệ thống | | |
| 9 | _(Tấn điền)_ | Do người dùng | | |
| 10 | _(Tấn điền)_ | Ngữ cảnh | | |
| 11 | _(Tấn điền)_ | Giới hạn hệ thống | | |
| 12 | _(Tấn điền)_ | Ngầm | | |
| 13 | _(Tấn điền)_ | Giới hạn hệ thống | | |
| 14 | _(Tấn điền)_ | Do người dùng | | |
| 15 | _(Tấn điền)_ | Hệ thống | | |
| 16 | _(Tấn điền)_ | Ngữ cảnh | | |
| 17 | _(Tấn điền)_ | Ngầm | | |
| 18 | _(Tấn điền)_ | Ngữ cảnh | | |
| 19 | _(Tấn điền)_ | Giới hạn hệ thống | | |
| 20 | _(Tấn điền)_ | Hệ thống | | |

**Tỉ lệ đồng thuận:** chưa tính — chờ nhãn độc lập của Người gắn nhãn 1 (Tấn)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi > 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh mẫu | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi `refund_ledger_write` ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại vì số tiền mà kiểm tra thấy đúng, theo tuần; ngưỡng > 1% số ca đóng | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = thieu_du_lieu, theo loại yêu cầu, báo cáo hằng tuần | Giữ cách chuyển kèm tóm tắt; đưa quoc_te ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành (`audit_sample_checked`); ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới; ghi phiên bản bảng giá vào trace | Kế toán trưởng |
