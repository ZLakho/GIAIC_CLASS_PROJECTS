# def get_first_element(lst : list):
#     print(lst)

# def main():
#     listElement = []
#     # flag = True
#     while True:
#         userinput = input("Enter and element to add in a list: ")
#         if userinput == "":
#             get_first_element(listElement)
#             break
#         else:
#             listElement.append(userinput)

# if __name__ == "__main__":
#     main()


def print_list(lst: list):
    print("Here's the list:", lst)

def main():
    elements = []
    user_input = input("Enter a value: ")
    while user_input:
        elements.append(user_input)
        user_input = input("Enter a value: ")
    print_list(elements)

if __name__ == "__main__":
    main()

