def main():
    max_num = int(input("Enter maximum number for even numbers: "))
    for i in range(max_num):
        if i % 2 == 0:
            print(i)

if __name__ == '__main__':
    main()