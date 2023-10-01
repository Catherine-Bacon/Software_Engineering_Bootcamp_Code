### ASSIGNMENT:

Create a **minesweeper function** which takes in a map of minesweeper locations (#) and outputs a proximity map.

Example of an input:\
[ ["-", "-", "-", "#", "#"],\
["-", "#", "-", "-", "-"],\
["-", "-", "#", "-", "-"],\
["-", "#", "#", "-", "-"],\
["-", "-", "-", "-", "-"] ]

Example of the expected output:\
[ ["1", "1", "2", "#", "#"],\
["1", "#", "3", "3", "2"],\
["2", "4", "#", "2", "0"],\
["1", "#", "#", "2", "0"],\
["1", "2", "2", "1", "0"] ]