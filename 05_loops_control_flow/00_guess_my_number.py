import random

def main():
    a = random.randint(0,100)
    b = int(input("Enter your guess: "))
    while a != b:
        if a > b:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        b = int(input("Enter your guess: "))
    print("Congratulations! You won")

if __name__ == '__main__':
    main()