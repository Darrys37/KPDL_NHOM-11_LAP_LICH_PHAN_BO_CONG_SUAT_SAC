# Đọc và chạy notebook nhóm

Mở `EV_RL_NHOM_BAN_CHON.ipynb`. Toàn bộ hàm đã nằm trong notebook; không cần chép các file `.py` của người sửa. Giữ thư mục `mo_hinh_caltech_150` cạnh notebook và chuẩn bị CSV nếu muốn chạy lại.

## Chạy

1. Chọn kernel Python có các thư viện được liệt kê ở cell đầu. Thiếu thư viện thì notebook tự cài bằng chính Python của kernel.
2. Giữ `CHE_DO = 'XEM_KET_QUA'` rồi Restart Kernel → Run All. Chế độ này đọc model đã có và chấm lại, không huấn luyện. Thiếu model/log sẽ báo đúng đường dẫn cần bổ sung.
3. CSV được tìm cạnh notebook, ở thư mục cha hoặc theo `EV_DATA`; trên máy hiện tại còn tìm bản trong `D:/Study/Khaiphadulieu/do-an-v3`. Muốn chuyển máy, đặt CSV cạnh notebook hoặc chỉ định đường dẫn.
4. Chỉ đổi `CHE_DO` thành `HOC_PHAN_THIEU` nếu muốn học lượt thiếu; `HOC_LAI` là học lại toàn bộ, tốn thời gian. Không dùng checkpoint hiện tại sau khi tự đổi dữ liệu, reward hoặc cách biểu diễn.

Kết quả bản dễ đọc nằm trong `ket_qua_de_hieu`. Kết quả cũ vẫn giữ trong `ket_qua_ban_chon` và `ket_qua_caltech` để đối chiếu.

## Tra khi vấn đáp

Sau khi chạy đến các cell định nghĩa công thức:

```python
tra_cuu('objective')  # J: công thức, đơn vị, tìm hàm nào bằng Ctrl+F
tra_cuu('F04')        # chờ ban đầu
tra_cuu('delay_min')  # chậm tương đương, khác thời gian sạc bù điện thiếu
tra_cuu('Q_ACTIONS')  # 9 tổ hợp ngân sách–ưu tiên
tra_cuu('observation')
```

Sau khi chạy đến phần kết quả:

```python
giai_thich_so('PPO', 'objective')
giai_thich_so('PPO', 'unmet_pct')
giai_thich_so('PPO', 'objective', ngay='2019-11-25', seed=42)

xe = chi_tiet_mot_ngay('2019-11-25', 'PPO', 42)
print(xe['Chờ (phút)'].mean())
print(xe['Chậm tương đương (phút)'].mean())
```

Nếu chưa chạy đến phần tạo dữ liệu/kết quả, các lệnh phụ thuộc phần đó sẽ chưa có biến để tra. Cách chắc chắn nhất là Run All ở chế độ xem kết quả trước.

## Cách lần theo một con số

**Ví dụ hỏi J:** xem số trong bảng chính → gọi `giai_thich_so('PPO','objective')` → máy in bốn phần cộng ra J → gọi `tra_cuu('F09')` → Ctrl+F `tinh_thanh_phan_J`. Reward từng bước ở `tinh_reward_buoc`; chỉ số một ngày ở `tinh_chi_so`.

**Ví dụ hỏi điện thiếu:** CSV cho yêu cầu khai báo; mỗi bước máy cấp `kW × 0,25 giờ` ra kWh; lấy yêu cầu trừ đã cấp. Tỷ lệ thiếu được tính từng ngày trước rồi mới lấy trung bình. Không thay tỷ lệ này bằng tổng thiếu chia tổng yêu cầu nếu đang giải thích bảng trung bình ngày.

**Ví dụ hỏi chờ/chậm:** `tinh_cho_cham_buoc` cộng phút từng xe; `MoiTruongSac.result` giữ số từng xe; `tinh_chi_so` lấy trung bình ngày. `chi_tiet_mot_ngay` giúp đối chiếu lại toàn bộ xe, không chỉ 8 xe xem trước.

## Đã kiểm tra

- 71/71 cell code chạy từ kernel mới, gồm 22 cell nhận xét riêng cho 22 bảng kết quả.
- Ba bảng lý thuyết cũng có cell nhận xét ngay sau.
- 1.328 dòng test, 8 dòng tổng hợp, 24 CI và 25 xe ngày minh họa khớp số cũ, sai khác lớn nhất 0.
- Các lệnh tra cứu và truy vết xe PPO/Q-learning/Fixed100/EDF đã thử thành công.
- Không huấn luyện mới, không thay model; không cập nhật Word.

Tách cell làm số cell tăng để mỗi bảng có nhận xét riêng. Phần thử nghiệm giữ nguyên; đây là tối ưu cách tổ chức, cách đọc và tra cứu, không phải tuyên bố tăng chất lượng PPO hoặc tốc độ huấn luyện.
