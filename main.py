<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>🚀 Game Bắn Súng</title>
  <style>
    body {
      background: #000;
      margin: 0;
      overflow: hidden;
    }
    canvas {
      display: block;
      margin: auto;
      background-color: #111;
      border: 2px solid #0f0;
    }
  </style>
</head>
<body>
<canvas id="gameCanvas" width="480" height="640"></canvas>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const ship = { x: 220, y: 580, width: 40, height: 20, color: "#0f0" };
const bullets = [];
const enemies = [];
let score = 0;
let gameOver = false;

// Create enemies
function spawnEnemy() {
  const x = Math.random() * (canvas.width - 30);
  enemies.push({ x, y: 0, width: 30, height: 20, color: "#f00", speed: 2 });
}

// Draw ship
function drawShip() {
  ctx.fillStyle = ship.color;
  ctx.fillRect(ship.x, ship.y, ship.width, ship.height);
}

// Draw bullets
function drawBullets() {
  ctx.fillStyle = "#0ff";
  bullets.forEach(b => ctx.fillRect(b.x, b.y, b.width, b.height));
}

// Draw enemies
function drawEnemies() {
  enemies.forEach(e => {
    ctx.fillStyle = e.color;
    ctx.fillRect(e.x, e.y, e.width, e.height);
  });
}

// Collision detection
function isColliding(a, b) {
  return (
    a.x < b.x + b.width &&
    a.x + a.width > b.x &&
    a.y < b.y + b.height &&
    a.y + a.height > b.y
  );
}

// Game loop
function update() {
  if (gameOver) return;

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  drawShip();

  // Move and draw bullets
  bullets.forEach(b => b.y -= 5);
  bullets.filter(b => b.y > 0);
  drawBullets();

  // Move enemies
  enemies.forEach(e => e.y += e.speed);
  drawEnemies();

  // Check bullet-enemy collision
  bullets.forEach((b, bi) => {
    enemies.forEach((e, ei) => {
      if (isColliding(b, e)) {
        bullets.splice(bi, 1);
        enemies.splice(ei, 1);
        score++;
      }
    });
  });

  // Check enemy-ship collision
  enemies.forEach(e => {
    if (isColliding(e, ship) || e.y > canvas.height) {
      gameOver = true;
      alert("💥 Game Over! Điểm: " + score);
      location.reload();
    }
  });

  // Show score
  ctx.fillStyle = "#fff";
  ctx.font = "16px Arial";
  ctx.fillText("Điểm: " + score, 10, 20);

  requestAnimationFrame(update);
}

// Controls
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") ship.x -= 20;
  if (e.key === "ArrowRight") ship.x += 20;
  if (e.key === " ") {
    bullets.push({
      x: ship.x + ship.width / 2 - 2,
      y: ship.y,
      width: 4,
      height: 10
    });
  }
});

// Enemy spawner
setInterval(spawnEnemy, 1000);

// Start game
update();
</script>
</body>
</html>
