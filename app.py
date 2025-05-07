import tkinter as tk
from tkinter import messagebox, simpledialog
from encryptor import Encryptor
from store import PasswordStore

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Password Manager")
        master_pwd = simpledialog.askstring("Master Password", "Enter master password:", show='*')

        if not master_pwd:
            messagebox.showerror("Error", "Master password required!")
            root.destroy()
            return

        self.encryptor = Encryptor(master_pwd)
        self.store = PasswordStore(self.encryptor)

        self.service_var = tk.StringVar()
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        tk.Label(root, text="Service").pack()
        tk.Entry(root, textvariable=self.service_var).pack()

        tk.Label(root, text="Username").pack()
        tk.Entry(root, textvariable=self.user_var).pack()

        tk.Label(root, text="Password").pack()
        tk.Entry(root, textvariable=self.pass_var, show='*').pack()

        tk.Button(root, text="Save", command=self.save).pack(pady=5)
        tk.Button(root, text="View All", command=self.view).pack()

        self.output = tk.Text(root, height=10, width=50)
        self.output.pack(pady=10)

    def save(self):
        s = self.service_var.get()
        u = self.user_var.get()
        p = self.pass_var.get()
        if s and u and p:
            self.store.save(s, u, p)
            messagebox.showinfo("Saved", f"Credentials for {s} saved.")
        else:
            messagebox.showwarning("Missing", "Fill all fields!")

    def view(self):
        self.output.delete(1.0, tk.END)
        data = self.store.load()
        for service, creds in data.items():
            self.output.insert(tk.END, f"{service}: {creds['username']} | {creds['password']}\n")

