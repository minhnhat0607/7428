<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PhoneStore - Cửa hàng điện thoại</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background: #f4f4f4;
    }
    header {
      background: #333;
      color: #fff;
      padding: 20px;
      text-align: center;
    }
    nav {
      display: flex;
      justify-content: center;
      background: #444;
    }
    nav a {
      color: #fff;
      padding: 14px 20px;
      display: block;
      text-decoration: none;
    }
    nav a:hover {
      background: #222;
    }
    .container {
      max-width: 1000px;
      margin: auto;
      padding: 20px;
    }
    .product {
      display: inline-block;
      width: 30%;
      margin: 1%;
      background: #fff;
      padding: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .product img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }
    .product h3, .product p {
      margin: 10px 0;
    }
    footer {
      text-align: center;
      padding: 20px;
      background: #333;
      color: white;
    }
    form input, form button {
      padding: 10px;
      margin: 5px;
    }
  </style>
</head>
<body>
  <header>
    <h1>📱 PhoneStore</h1>
    <p>Uy tín - Chất lượng - Hậu mãi tốt</p>
  </header>

  <nav>
    <a href="#products">Sản phẩm</a>
    <a href="#about">Giới thiệu</a>
    <a href="#contact">Liên hệ</a>
  </nav>

  <div class="container" id="products">
    <h2>Sản phẩm nổi bật</h2>
    <div class="product">
      <img src="https://via.placeholder.com/300x200?text=iPhone+15" alt="iPhone">
      <h3>iPhone 15 Pro Max</h3>
      <p>Giá: 32.000.000đ</p>
      <button>Mua ngay</button>
    </div>
    <div class="product">
      <img src="https://via.placeholder.com/300x200?text=Samsung+S24" alt="Samsung">
      <h3>Samsung Galaxy S24 Ultra</h3>
      <p>Giá: 28.000.000đ</p>
      <button>Mua ngay</button>
    </div>
    <div class="product">
      <img src="https://via.placeholder.com/300x200?text=Xiaomi+14" alt="Xiaomi">
      <h3>Xiaomi 14 Pro</h3>
      <p>Giá: 20.000.000đ</p>
      <button>Mua ngay</button>
    </div>
  </div>

  <div class="container" id="about">
    <h2>Về PhoneStore</h2>
    <p>Chúng tôi cung cấp các sản phẩm điện thoại chính hãng từ Apple, Samsung, Xiaomi,... với giá tốt nhất, bảo hành chính hãng và giao hàng nhanh chóng.</p>
  </div>

  <div class="container" id="contact">
    <h2>Liên hệ</h2>
    <form>
      <input type="text" placeholder="Họ và tên" required><br>
      <input type="email" placeholder="Email" required><br>
      <input type="text" placeholder="Tin nhắn..." required><br>
      <button type="submit">Gửi</button>
    </form>
  </div>

  <footer>
    &copy; 2025 PhoneStore. All rights reserved.
  </footer>
</body>
</html>
