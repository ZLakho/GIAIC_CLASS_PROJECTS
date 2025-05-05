def collect_contacts():
    book = dict()
    entry = input("Add contact? (yes/no): ").strip().lower()
    while entry == "yes":
        key = input("Enter name: ").strip()
        val = input("Enter number: ").strip()
        if key:
            book[key] = val
        entry = input("Add another? (yes/no): ").strip().lower()
    return book

def show_all(book):
    if not book:
        print("No contacts available.")
    else:
        for k in book.keys():
            print(f"{k} => {book[k]}")

def search_contact(book):
    while True:
        query = input("Search name (blank to exit): ").strip()
        if not query:
            break
        print(book.get(query, "Not found."))

def run():
    data = collect_contacts()
    print("\nSaved Contacts:")
    show_all(data)
    print("\nSearch Mode:")
    search_contact(data)

if __name__ == '__main__':
    run()
