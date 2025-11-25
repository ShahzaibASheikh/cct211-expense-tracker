import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.root = root
        self.app = app
        self.build_ui()

    def build_ui(self):
        self.root.title("Expense Tracker - Login")
        self.pack(padx=20, pady=20)

        tk.Label(self, text="Username").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(self, width=25)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self, text="Password").grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self, show="*", width=25)
        self.password_entry.grid(row=1, column=1)

        tk.Button(self, text="Login", width=12, command=self.login).grid(row=2, column=0, pady=10)
        tk.Button(self, text="Register", width=12, command=self.register).grid(row=2, column=1)

    def login(self):
        u = self.username_entry.get().strip()
        p = self.password_entry.get().strip()

        if not u or not p:
            messagebox.showerror("Error", "Fill in both fields.")
            return

        ok, user_id = self.app.user_model.login(u, p)
        if ok:
            self.app.current_user_id = user_id
            self.app.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid login.")

    def register(self):
        u = self.username_entry.get().strip()
        p = self.password_entry.get().strip()

        if not u or not p:
            messagebox.showerror("Error", "Fill in both fields.")
            return

        ok, msg = self.app.user_model.register(u, p)
        if ok:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)
