def main():
    base : float = float(input("Enter base of a triangle: "))
    perimeter : float = float(input("Enter perimeter of a triangle: "))
    height : float = base**2 + perimeter**2
    print(f"Height {height**2} = Base {base}**2 + Perimeter {perimeter}**2")

if __name__ == "__main__":
    main() 