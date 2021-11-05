class Node():

    def __init__(self, value = None, left = None, right = None, lvl = 0):
        self.value = value # значение корня узла
        self.left = left # левый дочерний узел
        self.right = right # правый дочерний узел
        self.lvl = lvl
    
    def __str__(self):
      return str(self.value)

class Tree():
  def __init__(self):
    self.root = None


  def add(self, value, lvl = 1):
    if self.root is None:
        self.root = Node(value, lvl = lvl)
    else:
        self.__add(value, node = self.root, lvl = lvl + 1)


  def __add(self, value, node, lvl):
    if value < node.value:
        if node.left is not None:
            self.__add(value = value, node = node.left, lvl = lvl + 1)
        else:
            node.left = Node(value = value, lvl = lvl)
    else:
        if node.right is not None:
            self.__add(value = value, node = node.right, lvl = lvl + 1)
        else:
            node.right = Node(value = value, lvl = lvl)
    

  def build_queue(self, ml):
    queue_1 = []
    queue_2 = [self.root]
    result_array = []
   
    while True:     
      for i in queue_2:
        if i is not None:      
          queue_1.append(i.left)
          queue_1.append(i.right)
      
      queue_1, queue_2 = queue_2, queue_1

      for i in queue_1:
        if i is not None:  
          result_array.append(i.value)
          
      queue_1 = []

      if len(queue_2) == 0:
        break
    return result_array


a = list(map(int, input().split()))
max_level = 4
tree = Tree()


for i in a:
    tree.add(i)




def output(root):
    if root is not None:
        print(root.value)
        output(root.left)
        output(root.right)

def transform(root, lvl = 1):
    if lvl == max_level:
        return

    if root is None:
        root = Node(value = None, lvl = lvl + 1)
        transform(root, lvl)

    else:
       if root.left is None:
           root.left = Node(value = None, lvl = lvl + 1)
           transform(root, lvl)
       elif root.right is None:
           root.right = Node(value = None, lvl = lvl + 1)
           transform(root, lvl)
       else:
           transform(root.left, lvl = lvl + 1)
           transform(root.right, lvl = lvl + 1)
    
    



transform(tree.root)
result_array = tree.build_queue(ml = max_level)
print(result_array)

with open('result.txt', 'w') as f:
    f.write(f"Входные данные: {a}\n")
    spaces = [2**i for i in range(max_level)]
    print(spaces)
    temp_level = max_level - 1

    for i in spaces:
        for j in range(i):

            tab = 2**(temp_level + 2)
            if j > 0:
                tab = 2**(temp_level + 3)

            extra_space = 3
            output = result_array[j]

            if len(str(output)) > 1:
                extra_space = 1
            
            if output is not None:
                if output < 0:
                    extra_space = 0

            if result_array[j] is None:
                output = '.'
                extra_space = 0
                         
            f.write(" " * tab + " " * extra_space + str(output))
            print(" " * tab + " " * extra_space + str(output))

        temp_level -= 1
        f.write("\n")
        result_array = result_array[i:]
