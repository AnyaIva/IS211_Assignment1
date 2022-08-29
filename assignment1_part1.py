def listDivide(numbers, divide = 2):             ## function returns the number of elements in the numbers list
  a = 0                                          ##                                that are divisible by divide
  for v in numbers:                             
            if v % divide == 0:                  ## if the value isn't divisible by divide, increase by 1
                a = a + 1\
        return a
class ListDivideException:                       ## custom exception class
  def testListDivide():                          ## function to perform tests on listDivide
      if not listDivide([1,2,3,4,5]) == 2:
             raise ListDivideException
      if not listDivide([2,4,6,8,10]) == 5:
             raise ListDivideException
      if not listDivide([30, 54, 63,98, 100], divide=10) == 2:
             raise ListDivideException
      if not listDivide([]) == 0:
             raise ListDivideException
      if not listDivide([1,2,3,4,5], 1) == 5:
             raise ListDivideException
  testListDivide():
    
