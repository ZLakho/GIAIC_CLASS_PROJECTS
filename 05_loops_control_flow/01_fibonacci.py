def main():
    max_term = int(input("Enter maximum term: "))
    current_term = 0
    next_term = 1
    while current_term <= max_term:
        print(current_term)
        temp_term = current_term + next_term
        current_term = next_term
        next_term = temp_term
        
if __name__ == '__main__':
    main()