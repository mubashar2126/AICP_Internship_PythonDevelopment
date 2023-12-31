import math

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
        print("Area of hexagon:", self.calcArea())
        print("Perimeter of hexagon:", self.calcPeri())
        print("Sum of angles of hexagon:", self.calcAngleSum())

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length * self.side_length

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        print("Area of Square:", self.calcAreaSquare())
        print("Perimeter of Square:", self.calcPeriSquare())

def main():
    # using the last digit of my cnic 5 as length of side
    cnic_last_digit = int("3840305109845"[-1])
    hexagon = Hexagon(cnic_last_digit)

    # len of side square = 5 + 1
    square = Square(cnic_last_digit + 1)

    while True:
        print("\nMenu:")
        print("1. Calculate area, perimeter, and sum of angles of hexagon")
        print("2. Calculate area and perimeter of square")
        print("Any other key to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hexagon.display()
        elif choice == '2':
            square.display()
        else:
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
