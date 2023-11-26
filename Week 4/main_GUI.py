import tkinter as tk


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return 1.5 * 1.732 * self.side_length * self.side_length

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 6 * 120

    def display(self):
        area = self.calcArea()
        perimeter = self.calcPeri()
        angle_sum = self.calcAngleSum()
        return f"Area of hexagon: {area}\nPerimeter of hexagon: {perimeter}\nSum of angles of hexagon: {angle_sum}"


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length ** 2

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        area = self.calcAreaSquare()
        perimeter = self.calcPeriSquare()
        return f"Area of Square: {area}\nPerimeter of Square: {perimeter}"


class App:
    def __init__(self, master):
        self.master = master
        master.title("Geometry Calculator")

        self.label = tk.Label(master, text="Enter 1 to calculate hexagon, 2 to calculate square, or any other key to exit:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.on_submit)
        self.submit_button.pack()

    def on_submit(self):
        choice = self.entry.get()
        if choice == '1':
            hexagon_side_length = int(str(your_cnic)[-1])
            hexagon = Hexagon(hexagon_side_length)
            result = hexagon.display()
        elif choice == '2':
            square_side_length = int(str(your_cnic)[-1]) + 1
            square = Square(square_side_length)
            result = square.display()
        else:
            result = "Exiting..."

        result_label = tk.Label(self.master, text=result)
        result_label.pack()


your_cnic = 3650295636507

root = tk.Tk()
app = App(root)
root.mainloop()
