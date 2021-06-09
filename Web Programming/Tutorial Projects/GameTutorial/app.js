let userScore = 0
let aiScore = 0
const userScore_span = document.getElementById("user-score")
const aiScore_span = document.getElementById("ai-score")
const scoreBoard_div = document.querySelector(".score-board")
const result_p = document.querySelector('.result p')
const rock_div = document.getElementById("rock")
const paper_div = document.getElementById("paper")
const scissors_div = document.getElementById("scissors")

const getAIChoice = () => {
  const choices = ["rock", "paper", "scissors"]
  const randomNumber = Math.floor(Math.random() * 3)
  return choices[randomNumber]
}

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

const userWins = (userChoice, aiChoice) => {
  userScore++
  userScore_span.innerHTML = userScore
  aiScore_span.innerHTML = aiScore
  result_p.innerHTML = `${capitalizeFirstLetter(userChoice)} beats ${aiChoice}. You win!`
  document.getElementById(userChoice).classList.add("green-glow")
  setTimeout(() => {
    document.getElementById(userChoice).classList.remove("green-glow")
  }, 300)
}

const userLoses = (userChoice, aiChoice) => {
  aiScore++
  userScore_span.innerHTML = userScore
  aiScore_span.innerHTML = aiScore
  result_p.innerHTML = `${capitalizeFirstLetter(userChoice)} loses to ${aiChoice}. You lose!`
  document.getElementById(userChoice).classList.add("red-glow")
  setTimeout(() => {
    document.getElementById(userChoice).classList.remove("red-glow")
  }, 300)
}

const userDraws = (userChoice, aiChoice) => {
  result_p.innerHTML = `${capitalizeFirstLetter(userChoice)} ties to ${aiChoice}. You draw!`
  document.getElementById(userChoice).classList.add("gray-glow")
  setTimeout(() => {
    document.getElementById(userChoice).classList.remove("gray-glow")
  }, 300)
}

const game = (userChoice) => {
  const aiChoice = getAIChoice()
  switch (userChoice + aiChoice) {
    case "rockscissors":
    case "paperrock":
    case "scissorspaper":
      userWins(userChoice, aiChoice)
      break
    case "rockpaper":
    case "paperscissors":
    case "scissorsrock":
      userLoses(userChoice, aiChoice)
      break
    case "rockrock":
    case "paperpaper":
    case "scissorsscissors":
      userDraws(userChoice, aiChoice)
      break
  }
}

const main = () => {
  rock_div.addEventListener("click", () => {
    game("rock")
  })

  paper_div.addEventListener("click", () => {
    game("paper")
  })

  scissors_div.addEventListener("click", () => {
    game("scissors")
  })
}

main()