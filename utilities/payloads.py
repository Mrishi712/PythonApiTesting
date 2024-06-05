# payload for add a book to library
def addBookPayload(name,isbn,aisle,author):
    addBookPayload = {
        "name": name,
        "isbn": isbn,
        "aisle": aisle ,
        "author": author
    }
    return addBookPayload


def deleteBookPayload(bookId):
    deleteBookpayload = {
        "ID": bookId
    }
    return deleteBookpayload


