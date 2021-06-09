// var initialBoard = [
//   [0, 0, 0, 1, 0, 5, 0, 6, 8],
//   [0, 0, 0, 0, 0, 0, 7, 0, 1],
//   [9, 0, 1, 0, 0, 0, 0, 3, 0],
//   [0, 0, 7, 0, 2, 6, 0, 0, 0],
//   [5, 0, 0, 0, 0, 0, 0, 0, 3],
//   [0, 0, 0, 8, 7, 0, 4, 0, 0],
//   [0, 3, 0, 0, 0, 0, 8, 0, 5],
//   [1, 0, 5, 0, 0, 0, 0, 0, 0],
//   [7, 9, 0, 4, 0, 1, 0, 0, 0],
// ];

// var isGameOver = true;
// var gameDifficulty = "Easy";
// var gameRunningTimeInSec = 0;

// Sudoku: Given numbers are in a different style than user-entered numbers, and
// given numbers cannot be changed. The player can get feedback on incorrect
// numbers at any time. There are multiple difficulty levels and multiple
// puzzles to choose from in each difficulty level. Puzzles are loaded using
// Ajax. Your program does not have to generate puzzles; it just needs to load
// and display puzzles from other sources. There is a timer that tells how long
// the player has been working on the puzzle. Please put the solution to one
// puzzle on the game description page or on the game grid so that I can easily
// test your game.

// Load boards from file or manually
const easy = [
  "6------7------5-2------1---362----81--96-----71--9-4-5-2---651---78----345-------",
  "685329174971485326234761859362574981549618732718293465823946517197852643456137298",
];
const medium = [
  "--9-------4----6-758-31----15--4-36-------4-8----9-------75----3-------1--2--3--",
  "619472583243985617587316924158247369926531478734698152891754236365829741472163895",
];
const hard = [
  "-1-5-------97-42----5----7-5---3---7-6--2-41---8--5---1-4------2-3-----9-7----8--",
  "712583694639714258845269173521436987367928415498175326184697532253841769976352841",
];

// Create variables
var timer;
var timeRemaining;
var lives;
var selectedNum;
var selectedTile;
var disableSelect;

function startGame() {
  // Choose board difficulty
  let board;
  if (document.getElementById("diff-1").checked) {
    board = easy[0];
  } else if (document.getElementById("diff-2").checked) {
    board = medium[0];
  } else {
    board = hard[0];
  }
  // Set lives to 3 and enable selecting numbers and tiles
  lives = 3;
  disableSelect = false;
  document.getElementById("lives").textContent = `Lives Remaining: ${lives}`;
  // Create board based on difficulty
  resetGame();
  generateBoard(board);
  startTimer();
  if (document.getElementById("theme-1").checked) {
    document.body.classList.remove("dark-theme");
  } else {
    document.body.classList.add("dark-theme");
  }

  document.getElementById("number-container").classList.remove("hidden");
}

function startTimer() {
  if (document.getElementById("time-1").checked) {
    timeRemaining = 180;
  } else if (document.getElementById("time-2").checked) {
    timeRemaining = 300;
  } else {
    timeRemaining = 600;
  }

  document.getElementById("timer").textContent = timeConversion(timeRemaining);
  timer = setInterval(() => {
    timeRemaining--;
    if (timeRemaining === 0) {
      endGame();
    }
    document.getElementById("timer").textContent =
      timeConversion(timeRemaining);
  }, 1000);
}

function timeConversion(time) {
  let minutes = Math.floor(time / 60);
  if (minutes < 10) {
    minutes = "0" + minutes;
  }
  let seconds = time % 60;
  if (seconds < 10) {
    seconds = "0" + seconds;
  }
  return minutes + ":" + seconds;
}

function endGame() {
  disableSelect = true;
  clearTimeout(timer);
  if (lives === 0 || timeRemaining === 0) {
    document.getElementById("lives").textContent = "You Lost!";
  } else {
    document.getElementById("lives").textContent = "You Won!";
  }
}

function generateBoard(board) {
  let idCount = 0;
  let boardDiv = document.getElementById("board");
  for (let i = 0; i < 81; i++) {
    let tile = document.createElement("p");
    if (board.charAt(i) != "-") {
      tile.textContent = board.charAt(i);
    } else {
      // Add an event listener
      tile.addEventListener("click", () => {
        if (!disableSelect) {
          if (tile.classList.contains("selected")) {
            tile.classList.remove("selected");
            selectedTile = null;
          } else {
            for (let i = 0; i < 81; i++) {
              document
                .querySelectorAll(".tile")
                [i].classList.remove("selected");
            }
            tile.classList.add("selected");
            selectedTile = tile;
            updateMove();
          }
        }
      });
    }
    tile.id = idCount;
    idCount++;
    tile.classList.add("tile");
    if ((tile.id > 17 && tile.id < 27) || (tile.id > 44 && tile.id < 54)) {
      tile.classList.add("bottom-border");
    }
    if ((tile.id + 1) % 9 == 3 || (tile.id + 1) % 9 == 6) {
      tile.classList.add("right-border");
    }
    boardDiv.appendChild(tile);
  }
}

function resetGame() {
  // Access all tiles
  let tiles = document.querySelectorAll(".tile");
  // Remove all tiles
  tiles.forEach((tile) => {
    tile.remove();
  });
  // Clear timer
  if (timer) {
    clearTimeout(timer);
  }
  // Deselect any numbers
  let selectedNumbers = document.querySelectorAll("#number-container p");
  selectedNumbers.forEach((number) => {
    number.classList.remove("selected");
  });
  // Clear selected variables
  selectedNum = null;
  selectedTile = null;
}

function updateMove() {
  if (selectedNum && selectedTile) {
    selectedTile.textContent = selectedNum.textContent;

    if (checkCorrect(selectedTile)) {
      selectedTile.classList.remove("selected");
      selectedNum.classList.remove("selected");
      selectedTile = null;
      selectedNum = null;
      if (checkDone()) {
        endGame();
      }
    } else {
      disableSelect = true;
      selectedTile.classList.add("incorrect");
      setTimeout(() => {
        lives--;
        if (lives === 0) {
          endGame();
        } else {
          document.getElementById(
            "lives"
          ).textContent = `Lives Remaining: ${lives}`;
          disableSelect = false;
        }
        selectedTile.classList.remove("incorrect");
        selectedTile.classList.remove("selected");
        selectedNum.classList.remove("selected");
        selectedTile.textContent = "";
        selectedTile = null;
        selectedNum = null;
      }, 1000);
    }
  }
}

function checkDone() {
  let tiles = document.querySelectorAll(".tiles");
  for (tile in tiles) {
    if (tile.textContent === "") {
      return false;
    }
    return true;
  }
}

function checkCorrect(tile) {
  let solution;
  if (document.getElementById("diff-1").checked) {
    solution = easy[1];
  } else if (document.getElementById("diff-2").checked) {
    solution = medium[1];
  } else {
    solution = hard[1];
  }

  if (solution.charAt(tile.id) === tile.textContent) {
    return true;
  } else {
    return false;
  }
}

window.onload = () => {
  console.log("Page Loaded!");
  // Run create new game function when button is clicked
  document.getElementById("start-button").addEventListener("click", startGame);
  let selectedNumbers = document.querySelectorAll("#number-container p");
  selectedNumbers.forEach((number) => {
    number.addEventListener("click", () => {
      if (!disableSelect) {
        if (number.classList.contains("selected")) {
          number.classList.remove("selected");
          selectedNum = null;
        } else {
          let selectedNumbers = document.querySelectorAll(
            "#number-container p"
          );
          selectedNumbers.forEach((number) => {
            number.classList.remove("selected");
          });
          number.classList.add("selected");
          selectedNum = number;
          updateMove();
        }
      }
    });
  });
};
