from tkinter import *
def move_pointer(self, direction, pointer):

        if direction == "left":
            pointer_position = self.pointer1_position if pointer == self.pointer1 else self.pointer2_position
            pointer_position -= 1
        elif direction == "right":
            pointer_position = self.pointer1_position if pointer == self.pointer1 else self.pointer2_position
            pointer_position += 1
        else:
            return

        if pointer == self.pointer1:
            self.pointer1_position = pointer_position
        elif pointer == self.pointer2:
            self.pointer2_position = pointer_position

        x = self.buttons[pointer_position].winfo_x()
        y = self.buttons[pointer_position].winfo_y()
        pointer.place(x=x + 32, y=y + 32) # added 32 steps to original coordinate to centre pointers
