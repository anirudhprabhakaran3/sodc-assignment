from audioop import add
from boolalg.bdd.node import Node
from boolalg.operations import cofactor, stringify

class BDD:

    def __init__(self):
        self.order = []
        self.ONE = Node(1)
        self.ZERO = Node(0)
        self.all_nodes = [None]
        self.edges = []

    def root(self):
        return self.all_nodes[1]

    def add_order(self, order):
        """
            Converts ordering to BDD format

            Input: Comma seperated string of characters
            Output: None
        """
        order = [x.strip() for x in order.split(',')]
        self.all_nodes = [None] * (2 ** (len(order)+1))
        root_node = Node(order[0])
        self.order = order
        self.all_nodes[1] = root_node

    def add_node(self, node, f):

        if node == None:
            return

        index = self.all_nodes.index(node)
        left_child = 2 * index
        right_child = 2 * index + 1

        index_in_order = self.order.index(node.name)

        if len(f) == 1:
            node.set_left_child(self.ZERO)
            node.set_right_child(self.ONE)
            self.all_nodes[left_child] = self.ZERO
            self.all_nodes[right_child] = self.ONE
            pc_tuple = (node.name, self.ONE.name, {'color': 'blue'})
            nc_tuple = (node.name, self.ZERO.name, {'color': 'red'})
            self.edges.append((node.id, self.ONE.id, {'color': 'blue'}))
            self.edges.append((node.id, self.ZERO.id, {'color': 'red'}))
            return

        pc, nc = cofactor(f, node.name)
        pc_string = stringify(pc)
        nc_string = stringify(nc)

        pc_count = 0
        nc_count = 0

        # Processing positive cofactor
        new_pc_node = None
        if pc == ['1']:
            node.set_right_child(self.ONE)
            self.all_nodes[right_child] = self.ONE
            pc_tuple = (node.name, self.ONE.name, {'color': 'blue'})
            self.edges.append((node.id, self.ONE.id, {'color': 'blue'}))
        elif pc == ['0']:
            node.set_right_child(self.ZERO)
            self.all_nodes[right_child] = self.ZERO
            pc_tuple = (node.name, self.ZERO.name, {'color': 'blue'})
            self.edges.append((node.id, self.ZERO.id, {'color': 'blue'}))
        else:
            for char in self.order[index_in_order+1:]:
                if (pc_count < 1) and (char in pc_string):
                    new_pc_node = Node(char)
                    node.set_right_child(new_pc_node)
                    self.all_nodes[right_child] = new_pc_node
                    pc_tuple = (node.name, new_pc_node.name, {'color': 'blue'})
                    self.edges.append((node.id, new_pc_node.id, {'color': 'blue'}))
                    pc_count += 1

        # Proecssing negative cofactor
        new_nc_node = None
        if nc == ['1']:
            node.set_left_child(self.ONE)
            self.all_nodes[left_child] = self.ONE
            nc_tuple = (node.name, self.ONE.name, {'color': 'red'})
            self.edges.append((node.id, self.ONE.id, {'color': 'red'}))
        elif nc == ['0']:
            node.set_left_child(self.ZERO)
            self.all_nodes[left_child] = self.ZERO
            nc_tuple = (node.name, self.ZERO.name, {'color': 'red'})
            self.edges.append((node.id, self.ZERO.id, {'color': 'red'}))
        else:
            for char in self.order[index_in_order+1:]:
                if (nc_count < 1) and (char in nc_string):
                    new_nc_node = Node(char)
                    node.set_left_child(new_nc_node)
                    self.all_nodes[left_child] = new_nc_node
                    nc_tuple = (node.name, new_nc_node.name, {'color': 'red'})
                    self.edges.append((node.id, new_nc_node.id, {'color': 'red'}))
                    nc_count += 1

        self.add_node(new_pc_node, pc)
        self.add_node(new_nc_node, nc)
    
    def print_all(self):
        print(f"Order given: {self.order}")
        print(f"List of all node objects: {self.all_nodes}")
        print()
        for node in self.all_nodes:
            print(node, end=" --> ")
        print()

    def generate(self, f, order):
        self.add_order(order)
        self.add_node(self.root(), f)
