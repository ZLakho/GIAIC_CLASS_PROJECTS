def main():
    age : int = int(input("Enter your age: "))
    if age < 16 :
        print("Sorry you can't vote anywhere")
    if age >= 16 and age < 25:
        print("You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")
    if age >= 25 and age < 48 :
        print("You can vote in Peturksbouipo where the voting age is 16, also, You can vote in Stanlau where the voting age is 25. But You cannot vote in Mayengua where the voting age is 48.") 
    if age >= 48:
        print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You can vote in Mayengua where the voting age is 48.")
if __name__ == '__main__':
    main()