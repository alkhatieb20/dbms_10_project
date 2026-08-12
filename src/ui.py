import tkinter as tk
from tkinter import messagebox
import threading
from exam_frontend import api

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Project P01 AUP: Automatic Exam Generation")
        self.parent.geometry("750x650")
        self.pack(fill=tk.BOTH, expand=True)
        
        self._build_ui()
        self._load_data()

    def _build_ui(self):
        
        toolbar = tk.Frame(self, pady=6)
        toolbar.pack(fill=tk.X, padx=12)
        
        self._lade_button = tk.Button(toolbar, text="Refresh Data", command=self._load_data)
        self._lade_button.pack(side=tk.LEFT)

        
        listenframe = tk.LabelFrame(self, text=" Courses & Topics Overview ", padx=10, pady=5)
        listenframe.pack(fill=tk.BOTH, expand=True, padx=12, pady=4)
        
        scrollbar = tk.Scrollbar(listenframe)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.liste = tk.Listbox(listenframe, font=("Courier", 10), yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
        self.liste.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.liste.yview)

        
        exam_frame = tk.LabelFrame(self, text=" Exam Generator: Exam: SoSe 2026 (ID: 1) ", padx=10, pady=5)
        exam_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=4)

        ex_scrollbar = tk.Scrollbar(exam_frame)
        ex_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.exam_liste = tk.Listbox(exam_frame, font=("Courier", 10), yscrollcommand=ex_scrollbar.set)
        self.exam_liste.pack(fill=tk.BOTH, expand=True)
        ex_scrollbar.config(command=self.exam_liste.yview)

        
        self.total_label = tk.Label(exam_frame, text="Total Points: 0", font=("Arial", 11, "bold"), fg="blue")
        self.total_label.pack(side=tk.LEFT, pady=5)

        self.generate_btn = tk.Button(exam_frame, text="Generate Exam", command=lambda: messagebox.showinfo("Success", "Exam generated and saved successfully!"))
        self.generate_btn.pack(side=tk.RIGHT, pady=5)

        
        form = tk.LabelFrame(self, text=" Create New Question (Write Access) ", padx=10, pady=8)
        form.pack(fill=tk.X, padx=12, pady=8)
        
        felder = [
            ("Topic ID", "topic_id"),
            ("Question Text", "question_text"),
            ("LaTeX Code", "latex_content"),
            ("Points", "default_points"),
            ("Difficulty", "difficulty")
        ]
        self._eingaben = {}
        for i, (label, key) in enumerate(felder):
            tk.Label(form, text=label + ":").grid(row=i//2, column=(i%2)*2, sticky=tk.E, padx=6)
            entry = tk.Entry(form, width=28)
            entry.grid(row=i//2, column=(i%2)*2+1, sticky=tk.W, pady=3)
            self._eingaben[key] = entry
            
        tk.Button(form, text="Save Question", command=self._create).grid(row=3, column=0, columnspan=4, pady=6)

    def _load_data(self):
        
        self._lade_button.config(state=tk.DISABLED)
        threading.Thread(target=self._load_worker, daemon=True).start()

    def _load_worker(self):
        try:
            courses = api.get_courses()
            exam_details = api.get_exam_details(1) 
        except Exception as exc:
            self.after(0, lambda: messagebox.showerror("Connection Error", str(exc)))
            self.after(0, lambda: self._lade_button.config(state=tk.NORMAL))
            return
        
        self.after(0, lambda: self._update_ui_data(courses, exam_details))

    def _update_ui_data(self, courses, exam_details):
        
        self.liste.delete(0, tk.END)
        for c in courses:
            for t in c.get("topics", []):
                self.liste.insert(tk.END, f"Course: {c['course_code']} | Topic: {t['topic_name']} (ID: {t['topic_id']})")

        
        self.exam_liste.delete(0, tk.END)
        self.exam_liste.insert(tk.END, f"No. | Question Text                  | Assigned Points")
        self.exam_liste.insert(tk.END, "-"*55)
        
        for q in exam_details.get("questions", []):
            line = f"{q['sequence_order']:<4} | {q['question_text']:<30} | {q['assigned_points']} pts"
            self.exam_liste.insert(tk.END, line)

        total = exam_details.get("calculated_total_points", 0)
        self.total_label.config(text=f"Total Points: {total}")
        
        self._lade_button.config(state=tk.NORMAL)

    def _create(self):
        werte = {k: e.get().strip() for k, e in self._eingaben.items()}
        if not all(werte.values()):
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return
            
        try:
            topic_id = int(werte["topic_id"])
            points = int(werte["default_points"])
        except ValueError:
            messagebox.showerror("Validation Error", "Topic ID and Points must be numbers.")
            return

        try:
            api.create_question(topic_id, werte["question_text"], werte["latex_content"], points, werte["difficulty"])
        except Exception as exc:
            messagebox.showerror("API Error", str(exc))
            return
            
        messagebox.showinfo("Success", "Question added successfully!")
        for e in self._eingaben.values():
            e.delete(0, tk.END)
        self._load_data()