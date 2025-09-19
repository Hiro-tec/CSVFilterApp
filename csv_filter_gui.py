import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class CsvFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV 列ごとOR条件フィルタツール（改良版）")

        self.df_input = None
        self.df_filter = None

        # 入力CSV
        tk.Button(root, text="入力CSVを選択", command=self.load_input_csv).pack(pady=5)
        self.input_label = tk.Label(root, text="未選択")
        self.input_label.pack()

        # フィルタCSV
        tk.Button(root, text="フィルタCSVを選択", command=self.load_filter_csv).pack(pady=5)
        self.filter_label = tk.Label(root, text="未選択")
        self.filter_label.pack()

        # 列選択エリア
        tk.Label(root, text="除外対象列を追加").pack(pady=5)
        frame = tk.Frame(root)
        frame.pack(pady=5)

        self.combo_col = ttk.Combobox(frame, state="readonly", width=20)
        self.combo_col.grid(row=0, column=0, padx=5)
        tk.Button(frame, text="追加", command=self.add_column).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="削除", command=self.remove_column).grid(row=0, column=2, padx=5)

        # 選択済み列リスト
        self.selected_cols_listbox = tk.Listbox(root, height=6)
        self.selected_cols_listbox.pack(pady=5)

        # 実行ボタン
        tk.Button(root, text="フィルタ実行", command=self.run_filter).pack(pady=10)

    def load_input_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.df_input = pd.read_csv(file_path)
            self.input_label.config(text=file_path)
            self.combo_col["values"] = list(self.df_input.columns)

    def load_filter_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.df_filter = pd.read_csv(file_path)
            self.filter_label.config(text=file_path)

    def add_column(self):
        col = self.combo_col.get()
        if col and col not in self.selected_cols_listbox.get(0, tk.END):
            self.selected_cols_listbox.insert(tk.END, col)

    def remove_column(self):
        selection = self.selected_cols_listbox.curselection()
        for i in reversed(selection):
            self.selected_cols_listbox.delete(i)

    def run_filter(self):
        if self.df_input is None or self.df_filter is None:
            messagebox.showerror("エラー", "入力CSVとフィルタCSVを選択してください")
            return

        selected_cols = self.selected_cols_listbox.get(0, tk.END)
        if not selected_cols:
            messagebox.showerror("エラー", "除外する列を選択してください")
            return

        mask = pd.Series([False] * len(self.df_input))
        for col in selected_cols:
            if col in self.df_filter.columns:
                mask |= self.df_input[col].isin(self.df_filter[col])

        filtered_df = self.df_input[~mask]

        save_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")])
        if save_path:
            filtered_df.to_csv(save_path, index=False, encoding="utf-8-sig")
            messagebox.showinfo("完了", f"フィルタ後のCSVを保存しました:\n{save_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CsvFilterApp(root)
    root.mainloop()
