def shortener(lst : list):
    max_length = 5
    while len(lst) != max_length:
        lst.pop()
    return lst

def main():
    numbers : list = [1,2,4,5,6,7,8,9]
    # print(len(numbers))
    result : list = shortener(numbers)
    print(result)
if __name__ == "__main__":
    main()
