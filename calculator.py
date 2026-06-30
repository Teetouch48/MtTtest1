import tkinter as tk


# สร้างหน้าต่าง
root = tk.Tk()

root.title("Mac Python Calculator")
root.geometry("350x500")


# ช่องแสดงผล
screen = tk.Entry(
    root,
    font=("Helvetica", 24),
    justify="right"
)

screen.pack(
    fill="x",
    padx=10,
    pady=10
)


# เมื่อกดปุ่ม
def press(value):

    if value == "=":

        try:
            answer = eval(screen.get())

            screen.delete(0, tk.END)
            screen.insert(0, str(answer))

        except:
            screen.delete(0, tk.END)
            screen.insert(0, "Error")


    elif value == "AC":

        screen.delete(0, tk.END)


    else:

        screen.insert(
            tk.END,
            value
        )



# ปุ่ม
buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
    "AC"
]


frame = tk.Frame(root)
frame.pack()


row = 0
col = 0


for b in buttons:

    button = tk.Button(
        frame,
        text=b,
        width=5,
        height=2,
        font=("Helvetica",18),
        command=lambda x=b: press(x)
    )

    button.grid(
        row=row,
        column=col,
        padx=5,
        pady=5
    )


    col += 1

    if col == 4:
        col = 0
        row += 1



root.mainloop()