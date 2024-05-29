class Empty(Exception):
    """Error attemptting to access an element from a empty container."""
    pass

class Stack:
    
    def __init__(self):
        """Create a empty stack"""
        self.__data = []
        
    def size(self):
        """Return the number of elements in the stack"""
        return len(self.__data)

    def is_empty(self):
        """Return `True` if the stack is empty"""
        return len(self.__data) == 0
    
    def push(self, value):
        """Add element `value` to the top of the stack"""
        self.__data.append(value)
        
    def top(self):
        """Return (but do not remove) the `element` at the top of the stack
        
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.__data[-1]
    
    def pop(self):
        """Remove and return the element from the top of the stack.
        
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.__data.pop()
    

        
        