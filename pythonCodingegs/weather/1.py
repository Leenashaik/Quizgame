import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is Python's primary design philosophy?",
        "options": ["A) Explicit is better than implicit.", "B) Readability counts.", "C) Complex is better than simple.", "D) There should be one-- and preferably only one --obvious way to do it."],
        "correct_answer": "B) Readability counts."
    },
    {
        "question": "Which statement is used to exit a loop prematurely in Python?",
        "options": ["A) break", "B) continue", "C) return", "D) exit"],
        "correct_answer": "A) break"
    },
    {
        "question": "What is the result of `2 + '3'` in Python?",
        "options": ["A) 5", "B) '23'", "C) TypeError", "D) 32"],
        "correct_answer": "C) TypeError"
    },
    {
        "question": "How do you define a function in Python?",
        "options": ["A) def my_function():", "B) function my_function():", "C) define my_function():", "D) func my_function():"],
        "correct_answer": "A) def my_function():"
    },
    {
        "question": "Which of the following is an example of a mutable data type in Python?",
        "options": ["A) int", "B) float", "C) str", "D) list"],
        "correct_answer": "D) list"
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Game")
        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        self.root.destroy()
        quiz_window = tk.Tk()
        app = QuizGame(quiz_window, name)

class QuizGame:
    def __init__(self, root, name):
        self.root = root
        self.root.title("Python Quiz Game")
        self.name = name
        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            button.config(fg="yellow", bg="red")
            button.pack()
            self.option_buttons.append(button)

        self.load_question()

    def load_question(self):
        if self.current_question < len(questions):
            question_data = questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
        else:
            self.show_score()

    def check_answer(self, selected_option):
        question_data = questions[self.current_question]
        if question_data["options"][selected_option] == question_data["correct_answer"]:
            self.score += 1

        self.current_question += 1
        self.load_question()

    def show_score(self):
        if self.score == 5:
            message = f"Excellent, {self.name}! You got a perfect score of 5/5."
        else:
            message = f"Better Luck Next Time, {self.name}. Your score is: {self.score}/{len(questions)}"
        messagebox.showinfo("Quiz Completed", message)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
