let tableDiv = document.getElementById("tileset-container")

const TILES = {
  0: "./assets/Grass.png",
  1: "./assets/Shore.png",
  2: "./assets/Highlighted-Boxes.png"
}

function createTilesTable(rows, columns) {
  let table = document.createElement("table")
  let tbody = document.createElement("tbody")
  table.appendChild(tbody)
  for (var row = 0; row < rows; row++) {
    let tr = document.createElement("tr")
    tr.classList.add("table-row")
    tbody.appendChild(tr)
    for (var column = 0; column < columns; column++) {
      let td = document.createElement("td")
      td.classList.add("table-cell")

      var image = document.createElement("img")
      image.src = TILES[row]
      image.classList.add(`tile-image`)
      image.style.left = `${column * -100}px`
      image.style.top = "0px"

      td.appendChild(image)
      tr.appendChild(td)
    }
  }
  tableDiv.appendChild(table)
  console.log("Table Created!")
}

window.onload = () => {
  console.log("Page Loaded!")
  createTilesTable(Object.keys(TILES).length, 5)
}

