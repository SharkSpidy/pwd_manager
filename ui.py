import tkinter as tk
from tkinter import ttk

class PasswordManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Password Manager")
        self.service_var = tk.StringVar()
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        self.build_widgets()

    def build_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Service:").grid(row=0, column=0, sticky="w", pady=2)
        ttk.Entry(frame, textvariable=self.service_var).grid(row=0, column=1, sticky="ew")

        ttk.Label(frame, text="Username:").grid(row=1, column=0, sticky="w", pady=2)
        ttk.Entry(frame, textvariable=self.user_var).grid(row=1, column=1, sticky="ew")

        ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky="w", pady=2)
        ttk.Entry(frame, textvariable=self.pass_var, show="*").grid(row=2, column=1, sticky="ew")

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.save_button = ttk.Button(button_frame, text="Save")
        self.save_button.grid(row=0, column=0, padx=5)

        self.view_button = ttk.Button(button_frame, text="View All")
        self.view_button.grid(row=0, column=1, padx=5)

        self.output = tk.Text(frame, height=10, wrap="word")
        self.output.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

        scroll = ttk.Scrollbar(frame, command=self.output.yview)
        scroll.grid(row=4, column=2, sticky="ns")
        self.output.config(yscrollcommand=scroll.set)

        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(4, weight=1)
