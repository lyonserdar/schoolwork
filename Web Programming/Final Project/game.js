// Constants
const PUZZLES = {
  debug: [
    {
      puzzle:
        "679518243543729618821634957794352186358461729216897534485276391962183475137945860",
      solution:
        "679518243543729618821634957794352186358461729216897534485276391962183475137945862",
    },
  ],
  easy: [
    {
      puzzle:
        "070000043040009610800634900094052000358460020000800530080070091902100005007040802",
      solution:
        "679518243543729618821634957794352186358461729216897534485276391962183475137945862",
    },
    {
      puzzle:
        "301086504046521070500000001400800002080347900009050038004090200008734090007208103",
      solution:
        "371986524846521379592473861463819752285347916719652438634195287128734695957268143",
    },
    {
      puzzle:
        "048301560360008090910670003020000935509010200670020010004002107090100008150834029",
      solution:
        "748391562365248791912675483421786935589413276673529814834962157296157348157834629",
    },
  ],
  medium: [
    {
      puzzle:
        "008317000004205109000040070327160904901450000045700800030001060872604000416070080",
      solution:
        "298317645764285139153946278327168954981453726645792813539821467872634591416579382",
    },
    {
      puzzle:
        "040890630000136820800740519000467052450020700267010000520003400010280970004050063",
      solution:
        "142895637975136824836742519398467152451328796267519348529673481613284975784951263",
    },
    {
      puzzle:
        "561092730020780090900005046600000427010070003073000819035900670700103080000000050",
      solution:
        "561492738324786195987315246659831427418279563273564819135928674746153982892647351",
    },
  ],
  hard: [
    {
      puzzle:
        "310450900072986143906010508639178020150090806004003700005731009701829350000645010",
      solution:
        "318457962572986143946312578639178425157294836284563791425731689761829354893645217",
    },
    {
      puzzle:
        "800134902041096080005070010008605000406310009023040860500709000010080040000401006",
      solution:
        "867134952241596783395872614978625431456318279123947865534769128619283547782451396",
    },
    {
      puzzle:
        "165293004000001632023060090009175000500900018002030049098000006000000950000429381",
      solution:
        "165293874974851632823764195489175263536942718712638549398517426241386957657429381",
    },
  ],
};

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
      }
      this.style.backgroundColor = "#FFCB00";
      this.classList.toggle("selected");
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
    PUZZLES[difficulty][Math.floor(Math.random() * PUZZLES[difficulty].length)];
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

function assignment4Input() {
  let text = document.getElementById("assignment-4-input").value;
  document.getElementById("assignment-4-input-text").textContent = text;
}

function main() {
  createGameSelectOptions();
  createGameBoard(9, 9);
  listenStartNewGame();
  assignment4Anim();
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
// TODO: Game grid that uses CSS and is generated by JavaScript
// TODO: User input in the form of text, select options, and/or buttons
// TODO: User input in the form of mouse clicks
// TODO: Dynamic modification of HTML using innerHTML or DOM functions
// TODO: Use of XMLHttpRequest to load JSON or XML game grid data
// TODO: HTML5 audio or video tags, canvas or local storage
// TODO: Game Logic
// TODO: Extra Credit: Second HTML5 component

// Remove all children of element
// while (element.firstChild) {
//   element.removeChild(element.firstChild);
// }
