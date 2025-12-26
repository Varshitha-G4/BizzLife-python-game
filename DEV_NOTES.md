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
