document.addEventListener("DOMContentLoaded", () => {

const buttons = document.querySelectorAll(".keyboard-row button");
const game = JSON.parse(document.getElementById('room-name').textContent);

const gameSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/game/'
    + game
    + '/'
);
gameSocket.onopen = function(e) {
    console.log("online")
};
let activePlayer = ''
gameSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if(data.type === 'connected_message'){
        console.log("Recieved connected: "+data.connected);
    }
    console.log("Recieved data: "+data);
    console.log("Recieved message: "+data.message);
    console.log("Recieved user: "+data.user);
    
    //updateBoard(data.letter, data.number)
    activePlayer = data.user
    
};
gameSocket.onclose = function(e) {
    console.error('Socket closed unexpectedly');
};
createBoard()

function createBoard(){
    if(!document.getElementById('64')){
    
        const gameBox = document.getElementById("box-holder");
        let counter = 1
        for (let index = 0; index < 8; index++) {
            
            let box_row = document.createElement("div");
            box_row.classList.add("row");
            box_row.classList.add("justify-content-center");
            box_row.setAttribute("id", "r-"+index);
            gameBox.appendChild(box_row);
            for(let jindex = 0; jindex < 8; jindex++) {
    
                
                let box = document.createElement("div");
                box.classList.add("col");
                box.classList.add("letter-box");
                box.setAttribute("id", counter);
                box_row.appendChild(box);
                counter += 1
                
            }
        }
    }
}



const boxes = document.querySelectorAll(".col.letter-box");


for (let i = 0; i < boxes.length; i++) {
    
    boxes[i].onclick = ({ target }) => {
        let turn_id = document.getElementById("turn-id")
        console.log("active: "+activePlayer)
        console.log("turn_id: "+turn_id.innerHTML)
        if(activePlayer != turn_id.innerHTML){
            if(target.innerHTML == ''){
                const lette = target.getAttribute("id");
                if(document.querySelector(".selected")){
                    selected = document.querySelector(".selected")
                    console.log(selected)
                    selected.innerHTML = ''
                    selected.classList.remove("selected")
                }
                
                
                target.classList.add("selected")
                
                selectedBox(target)
                
                console.log(target.getAttribute("id"))
            }
        }
    };
  }

function selectedBox(box) {

    for (let i = 0; i < buttons.length; i++) {
        buttons[i].onclick = ({ targetButton }) => {
            let turn_id = document.getElementById("turn-id")
            // check if it is player's turn and if the selected box is free
            if(activePlayer != turn_id.innerHTML & !box.classList.contains("player1submitted") & !box.classList.contains("player2submitted")){
                const letter = targetButton.getAttribute("data-key");
    
            if (letter === "enter") {
                submitLetter(box);
                return;
            }
        
            if (letter === "del") {
                deleteLetter();
                return;
            }
            box.innerHTML = letter
            
            console.log(letter)
            }
          
        };
      }
}
function deleteLetter(){
    if(document.querySelector(".selected")){
        selected = document.querySelector(".selected")
        console.log(selected)
        selected.innerHTML = ''
        selected.classList.remove("selected")
    }
}

function submitLetter(mess){
    if(mess.innerHTML != ''){
        let turn = document.getElementById("turn-alert")
        let turn_id = document.getElementById("turn-id")
        const user = turn_id.innerHTML 
        const message = mess.innerHTML
        const number = mess.getAttribute("id")
        let color = ''
        if(turn.innerHTML === "Player 1"){
            color = 'b59f3b'
        }
        if(turn.innerHTML === "Player 2"){
            color = 'b60d0d8c'
        }
        console.log(color)
        const usermessage = 'playtunes'
        gameSocket.send(JSON.stringify({
            'letter': message,
            'number': number,
            'color': color,
            'user': user
        }));


}

}


function updateBoard(letter, number){
    let turn = document.getElementById("turn-alert")
    let updatedbox = document.getElementById(number)
    if(turn.innerHTML === "Player 1"){
        turn.innerHTML = "Player 2"
        turn.style = "background-color: #b60d0d8c;"
        updatedbox.classList.remove("selected")
        updatedbox.innerHTML = letter
        updatedbox.classList.add("player1submitted")
    }
    else{
        turn.innerHTML = "Player 1"
        turn.style = "background-color: #b59f3b;"
        updatedbox.classList.remove("selected")
        updatedbox.innerHTML = letter
        updatedbox.classList.add("player2submitted")
    }
}


  




});