def sum(numbers: list) -> float:
    numberss : list = numbers
    result : float = 0
    for number in numberss:
        result = result + number
    return result

def main():
    numbers : list = [1,2,3,4,5]
    result = sum (numbers)
    print(result)
if __name__ == "__main__":
    main()