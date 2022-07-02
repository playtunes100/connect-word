class Node:
       def __init__(self, index):
        self.index = index
        self.data = None
        self.color = None
        self.next = None
        self.prev = None
        self.top = None
        self.bottom = None
        self.topnext = None
        self.topprev = None
        self.bottomprev = None
        self.bottomnext = None

class queen_linked_list:
   def __init__(self,row,col):
        self.row = row
        self.col = col
        self.length = row*col
        self.head = None
        PrevNode = None
        RowNode = None
        for i in range(self.length):
            NewNode = Node(i)
            
            if i == 0:
                self.head = NewNode
                PrevNode = self.head
                RowNode = self.head
            else:
                NewNode.prev = PrevNode
                PrevNode.next = NewNode
                PrevNode = NewNode
                if i >= col:
                    NewNode.top = RowNode
                    RowNode.bottom = NewNode
                    if (i%col) != 0:
                        NewNode.topprev = RowNode.prev
                        RowNode.prev.bottomnext = NewNode
                    
                    if (i%col) != col-1:
                        NewNode.topnext = RowNode.next
                        RowNode.next.bottomprev = NewNode
                    RowNode = RowNode.next
                    
            
        
        
# Adding data elements		
   def push(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode
      
   #gets list of values along the horizontal values of the index
   def getHorizontal(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
        
        node = self.fetch(index)
        l_word = ""
        r_word = ""
        leftNode = node.prev
        rightNode = node.next
        
        if leftNode is not None:
            while leftNode.data is not None:
                if (leftNode.index != (self.col*round(leftNode.index//self.col))-1) and (leftNode.color == node.color):
                    l_word = str(leftNode.data) + l_word
                    leftNode = leftNode.prev
                if leftNode is None or leftNode.index == ((self.col*round(leftNode.index//self.col))-1) or leftNode.color != node.color:
                    break
                
        if rightNode is not None:
            while rightNode.data is not None:
                if (rightNode.index != (self.col*round(rightNode.index/self.col))) and (rightNode.color == node.color):
                    r_word += str(rightNode.data)
                    rightNode = rightNode.next
                if rightNode is None or rightNode.index == (self.col*round(rightNode.index/self.col)) or rightNode.color != node.color:
                    break
                
                  
        return l_word+str(node.data)+r_word

   def getVertical(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
        node = self.fetch(index)
        t_word = ""
        b_word = ""
        topNode = node.top
        bottomNode = node.bottom
        
        if topNode is not None:
            while topNode.data is not None and topNode.color == node.color:
                t_word = str(topNode.data) + t_word
                topNode = topNode.prev
                if topNode is None or topNode.color != node.color:
                    break

        if bottomNode is not None:
            while bottomNode.data is not None and bottomNode.color == node.color:
                b_word += str(bottomNode.data)
                bottomNode = bottomNode.next
                if bottomNode is None or bottomNode.color != node.color:
                    break

        return t_word+str(node.data)+b_word
        
   def getRising(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
        node = self.fetch(index)
        s_word = ""
        e_word = ""
        startNode = node.bottomprev
        endNode = node.topnext
        
        if startNode is not None:
            while startNode.data is not None and startNode.color == node.color:
                s_word = str(startNode.data) + s_word
                startNode = startNode.bottomprev
                if startNode is None or startNode.color != node.color:
                    break
                
        if endNode is not None:
            while endNode.data is not None and endNode.color == node.color:
                e_word += str(endNode.data)
                endNode = endNode.topnext
                if endNode is None or endNode.color != node.color:
                    break

        return s_word+str(node.data)+e_word
        
   def getFalling(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
        node = self.fetch(index)
        s_word = ""
        e_word = ""
        startNode = node.topprev
        endNode = node.bottomnext
        
        if startNode is not None:
            while startNode.data is not None and startNode.color == node.color:
                s_word = str(startNode.data) + s_word
                startNode = startNode.topprev
                if startNode is None or startNode.color != node.color:
                    break
                
        if endNode is not None:
            while endNode.data is not None and endNode.color == node.color:
                e_word += str(endNode.data)
                endNode = endNode.bottomnext
                if endNode is None or endNode.color != node.color:
                    break

        return s_word+str(node.data)+e_word

   def fetch(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
            
        node = self.head
        
        while (node is not None):
            if node.index == index:
                return node
            node = node.next
   
   def insertInNode(self, index, data, color):
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
        node = self.head
        
        while (node is not None):
            if node.index == index:
                node.data = data
                node.color = color
                node = None
            else:
                node = node.next


# Print the Multi Linked list		
   def listprint(self, node):
      while (node is not None):
        print("Node: "+str(node.index)),
        
        
        if node.topprev is not None:
            print( "top prev: "+str(node.topprev.index))
        if node.top is not None:
            print(" Top: "+str(node.top.index))
        if node.topnext is not None:
            print(" Top Next: "+str(node.topnext.index))
        if node.data is not None:
            print("Data: "+node.data)
        if node.color is not None:
            print("Color: "+node.color)
        if node.bottomprev is not None:
            print(" Bottom prev: "+str(node.bottomprev.index))
        if node.bottom is not None:
            print(" bottom: "+str(node.bottom.index))
        if node.bottomnext is not None:
            print(" Bottom Next: "+str(node.bottomnext.index))
        
        node = node.next
