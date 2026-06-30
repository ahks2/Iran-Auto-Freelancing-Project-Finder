import tkinter as tk
from tkinter import ttk

class UI:

    def __init__(self):
        self.user_field = ""
        self.user_search = ""
        self.user_price = 0

        self.root = tk.Tk()
        self.root.title("Project Finder")
        self.root.config(padx=20, pady=20)

        fields = [
            "All",
            "Programming",
            "Transcribing",
            "Design",
            "Marketing",
            "Business",
            "Architecture",
            "Others"
        ]

        try:
            self.logos_image = tk.PhotoImage(file="media/logos.png")
            canvas = tk.Canvas(self.root, width=200, height=150)
            canvas.create_image(105, 65, image=self.logos_image)
            canvas.grid(row=0, column=0, columnspan=2)
        except tk.TclError:
            print("Error: Could not load media/logos.png.")

        # FIELD
        tk.Label(self.root, text="Field").grid(row=1, column=0, sticky="w")

        self.fields_var = tk.StringVar()
        self.field_box = ttk.Combobox(
            self.root,
            textvariable=self.fields_var,
            values=fields,
            state="readonly",
            width=25
        )
        self.field_box.set("Programming")
        self.field_box.grid(row=1, column=1)

        # SEARCH
        tk.Label(self.root, text="Search").grid(row=2, column=0, sticky="w")

        self.search_entry = tk.Entry(self.root, width=28)
        self.search_entry.grid(row=2, column=1)

        # PRICE
        tk.Label(self.root, text="Min Price").grid(row=3, column=0, sticky="w")

        self.price_entry = tk.Entry(self.root, width=28)
        self.price_entry.insert(0, "200000000")
        self.price_entry.grid(row=3, column=1)

        # START BUTTON
        start_button = tk.Button(
            self.root,
            text="Start",
            command=self.search,
            bg="#4160f5",
            fg="white",
            width=15
        )
        start_button.grid(row=4, column=0, columnspan=2, pady=20)

    def search(self):

        self.user_field = self.fields_var.get()
        self.user_search = self.search_entry.get()

        try:
            self.user_price = int(self.price_entry.get())
        except:
            self.user_price = 0

        self.root.destroy()

    def start(self):
        self.root.mainloop()
        return self.user_field, self.user_search, self.user_price