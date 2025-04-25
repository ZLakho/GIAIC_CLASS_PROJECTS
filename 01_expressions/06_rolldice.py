import random

def main():
    roll_dice_01 : int = int(random.randint(1 , 6))
    roll_dice_02 : int = int(random.randint(1 , 6))
    total : int = roll_dice_01 + roll_dice_02
    print(f"First dice number is {roll_dice_01} and second dice number is {roll_dice_02} and their total is {total}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()