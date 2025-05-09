# LTTKUD
# Quản Lý Sinh Viên

Đây là một ứng dụng quản lý sinh viên được xây dựng bằng Python và PyQt6. Ứng dụng cho phép thêm, sửa, xóa, tìm kiếm và quản lý thông tin sinh viên, bao gồm sinh viên chính quy và sinh viên tại chức.

## Các tính năng chính

- **Thêm sinh viên**: Cho phép thêm sinh viên mới vào cơ sở dữ liệu.
- **Sửa thông tin sinh viên**: Cập nhật thông tin của sinh viên hiện có.
- **Xóa sinh viên**: Xóa sinh viên khỏi cơ sở dữ liệu.
- **Tìm kiếm sinh viên**: Tìm kiếm sinh viên theo ID, tên hoặc khoa.
- **Phân loại sinh viên**: Quản lý sinh viên chính quy và tại chức với các thông tin đặc thù.

## Yêu cầu hệ thống

- Python 3.10 trở lên
- PyQt6
- MySQL Connector

## Cài đặt

1 Các thư viện cần thiết
pip install PyQt6 mysql-connector-python

2 Cấu hình cơ sở dữ liệu
Đảm bảo MySQL đã được cài đặt và chạy.
Tạo cơ sở dữ liệu lttkud và các bảng cần thiết.
Cập nhật thông tin kết nối trong file dbconnect.py.

3 Chạy ứng dụng
python main.py

##Hướng dẫn sử dụng
Thêm sinh viên:

Nhấn nút "Add" để mở form thêm sinh viên.
Điền thông tin và nhấn "Save".
Sửa thông tin sinh viên:

Chọn sinh viên từ bảng.
Nhấn nút "Edit" để mở form chỉnh sửa.
Cập nhật thông tin và nhấn "Save".
Xóa sinh viên:

Chọn sinh viên từ bảng.
Nhấn nút "Delete" và xác nhận.
Tìm kiếm sinh viên:

Sử dụng các trường tìm kiếm để lọc sinh viên theo ID, tên hoặc khoa.
Đóng góp
Nếu bạn muốn đóng góp cho dự án, vui lòng tạo một pull request hoặc mở một issue trên GitHub.
