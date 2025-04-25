def main():
    divident : int = int(input("Enter a number to be divided: "))
    divideBy : int = int(input("Enter a number to be divide by: "))
    result : int = divideBy // divident
    result2 : int = divideBy % divident
    print(f"The divisor is {result} and the remainder is {result2}")
    

if __name__ == "__main__":
    main() 