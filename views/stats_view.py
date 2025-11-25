import tkinter as tk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StatsView(tk.Toplevel):
    def __init__(self, root, app):
        super().__init__(root)
        self.app = app
        self.title("Spending Stats")
        self.geometry("500x400")
        self.build_chart()

    def build_chart(self):
        expenses = self.app.expense_model.get_expenses(self.app.current_user_id)

        if not expenses:
            tk.Label(self, text="No expenses to show yet.").pack(pady=20)
            return

        df = pd.DataFrame(expenses, columns=["id", "title", "amount", "category", "date", "note"])
        summary = df.groupby("category")["amount"].sum()

        fig = Figure(figsize=(5, 4))
        ax = fig.add_subplot(111)
        summary.plot(kind="bar", ax=ax, title="Spending by Category")
        ax.set_ylabel("Amount ($)")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
