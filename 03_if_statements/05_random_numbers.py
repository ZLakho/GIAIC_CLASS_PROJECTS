import random

def main():
    num_lst = []
    for i in range(10):
        number : int = random.randint(1,100)
        if number not in num_lst:
            print(f"{i+1}: {number}")
            num_lst.append(number)
        else:
            continue
    print(num_lst)

if __name__ == '__main__':
    main()