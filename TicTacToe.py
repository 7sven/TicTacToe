import tkinter as tk

"""
Creates the select screen on which you can chose between the two game modes
"""
select_screen = tk.Tk()
select_screen.title("Tic Tac Toe")
select_screen.geometry("600x600")

"""
creates the single player window and hides it directly at the beginning, so you can't see it
"""
single_player = tk.Tk()
single_player.title("Tic Tac Toe")
single_player.geometry("600x600")
single_player.withdraw()

"""
creates the multi player window and hides it directly at the beginning, so you can't see it
"""
multi_player = tk.Tk()
multi_player.title("Tic Tac Toe")
multi_player.geometry("600x600")
multi_player.withdraw()

"""
a list in which all the nine buttons of tic tac toe are saved
"""
button = []

"""
boolean which shows which player is currently active, since there are only two players booleans are fine, otherwise 
would have used enum or because this i python a dictionary 
"""
player = True

"""
function which handles what it should show when one of the nine tic tac toe buttons is pressed
"""
# TODO  different game modes, check if game ends (yet not included)
def press_button(button_number):
    global player
    if player:
        button[button_number].configure(text="X", state='disabled')
    else:
        button[button_number].configure(text="O", state='disabled')
    player = not player


"""
a function which creates nine buttons
"""
def create_buttons(window):
    global button
    for i in range(9):
        button.append(tk.Button(master=window, width=20, height=8, command=lambda x=i: press_button(x)))
    for i in range(3):
        for j in range(3):
            button[(i * 3) + j].grid(column=i, row=j, sticky="NESW", padx=5, pady=5)


"""
function of what happens when multi player is chosen
"""
def multy_gamemode():
    select_screen.withdraw()
    multi_player.deiconify()
    create_buttons(multi_player)


"""
function so that every window is closed when you click on the cross, the protocols are the caller of the function
"""
def on_closing():
    select_screen.destroy()
    single_player.destroy()
    multi_player.destroy()


select_screen.protocol("WM_DELETE_WINDOW", on_closing)
single_player.protocol("WM_DELETE_WINDOW", on_closing)
multi_player.protocol("WM_DELETE_WINDOW", on_closing)

"""
buttons for each game mode
"""
mulButton = tk.Button(master=select_screen, text="Start multi player", width=40, height=2, command=multy_gamemode)
singButton = tk.Button(master=select_screen, text="Start single player", width=40, height=2)
mulButton.pack()
singButton.pack()

"""
main function. used the if version and not the instant start for if you want to include a python program somewhere else
"""
if __name__ == "__main__":
    select_screen.mainloop()
