mylist = [1,2,3]

print(mylist)
print(len(mylist))


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'<Book Object {self.title} {self.author} {self.pages}>'

    def __len__(self):
        return self.pages

book = Book('Python Rocks!', 'Jose', 120)
print(book.__str__())
print(book.__len__())