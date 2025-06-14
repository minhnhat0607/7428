<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>PhoneStore - Cửa hàng điện thoại</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background-color: #f2f2f2;
    }

    header {
      background-color: #333;
      color: white;
      padding: 20px 0;
      text-align: center;
    }

    nav {
      background-color: #444;
      display: flex;
      justify-content: center;
      gap: 20px;
      padding: 10px;
    }

    nav a {
      color: white;
      text-decoration: none;
      font-weight: bold;
    }

    .container {
      padding: 20px;
    }

    .products {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
    }

    .product {
      background-color: white;
      border-radius: 8px;
      padding: 15px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      text-align: center;
    }

    .product img {
      max-width: 100%;
      height: auto;
    }

    .product h3 {
      margin: 10px 0 5px;
    }

    .product p {
      margin: 0;
      color: green;
      font-weight: bold;
    }

    footer {
      text-align: center;
      background-color: #333;
      color: white;
      padding: 15px;
      margin-top: 30px;
    }
  </style>
</head>
<body>
  <header>
    <h1>📱 PhoneStore</h1>
    <p>Chuyên cung cấp điện thoại chính hãng</p>
  </header>

  <nav>
    <a href="#">Trang chủ</a>
    <a href="#">Sản phẩm</a>
    <a href="#">Liên hệ</a>
    <a href="#">Giỏ hàng</a>
  </nav>

  <div class="container">
    <h2>Sản phẩm nổi bật</h2>
    <div class="products">
      <div class="product">
        <img src="https://via.placeholder.com/200x250" alt="iPhone 15" />
        <h3>iPhone 15 Pro Max</h3>
        <p>28.990.000đ</p>
      </div>
      <div class="product">
        <img src="https://via.placeholder.com/200x250" alt="Samsung S24" />
        <h3>Samsung Galaxy S24 Ultra</h3>
        <p>25.990.000đ</p>
      </div>
      <div class="product">
        <img src="https://via.placeholder.com/200x250" alt="Xiaomi 14" />
        <h3>Xiaomi 14</h3>
        <p>18.990.000đ</p>
      </div>
      <!-- Thêm sản phẩm khác -->
    </div>
  </div>

  <footer>
    &copy; 2025 PhoneStore. Mọi quyền được bảo lưu.
  </footer>
</body>
</html>
