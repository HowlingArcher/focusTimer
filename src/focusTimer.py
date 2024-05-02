# # #!/usr/bin/env python3

# import tkinter as tk
# import webbrowser
# import sys
# from tkinter import messagebox

# # Global variables
# root = None
# about_label = None
# about_label2 = None
# username_label = None
# about_button = None
# go_back_button = None
# start_timer_button = None
# canvas = None
# circle = None
# timer_started = False

# def callback(url):
#     webbrowser.open_new(url)

# def start_timer():
#     global start_timer_button, timer_started, circle

#     timer_started = True
#     start_timer_button.config(text="Timer Started!", state="disabled", bg="red", fg="white", cursor="arrow")
#     draw_circle()

#     wait(5)

# def wait(minutes):
#     global timer_started
#     update_window_title(root.title())

#     # Wait for the specified number of minutes
#     root.after(minutes * 1000 * 60, end_timer)

# def update_window_title(page):
#     global root, timer_started
#     if "| Focus Timer" in page:
#         page = page.split("|")[0].strip()
#     if "Focus Timer - ACTIVE" in page:
#         page = page.split("|")[0].strip()
#     if timer_started:
#         root.title(f"{page} | Focus Timer - ACTIVE")
#     else:
#         root.title(f"{page} | Focus Timer")


# def end_timer():
#     global start_timer_button, timer_started, circle

#     timer_started = False
#     start_timer_button.config(text="Start break!", state="normal", bg="#555", fg="white", cursor="hand2")
#     canvas.itemconfig(circle, fill="lime", outline="lime")
    
#     update_window_title(root.title())
#     show_popup()

# def show_popup():
#     messagebox.showinfo("Time's up!", "Time's up! Your break is over. Get back to work!")

# # Function to draw a red circle on the canvas
# def draw_circle():
#     global circle
#     canvas.itemconfig(circle, fill="red")

# def update_circle():
#     global circle
#     if timer_started:
#         canvas.itemconfig(circle, fill="red")
#     else:
#         canvas.itemconfig(circle, fill="lime")
#     title = root.title()
#     update_window_title(title or "home")

# # Function to show the about information in the main window
# def show_info(show_about_info):
#     global about_label, about_label2, username_label, about_button, go_back_button
    
#     if show_about_info:
#         root.title("About")
#         about_label.config(text="Focus Timer", font=("Helvetica", 20), bg="#222", fg="white")
#         about_label2.config(text="This is a simple application designed to help you manage your time effectively.\n\nVersion 1.0\n\nDeveloped by:", bg="#222", fg="white")
#         username_label.config(text="HowlingArcher", fg="cyan", cursor="hand2")
#         username_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/HowlingArcher"))
#     else:
#         root.title("Home")
#         about_label.config(text="", bg="#222")
#         about_label2.config(text="", bg="#222")
#         username_label.config(text="", bg="#222")
    
#     # Toggle visibility of buttons and labels
#     if show_about_info:
#         about_button.pack_forget()
#         go_back_button.pack(side=tk.LEFT, padx=5)  # Add go_back_button to button_frame
#         username_label.pack()
#     else:
#         about_button.pack(side=tk.LEFT, padx=5)
#         go_back_button.pack_forget()
#         username_label.pack_forget()
    
#     update_window_title("About" if show_about_info else "Home")

# # Function to save the data and quit the application
# def save_and_quit():
#     result = messagebox.askquestion("Quit Confirmation", "Are you sure you want to quit?\nWe will stop reminding you about getting back to work.")
#     if result == "yes":
#         sys.exit()
#     else:
#         return

# def main():
#     global root, about_button, go_back_button, about_label, about_label2, username_label, start_timer_button, canvas, circle

#     root = tk.Tk()
#     root.title("Home")

#     icon = tk.PhotoImage(file="src/favicon.ico")
#     root.call('wm', 'iconphoto', root._w, icon)

#     root.geometry("500x300")  # Set default width to 500 pixels
#     root.minsize(500, 300)    # Set minimum size

#     # Set background color
#     root.configure(bg="#222")

#     # Create a colored frame for the main content
#     main_frame = tk.Frame(root, bg="#222")
#     main_frame.pack(expand=True, fill=tk.BOTH)
    
#     # Create a frame to contain the buttons
#     button_frame = tk.Frame(main_frame, bg="#222")
#     button_frame.pack(side=tk.TOP, pady=20)

#     # Create a frame to contain both the canvas and the about button
#     canvas_and_button_frame = tk.Frame(main_frame, bg="#222")
#     canvas_and_button_frame.pack(side=tk.TOP, padx=5, pady=20)

#     # Create a canvas to draw the circle
#     canvas = tk.Canvas(canvas_and_button_frame, width=30, height=30, bg="#222", highlightthickness=0)
#     canvas.pack(side=tk.LEFT)  # Pack canvas to the left within the frame

#     # Draw initial circle
#     circle = canvas.create_oval(5, 5, 25, 25, fill="lime")

#     # Create the about button
#     about_button = tk.Button(canvas_and_button_frame, text="About", command=lambda: show_info(True), bg="#333", fg="white")
#     about_button.pack(side=tk.RIGHT, padx=5)

#     go_back_button = tk.Button(canvas_and_button_frame, text="Go Back", command=lambda: show_info(False), bg="#333", fg="white")
#     go_back_button.pack(side=tk.LEFT, padx=5)  # Add go_back_button to button_frame

#     # Create the start timer button
#     start_timer_button = tk.Button(canvas_and_button_frame, text="Start break!", bg="lime", fg="black", cursor="hand2", command=start_timer)
#     start_timer_button.pack(side=tk.RIGHT)

#     about_label = tk.Label(main_frame, text="", bg="#222")
#     about_label.pack(pady=20)
#     about_label.config(font=("Helvetica", 12), bg="#222", fg="white")

#     about_label2 = tk.Label(main_frame, text="", bg="#222")
#     about_label2.pack(pady=20)
#     about_label2.config(bg="#222", fg="white")

#     # Label to display username
#     username_label = tk.Label(main_frame, text="", bg="#222")
#     username_label.pack()
#     username_label.config(bg="#222", fg="white")

#     # Call show_info() to display the default information at startup
#     show_info(False)

#     # Bind the window closing event to save_and_quit
#     root.protocol("WM_DELETE_WINDOW", save_and_quit)

#     # Schedule update of circle every 100 milliseconds
#     root.after(100, update_circle)

#     root.mainloop()

# if __name__ == "__main__":
#     main()


#!/usr/bin/env python3

import tkinter as tk
import webbrowser
import sys
from tkinter import messagebox

class FocusTimerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Home")
        self.root.geometry("500x300")
        self.root.minsize(500, 300)
        self.root.configure(bg="#222")
        self.timer_started = False
        self.create_widgets()
        self.update_circle()

    def create_widgets(self):
        self.create_main_frame()
        self.create_canvas_and_buttons()
        self.create_labels()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root, bg="#222")
        self.main_frame.pack(expand=True, fill=tk.BOTH)

    def create_canvas_and_buttons(self):
        self.canvas_and_button_frame = tk.Frame(self.main_frame, bg="#222")
        self.canvas_and_button_frame.pack(side=tk.TOP, padx=5, pady=20)

        self.canvas = tk.Canvas(self.canvas_and_button_frame, width=30, height=30, bg="#222", highlightthickness=0)
        self.canvas.pack(side=tk.LEFT)

        self.circle = self.canvas.create_oval(5, 5, 25, 25, fill="lime")

        self.about_button = tk.Button(self.canvas_and_button_frame, text="About", command=self.show_about_info, bg="#333", fg="white")
        self.about_button.pack(side=tk.RIGHT, padx=5)

        self.go_back_button = tk.Button(self.canvas_and_button_frame, text="Go Back", command=self.show_home, bg="#333", fg="white")
        self.start_timer_button = tk.Button(self.canvas_and_button_frame, text="Start break!", bg="lime", fg="black", cursor="hand2", command=self.start_timer)
        self.start_timer_button.pack(side=tk.RIGHT)

    def create_labels(self):
        self.about_label = tk.Label(self.main_frame, text="", bg="#222", font=("Helvetica", 12), fg="white")
        self.about_label.pack(pady=20)

        self.about_label2 = tk.Label(self.main_frame, text="", bg="#222", fg="white")
        self.about_label2.pack(pady=20)

        self.username_label = tk.Label(self.main_frame, text="", bg="#222", fg="white")

    def show_about_info(self):
        self.root.title("About")
        self.about_label.config(text="Focus Timer", font=("Helvetica", 20), bg="#222", fg="white")
        self.about_label2.config(text="This is a simple application designed to help you manage your time effectively.\n\nVersion 1.0\n\nDeveloped by:", bg="#222", fg="white")
        self.username_label.config(text="HowlingArcher", fg="cyan", cursor="hand2")
        self.username_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/HowlingArcher"))
        self.about_button.pack_forget()
        self.go_back_button.pack(side=tk.LEFT, padx=5)
        self.username_label.pack()
        self.update_window_title("About")

    def show_home(self):
        self.root.title("Home")
        self.about_label.config(text="", bg="#222")
        self.about_label2.config(text="", bg="#222")
        self.username_label.config(text="", bg="#222")
        self.about_button.pack(side=tk.LEFT, padx=5)
        self.go_back_button.pack_forget()
        self.username_label.pack_forget()
        self.update_window_title("Home")

    def start_timer(self):
        self.timer_started = True
        self.start_timer_button.config(text="Timer Started!", state="disabled", bg="red", fg="white", cursor="arrow")
        self.draw_circle()
        self.root.after(5 * 60*1000, self.end_timer)

    def draw_circle(self):
        self.canvas.itemconfig(self.circle, fill="red")

    def update_circle(self):
        fill_color = "red" if self.timer_started else "lime"
        self.canvas.itemconfig(self.circle, fill=fill_color)
        self.update_window_title(self.root.title() or "Home")
        self.root.after(100, self.update_circle)

    def end_timer(self):
        self.timer_started = False
        self.start_timer_button.config(text="Start break!", state="normal", bg="#555", fg="white", cursor="hand2")
        self.canvas.itemconfig(self.circle, fill="lime")
        self.update_window_title(self.root.title())
        self.show_popup()

    # def show_popup(self):
    #     messagebox.showinfo("Time's up!", "Time's up! Your break is over. Get back to work!")

    def show_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Time's up!")
        popup.geometry("300x100")
        popup.configure(bg="#222")
        popup_label = tk.Label(popup, text="Time's up! Your break is over. Get back to work!", bg="#222", fg="white")
        popup_label.pack(pady=20)
        popup.focus_set()  # Set focus to the popup window
        popup.grab_set()   # Grab the focus so the user cannot interact with other windows
        popup.transient(self.root)  # Set the popup window as transient to the main window
        popup.attributes('-topmost', 'true')  # Make the popup window appear on top
        popup_button = tk.Button(popup, text="OK", command=popup.destroy, bg="#333", fg="white")
        popup_button.pack(pady=10)

    def update_window_title(self, page):
        if "| Focus Timer" in page:
            page = page.split("|")[0].strip()
        if "Focus Timer - ACTIVE" in page:
            page = page.split("|")[0].strip()
        if self.timer_started:
            self.root.title(f"{page} | Focus Timer - ACTIVE")
        else:
            self.root.title(f"{page} | Focus Timer")

    def save_and_quit(self):
        result = messagebox.askquestion("Quit Confirmation", "Are you sure you want to quit?\nWe will stop reminding you about getting back to work.")
        if result == "yes":
            sys.exit()

def main():
    app = FocusTimerApp()
    app.root.protocol("WM_DELETE_WINDOW", app.save_and_quit)
    app.root.mainloop()

if __name__ == "__main__":
    main()
