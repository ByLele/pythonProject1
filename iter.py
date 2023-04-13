import dis
class NodeIter:
    def __init__(self,node):
        self.curr_node = node
    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        node,self.curr_node = self.curr_node,self.curr_node.next
        return node

    def __iter__(self):
        return self
class Node:
    def __init__(self,name):
        self.name = name
        self.next = None
    def __iter__(self):
        return NodeIter(self)
#TODO:生成器写法

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next

node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
dis.dis(Node)
node1.next = node2
node2.next = node3
for i in node1:
    print(i.name)