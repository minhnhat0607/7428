<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Game Ghép Mô Hình</title>
  <style>
    body {
      font-family: sans-serif;
      text-align: center;
      background: #f0f0f0;
    }

    h1 {
      margin-top: 20px;
      color: #333;
    }

    #puzzle {
      width: 300px;
      height: 300px;
      margin: 20px auto;
      display: flex;
      flex-wrap: wrap;
      border: 4px solid #333;
    }

    .tile {
      width: 100px;
      height: 100px;
      box-sizing: border-box;
      border: 1px solid #ccc;
      background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Iconic_image_of_the_Earth_by_Apollo_17.jpg/600px-Iconic_image_of_the_Earth_by_Apollo_17.jpg');
      background-size: 300px 300px;
    }

    .tile.dragging {
      opacity: 0.5;
    }

    button {
      padding: 10px 20px;
      margin-top: 10px;
      font-size: 16px;
    }
  </style>
</head>
<body>

<h1>🧩 Game Ghép Mô Hình</h1>
<div id="puzzle"></div>
<button onclick="shuffle()">🔄 Trộn Lại</button>

<script>
  const puzzle = document.getElementById('puzzle');
  const positions = [];

  function createTiles() {
    for (let i = 0; i < 9; i++) {
      const tile = document.createElement('div');
      tile.classList.add('tile');
      tile.draggable = true;
      const x = (i % 3) * -100;
      const y = Math.floor(i / 3) * -100;
      tile.style.backgroundPosition = `${x}px ${y}px`;
      tile.dataset.index = i;
      positions.push(i);
      puzzle.appendChild(tile);
    }
  }

  function shuffle() {
    const tiles = [...puzzle.children];
    for (let i = tiles.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [tiles[i].style.backgroundPosition, tiles[j].style.backgroundPosition] = [tiles[j].style.backgroundPosition, tiles[i].style.backgroundPosition];
      [tiles[i].dataset.index, tiles[j].dataset.index] = [tiles[j].dataset.index, tiles[i].dataset.index];
    }
  }

  let draggedTile;

  puzzle.addEventListener('dragstart', (e) => {
    if (e.target.classList.contains('tile')) {
      draggedTile = e.target;
      draggedTile.classList.add('dragging');
    }
  });

  puzzle.addEventListener('dragend', () => {
    if (draggedTile) {
      draggedTile.classList.remove('dragging');
    }
  });

  puzzle.addEventListener('dragover', (e) => {
    e.preventDefault();
  });

  puzzle.addEventListener('drop', (e) => {
    e.preventDefault();
    if (e.target.classList.contains('tile') && draggedTile !== e.target) {
      const tempBg = draggedTile.style.backgroundPosition;
      const tempIndex = draggedTile.dataset.index;
      draggedTile.style.backgroundPosition = e.target.style.backgroundPosition;
      draggedTile.dataset.index = e.target.dataset.index;
      e.target.style.backgroundPosition = tempBg;
      e.target.dataset.index = tempIndex;
    }
  });

  createTiles();
  shuffle();
</script>

</body>
</html>
