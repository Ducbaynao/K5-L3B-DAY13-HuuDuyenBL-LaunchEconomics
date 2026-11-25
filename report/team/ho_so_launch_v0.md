# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: HuuDuyenBL · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công, gấp 16,3× hoá đơn token chia số yêu cầu (274,7 đ). Trong phạm vi `noi_dia` + `hang_nang`: 3.414 đ, cộng cố định 40 triệu đ/tháng thành 4.599 đ (0,38×) ở 45.000 yêu cầu/tháng, 5.784 đ (0,48×) nếu còn một nửa khối lượng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8% khi gấp đôi) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1% khi tăng 25%). Giá token chỉ ±5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]. Thu hẹp `noi_dia` + `hang_nang`: 0,22× và 0,69×; loại `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×). Số bất lợi: xem lại 100% còn 0,98×–1,03× [simulated] | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính 82,83% (994/1.200) · Dùng, bỏ qua gợi ý 27,12% (48/177) · An toàn, mở lại 7 ngày 4,25% (51/1.200). Đây là số của đợt chạy thử, chưa có nhóm đối chứng; 10 event có `trace_id` (xem `chi_so.md`) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca gắn 5 loại; bảng khắc phục 5 ca đã nháp, đang chờ nhãn độc lập của người gắn nhãn 1 để tính đồng thuận (mục tiêu ≥ 16/20) | Chưa | Trưởng nhóm CSKH |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên; cỡ mẫu D1, mức chênh và luật dừng đang hoàn thiện trong `pilot_plan.yaml` | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,8%) · xem lại 100% kéo dài: 11.743 đ (0,98×) · khối lượng còn một nửa: cố định +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- _Nháp, chờ cả nhóm thống nhất và chờ mục 5, 6 hoàn thiện:_ nghiêng về **Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, vì 0,22× và 0,69× ở quy mô đầy đủ, nhưng phải nêu con số bất lợi: xem lại 100% chỉ còn 0,98×–1,03× [simulated], và mức chênh phát hiện được sẽ lớn hơn 5 điểm vì không đủ người cho 1.251 yêu cầu mỗi nhóm.
- Điều kiện dự kiến (người phụ trách, ngày kiểm tra sẽ chốt sau): bật đủ event có `trace_id` và thay phút simulated bằng phút đo thật sau tuần 1; có kế hoạch giảm xem lại theo bậc; Giám đốc vận hành ký chấp nhận mức chênh phát hiện được của pilot.
