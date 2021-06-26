class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)

    def add_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head)
        self.head = new_node

    def remove_node(self, value_to_remove):
        current_node = self.head
        if current_node.get_value() == value_to_remove:
            self.head = current_node.get_next_node()

        while current_node:
            next_node = current_node.get_next_node()

            if current_node.get_next_node() == None:
                break

            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                next_node = None
            current_node = current_node.get_next_node()
            
        return




