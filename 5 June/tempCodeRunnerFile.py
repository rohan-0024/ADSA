from dequeue import dequeue

class Palindrome():
    def __init__(self):
        self.queue = dequeue()
        
    def check(self,string):
        
        l,r = 0, len(string) - 1
        while l <= r:
            a = self.queue.pushFront(string[l])
            b = self.queue.pushBack(string[r])
            l += 1
            r -= 1
        return b 

find = Palindrome()
print(find.check("abba"))
            