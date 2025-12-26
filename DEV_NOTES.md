## Added scrollable element (ver2)

Problem:
- Game board width exceeded screen width
- Right-side tiles were not visible on smaller screens

Solution:
- Introduced Canvas with game_frame for scrolling
- Redirected widget parenting to game_frame
- Kept keyboard bindings on root window

Key takeaway:
- Canvas + Frame is required for scrollable layouts in Tkinter

## Removed overwriting problem (ver2)

Problem:
- When the money is deducted from bank, if the money changes from, for example 4 digit to 3 digit, the values of the previous number was shown since it was overwriting

Solution:
- Created a new array to store the updated values
- Takes the values from the array and renders on the screen instead of overwriting

## Bank: History storage (ver2)

Problem:
- Bank had to be minimized everytime after updating since it was not able to store history

Solution:
- Changed money = [50000, 50000] as a global variable in money_update.py
- It now stores even after closing the bank window

