class Node():
    def __init__(self, value = None, offset = None, left = None, right = None):
        self._value = value # значение корня узла
        self._offset = offset # номер строки в файле
        self._left = left # левый дочерний узел
        self._right = right # правый дочерний узел
    

    def __str__(self):
      return str(self._value)



class Tree():
    def __init__(self):
        self._root = None

    @property
    def get_root(self):
        return self._root



    def add(self, value, offset):
      if self._root is None:
          self._root = Node(value, offset)
      else:
          self.__add(value, offset, self._root)
    

    def __add(self, value, offset, node):
      if value < node._value:
          if node._left is not None:
              self.__add(value, offset, node._left)
          else:
              node._left = Node(value, offset)
      else:
          if node._right is not None:
              self.__add(value, offset, node._right)
          else:
              node._right = Node(value, offset)


    def search(self, node, value):
        if node._value is not None:
            
            if node._value == value:
                return node._offset
    
            else:
                if value > node._value:
                    return self.search(node._right, value)
                return self.search(node._left, value)
        else:
            return "Error! Tree is empty :("
            