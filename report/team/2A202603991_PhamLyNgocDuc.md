# Báo cáo cá nhân — Phạm Lý Ngọc Đức — 2A202603991

## 1. Thông tin thành viên

- Họ tên: Phạm Lý Ngọc Đức.
- MSSV: 2A202603991.
- Email: 26ai.ducpln@vinuni.edu.vn.
- Nhóm: HuuDuyenBL · Lớp: L3B.
- Vai trò: Tôi là Người 1, phụ trách code, tính toán và kiểm tra kỹ thuật.

## 2. Phần việc phụ trách

Tôi phụ trách phần tính toán A1–A4, B1–B4 trong `src/lab13.py`, tính tỉ lệ mở lại ở CP4 và ba chỉ số E1 ở CP5. Tôi cung cấp kết quả để các thành viên kiểm số và hoàn thiện hồ sơ. Ở CP3, hai thành viên còn lại gắn nhãn độc lập; phần đóng góp của tôi tập trung vào kiểm tra code và kết quả A–B. Ở CP4, tôi phối hợp kiểm tra và ghép phần D1 do Người 2 viết.

## 3. Đóng góp cụ thể

### CP1 — Mô hình chi phí

Tôi hoàn thiện ba hàm A1 và chạy bộ kiểm tra có sẵn, đạt các kết quả 1,20; 1,25; 1,25. Trong hàm `mo_hinh`, tôi cộng chi phí token và tool của mọi lần chạy, kể cả lần lỗi, cộng thời gian xem lại và làm lại rồi chia cho số yêu cầu có `ket_qua == 'thanh_cong'`.

Tôi tính được 978 việc thành công, tổng chi phí 4.373.585 đ và chi phí mỗi việc thành công 4.472 đ [simulated]. Khi cộng phần nhân viên tiếp nhận các ca không thành công theo mô hình của lab, chi phí cả hệ thống là 5.865 đ/yêu cầu [simulated]. Tôi phân biệt hai đại lượng này khi so với baseline 12.000 đ.

Tôi tách kết quả theo bốn loại yêu cầu và tính chi phí cố định cho phạm vi `noi_dia` + `hang_nang`. Phạm vi có 982 yêu cầu, 900 thành công; tỉ lệ 900/1.200 = 75% dùng để quy đổi số việc thành công trong phạm vi từ tổng lượng yêu cầu toàn công ty. Chi phí gồm cố định là 4.599 đ/việc ở 45.000 yêu cầu/tháng và 5.784 đ/việc nếu khối lượng giảm một nửa [simulated].

### CP2 — Độ nhạy và giới hạn chạy lại

Tôi bổ sung chín kịch bản B1, kịch bản kết hợp B2, bảng giới hạn chạy B3 và trường hợp xem lại 100% B4. Trong các kịch bản đã thử, làm lại tăng gấp đôi làm chi phí mỗi việc thành công tăng 51,8%; xem lại tăng gấp đôi làm tăng 40,7%; lương tăng 25% làm tăng 23,1% [simulated].

Trên toàn mẫu, giới hạn hai lần chạy cho chi phí cả hệ thống thấp nhất, 6.901.220 đ; giới hạn một lần cho chi phí mỗi việc thành công thấp nhất, 4.111 đ [simulated]. Tôi nhận thấy chỉ tối ưu chi phí mỗi việc thành công có thể đẩy thêm việc sang nhân viên.

Trong phạm vi pilot, khi xem lại toàn bộ 948 yêu cầu có ít nhất một lần chạy `ok`, chi phí là 11.743 đ/việc theo giả định làm lại 9 phút, hoặc 12.415 đ/việc khi dùng trung bình chưa làm tròn của dữ liệu phút làm lại [simulated]. Các mức này chưa gồm cố định và phần nhân viên tiếp nhận yêu cầu không thành công; vì vậy tôi không xem chúng là chi phí đầy đủ của toàn hệ thống.

### CP3–CP4 — Kiểm tra và phối hợp

Tôi rà soát kết quả A–B và kiểm tra bản CP3 đã ghép. Tôi không nhận phần gắn nhãn độc lập của hai thành viên là đóng góp của mình.

Tôi tính tỉ lệ mở lại là 51/1.200 = 4,25% trên toàn mẫu và 39/982 = 3,97% trong phạm vi pilot. Tôi ghép code D1 của Người 2 với hàm tỉ lệ mở lại của mình, xử lý conflict tại cuối `src/lab13.py` và loại phần in trùng. Sau khi ghép, chương trình chạy hết và kiểm tra D1 đạt 1.251, 859, 299.

Tôi hiểu 859 là cỡ mẫu hiệu dụng mỗi nhóm ở mức chênh 6 điểm phần trăm. Với 20 nhân viên mỗi nhóm và 299 yêu cầu/người, số yêu cầu thực tế là 5.980 mỗi nhóm, hệ số thiết kế 6,96. Nếu tác động thật chỉ 5 điểm, power theo phép tính của nhóm còn khoảng 0,64.

### CP5 — Chỉ số E1

Tôi viết `in_e1(reqs)` để in cả tử số, mẫu số và phần trăm. Chỉ số chính là 994/1.200 = 82,83%; tỉ lệ bỏ qua gợi ý trong các ca được xem lại là 48/177 = 27,12%; tỉ lệ mở lại là 51/1.200 = 4,25%.

Tôi đối chiếu công thức với cách ánh xạ event trong báo cáo và nêu các điểm cần thống nhất về mẫu số, cờ yêu cầu được xem lại và thời điểm tạo yêu cầu. Ba chỉ số trên không phụ thuộc cột `_simulated`, nhưng toàn bộ dữ liệu lab vẫn là giả lập và chưa có đối chứng để kết luận tác động của trợ lý.

## 4. Bằng chứng

| Phần việc của tôi | Bằng chứng trong repo |
| --- | --- |
| CP1, A1–A4 | Commit `7f611b5`; các hàm A1, `mo_hinh`, `in_a2`, `in_a3`, `in_a4` trong `src/lab13.py` |
| CP2, B1–B4 | Commit `3dc007e`; các hàm `in_b1` đến `in_b4` |
| CP4, tỉ lệ mở lại | Commit `3b46844`; hàm `in_ty_le_mo_lai` |
| Ghép code và xử lý conflict CP4 | Commit `6d0d673`; giữ code D1 của Người 2 và phần tính tỉ lệ của tôi |
| CP5, ba chỉ số E1 | Commit `bc104f2`; hàm `in_e1` |

Tôi kiểm tra chương trình từ thư mục `src` bằng lệnh sau:

```powershell
.\.venv\Scripts\python.exe lab13.py
```

Chương trình in A1 ĐẠT, chạy hết A–B, đạt kiểm tra D1 và in ba chỉ số E1 như trên. Các bảng dùng chung được trình bày trong [bảng chi phí](bang_chi_phi.md), [đặc tả chỉ số](chi_so.md) và [kế hoạch pilot](pilot_plan.yaml).

## 5. Công cụ AI đã dùng

Tôi sử dụng ChatGPT/Codex để giải thích yêu cầu, gợi ý và hỗ trợ viết code, kiểm tra công thức, xử lý conflict Git và biên tập báo cáo. Tôi dùng output chạy trên hai CSV của repo, ba phép thử A1 và các số đối chiếu trong tài liệu để kiểm tra kết quả; tôi không dùng câu trả lời của AI thay cho kết quả tính toán.

Tôi giữ nguyên hai file CSV, ghi nhãn `simulated` cho kết quả phụ thuộc phút giả lập và phân biệt phần code của mình với D1 do Người 2 viết. Phần gắn nhãn và kết quả duyệt chéo phải phản ánh việc nhóm thực hiện, không được suy ra từ AI.

## 6. Tự đánh giá

Tôi đã hoàn thành phần code và tính toán được phân công ở CP1, CP2, CP4 và CP5. Qua bài lab, tôi hiểu vì sao chi phí phải cộng cả lần chạy lỗi, vì sao cần tính phần nhân viên tiếp nhận việc và vì sao số cụm giới hạn cỡ mẫu hiệu dụng.

Hạn chế của kết quả là thời gian nhân viên còn giả lập, đợt chạy thử chưa có đối chứng và hiệu quả kinh tế thay đổi mạnh khi phải xem lại 100%. Tôi cần tiếp tục đối chiếu định nghĩa chỉ số với event, phối hợp kiểm tra hồ sơ cuối và bổ sung kết quả duyệt chéo sau khi nhóm thực hiện.
