import tkinter as tk

def hello():
    print("Hello!")

def about():
    print("This is a simple menu example.")

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("Menu with Submenu Example")

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create a "File" menu with submenus
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=hello)
file_menu.add_command(label="Open", command=hello)
file_menu.add_separator()  # Adds a separator line
file_menu.add_command(label="Exit", command=quit_app)

# Create a "Help" menu with submenus
help_menu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

root.mainloop()
