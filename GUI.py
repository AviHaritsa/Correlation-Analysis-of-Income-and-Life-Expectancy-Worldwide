import tkinter as tk
from tkinter.font import Font

def button_click(country):
    if country == "Australia":
        print(3075.910532)
    elif country == "Canada":
        print(556.257342)
    elif country == "Germany":
        print(1457.954010)
    elif country == "Finland":
        print(-1529.175647)
    elif country == "France":
        print(-5995.936751)
    elif country == "United Kingdom":
        print(2519.620940)
    elif country == "Norway":
        print(10019.744682)
    elif country == "New Zealand":
        print(-5131.093093)
    elif country == "Poland":
        print(-21706.412402)
    elif country == "United States":
        print(16733.130387)

root = tk.Tk()
root.title("Average Income Deviation")
root.configure(bg='black')

button_font = Font(family="cursive", size=10, weight="bold")

frame = tk.Frame(root, bg='black')
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

countries = ["Australia", "Canada", "Germany", "Finland", "France", "United Kingdom", "Norway", "New Zealand", "Poland", "United States"]
for i, country in enumerate(countries):
    row = i // 5
    col = i % 5
    button = tk.Button(frame, text=country, font="Times", fg="red", bg="white", bd=2, relief="raised", command=lambda c=country: button_click(c))
    button.grid(row=row, column=col, sticky=tk.NSEW)
    frame.grid_columnconfigure(col, weight=1)
    frame.grid_rowconfigure(row, weight=1)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
avg_income_label = tk.Label(root, text="The average income was 44627.37 for all the countries included. The number shown when clicked shows the deviation from the average income for each country.", font=("Arial", 12), bg='black', fg='white')
avg_income_label.pack(side=tk.TOP, padx=10, pady=10)
root.mainloop()
