import tkinter as tk
from tkinter import messagebox
import pygame
import csv
import time
import sys


class WorkoutTimer:
    def __init__(self, root, instructions):
        self.root = root
        self.root.title("Workout Timer")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="", font=("Helvetica", 18))
        self.label.pack(pady=20)

        self.time_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.time_label.pack(pady=10)

        self.start_button = tk.Button(
            root, text="Start Workout", command=self.start_workout
        )
        self.start_button.pack(pady=10)

        self.instructions = instructions
        self.current_instruction = 0
        pygame.mixer.init()

    def start_workout(self):
        self.start_button.pack_forget()
        self.next_instruction()

    def next_instruction(self):
        if self.current_instruction < len(self.instructions):
            instruction, duration = self.instructions[self.current_instruction]
            self.label.config(text=instruction)
            pygame.mixer.music.load("bing.wav")
            pygame.mixer.music.play()
            self.countdown(int(duration))
            self.current_instruction += 1
        else:
            messagebox.showinfo(
                "Workout Complete", "Great job! You've completed the workout."
            )
            self.root.destroy()

    def countdown(self, remaining):
        if remaining >= 0:
            self.time_label.config(text=f"Time remaining: {remaining} seconds")
            self.root.after(1000, self.countdown, remaining - 1)
        else:
            self.next_instruction()


def read_instructions_from_csv(file_path):
    instructions = []
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            instructions.append((row[0], row[1]))
    return instructions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python workout.py <instructions.csv>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    instructions = read_instructions_from_csv(csv_file_path)

    root = tk.Tk()
    app = WorkoutTimer(root, instructions)
    root.mainloop()
