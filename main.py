import tkinter as tk
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        # Create start button
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        # Create reset button
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

        # Create label to display time remaining
        self.time_label = tk.Label(master, text="25:00")
        self.time_label.pack()

        # Set timer duration
        self.duration = 1500 # 25 minutes in seconds
        self.time_remaining = self.duration
        self.is_running = False

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state="disabled")
        self.countdown()

    def reset_timer(self):
        self.time_remaining = self.duration
        self.time_label.config(text="25:00")
        self.start_button.config(state="normal")
        self.is_running = False

    def countdown(self):
        if self.is_running:
            minutes, seconds = divmod(self.time_remaining, 60)
            self.time_label.config(text="{:02}:{:02}".format(minutes, seconds))
            self.time_remaining -= 1
            if self.time_remaining < 0:
                self.reset_timer()
            else:
                self.master.after(1000, self.countdown)

root = tk.Tk()
pomodoro = PomodoroTimer(root)
root.mainloop()
