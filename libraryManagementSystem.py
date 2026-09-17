
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

def add_book(addbook):
    
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
    
    Input_1 = input("Enter the name of book to search: ")
    if (Input_1 in searchbook):
        print(Input_1,"is available!")
    else:
        print(Input_1,"is not available!")
        print()
    return searchbook

def issue_book(issue):
    
    Input_2 = input("Enter the name of book to issue: ")
    if(Input_2 in issue):
        books_issue.append(Input_2)
        issue.pop(Input_2)
        print(Input_2,"is issued!")
        print()
    else:
        print(Input_2,"is not available!")
        print()
    return issue 

def return_book(returnbook):

    Input_3 = input("Enter the book you want to return: ")
    if(Input_3 in returnbook):
        value_1 = "Available"
        returnbook.remove(Input_3)
        modules.update({Input_3 : value_1})
        print("The book is returned back to the library!")
    else:
        print("The book doesn't belong to this Libarary!")
            
    return returnbook

def show_book(show):
    for key in show:
        print(key)

def issued_book(issue):
    if(Input == 6):
        if(len(issue) == 0):
             print("No books issued!")
        else:
             for i in issue:
                  print(i)

while exit == False:

    Input = int(input("Enter your choice: "))

    if(Input == 1):
        modules = add_book(modules)
        print()

    elif(Input == 2):
        modules = search_book(modules)
        print()

    elif(Input == 3):
        modules = issue_book(modules)
        print()

    elif(Input == 4):
        return_book(books_issue)

    elif(Input == 5):
        show_book(modules)

    elif(Input == 6):
        issued_book(books_issue)

    elif(Input == 7):
        print("Thank you!")
        exit = True

    else:
        print("Invalid input!")
        print()
        
