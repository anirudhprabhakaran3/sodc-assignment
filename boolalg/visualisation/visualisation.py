import matplotlib.pyplot as plt

from math import log2, floor

def draw_arrow(plt, arr_start, arr_end, color):
       dx = arr_end[0] - arr_start[0]
       dy = arr_end[1] - arr_start[1]
       plt.arrow(arr_start[0], arr_start[1], dx, dy, head_width=0.1, head_length=0.2, length_includes_head=True, color=color)

def show_tree(bdd):
    height = floor(log2(len(bdd.all_nodes)))
    nodes = {}

    ONE = False
    ZERO = False

    counter = 1
    temp_counter = 0
    if bdd.root() == bdd.ONE or (bdd.root().get_left_child() == bdd.ONE and bdd.root().get_right_child() == bdd.ONE):
        ONE = (1, 3, 0)
        nodes[bdd.ONE.get_id()] = ONE
        bdd.edges = []
    elif bdd.root() == bdd.ZERO or (bdd.root().get_left_child() == bdd.ZERO and bdd.root().get_right_child() == bdd.ZERO):
        ZERO = (0, -3, 0)
        nodes[bdd.ZERO.get_id()] = ZERO
        bdd.edges = []
    else:
        for node in bdd.all_nodes:
            if node == None:
                counter += 1
                continue

            temp_x = floor(log2(counter))
            if temp_counter > temp_x:
                temp_counter = -temp_x
            y = height - temp_x
            x = temp_counter
            temp_counter += 1
            counter += 1

            if node.name == 1:
                ONE = (node.name, 1, 0)
                continue

            if node.name == 0:
                ZERO = (node.name, -1, 0)
                continue

            nodes[node.get_id()] = (node.name, x, y)
    
        nodes[bdd.ONE.get_id()] = ONE
        nodes[bdd.ZERO.get_id()] = ZERO

    for (id, node) in nodes.items():
        plt.plot(node[1], node[2], 'go', markersize=20)
        plt.annotate(node[0], (node[1], node[2]), size=14)

    for edge in bdd.edges:
        node1, node2, opts = edge
        id1 = node1.id
        id2 = node2.id
        node1 = nodes[id1]
        node2 = nodes[id2]
        color = opts['color']
        draw_arrow(plt, node1[1:], node2[1:], color)

    plt.show()