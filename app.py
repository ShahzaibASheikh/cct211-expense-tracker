import tkinter as tk

from models.db import Database
from models.user_model import UserModel
from models.expense_model import ExpenseModel

from views.login_view import LoginView
from views.dashboard_view import DashboardView

class App:
    def __init__(self, root):
        self.root = root

        # models
        self.db = Database()
        self.user_model = UserModel(self.db)
        self.expense_model = ExpenseModel(self.db)

        self.current_user_id = None
        self.current_view = None

        self.show_login()

    def clear_view(self):
        if self.current_view:
            self.current_view.destroy()

    def show_login(self):
        self.clear_view()
        self.current_view = LoginView(self.root, self)

    def show_dashboard(self):
        self.clear_view()
        self.current_view = DashboardView(self.root, self)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    app = App(root)
    root.mainloop()
