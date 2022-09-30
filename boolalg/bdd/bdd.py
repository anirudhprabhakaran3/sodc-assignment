from math import floor
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
        self.unique = {}

    def root(self):
        """
            Return the root node of the BDD
        """
        return self.all_nodes[0]

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
        self.all_nodes = [None] * (2 ** (len(order) + 1))
        if f == ['1']:
            root_node = self.ONE
            order = [1]
        elif f == ['0']:
            root_node = self.ZERO
            order = [0]
        else:
            root_node = Node(order[0])
        self.order = order
        self.all_nodes[0] = root_node

    def add_node(self, node, f):
        """
            Adds a node to the BDD
            Input:
                node: An object of class boolalg.bdd.node.Node
                f: Function associated with that node
            Output:
                None
                Node is added to the BDD
        """

        if f == ['1'] or f == ['0']:
            return

        if node == None:
            return

        index = self.all_nodes.index(node)
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        index_in_order = self.order.index(node.name)

        if len(f) == 1 and len(f[0]) == 1:
            node.set_left_child(self.ZERO)
            node.set_right_child(self.ONE)
            self.all_nodes[left_child] = self.ZERO
            self.all_nodes[right_child] = self.ONE
            self.edges.append((node, self.ONE, {'color': 'blue'}))
            self.edges.append((node, self.ZERO, {'color': 'red'}))
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

            self.edges.append((node, self.ONE, {'color': 'blue'}))
        elif pc == ['0']:
            node.set_right_child(self.ZERO)
            self.all_nodes[right_child] = self.ZERO

            self.edges.append((node, self.ZERO, {'color': 'blue'}))
        else:
            for char in self.order[index_in_order+1:]:
                if (pc_count < 1) and (char in pc_string):
                    if self.find(char) == None:
                        new_pc_node = Node(char)
                        self.unique[char] = new_pc_node
                    else:
                        new_pc_node = self.find(char)
                    node.set_right_child(new_pc_node)
                    self.all_nodes[right_child] = new_pc_node
                    self.edges.append((node, new_pc_node, {'color': 'blue'}))
                    pc_count += 1

        # Proecssing negative cofactor
        new_nc_node = None
        if nc == ['1']:
            node.set_left_child(self.ONE)
            self.all_nodes[left_child] = self.ONE
            self.edges.append((node, self.ONE, {'color': 'red'}))
        elif nc == ['0']:
            node.set_left_child(self.ZERO)
            self.all_nodes[left_child] = self.ZERO
            self.edges.append((node, self.ZERO, {'color': 'red'}))
        else:
            for char in self.order[index_in_order+1:]:
                if (nc_count < 1) and (char in nc_string):
                    if self.find(char) == None:
                        new_nc_node = Node(char)
                        self.unique[char] = new_nc_node
                    else:
                        new_nc_node = self.find(char)
                    node.set_left_child(new_nc_node)
                    self.all_nodes[left_child] = new_nc_node
                    self.edges.append((node, new_nc_node, {'color': 'red'}))
                    nc_count += 1

        self.add_node(new_pc_node, pc)
        self.add_node(new_nc_node, nc)

    def find(self, name):
        """
            Find if an existing node of that name exists.
            Input:
                name: String corresponding to name of node
            Output:
                Node/None: If found, returns the node, or None
        """
        if name in self.unique.keys():
            return self.unique[name]
        return None

    def reduce(self):
        if self.root() == self.ONE:
            return ['1']
        elif self.root() == self.ZERO:
            return ['0']

        location_of_ones = []
        list_of_cubes = []
        for (index, node) in enumerate(self.all_nodes):
            if node == self.ONE:
                location_of_ones.append(index)

        for location in location_of_ones:
            index = location
            cube = ""
            while index > 0:
                parent = floor((index-1) / 2)
                if (2*parent + 2) == index:
                    variable = self.all_nodes[parent].name
                    cube += variable
                index = parent
            cube = ''.join(sorted(cube))
            list_of_cubes.append(cube)
        return list_of_cubes
            
    
    def print_all(self):
        """
            Prints the list of nodes in the BDD
        """
        print()
        for (index, node) in enumerate(self.all_nodes):
            if node != None:
                print(f"{index}: {node}")

    def generate(self, f, ordering):
        """
            Wrapper function for BDD
            Adds the ordering and adds other nodes to the BDD
        """
        f = order(apply_rules(f))
        self.unique['1'] = self.ONE
        self.unique['0'] = self.ZERO
        self.add_order(ordering, f)
        self.add_node(self.root(), f)
        if self.all_nodes[1] == self.ONE and self.all_nodes[2] == self.ONE:
            self.all_nodes[0] = self.ONE
            self.all_nodes[1] = self.all_nodes[2] = None
        elif self.all_nodes[1] == self.ZERO and self.all_nodes[2] == self.ZERO:
            self.all_nodes[0] = self.ZERO
            self.all_nodes[1] = self.all_nodes[2] = None
