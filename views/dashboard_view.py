import tkinter as tk
from tkinter import ttk, messagebox
from .expense_form import ExpenseForm
from .stats_view import StatsView

class DashboardView(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.root = root
        self.app = app
        self.build_ui()
        self.refresh_table()

    def build_ui(self):
        self.root.title("Expense Tracker - Dashboard")
        self.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(self, text="Your Expenses", font=("Arial", 16, "bold")).pack(pady=5)

        cols = ("id", "title", "amount", "category", "date", "note")
        self.table = ttk.Treeview(self, columns=cols, show="headings", height=12)

        self.table.heading("id", text="ID")
        self.table.heading("title", text="Title")
        self.table.heading("amount", text="Amount")
        self.table.heading("category", text="Category")
        self.table.heading("date", text="Date (YYYY-MM-DD)")
        self.table.heading("note", text="Note")

        for c in cols:
            self.table.column(c, width=120)

        self.table.pack(fill="both", expand=True)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=8)

        tk.Button(btn_frame, text="Add Expense", command=self.add_expense).grid(row=0, column=0, padx=4)
        tk.Button(btn_frame, text="Edit Selected", command=self.edit_expense).grid(row=0, column=1, padx=4)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_expense).grid(row=0, column=2, padx=4)
        tk.Button(btn_frame, text="View Stats", command=self.view_stats).grid(row=0, column=3, padx=4)
        tk.Button(btn_frame, text="Logout", command=self.logout).grid(row=0, column=4, padx=4)

        self.total_label = tk.Label(self, text="")
        self.total_label.pack()

    def refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        expenses = self.app.expense_model.get_expenses(self.app.current_user_id)

        total = 0
        for e in expenses:
            self.table.insert("", "end", values=e)
            total += float(e[2])

        self.total_label.config(text=f"Total spending: ${total:.2f}")

    def add_expense(self):
        ExpenseForm(self.root, self.app, on_save=self.refresh_table)

    def get_selected_expense(self):
        selected = self.table.selection()
        if not selected:
            return None
        return self.table.item(selected[0])["values"]

    def edit_expense(self):
        values = self.get_selected_expense()
        if not values:
            messagebox.showerror("Error", "Select an expense to edit.")
            return
        ExpenseForm(self.root, self.app, expense=values, on_save=self.refresh_table)

    def delete_expense(self):
        values = self.get_selected_expense()
        if not values:
            messagebox.showerror("Error", "Select an expense to delete.")
            return

        expense_id = values[0]
        if messagebox.askyesno("Confirm", "Delete this expense?"):
            self.app.expense_model.delete_expense(expense_id)
            self.refresh_table()

    def view_stats(self):
        StatsView(self.root, self.app)

    def logout(self):
        self.app.current_user_id = None
        self.app.show_login()
