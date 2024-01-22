const divs = document.querySelectorAll('.cell')
divs.forEach(element => {
    element.addEventListener("click", handler);
});

function handler(e) {
    if (e.type == "click") {
      alert("You clicked a cell");
  }
}

//rule of game of life
//case-death rule: if an alive cell has no alive neighbor or exactly one alive neighbor
//   it's gonna die for next generation
//case-alive rule: if an alive cell has exactly two neighbors
//   it's gonna be alive for next generation
//case-birth rule: if a cell has exactly three alive neighbors
//   it's gonna be alive for next generation
