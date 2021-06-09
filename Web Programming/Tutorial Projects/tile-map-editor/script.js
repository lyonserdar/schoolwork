const sizeOfCrop = 32

var canvas = document.querySelector("canvas")
var tilesetContainer = document.querySelector(".tileset-container")
var tilesetSelection = document.querySelector(".tileset-container-selection")
var tilesetImage = document.querySelector("#tileset-source")

var selection = [0, 0]

var currentLayer = 0

var layers = [
  {
    // "0-0": [0, 0]
  },
  {},
  {}
]

function draw() {
  var ctx = canvas.getContext("2d")
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  layers.forEach(layer => {
    Object.keys(layer).forEach(key => {
      var positionX = Number(key.split("-")[0])
      var positionY = Number(key.split("-")[1])
      var [tilesheetX, tilesheetY] = layer[key]

      ctx.drawImage(
        tilesetImage,
        tilesheetX * 32, tilesheetY * 32,
        sizeOfCrop, sizeOfCrop,
        positionX * 32, positionY * 32,
        sizeOfCrop, sizeOfCrop
      )
    })
  })
}

function getCoords(event) {
  const { x, y } = event.target.getBoundingClientRect();
  const mouseX = event.clientX - x;
  const mouseY = event.clientY - y;
  return [Math.floor(mouseX / 32), Math.floor(mouseY / 32)]
}

tilesetContainer.addEventListener("mousedown", event => {
  selection = getCoords(event)
  tilesetSelection.style.left = selection[0] * sizeOfCrop + "px"
  tilesetSelection.style.top = selection[1] * sizeOfCrop + "px"
})

var isMouseDown = false
canvas.addEventListener("mousedown", () => {
  isMouseDown = true
})
canvas.addEventListener("mouseup", () => {
  isMouseDown = false
})
canvas.addEventListener("mouseleave", () => {
  isMouseDown = false
})
canvas.addEventListener("mousedown", addTile)
canvas.addEventListener("mousemove", event => {
  if (isMouseDown) {
    addTile(event)
  }
})

function addTile(event) {
  var clicked = getCoords(event)
  var key = clicked[0] + "-" + clicked[1]

  if (event.shiftKey) {
    delete layers[currentLayer][key]
  } else {
    layers[currentLayer][key] = [selection[0], selection[1]]
  }

  draw()
}

function setLayer(layer) {
  currentLayer = layer
  var oldActiveLayer = document.querySelector(".editing-layer.active")
  if (oldActiveLayer) {
    oldActiveLayer.classList.remove("active")
  }
  document.querySelector(`[tile-layer="${currentLayer}"]`).classList.toggle("active")
}

function clearCanvas() {
  layers = [{}, {}, {}]
  draw()
}

function exportImage() {
  var data = canvas.toDataURL()
  var image = new Image()
  image.src = data
  var newWindow = window.open("")
  newWindow.document.write(image.outerHTML)

}

tilesetImage.src = "https://assets.codepen.io/21542/TileEditorSpritesheet.2x_2.png"

tilesetImage.onload = () => {
  draw()
  setLayer(0)
}