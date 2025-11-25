class ExpenseModel:
    def __init__(self, db):
        self.db = db

    # CREATE
    def add_expense(self, user_id, title, amount, category, date, note=""):
        self.db.query("""
            INSERT INTO expenses (user_id, title, amount, category, date, note)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, title, amount, category, date, note))

    # READ
    def get_expenses(self, user_id):
        cursor = self.db.query("""
            SELECT id, title, amount, category, date, note
            FROM expenses
            WHERE user_id=?
            ORDER BY date DESC
        """, (user_id,))
        return cursor.fetchall()

    # UPDATE
    def update_expense(self, expense_id, title, amount, category, date, note=""):
        self.db.query("""
            UPDATE expenses
            SET title=?, amount=?, category=?, date=?, note=?
            WHERE id=?
        """, (title, amount, category, date, note, expense_id))

    # DELETE
    def delete_expense(self, expense_id):
        self.db.query("DELETE FROM expenses WHERE id=?", (expense_id,))
