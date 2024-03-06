import re
import tkinter as tk

class RegexCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title('RegEx Checker')

        self.create_widgets()

    def create_widgets(self):
        # Regex Entry
        self.regex_label = tk.Label(self.master, text='Enter Regex: ')
        self.regex_label.grid(row=0, column=0, padx=5, pady=5)

        self.regex_entry = tk.Entry(self.master, width=50)
        self.regex_entry.grid(row=0, column=1, padx=5, pady=5)

        # Text Entry
        self.text_label = tk.Label(self.master, text='Enter Text')
        self.text_label.grid(row=1, column=0, padx=5, pady=5)

        self.text_entry = tk.Text(self.master, width=50, height=10)
        self.text_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.find_button = tk.Button(self.master, text='Find Matches', command=self.find_matches)
        self.find_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='we')

        self.check_button = tk.Button(self.master, text='Check Matches', command=self.check_match)
        self.check_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='we')

        # Result Label
        self.result_label = tk.Label(self.master, text='', fg='green')
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def find_matches(self):
        regex = self.regex_entry.get()
        text = self.text_entry.get("1.0", "end-1c")

        if regex and text:
            self.clear_previous_matches()
            matches = re.finditer(regex, text)
            for match in matches:
                self.tag_match(match.start(), match.end())

    def check_match(self):
        regex = self.regex_entry.get()
        text = self.text_entry.get("1.0", "end-1c")

        if regex and text:
            if re.search(regex, text):  # Use re.search instead of re.match
                self.result_label.config(text='Regex found a match in the text!', fg='green')
            else:
                self.result_label.config(text='Regex did not find a match in the text!', fg='red')
        else:
            self.result_label.config(text='', fg='green')  # Reset result label if either regex or text is empty


    def clear_previous_matches(self):
        self.text_entry.tag_remove("match", "1.0", "end")

    def tag_match(self, start, end):
        start_index = f"1.0 + {start} chars"
        end_index = f"1.0 + {end} chars"
        self.text_entry.tag_add("match", start_index, end_index)
        self.text_entry.tag_config("match", foreground="black", background="red", font=('Arial', 10, 'bold'))

if __name__ == "__main__":
    root = tk.Tk()
    app = RegexCheckerApp(root)
    root.mainloop()

#758-827-4650
#942-214-1676