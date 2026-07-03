import tkinter as tk
from tkinter import messagebox

class Questions:

    questions = [

        {
            "question": "Which language is mainly used for AI?",
            "options": [
                "Python",
                "HTML",
                "CSS",
                "XML"
            ],
            "answer": "Python"
        },

        {
            "question": "Which keyword is used for loop?",
            "options": [
                "for",
                "stop",
                "break",
                "pass"
            ],
            "answer": "for"
        },

        {
            "question": "GUI full form?",
            "options": [
                "Graphical User Interface",
                "General User Internet",
                "Graphic Uniform Input",
                "None"
            ],
            "answer": "Graphical User Interface"
        },
        {
            "questions":"File extension for python files?",
            "options":[
                ".pt",
                ".python",
                ".py",
                ".pyt"
            ],
            "answer":".py"
        },
        {
            "question":"Which keyword is used to print output in Python?",
            "options":[
                "echo",
                "display",
                "show",
                "print",
            ],
            "answer":"print"
        },
       
        
    ]

    @classmethod
    def quest(cls):

        return cls.questions


root = tk.Tk()

root.title("Advanced Quiz App")

root.geometry("700x500")

root.config(bg="#0f172a")

score = 0

question_no = 0

time_left = 15

questions = Questions.quest()

selected = tk.StringVar()

title = tk.Label(
    root,
    text="⚡ ADVANCED QUIZ APPLICATION ⚡",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="cyan"
)

title.pack(pady=20)

score_label = tk.Label(
    root,
    text="Score : 0",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="white"
)

score_label.pack()

timer_label = tk.Label(
    root,
    text="Time Left : 15",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="yellow"
)

timer_label.pack(pady=10)

frame = tk.Frame(
    root,
    bg="#1e293b",
    padx=20,
    pady=20
)

frame.pack(pady=20)

question_label = tk.Label(
    frame,
    text="",
    font=("Arial", 18, "bold"),
    wraplength=500,
    bg="#1e293b",
    fg="white"
)

question_label.pack(pady=20)

option1 = tk.Radiobutton(
    frame,
    text="",
    variable=selected,
    value="",
    font=("Arial", 14),
    bg="#1e293b",
    fg="cyan",
    selectcolor="#334155"
)

option1.pack(anchor="w", pady=5)

option2 = tk.Radiobutton(
    frame,
    text="",
    variable=selected,
    value="",
    font=("Arial", 14),
    bg="#1e293b",
    fg="cyan",
    selectcolor="#334155"
)

option2.pack(anchor="w", pady=5)

option3 = tk.Radiobutton(
    frame,
    text="",
    variable=selected,
    value="",
    font=("Arial", 14),
    bg="#1e293b",
    fg="cyan",
    selectcolor="#334155"
)

option3.pack(anchor="w", pady=5)

option4 = tk.Radiobutton(
    frame,
    text="",
    variable=selected,
    value="",
    font=("Arial", 14),
    bg="#1e293b",
    fg="cyan",
    selectcolor="#334155"
)

option4.pack(anchor="w", pady=5)


def timer():

    global time_left

    timer_label.config(
        text="Time Left : " + str(time_left)
    )

    if time_left > 0:

        time_left -= 1

        root.after(1000, timer)

    else:

        messagebox.showwarning(
            "Time Up",
            "Next Question"
        )

        next_question()


def show_question():

    global question_no
    global time_left

    time_left = 15

    q = questions[question_no]

    question_label.config(
        text=q["question"]
    )

    option1.config(
        text=q["options"][0],
        value=q["options"][0]
    )

    option2.config(
        text=q["options"][1],
        value=q["options"][1]
    )

    option3.config(
        text=q["options"][2],
        value=q["options"][2]
    )

    option4.config(
        text=q["options"][3],
        value=q["options"][3]
    )

    selected.set("")

    timer()


def check_answer():

    global score

    user_answer = selected.get()

    correct = questions[question_no]["answer"]

    if user_answer == correct:

        score += 1

        score_label.config(
            text="Score : " + str(score)
        )

        messagebox.showinfo(
            "Correct",
            "Awesome! Correct Answer"
        )

    else:

        messagebox.showerror(
            "Wrong",
            "Wrong Answer"
        )

    next_question()


def next_question():

    global question_no

    question_no += 1

    if question_no < len(questions):

        show_question()

    else:

        finish_quiz()


def finish_quiz():

    if score == len(questions):

        msg = "🏆Excellent Performance"

    elif score >= 2:

        msg = "🔥Good Job"

    else:

        msg = "🙂Keep Practicing"

    messagebox.showinfo(
        "Quiz Finished",
        "Final Score : "
        + str(score)
        + "\n"
        + msg
    )

    root.destroy()


submit_btn = tk.Button(
    root,
    text="SUBMIT ANSWER",
    font=("Arial", 16, "bold"),
    bg="cyan",
    fg="black",
    padx=20,
    pady=10,
    command=check_answer
)

submit_btn.pack(pady=20)

show_question()

root.mainloop()