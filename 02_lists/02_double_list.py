def double(numbers: list) -> int:
    numberss : list = numbers
    for i in range(len(numbers)):
        numberss[i] = numberss[i] + numberss[i]
    return numberss

def main():
    numbers : list = [1,2,3,4,5]
    result : list = double (numbers)
    print(result)
    
if __name__ == "__main__":
    main()