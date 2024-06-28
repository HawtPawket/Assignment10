# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.









library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def addNewBook(library, title, author):
    newBook = (title, author)
    if newBook not in library:
        library.append(newBook)
        print(f"New book '{title}' by {author} added to the library.")
    else:
        print(f"Newly added book '{title}' by {author} already exists in the library.")


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

addNewBook(library, "To Kill a Mockingbird", "Harper Lee")

addNewBook(library, "1984", "George Orwell")
