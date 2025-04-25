def main():
    mass : float = float(input("Enter your mass in kilos: "))
    C : int = 299792458
    e = mass*(C**2)
    print(f"Your mass in Energy is {e} joules of energy")

if __name__ == "__main__":
    main() 