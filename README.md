# Nhóm 11 – Lập lịch phân bổ công suất sạc xe điện

Đồ án môn **Khai phá dữ liệu**, Hồ Chí Minh, 2026.

| Thành viên | MSSV |
|---|---|
| Nguyễn Quốc Bảo | 2351067085 |
| Trần Tất Phát | 2351067106 |
| Trần Minh Quân | 2351067110 |

## Nội dung nộp

- [Báo cáo PDF](Bao_cao/bao_cao_nhom_11_lap_lich_xe_dien.pdf): 54 trang, gồm bìa và các phần đầu báo cáo.
- [Slide thuyết trình](Slide/Bao_Cao_EV_RL_Nhom.pptx): 24 slide.
- [Notebook chính đã chạy](Source_code/EV_RL_NHOM_BAN_CHON.ipynb).
- [Hướng dẫn tra cứu công thức và số liệu](Source_code/HUONG_DAN_TRA_CUU.md).
- `Source_code/ket_qua_de_hieu/`: bảng CSV, hình và kết luận của thí nghiệm chính.
- `Source_code/mo_hinh_caltech_150/`: model, cấu hình và log huấn luyện đã lưu.
- `data/caltech_merged_15min.csv.zip`: CSV dữ liệu đã nén; giải nén bằng script đi kèm.

## Bài toán và phạm vi

Mỗi 15 phút, chọn công suất sạc cho các xe đang kết nối. Mô phỏng kiểm tra giới hạn từng cổng, nhóm cổng (pod), pha điện và tổng trạm 150 kW. Nhóm so sánh PPO, Q-learning với FIFO, EDF, LLF, Fixed100, AverageRate và Equal.

Tập mô phỏng gồm 7.339 phiên trong 276 ngày của năm 2019. Chia theo thời gian: 70% ngày đầu dành cho phát triển, 30% ngày cuối để test. Phần phát triển được tách thành 155 ngày train và 38 ngày validation; test có 83 ngày.

PPO được đánh giá qua 5 seed, khoảng 300.000 bước mỗi seed. Các model tuning và model cuối được giữ để xem lại kết quả. Kết quả hiện tại chưa đủ bằng chứng kết luận PPO vượt EDF hoặc LLF theo chỉ số J. Đây là mô phỏng trên nhóm phiên đã chọn, chưa phải triển khai điều khiển trạm thực.

## Cài đặt và chạy

Môi trường gốc dùng Python 3.14 trên Windows; các phiên bản thư viện chính được ghi trong `requirements.txt`.

Chạy trong thư mục repo:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe Source_code/chuan_bi_du_lieu.py
cd Source_code
..\.venv\Scripts\python.exe -m notebook EV_RL_NHOM_BAN_CHON.ipynb
```

Giữ kernel và thư mục làm việc tại `Source_code`, rồi chạy các cell theo thứ tự. Có thể đọc ngay các output đã lưu mà không cần chạy lại.

Notebook mặc định `CHE_DO = 'XEM_KET_QUA'`: nạp model có sẵn và tính lại các bảng, không huấn luyện mới. Chạy lại toàn bộ vẫn cần thời gian đọc CSV và mô phỏng. Các chế độ `HOC_PHAN_THIEU` và `HOC_LAI` phục vụ huấn luyện; `HOC_LAI` có thể mất nhiều giờ. Nên sao lưu model và kết quả trước khi thay đổi chế độ.

## Dữ liệu và nguồn phương pháp

CSV được nhóm tổng hợp từ [Caltech ACN-Data](https://ev.caltech.edu/dataset). File nén chứa đúng một CSV; cần khoảng 244 MB sau giải nén. Dữ liệu được đưa kèm để giảng viên chạy lại mà không cần khóa API. Đây là dữ liệu lịch sử, công suất do thuật toán cấp trong bài được tính bởi simulator.

- Lee, Z. J., Li, T. và Low, S. H. (2019). *ACN-Data: Analysis and Applications of an Open EV Charging Dataset*. ACM e-Energy. [Bài gốc](https://ev.caltech.edu/assets/pub/ACN_Data_Analysis_and_Applications.pdf).
- [ACNPortal v0.3.3 – cấu hình mạng Caltech](https://github.com/zach401/acnportal/blob/v0.3.3/acnportal/acnsim/network/sites/caltech_acn.py).
- Schulman và cộng sự (2017). [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347).
- Watkins và Dayan (1992). [Q-learning](https://doi.org/10.1007/BF00992698).
