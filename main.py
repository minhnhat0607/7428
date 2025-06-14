<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PhoneStore - Cửa hàng điện thoại</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      margin: 0;
      padding: 0;
    }
    header {
      background: #333;
      color: #fff;
      text-align: center;
      padding: 1rem;
    }
    .products {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      padding: 20px;
    }
    .product {
      background: #fff;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
    }
    .product img {
      width: 100%;
      height: auto;
    }
    .product h3 {
      margin: 10px 0 5px;
    }
  </style>
</head>
<body>
  <header>
    <h1>📱 PhoneStore</h1>
    <p>Cửa hàng điện thoại chính hãng</p>
  </header>
  <section class="products">
    <div class="product">
      <img src="https://via.placeholder.com/250x300" alt="iPhone 15">
      <h3>iPhone 15</h3>
      <p>Giá: 28.990.000đ</p>
    </div>
    <div class="product">
      <img src="https://via.placeholder.com/250x300" alt="Samsung S24">
      <h3>Samsung Galaxy S24</h3>
      <p>Giá: 25.990.000đ</p>
    </div>
    <!-- Thêm sản phẩm khác -->
  </section>
</body>
</html>
