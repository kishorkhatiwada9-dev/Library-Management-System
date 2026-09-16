
modules = {
    "physics" : "Available",
    "Java" : "Available",
    "C++" : "Available"
}

print("======== Libarary Management System =========")
print("1. Add Book.")
print("2. Search Book.")
print("3. Issue Book.")
print("4. Return Book.")
print("5. Show Book.")
print("6. Issued Book")
print("7. Exit.")
exit = False

books_issue = []

while exit == False:
    Input = int(input("Enter your choice: "))

    def add_book(addbook):
        if(Input == 1):
            book_name = input("Enter book name to add: ")
            if (book_name in addbook):
                print("Already available!")

            elif(book_name in books_issue):
                print(book_name,"is issued!")
                
            else:
                value = "Available"
                addbook.update({book_name : value})
                print(book_name, "is added!") 
            return addbook
    def search_book(searchbook):
        if(Input == 2):
            Input_1 = input("Enter the name of book to search: ")
            if (Input_1 in searchbook):
                print(Input_1,"is available!")
            else:
                print(Input_1,"is not available!")
                print()
            return searchbook

    if(Input == 1):
        modules = add_book(modules)
        print()

    def issued_book(issue):
        if(Input == 6):
            for i in issue:
                print(i)

