import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🐍 Snake Game", page_icon="🐍")
st.title("🐍 Game Con Rắn (Đẹp hơn)")

snake_game_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <style>
    body {
      margin: 0;
      background-color: #1e1e1e;
      font-family: 'Segoe UI', sans-serif;
      color: white;
      text-align: center;
    }
    canvas {
      background-color: #111;
      display: block;
      margin: 0 auto;
      border: 3px solid #00ffcc;
      box-shadow: 0 0 20px #00ffcc;
    }
    h3 {
      margin-top: 10px;
      color: #00ffcc;
    }
    #score {
      font-size: 20px;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <h3>🐍 Dùng các phím mũi tên để điều khiển rắn</h3>
  <canvas id="gameCanvas" width="400" height="400"></canvas>
  <div id="score">Điểm: 0</div>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const gridSize = 20;
const tileCount = canvas.width / gridSize;
let snake = [{x: 10, y: 10}];
let dx = 0;
let dy = 0;
let food = {x: 15, y: 15};
let score = 0;

function drawGame() {
  update();
  draw();
  if (checkGameOver()) {
    setTimeout(() => {
      alert("💀 Game Over! Tổng điểm: " + score);
      document.location.reload();
    }, 100);
  } else {
    setTimeout(drawGame, 120);
  }
}

function update() {
  const head = {x: snake[0].x + dx, y: snake[0].y + dy};
  snake.unshift(head);
  if (head.x === food.x && head.y === food.y) {
    score++;
    document.getElementById("score").innerText = "Điểm: " + score;
    food = {
      x: Math.floor(Math.random() * tileCount),
      y: Math.floor(Math.random() * tileCount)
    };
  } else {
    snake.pop();
  }
}

function draw() {
  ctx.fillStyle = "#111";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Snake
  for (let i = 0; i < snake.length; i++) {
    ctx.fillStyle = i === 0 ? "#00ffcc" : "#33ff99";
    ctx.fillRect(snake[i].x * gridSize, snake[i].y * gridSize, gridSize - 2, gridSize - 2);
  }

  // Food
  ctx.fillStyle = "#ff3c38";
  ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
}

function checkGameOver() {
  const head = snake[0];
  if (
    head.x < 0 || head.x >= tileCount ||
    head.y < 0 || head.y >= tileCount
  ) return true;

  for (let i = 1; i < snake.length; i++) {
    if (head.x === snake[i].x && head.y === snake[i].y) return true;
  }
  return false;
}

document.addEventListener("keydown", e => {
  switch (e.key) {
    case "ArrowUp": if (dy === 0) { dx = 0; dy = -1; } break;
    case "ArrowDown": if (dy === 0) { dx = 0; dy = 1; } break;
    case "ArrowLeft": if (dx === 0) { dx = -1; dy = 0; } break;
    case "ArrowRight": if (dx === 0) { dx = 1; dy = 0; } break;
  }
});

drawGame();
</script>
</body>
</html>
"""

components.html(snake_game_html, height=520)
