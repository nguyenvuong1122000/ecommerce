###  A simple Ecomerce WebSite

# eCommerce

- Đây là repo chứa code của môn học PROJECT II học kì 20202 do sinh viên Nguyễn Thịnh Vượng thực hiện.
- Đề tài : Xây dựng hệ thống thương mại điện tử


## Các chức năng 

- <b>Customer Features </b>

| Chức năng   |  Coded?       | Mô tả  |
|----------|:-------------:|:-------------|
| Tìm kiếm sản phẩm   | &#10004; | Chức năng tìm kiếm sản phẩm dựa trên người dùng nhập   |
| Danh sách  | &#10004; | Chức năng xem danh sách sản phẩm  |
| Thêm sản phẩm vào giỏ  | &#10004; | Chức năng thêm sản phẩm vào giỏ hàng đang có, nếu người dùng chưa có giỏ hàng thì tạo mới  |
| Xóa sản phẩm khỏi giỏ   | &#10004; | Chức năng xóa sản phẩm khỏi hàng hiện tại  |
| Xem danh sách sản phẩm trong giỏ   | &#10004; | Chức năng xem danh sách sản phẩm trong giỏ hàng  |
| Bình luận   | &#10004; | Chức năng bình luận  |
| Tạo đơn đặt hàng  |&#10004; | Chức năng tạo đơn hàng từ, thông tin đơn hàng được nhập và lấy từ giỏ hàng |

- <b>Seller Features </b>

| Feature  |  Coded?       | Mô tả  |
|----------|:-------------:|:-------------|
| Tìm kiếm sản phẩm   | &#10004; | Chức năng tìm kiếm sản phẩm dựa trên người dùng nhập   |
| Danh sách  | &#10004; | Chức năng xem danh sách sản phẩm  |
| Bình luận   | &#10004; | Chức năng bình luận  |
| Thêm sản phẩm vào hệ thống   | &#10004; | Chức năng thêm sản phẩm vào hệ thống  |
| Xóa sản phẩm| &#10004;   | Ability to see the Cart and it items |
| Xem thông tin các đơn đặt hàng  | &#10004; | Ability of Remove a Cart |
| Đổi trạng thái giao hàng   | &#10004; | Ability of Remove a Cart |


## Running project



- Để bắt đầu và run project này, máy tính cần cài sẵn Python 3.8 trong máy. Nên tạo một virtual environment để quản lý các thư viện
```
pip install virtualenv
```

 - Tải code của project này về máy. Trên terminal (linux) hoặc windows terminal, chạy command sau 

```
virtualenv env
```

- Command đó sẽ tạo  `env` trong project directory. Kích hoạt `env` đó bằng command  :

```
source env/bin/active
```

- Sau đó cài đặt các thư viện bổ trợ cần thiết : 
```
pip install -r requirements.txt
```

- Khởi chạy sever : 
```
python manage.py runserver
```
- Username của admin : vuong

- Password của admin : 123


