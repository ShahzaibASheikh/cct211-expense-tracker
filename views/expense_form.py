import tkinter as tk
from tkinter import messagebox

class ExpenseForm(tk.Toplevel):
    def __init__(self, root, app, expense=None, on_save=None):
        super().__init__(root)
        self.app = app
        self.expense = expense
        self.on_save = on_save

        self.title("Add Expense" if expense is None else "Edit Expense")
        self.geometry("350x250")
        self.build_ui()

        if self.expense:
            self.fill_fields()

    def build_ui(self):
        tk.Label(self, text="Title").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.title_entry = tk.Entry(self, width=25)
        self.title_entry.grid(row=0, column=1)

        tk.Label(self, text="Amount").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.amount_entry = tk.Entry(self, width=25)
        self.amount_entry.grid(row=1, column=1)

        tk.Label(self, text="Category").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.category_entry = tk.Entry(self, width=25)
        self.category_entry.grid(row=2, column=1)

        tk.Label(self, text="Date (YYYY-MM-DD)").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.date_entry = tk.Entry(self, width=25)
        self.date_entry.grid(row=3, column=1)

        tk.Label(self, text="Note").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.note_entry = tk.Entry(self, width=25)
        self.note_entry.grid(row=4, column=1)

        tk.Button(self, text="Save", command=self.save).grid(row=5, column=0, columnspan=2, pady=12)

    def fill_fields(self):
        # expense = (id, title, amount, category, date, note)
        self.title_entry.insert(0, self.expense[1])
        self.amount_entry.insert(0, self.expense[2])
        self.category_entry.insert(0, self.expense[3])
        self.date_entry.insert(0, self.expense[4])
        self.note_entry.insert(0, self.expense[5])

    def save(self):
        title = self.title_entry.get().strip()
        amount = self.amount_entry.get().strip()
        category = self.category_entry.get().strip()
        date = self.date_entry.get().strip()
        note = self.note_entry.get().strip()

        if not title or not amount or not category or not date:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        try:
            amount_val = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        if self.expense is None:
            self.app.expense_model.add_expense(
                self.app.current_user_id, title, amount_val, category, date, note
            )
        else:
            self.app.expense_model.update_expense(
                self.expense[0], title, amount_val, category, date, note
            )

        if self.on_save:
            self.on_save()
        self.destroy()
