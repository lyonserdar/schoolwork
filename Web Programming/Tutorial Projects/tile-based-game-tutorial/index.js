var ctx = null
var tileWidth = 40
var tileHight = 40
var mapWidth = 10
var mapHeight = 10
var currentSecond = 0
var frameCount = 0
var frameLastSecond = 0
var lastFrameTime = 0
var keysDown = {
  37: false,
  38: false,
  39: false,
  40: false
}

class Character {
  constructor() {
    this.tileFrom = [1, 1]
    this.tileTo = [1, 1]
    this.timeMoved = 0
    this.dimensions = [30, 30]
    this.position = [45, 45]
    this.delayMove = 700
  }

  placeAt(x, y) {
    this.tileFrom = [x, y]
    this.tileTo = [x, y]
    this.position = [
      tileWidth * x + (tileWidth - this.dimensions[0]) / 2,
      tileHight * y + (tileHight - this.dimensions[1]) / 2
    ]
  }

  processMovement(t) {
    if (this.tileFrom[0] == this.tileTo[0] && this.tileFrom[1] == this.tileTo[1]) {
      return false
    }

    if (t - this.timeMoved >= this.delayMove) {
      this.placeAt(this.tileTo[0], this.tileTo[1])
    } else {
      this.position[0] = this.tileFrom[0] * tileWidth + (tileWidth - this.dimensions[0]) / 2
      this.position[1] = this.tileFrom[1] * tileHight + (tileHight - this.dimensions[1]) / 2
      
      
    
    }
  }
}

var player = new Character()

var gameMap = [
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 1, 1, 1, 0, 1, 1, 1, 1, 0,
  0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
  0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
  0, 1, 0, 1, 0, 0, 0, 1, 1, 0,
  0, 1, 0, 1, 0, 1, 0, 0, 1, 0,
  0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
  0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
  0, 1, 1, 1, 0, 1, 1, 1, 1, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]



window.onload = () => {
  ctx = document.getElementById("game").getContext("2d")
  requestAnimationFrame(drawGame)
  ctx.font = "bold 10pt sans-serif"
}

function drawGame() {
  if (ctx == null) {
    return
  }

  var sec = Math.floor(Date.now() / 1000)
  if (sec != currentSecond) {
    currentSecond = sec
    frameLastSecond = frameCount
    frameCount = 1
  } else {
    frameCount++
  }

  for (let y = 0; y < mapHeight; y++) {
    for (let x = 0; x < mapWidth; x++) {
      switch (gameMap[y * mapWidth + x]) {
        case 0:
          ctx.fillStyle = "black"
          break
        case 1:
        default:
          ctx.fillStyle = "white"
          break
      }
      ctx.fillRect(x * tileWidth, y * tileHight, tileWidth, tileHight)
    }
  }

  ctx.fillStyle = "red"
  ctx.fillText(`FPS: ${frameLastSecond}`, 10, 20)

  requestAnimationFrame(drawGame)
}