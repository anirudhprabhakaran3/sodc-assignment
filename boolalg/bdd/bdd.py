from boolalg.operations import apply_rules
from boolalg.utils import order
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

    def add_order(self, order, f):
        """
            Converts ordering to BDD format

            Input: Comma seperated string of characters
            Output: None
        """
        stringify_f = stringify(f)
        order = [x.strip() for x in order.split(',')]
        new_order = []
        for char in order:
            if char in stringify_f:
                new_order.append(char)
        order = new_order
        self.all_nodes = [None] * (2 ** (len(order)+1))
        if f == ['1']:
            root_node = self.ONE
            order = [1]
        elif f == ['0']:
            root_node = self.ZERO
            order = [0]
        else:
            root_node = Node(order[0])
        self.order = order
        self.all_nodes[1] = root_node

    def add_node(self, node, f):

        if f == ['1'] or f == ['0']:
            return

        if node == None:
            return

        index = self.all_nodes.index(node)
        left_child = 2 * index
        right_child = 2 * index + 1

        index_in_order = self.order.index(node.name)

        if len(f) == 1 and len(f[0]) == 1:
            node.set_left_child(self.ZERO)
            node.set_right_child(self.ONE)
            self.all_nodes[left_child] = self.ZERO
            self.all_nodes[right_child] = self.ONE
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
            self.edges.append((node.id, self.ONE.id, {'color': 'blue'}))
        elif pc == ['0']:
            node.set_right_child(self.ZERO)
            self.all_nodes[right_child] = self.ZERO
            self.edges.append((node.id, self.ZERO.id, {'color': 'blue'}))
        else:
            for char in self.order[index_in_order+1:]:
                if (pc_count < 1) and (char in pc_string):
                    new_pc_node = Node(char)
                    node.set_right_child(new_pc_node)
                    self.all_nodes[right_child] = new_pc_node
                    self.edges.append((node.id, new_pc_node.id, {'color': 'blue'}))
                    pc_count += 1

        # Proecssing negative cofactor
        new_nc_node = None
        if nc == ['1']:
            node.set_left_child(self.ONE)
            self.all_nodes[left_child] = self.ONE
            self.edges.append((node.id, self.ONE.id, {'color': 'red'}))
        elif nc == ['0']:
            node.set_left_child(self.ZERO)
            self.all_nodes[left_child] = self.ZERO
            self.edges.append((node.id, self.ZERO.id, {'color': 'red'}))
        else:
            for char in self.order[index_in_order+1:]:
                if (nc_count < 1) and (char in nc_string):
                    new_nc_node = Node(char)
                    node.set_left_child(new_nc_node)
                    self.all_nodes[left_child] = new_nc_node
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

    def generate(self, f, ordering):
        f = order(apply_rules(f))
        self.add_order(ordering, f)
        self.add_node(self.root(), f)
