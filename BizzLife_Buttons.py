from tkinter import *



def create_buttons(self):
    self.buttons = []
    #dimensions of where the grid buttons should be placed

    positions = [
        (0, 613), (104, 613), (104, 517), (104, 421),
        (104, 325), (104, 229), (104, 133), (104, 37),
        (209, 37), (314, 37), (314, 133), (314, 229),
        (314, 325), (314, 421), (314, 517), (314, 613),
        (418, 613), (522, 613), (522, 517), (522, 421),
        (522, 325), (522, 229), (522, 133), (522, 37),
        (626, 37), (730, 37), (730, 133), (730, 229),
        (730, 325), (730, 421), (730, 517), (730, 613),
        (835, 613), (940, 613), (940, 517), (940, 421),
        (940, 325), (940, 229), (940, 133), (940, 37),
        (1044, 37), (1148, 37), (1148, 133), (1148, 229),
        (1148, 325), (1148, 421), (1148, 517), (1148, 613),
        (1252, 613), (1356, 613), (1356, 517), (1356, 421),
        (1356, 325), (1356, 229), (1356, 133), (1356, 37),
        (1460, 37)
    ]

    for i, position in enumerate(positions):
        button = Button(fg="black", bg="#f15874", height=5, width=12, padx=5, pady=5,
                        command=lambda i=i: self.button_click(i + 1))

        # Change the color of every 3rd button to yellow
        if (i + 1) % 3 == 0:

            button.config(bg="yellow")
        elif (i + 2) % 3 == 0:
            button.config(bg="#53E835")

        button.place(x=position[0], y=position[1])
        #adding the positions to a new list to form grids

        self.buttons.append(button)

