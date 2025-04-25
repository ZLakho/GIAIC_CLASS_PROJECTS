def get_first_element(lst : list):
    print(lst[0])

def main():
    listElement : list = list(input("Enter and element to add in a list: "))
    if listElement != []:
        get_first_element(listElement)
    else:
        while listElement == []:
            listElement : list = list(input("Enter and element to add in a list: "))
        get_first_element(listElement)


if __name__ == "__main__":
    main()
