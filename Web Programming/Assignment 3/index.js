var gameControlsDiv = document.getElementById("game-controls")
var boardDiv = document.getElementById("board-container")
var gameTimerLabel = document.getElementById("game-timer")
var gameDifficultyLabel = document.getElementById("game-difficulty")

var initialBoard = [
  [0, 0, 0, 1, 0, 5, 0, 6, 8],
  [0, 0, 0, 0, 0, 0, 7, 0, 1],
  [9, 0, 1, 0, 0, 0, 0, 3, 0],
  [0, 0, 7, 0, 2, 6, 0, 0, 0],
  [5, 0, 0, 0, 0, 0, 0, 0, 3],
  [0, 0, 0, 8, 7, 0, 4, 0, 0],
  [0, 3, 0, 0, 0, 0, 8, 0, 5],
  [1, 0, 5, 0, 0, 0, 0, 0, 0],
  [7, 9, 0, 4, 0, 1, 0, 0, 0],
]

var isGameOver = true
var gameDifficulty = "Easy"
var gameRunningTimeInSec = 0

function createBoardView(board) {
  if (document.getElementById("board")) {
    document.getElementById("board").remove()
  }
  let rows = board.length
  let columns = board[0].length
  let table = document.createElement("table")
  table.classList.add("board")
  table.setAttribute("id", "board")
  let tbody = document.createElement("tbody")
  table.appendChild(tbody)
  for (var row = 0; row < rows; row++) {
    let tr = document.createElement("tr")
    tr.classList.add("table-row")
    tbody.appendChild(tr)
    for (var col = 0; col < columns; col++) {
      let td = document.createElement("td")
      if (row < 3 && col < 3 || row < 3 && col > 5) {
        td.classList.add("table-cell-light-given")
      } else if (row > 2 && row < 6 && col > 2 && col < 6) {
        td.classList.add("table-cell-light-given")
      } else if (row > 5 && col < 3 || row > 5 && col > 5) {
        td.classList.add("table-cell-light-given")
      } else {
        td.classList.add("table-cell-dark-given")
      }
      let number = board[row][col].number
      if (!board[row][col].isGiven) {
        td.onclick = (event) => {
          console.log(`row: ${event.target.parentNode.rowIndex}`, `col: ${event.target.cellIndex}`)
        }
      }
      td.appendChild(document.createTextNode(`${number ? number : ""}`))
      tr.appendChild(td)
    }
  }
  boardDiv.appendChild(table)
  console.log("Table Created!")
}

function createBoard(initBoard) {
  let board = []
  initBoard.forEach(row => {
    let boardRow = []
    row.forEach(col => {
      boardRow.push({
        number: col,
        isGiven: col ? true : false
      })
    })
    board.push(boardRow)
  })
  return board
}

function startGame() {
  isGameOver = false
  let board = createBoard(initialBoard)
  createBoardView(board)
  displayGameMode()
  startGameTimer()
}

function displayGameMode() {
  gameDifficultyLabel.innerHTML = "Game Difficulty: " + gameDifficulty
}

function endGame() {
  isGameOver = true
}

function startGameTimer() {
  gameRunningTimeInSec = 0
  timer()
}

function timer() {
  function pad(num, size) {
    num = num.toString()
    while (num.length < size) {
      num = "0" + num
    }
    return num
  }

  if (!isGameOver) {
    gameRunningTimeInSec++
    let secs = pad(gameRunningTimeInSec % 60, 2)
    let mins = pad(Math.floor(gameRunningTimeInSec / 60) % 60, 2)
    let hours = pad(Math.floor(gameRunningTimeInSec / 3600), 2)
    gameTimerLabel.innerHTML = hours + ":" + mins + ":" + secs
    setTimeout("timer()", 1000)
  }
}

function createNewGameButton() {
  var btn = document.createElement("button")
  btn.innerHTML = "Start a New Game"
  btn.onclick = startGame
  gameControlsDiv.appendChild(btn)
}

function createResetButton() {
  var resetButton = document.createElement("button")
  resetButton.innerHTML = "Reset"
  resetButton.onclick = () => {
    startGame()
  }
  gameControlsDiv.appendChild(resetButton)
}

function createControls() {
  createNewGameButton()
  createResetButton()
}

window.onload = () => {
  console.log("Page Loaded!")
  createControls()
}


// Sudoku: Given numbers are in a different style than user-entered numbers, and
// given numbers cannot be changed. The player can get feedback on incorrect
// numbers at any time. There are multiple difficulty levels and multiple
// puzzles to choose from in each difficulty level. Puzzles are loaded using
// Ajax. Your program does not have to generate puzzles; it just needs to load
// and display puzzles from other sources. There is a timer that tells how long
// the player has been working on the puzzle. Please put the solution to one
// puzzle on the game description page or on the game grid so that I can easily
// test your game.