import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("320x460")
        self.root.resizable(False, False)
        self.root.configure(bg="#17171c")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display screen area
        display_frame = tk.Frame(self.root, width=320, height=100, bg="#17171c")
        display_frame.pack(fill="x") #ADD THE missing line to pack the display frame
        display_frame.pack_propagate(False)

        self.display = tk.Entry(
            display_frame,
            font=("Helvetica", 32),
            textvariable=self.input_text,
            justify="right",
            bg="#17171c",
            fg="#ffffff",
            bd=0,
            insertbackground="white"
        )
        self.display.pack(fill="both", expand=True, padx=2, pady=2)

        # Buttons grid container
        btns_frame = tk.Frame(self.root, bg="#17171c")
        btns_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Button layout configurations: (Text, Row, Column, Background Color, Text Color)
        buttons = [
            ("C", 1, 0, "#3a3a43", "#ff5e57"),
            ("+/-", 1, 1, "#3a3a43", "#ffffff"),
            ("%", 1, 2, "#3a3a43", "#ffffff"),
            ("÷", 1, 3, "#4b4b5a", "#00d2d3"),
            
            ("7", 2, 0, "#2c2c35", "#ffffff"),
            ("8", 2, 1, "#2c2c35", "#ffffff"),
            ("9", 2, 2, "#2c2c35", "#ffffff"),
            ("×", 2, 3, "#4b4b5a", "#00d2d3"),
            
            ("4", 3, 0, "#2c2c35", "#ffffff"),
            ("5", 3, 1, "#2c2c35", "#ffffff"),
            ("6", 3, 2, "#2c2c35", "#ffffff"),
            ("-", 3, 3, "#4b4b5a", "#00d2d3"),
            
            ("1", 4, 0, "#2c2c35", "#ffffff"),
            ("2", 4, 1, "#2c2c35", "#ffffff"),
            ("3", 4, 2, "#2c2c35", "#ffffff"),
            ("+", 4, 3, "#4b4b5a", "#00d2d3"),
            
            ("0", 5, 0, "#2c2c35", "#ffffff"),
            (".", 5, 1, "#2c2c35", "#ffffff"),
            ("⌫", 5, 2, "#3a3a43", "#ffa502"),
            ("=", 5, 3, "#00d2d3", "#17171c"),
        ]

        # Allocate grid space evenly
        for i in range(6):
            btns_frame.rowconfigure(i, weight=1)
        for i in range(4):
            btns_frame.columnconfigure(i, weight=1)

        # Render layout
        for (text, row, col, bg_col, fg_col) in buttons:
            btn = tk.Button(
                btns_frame,
                text=text,
                font=("Helvetica", 18, "bold"),
                bg=bg_col,
                fg=fg_col,
                bd=0,
                activebackground="#575766",
                activeforeground="#ffffff",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == "+/-":
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.input_text.set(self.expression)
        elif char == "%":
            if self.expression:
                try:
                    self.expression = str(float(self.expression) / 100)
                    self.input_text.set(self.expression)
                except Exception:
                    pass
        elif char == "=":
            try:
                # Map visual user symbols to core python operators
                eval_expr = self.expression.replace("×", "*").replace("÷", "/")
                result = str(eval(eval_expr))
                
                # Format to remove trailing .0 for whole float numbers
                if result.endswith(".0"):
                    result = result[:-2]
                    
                self.input_text.set(result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero!")
                self.expression = ""
                self.input_text.set("")
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.input_text.set("")
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
