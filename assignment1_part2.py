class Book:                                                         ## class with two attributes
 
def __init__ (self,author="",title=""):                             ## function that sets author and title ( to the blank string) to variables
  self.author = author
  self.title = title
  def display(self):                                                ## function that prints string representing the book by title written by author
      print (f"{self.title} 'written by' {self.author}"):
object1 = Book("Of Mice and Men", "John Steinbeck")                 ## two objects from the book class
object2 = Book("To kill a Mockingbird", "Harper Lee")
object1.display()
object2.display()
