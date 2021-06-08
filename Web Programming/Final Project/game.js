// Constants
const PUZZLE_URL = "./data/puzzles.json";

// Debug Elements
var debugEl = document.getElementById("debug");
var cellCoordsEl = document.getElementById("cell-coords");

// Elements
var gameDifficultyEl = document.getElementById("game-difficulty");
var gameTimeEl = document.getElementById("game-time");

// Variables
var selectOption = null;
var boardTable = null;
var puzzle = null;
var solution = null;
var grid = [[], [], [], [], [], [], [], [], []];
var gameRunningTimeInSec = 0;
var isGameOver = true;
var gameTimer = null;
var puzzles = null;

function createGameSelectOptions() {
  let gameSelectOptionsEl = document.getElementById("game-select-options");
  for (let i = 0; i < 9; i++) {
    let option = document.createElement("button");
    option.textContent = i + 1;
    option.style.height = "60px";
    option.style.width = "60px";
    option.style.border = "none";
    option.style.fontWeight = "500";
    option.style.fontSize = "50px";
    setCellColor(option, i);
    option.onclick = function () {
      let options = this.parentNode.children;
      for (let i = 0; i < options.length; i++) {
        setCellColor(options[i], i);
        options[i].classList.remove("selected");
      }
      this.style.backgroundColor = "#FFCB00";
      this.classList.add("selected");
      console.log("toggle");
      if (selectOption && selectOption === option.textContent) {
        selectOption = null;
      } else {
        selectOption = option.textContent;
      }
    };
    option.onmouseenter = function () {
      this.style.backgroundColor = "#FFCB00";
    };
    option.onmouseleave = function () {
      let index = [...this.parentNode.children].indexOf(this);
      if (!this.classList.contains("selected")) {
        setCellColor(this, index);
      }
    };
    gameSelectOptionsEl.appendChild(option);
  }
}

function createGameBoard(rows, cols) {
  let gameBoardEl = document.getElementById("game-board");
  boardTable = document.createElement("table");
  boardTable.style.borderCollapse = "collapse";
  for (let row = 0; row < rows; row++) {
    let tr = document.createElement("tr");
    boardTable.appendChild(tr);
    for (let col = 0; col < cols; col++) {
      let td = document.createElement("td");
      td.style.color = "#0b0c10";
      td.style.textAlign = "center";
      td.style.width = "50px";
      td.style.height = "50px";
      td.style.fontSize = "40px";
      setCellColor(td, row * 9 + col);
      if (col === 2 || col === 5) {
        td.style.borderRight = "2px solid #BFBFBF";
      }
      if (row === 2 || row === 5) {
        td.style.borderBottom = "2px solid #BFBFBF";
      }
      tr.appendChild(td);
    }
  }
  gameBoardEl.appendChild(boardTable);
}

function setCellColor(cell, cellIndex) {
  if (cellIndex % 2) {
    cell.style.backgroundColor = "#F9F9F9";
  } else {
    cell.style.backgroundColor = "#FFFFFF";
  }
}

function checkGameEnded() {
  for (let i = 0; i < 81; i++) {
    let row = Math.floor(i / 9);
    let col = Math.floor(i % 9);
    let cell = grid[row][col];
    if (cell === "0") {
      return false;
    }
  }
  // TODO: Verify the winning board
  return true;
}

function checkCellInputCorrect(index, input) {
  return solution.charAt(index) === input;
}

function setupInitialBoard(board) {
  for (let i = 0; i < 81; i++) {
    let row = Math.floor(i / 9);
    let col = Math.floor(i % 9);
    grid[row][col] = board.charAt(i);
    let cell = boardTable.rows[row].cells[col];
    setCellColor(cell, i);
    cell.textContent = "";
    if (board.charAt(i) != "0") {
      cell.textContent = board.charAt(i);
      cell.style.backgroundColor = "#E1E1E1";
      cell.style.fontWeight = "bold";
      cell.onclick = function () {
        return false;
      };
      cell.onmouseenter = function () {
        return false;
      };
      cell.onmouseleave = function () {
        return false;
      };
    } else {
      cell.onclick = function () {
        let rowIndex = this.parentNode.rowIndex;
        let colIndex = this.cellIndex;
        cellCoordsEl.textContent = `Cell Coords: (${rowIndex}, ${colIndex})`; // Debug
        this.textContent = selectOption;
        grid[rowIndex][colIndex] = selectOption;
        let boardIndex = rowIndex * 9 + colIndex;
        if (!checkCellInputCorrect(boardIndex, selectOption)) {
          this.style.color = "red";
          setTimeout(() => {
            this.textContent = "";
            this.style.color = "#0b0c10";
            grid[rowIndex][colIndex] = "0";
          }, 250);
        } else {
          if (checkGameEnded()) {
            endGame();
          }
        }
      };
      cell.onmouseenter = function () {
        this.style.color = "#FFCB00";
      };
      cell.onmouseleave = function () {
        let rowIndex = this.parentNode.rowIndex;
        let colIndex = this.cellIndex;
        setCellColor(this, rowIndex * 9 + colIndex);
        this.style.color = "#0b0c10";
      };
    }
  }
}

function getBoardValues(difficulty) {
  let board =
    puzzles[difficulty][Math.floor(Math.random() * puzzles[difficulty].length)];
  return { puzzle: board.puzzle, solution: board.solution };
}

function startTimer() {
  gameRunningTimeInSec = 0;
  gameTimeEl.textContent = "00:00:00";
  isGameOver = false;
  timer();
}

function endTimer() {
  isGameOver = true;
  if (gameTimer) {
    clearTimeout(gameTimer);
  }
}

function timer() {
  function pad(num, size) {
    num = num.toString();
    while (num.length < size) {
      num = "0" + num;
    }
    return num;
  }

  if (!isGameOver) {
    let secs = pad(gameRunningTimeInSec % 60, 2);
    let mins = pad(Math.floor(gameRunningTimeInSec / 60) % 60, 2);
    let hours = pad(Math.floor(gameRunningTimeInSec / 3600), 2);
    gameTimeEl.textContent = hours + ":" + mins + ":" + secs;
    gameRunningTimeInSec++;
    gameTimer = setTimeout(timer, 1000);
  }
}

function startNewGame() {
  console.log("new game started");
  endTimer();
  let difficulty = gameDifficultyEl.value;
  let board = getBoardValues(difficulty);
  puzzle = board.puzzle;
  solution = board.solution;
  setupInitialBoard(puzzle);
  startTimer();
}

function endGame() {
  console.log("game ended");
  endTimer();
}

function listenStartNewGame() {
  document
    .getElementById("start-new-game")
    .addEventListener("click", startNewGame);
}

function assignment4Anim() {
  var assignment4AnimEl = document.getElementById("assignment-4-anim");
  var elPos = 0;
  var intervalId = setInterval(frame, 50);
  function frame() {
    if (elPos == 170) {
      clearInterval(intervalId);
      assignment4AnimEl.remove();
    } else {
      elPos++;
      assignment4AnimEl.style.top = `${elPos}px`;
    }
  }
}

// Assignment 4
function assignment4Input() {
  let text = document.getElementById("assignment-4-input").value;
  document.getElementById("assignment-4-input-text").textContent = text;
}

// Assignment 5
var username = "";
var timestamp = "";
function clearLocalStorage() {
  localStorage.removeItem("cs2550timestamp");
  assignment5Storage();
}

// Assignment 5
function assignment5Storage() {
  const user = JSON.parse(localStorage.getItem("cs2550timestamp"));
  document.getElementById("username").textContent = user?.userName;
  document.getElementById("timestamp").textContent = user?.timestamp;
}

// Assignment 6
function fetchPuzzles() {
  let xhr = new XMLHttpRequest();
  xhr.open("GET", PUZZLE_URL);
  xhr.responseType = "json";
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onload = function () {
    if (this.status == 200) {
      puzzles = this.response;
      document.getElementById("game-data").textContent =
        JSON.stringify(puzzles);
    } else {
      authErrorEl.textContent = "Server Error.";
    }
  };
  xhr.send();
}

function toggleDebug() {
  let debugEls = document.querySelectorAll(".debug");
  debugEls.forEach((el) => {
    el.classList.toggle("hidden");
  });
}

function main() {
  fetchPuzzles();
  createGameSelectOptions();
  createGameBoard(9, 9);
  listenStartNewGame();
  assignment4Anim();
  assignment5Storage();
}

window.onload = main;

// DONE: Set given numbers style to bold
// DONE: Given numbers cannot be changed
// DONE: Player feedback on incorrect numbers
// DONE: Multiple difficulty levels
// DONE: Multiple puzzles for each difficulty
// TODO: Puzzles are loaded using Ajax
// TODO: Puzzles needs to be loaded from other sources.
// TODO: Timer that tells how long the player working on the puzzle
// TODO: Put a solution to the puzzle for the instructor

// TODO: Documentation
// DONE: Game grid that uses CSS and is generated by JavaScript
// DONE: User input in the form of text, select options, and/or buttons
// DONE: User input in the form of mouse clicks
// DONE: Dynamic modification of HTML using innerHTML or DOM functions
// TODO: Use of XMLHttpRequest to load JSON or XML game grid data
// TODO: HTML5 audio or video tags, canvas or local storage
// TODO: Game Logic
// TODO: Extra Credit: Second HTML5 component

// Remove all children of element
// while (element.firstChild) {
//   element.removeChild(element.firstChild);
// }
