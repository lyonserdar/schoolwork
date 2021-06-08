The sudoku puzzle data is stored in "data" folder and "puzzles.json" file.

The file has 4 keys (debug, easy, medium, hard) and each has an array of puzzles and their solutions.

Once the game page is loaded the entire JSON data will be requested and stored in a variable.

Please click the "Toggle Debug" button to see the JSON that retrieved using AJAX.

Here is a sample for how data is stored:

"debug": [
    {
      "puzzle":
        "679518243543729618821634957794352186358461729216897534485276391962183475137945860",
      "solution":
        "679518243543729618821634957794352186358461729216897534485276391962183475137945862"
    }
  ],


To see the changes easily please only change the debug puzzle since there is only once of them.
And select game difficulty "Debug".
The other keys that represent other difficulties have multiple puzzles in the array and the game 
will pick a random one when you start a new game. This will make it harder to see the changes you make.

"puzzle" key is the initial state of the puzzle and "0"s represent empty cells.
"solution" is for giving player feedback if they make a mistake and checking if the game ended.

Ex. 
{
    "puzzle":
        "070000043040009610800634900094052000358460020000800530080070091902100005007040802",
    "solution":
        "679518243543729618821634957794352186358461729216897534485276391962183475137945862"
},


The string length is 81 that represents 9x9 grid.