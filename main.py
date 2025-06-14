import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🐍 Snake Game", page_icon="🐍")
st.title("🐍 Game Con Rắn")

# HTML + JavaScript Snake Game
snake_game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    text-align: center;
    background: #111;
    color: white;
  }
  canvas {
    background: #000;
    display: block;
    margin: auto;
    border: 2px solid white;
  }
</style>
</head>
<body>
<h3>🐍 Dùng các phím mũi tên để điều khiển rắn</h3>
<canvas id="gameCanvas" width="400" height="400"></canvas>
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
    alert("💀 Game Over! Điểm: " + score);
    document.location.reload();
  } else {
    setTimeout(drawGame, 100);
  }
}

function update() {
  const head = {x: snake[0].x + dx, y: snake[0].y + dy};
  snake.unshift(head);
  if (head.x === food.x && head.y === food.y) {
    score++;
    food = {
      x: Math.floor(Math.random() * tileCount),
      y: Math.floor(Math.random() * tileCount)
    };
  } else {
    snake.pop();
  }
}

function draw() {
  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = "lime";
  snake.forEach(part => {
    ctx.fillRect(part.x * gridSize, part.y * gridSize, gridSize - 2, gridSize - 2);
  });

  ctx.fillStyle = "red";
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
    case "ArrowUp":
      if (dy === 0) { dx = 0; dy = -1; }
      break;
    case "ArrowDown":
      if (dy === 0) { dx = 0; dy = 1; }
      break;
    case "ArrowLeft":
      if (dx === 0) { dx = -1; dy = 0; }
      break;
    case "ArrowRight":
      if (dx === 0) { dx = 1; dy = 0; }
      break;
  }
});

drawGame();
</script>
</body>
</html>
"""

# Render HTML game in Streamlit
components.html(snake_game_html, height=500)
