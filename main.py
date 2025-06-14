import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🐍 Snake Tăng Tốc", page_icon="🐍")
st.title("🐍 Game Con Rắn (Tăng tốc mỗi lần ăn)")

snake_game_html = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      background: #121212;
      color: #00ffcc;
      font-family: 'Segoe UI', sans-serif;
      text-align: center;
    }
    canvas {
      background-color: #000;
      display: block;
      margin: auto;
      border: 3px solid #00ffcc;
      box-shadow: 0 0 20px #00ffcc;
    }
    h3 { margin-top: 10px; }
    #score { font-size: 18px; margin-top: 10px; }
  </style>
</head>
<body>
  <h3>🐍 Điều khiển: phím mũi tên (rắn xuyên tường)</h3>
  <canvas id="gameCanvas" width="400" height="400"></canvas>
  <div id="score">Điểm: 0 | Tốc độ: 150ms</div>

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
let speed = 150; // tốc độ ban đầu
let timer;

function drawGame() {
  update();
  draw();
  if (checkCollision()) {
    clearTimeout(timer);
    setTimeout(() => {
      alert("💀 Game Over! Điểm: " + score);
      document.location.reload();
    }, 100);
  } else {
    timer = setTimeout(drawGame, speed);
  }
}

function update() {
  let headX = (snake[0].x + dx + tileCount) % tileCount;
  let headY = (snake[0].y + dy + tileCount) % tileCount;
  const newHead = {x: headX, y: headY};
  snake.unshift(newHead);

  if (newHead.x === food.x && newHead.y === food.y) {
    score++;
    speed = Math.max(30, speed - 10); // tăng tốc mỗi lần ăn
    food = {
      x: Math.floor(Math.random() * tileCount),
      y: Math.floor(Math.random() * tileCount)
    };
  } else {
    snake.pop();
  }

  document.getElementById("score").innerText = "Điểm: " + score + " | Tốc độ: " + speed + "ms";
}

function draw() {
  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  for (let i = 0; i < snake.length; i++) {
    ctx.fillStyle = i === 0 ? "#00ffcc" : "#33ff99";
    ctx.fillRect(snake[i].x * gridSize, snake[i].y * gridSize, gridSize - 2, gridSize - 2);
  }

  ctx.fillStyle = "#ff3333";
  ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
}

function checkCollision() {
  const head = snake[0];
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
