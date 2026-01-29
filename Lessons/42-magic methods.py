# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f'"{self.title}" by {self.author}'
    
    # __eq__() = equal / used to check if two objects are the same
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    

    # __lt__() = less than / used to compare value
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    # __gt__() = greater than
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    # __add__() = adding objects 
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
        


book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R Tolkien", 310)


# print(book1)
# print(book2)
# print(book3)

# print(book1 == book4)

# print(book2 < book3)
# print(book2 + book3)

# print("Lewis" in book3)

print(book1["audio"])