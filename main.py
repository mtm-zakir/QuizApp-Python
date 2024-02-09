import tkinter as tk
from tkinter import messagebox

from quiz_data import quiz_data  # Assuming quiz_data is imported from an external file


# Function to display the current question and choices
def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")


# Function to check the selected answer and provide feedback
def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice]["text"]

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text="Incorrect!", fg="red")

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")


# Function to move to the next question
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()


# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")

# Create the question label
qs_label = tk.Label(
    root,
    anchor="center",
    wraplength=500,
    font=("Helvetica", 20),
    pady=10
)
qs_label.pack()

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = tk.Button(
        root,
        font=("Helvetica", 16),
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = tk.Label(
    root,
    anchor="center",
    font=("Helvetica", 16),
    pady=10
)
feedback_label.pack()

# Initialize the score
score = 0

# Create the score label
score_label = tk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    font=("Helvetica", 16),
    pady=10
)
score_label.pack()

# Create the next button
next_btn = tk.Button(
    root,
    text="Next",
    font=("Helvetica", 16),
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()
