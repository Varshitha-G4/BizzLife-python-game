from tkinter import *
def click_rules():
    win=Toplevel()
    
    # Get screen dimensions
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    
    # Window dimensions
    window_width = 990
    window_height = 730
    
    # Calculate center position
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    # Set window size and position
    win.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    cv=Canvas(win, height=730, width=990)
    filename=PhotoImage(file="images\Rules.png")
    image=cv.create_image(10, 10, anchor=NW, image=filename)
    cv.pack()
    
    # Keep reference to prevent garbage collection
    cv.image = filename
    
    win.mainloop()