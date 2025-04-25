def main():
    height : int = int(input("Enter your height: "))
    min_height : int = 50
    if height < min_height:
        while height < min_height:
            print("Sorry, you are not taller enough to ride this, better luck next year.")
            height : int = int(input("Enter your height: "))
        print("You can ride, Enjoy.")
    else:
        print("You can ride, Enjoy.")
    

if __name__ == '__main__':
    main()