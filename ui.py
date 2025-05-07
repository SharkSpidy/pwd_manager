import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class PasswordManagerUI:
    def __init__(self, root, save_callback, view_callback):
        self.root = root
        self.root.title("🔐 Password Manager")
        self.root.geometry("400x400")
        self.save_callback = save_callback
        self.view_callback = view_callback

        self.service_var = tk.StringVar()
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        form_frame = ttk.LabelFrame(self.root, text="Add Credentials")
        form_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(form_frame, text="Service:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(form_frame, textvariable=self.service_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Username:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(form_frame, textvariable=self.user_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Password:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(form_frame, textvariable=self.pass_var, show='*').grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(form_frame, text="Save", command=self.save_callback).grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(self.root, text="View Saved Passwords", command=self.view_callback).pack(pady=5)

        output_frame = ttk.LabelFrame(self.root, text="Stored Credentials")
        output_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.output = tk.Text(output_frame, height=10, wrap="word")
        self.output.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(output_frame, command=self.output.yview)
        scrollbar.pack(side="right", fill="y")
        self.output.config(yscrollcommand=scrollbar.set)

    def get_input(self):
        return self.service_var.get(), self.user_var.get(), self.pass_var.get()

    def clear_inputs(self):
        self.service_var.set("")
        self.user_var.set("")
        self.pass_var.set("")

    def show_output(self, text):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, text)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def show_warning(self, title, message):
        messagebox.showwarning(title, message)
