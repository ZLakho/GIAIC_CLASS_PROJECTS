def main():
    year : int = int(input("Enter year: "))
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Its a leap year")
    else:
        print("its not a leap year")

if __name__ == '__main__':
    main()
