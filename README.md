# connect-word
A connect 4 and wordle-like board game.

## How To Play
The board consists of 8 x 8 squares.

Each player gets a turn placing a letter in a square by selecting on the square and selecting a letter.

The game is over if a player can make a 3 or more letters English word using only letters placed by the players.

The role of the other players is to stop each other from building a word while trying to build a word first.

The word can be horizontal, vertical, diagonal or reverse diagonal.

Unfortunately the game cannot yet automatically detect a win, the players will have to alert each other of a win.

Any player can start First.

Win example

![win](https://github.com/playtunes100/connect-word/blob/20da55b521868d01d4bbe68e9acceb84e2e9bd36/images/win.png)

Not win example

![Not win!](https://github.com/playtunes100/connect-word/blob/20da55b521868d01d4bbe68e9acceb84e2e9bd36/images/lose.png)

## How to install
clone the repo
`git clone https://github.com/playtunes100/connect-word.git`

pull docker image from dockerhub
`docker pull playtunes/connectword-0.2`.

or build the image
`docker build -t connectword-0.2 .`.

run `docker compose up -d`
visit `localhost:8001`.

