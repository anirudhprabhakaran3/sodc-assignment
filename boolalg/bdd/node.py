import uuid

class Node:

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.left_child = None
        self.right_child = None

    def print(self):
        print()
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Left child: {self.left_child}")
        print(f"Right Child: {self.right_child}")

    def get_left_child(self):
        return self.left_child

    def set_left_child(self, node):
        self.left_child = node

    def get_right_child(self):
        return self.right_child

    def set_right_child(self, node):
        self.right_child = node
    
    def get_id(self):
        return self.id

    def __str__(self):
        return f"{self.name}"

    def __eq__(self, other):
        if other == None:
            return False
        return self.get_id() == other.get_id()