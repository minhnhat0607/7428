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

    const player = {
      x: canvas.width / 2 - 15,
      y: canvas.height - 50,
      width: 30,
      height: 30,
      speed: 5,
      color: "lime",
      bullets: []
    };

    function drawPlayer() {
      ctx.fillStyle = player.color;
      ctx.fillRect(player.x, player.y, player.width, player.height);
    }

    function drawBullets() {
      ctx.fillStyle = "red";
      player.bullets.forEach((bullet, i) => {
        bullet.y -= 7;
        ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
        if (bullet.y < 0) player.bullets.splice(i, 1);
      });
    }

    document.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft" && player.x > 0) player.x -= player.speed;
      if (e.key === "ArrowRight" && player.x + player.width < canvas.width) player.x += player.speed;
      if (e.key === " ") {
        player.bullets.push({
          x: player.x + player.width / 2 - 2,
          y: player.y,
          width: 4,
          height: 10
        });
      }
    });

    function gameLoop() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      drawPlayer();
      drawBullets();
      requestAnimationFrame(gameLoop);
    }

    gameLoop();
  </script>
</body>
</html>
