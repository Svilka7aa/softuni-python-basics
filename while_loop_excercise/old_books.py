favourite_book = input()

books_count = 0
book = input()
found_it = False

while book != "No More Books":
    if book == favourite_book:
        found_it = True
        break


    book = input()
    books_count += 1
if found_it:
    print(f"You checked {books_count} books and found it.")

else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")