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
    for node in bdd.all_nodes[1:]:
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
            ONE = (node.name, x, y)
            continue

        if node.name == 0:
            ZERO = (node.name, x, y)
            continue

        nodes[node.get_id()] = (node.name, x, y)
    
    nodes[bdd.ONE.get_id()] = ONE
    nodes[bdd.ZERO.get_id()] = ZERO

    for (id, node) in nodes.items():
        plt.plot(node[1], node[2], 'go', markersize=20)
        plt.annotate(node[0], (node[1], node[2]), size=14)

    for edge in bdd.edges:
        id1, id2, opts = edge
        node1 = nodes[id1]
        node2 = nodes[id2]
        color = opts['color']
        draw_arrow(plt, node1[1:], node2[1:], color)

    plt.show()


    # g = nx.DiGraph()

    # labelsdict = {}

    # for node in bdd.all_nodes:
    #     if node == None:
    #         continue
    #     g.add_node(node.get_id())
    #     labelsdict[node.get_id()] = node.name

    # g.add_nodes_from(bdd.order)
    # g.add_node(1)
    # g.add_node(0)

    # g.add_edges_from(bdd.edges)

    # nx.draw(g, labels=labelsdict, with_labels=True)
    # plt.show()
