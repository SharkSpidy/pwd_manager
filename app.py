import tkinter as tk
from tkinter import messagebox, simpledialog
from encryptor import Encryptor
from store import PasswordStore
from ui import PasswordManagerUI

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        master_pwd = simpledialog.askstring("Master Password", "Enter master password:", show='*')
        if not master_pwd:
            messagebox.showerror("Error", "Master password required!")
            root.destroy()
            return

        self.encryptor = Encryptor(master_pwd)
        self.store = PasswordStore(self.encryptor)
        self.ui = PasswordManagerUI(root)

        # Wire buttons to logic
        self.ui.save_button.config(command=self.save)
        self.ui.view_button.config(command=self.view)

    def save(self):
        s = self.ui.service_var.get()
        u = self.ui.user_var.get()
        p = self.ui.pass_var.get()
        if s and u and p:
            self.store.save(s, u, p)
            messagebox.showinfo("Saved", f"Credentials for {s} saved.")
        else:
            messagebox.showwarning("Missing", "Fill all fields!")

    def view(self):
        self.ui.output.delete(1.0, tk.END)
        data = self.store.load()
        for service, creds in data.items():
            self.ui.output.insert(tk.END, f"{service}: {creds['username']} | {creds['password']}\n")
