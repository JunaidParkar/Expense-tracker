import customtkinter as tk

class Transaction:
    def __init__(self, serial, date, amount, description, category, transaction_type):
        self.serial = serial
        self.date = date
        self.amount = amount
        self.description = description
        self.category = category
        self.transaction_type = transaction_type

class Table:
    def __init__(self, master, transactions):
        self.master = master
        self.transactions = transactions
        self.table_frame = tk.CTkFrame(master)
        self.table_frame.pack(pady=10)

        self.headers = ["Serial", "Date", "Amount", "Description", "Category", "Type", "Select"]
        self.column_widths = [50, 100, 80, 300, 150, 100, 50]

        self.create_table()

    def create_table(self):
        # Create headers
        for i, header in enumerate(self.headers):
            header_label = tk.CTkLabel(self.table_frame, text=header, width=self.column_widths[i], anchor='center')
            header_label.grid(row=0, column=i, sticky='nsew')

        # Create rows
        for i, transaction in enumerate(self.transactions):
            row_frame = tk.CTkFrame(self.table_frame, fg_color='gray', corner_radius=5)
            row_frame.grid(row=i+1, column=0, columnspan=7, sticky='nsew')

            for j, value in enumerate(self.get_row_values(transaction)):
                cell_textbox = tk.CTkTextbox(row_frame, width=self.column_widths[j], height=1, wrap='char', border_width=0)
                cell_textbox.insert('0.0', value)
                cell_textbox.configure(state='disabled')
                cell_textbox.grid(row=0, column=j, sticky='nsew')

    def get_row_values(self, transaction):
        return (transaction.serial, transaction.date, transaction.amount,
                transaction.description, transaction.category, transaction.transaction_type, '')

root = tk.CTk()

transactions = [
    Transaction(1, '2023-01-01', 100, 'Payment to XYZ kjbn byvbnv nv gvbn ghvtyggvtygv ftyv jhv gjfb gvtv bghdcrfv  cgtkfouljhn cvgytc bgkycybgctdgbty5chn njbyuvm njgtyc   b', 'Expenses', 'Out'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In'),
    Transaction(2, '2023-01-02', 200, 'Salary from ABC', 'Income', 'In')
]

# table = Table(root, transactions)

root.mainloop()