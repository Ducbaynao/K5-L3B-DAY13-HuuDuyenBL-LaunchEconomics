# Phiếu chấm hội đồng Gate 2a

Tôi đánh giá nhóm T108 theo bằng chứng đã được cung cấp: output chương trình A–B, D1 và E1. Điểm dưới đây phản ánh mức độ đáp ứng được chứng minh trong lần đánh giá này; tôi chưa có hồ sơ launch, kế hoạch pilot hoặc câu trả lời tại buổi duyệt để xác nhận các phần còn thiếu.

- Nhóm chấm (hội đồng): HuuDuyenBL · Lớp L3B.
- Người ghi phiếu: Phạm Lý Ngọc Đức · MSSV 2A202603991.
- Nhóm được chấm: T108.
- Bằng chứng đã nhận: output A1, A2–A4, B1–B4, D1 và E1 do nhóm cung cấp.
- Trạng thái: Đánh giá trên output đã nhận; tổng 5/30, quyết định No-go tại lần đánh giá này. Tôi chưa trực tiếp chạy code của nhóm được chấm.

## Đánh giá theo ba tiêu chí hội đồng

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 0/10 | Chưa đủ minh chứng để ghi nhận điểm tiêu chí này: tôi chưa nhận đề xuất cuối và cách xử lý rủi ro. Tôi ghi nhận CPS 4.472 đ, chi phí cả hệ thống 5.865 đ/yêu cầu và B4 lên 11.743–12.415 đ/việc [simulated]. Nhóm đã in số bất lợi, nhưng chưa cung cấp đề xuất cuối và cách xử lý để tôi đánh giá sự nhất quán. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 5/10 | Output có nhãn simulated ở tiêu đề và [sim] tại nhiều dòng. A4/B4 tính riêng noi_dia + hang_nang; A3 cho thấy quoc_te tốn 22.515 đ/việc, 1,88× baseline [simulated]. Tôi cần xem hồ sơ để xác nhận nhãn đầy đủ và phạm vi pilot thực sự được chọn. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 0/10 | Chưa đủ minh chứng về kế hoạch pilot để ghi nhận điểm: D1 nêu đúng 1.251 mẫu/nhóm cho 5 điểm, và 859 mẫu hiệu dụng/nhóm cho 6 điểm với 20 nhân viên, 299 yêu cầu/người, DE 6,96. Chưa có bằng chứng về cách chia thực tế, đối chứng đồng thời, kiểm soát ảnh hưởng gián tiếp và luật dừng. |
| **Tổng** | | | | **5 / 30** | Tôi ghi 0 ở hai tiêu chí chưa có đủ minh chứng; đây không phải kết luận rằng các phần chưa nhận đã được kiểm tra và làm sai. Điểm có thể được xét lại khi bổ sung hồ sơ. |

## Nhận xét từ kết quả đã cung cấp

- **A1–A4:** Tôi ghi nhận ba phép thử A1 ĐẠT. Tổng chi phí 4.373.585 đ chia 978 việc thành công ra khoảng 4.472 đ/việc; phần cố định là 1.185 đ/việc ở 45.000 yêu cầu/tháng, tăng lên 2.370 đ khi khối lượng còn một nửa [simulated].
- **B1–B2:** Các số khớp đối chiếu: làm lại gấp đôi tăng 51,8%, xem lại gấp đôi tăng 40,7%, lương tăng 25% làm tăng 23,1%; kết hợp token và xem lại gấp đôi tăng 46,3% [simulated].
- **B3:** Tôi đồng ý với kết quả số học trên toàn mẫu: hai lần chạy có chi phí cả hệ thống thấp nhất, 6.901.220 đ, còn một lần chạy cho CPS thấp nhất, 4.111 đ [simulated]. Cần kiểm tra lại trong phạm vi pilot nếu dùng kết quả này để chọn giới hạn vận hành.
- **B4:** 11.743 đ thấp hơn baseline 12.000 đ khoảng 2,1%, còn 12.415 đ cao hơn khoảng 3,5% [simulated]. Tôi lưu ý đây là CPS theo kịch bản B4, chưa gồm chi phí cố định và phần nhân viên tiếp nhận yêu cầu không thành công.
- **D1:** Tôi ghi nhận đánh đổi đã được thể hiện bằng số: với 20 nhân viên/nhóm, mẫu hiệu dụng luôn nhỏ hơn 1.000; mục tiêu 5 điểm cần 1.251. Phương án 6 điểm cần 20 × 299 = 5.980 yêu cầu thực tế/nhóm; power còn khoảng 0,64 nếu tác động thật chỉ 5 điểm.
- **E1:** Ba kết quả khớp đối chiếu: chính 994/1.200 = 82,83%; bỏ qua gợi ý 48/177 = 27,12%; mở lại 51/1.200 = 4,25%. Tôi xem đây là kết quả đợt chạy thử giả lập, chưa phải bằng chứng tác động vì chưa có đối chứng.
- **Phần chưa nhận:** Bảng lỗi C, danh sách event, hồ sơ launch, kế hoạch pilot và đề xuất cuối. Tôi chưa đánh giá các phần này từ output hiện có.

## Quyết định và lý do

**Quyết định của hội đồng:** **No-go** tại lần đánh giá trên bằng chứng đã nhận.

**Lý do:** Tôi chưa đủ cơ sở duyệt pilot vì chưa nhận đề xuất cuối, thiết kế đối chứng và luật dừng. Dù số tính khớp đối chiếu, B4 đạt 12.415 đ/việc [simulated] và power chỉ 0,64 ở mức chênh 5 điểm; cần kế hoạch xử lý cụ thể trước khi quay lại cổng.

## Câu hỏi cho đội trình

**Một câu hỏi:** Nếu pilot phải xem lại 100% khiến CPS lên 12.415 đ/việc [simulated], đồng thời thiết kế chỉ có power khoảng 0,64 khi tác động thật là 5 điểm, nhóm chọn quyết định nào và quy định ngưỡng dừng, người có quyền dừng, thời hạn xử lý ra sao?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chưa nhận. Tôi sẽ ghi câu trả lời thực tế, không dùng câu trả lời dự kiến thay cho biên bản.

## Việc cần làm để quay lại Gate 2a

- Đề xuất Go / Go có điều kiện / No-go và phạm vi pilot trong hồ sơ của T108.
- Kế hoạch pilot: cách chia, đối chứng đồng thời, cỡ mẫu thực tế và hiệu dụng, kiểm soát ảnh hưởng gián tiếp, ngày quyết định.
- Ít nhất 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng, thời hạn, vai trò và rollback.
- Nhãn simulated trong các file hồ sơ, bảng lỗi và danh sách event để kiểm tra bằng chứng liên quan.
- Sau khi nhận bổ sung, tôi sẽ đánh giá lại ba tiêu chí, cập nhật tổng điểm và quyết định; câu trả lời của đội trình chỉ được ghi khi thực sự nhận được.
