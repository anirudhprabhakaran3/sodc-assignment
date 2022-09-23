import networkx as nx
import matplotlib.pyplot as plt

def show_tree(bdd):
    g = nx.DiGraph()

    for node in bdd.all_nodes:
        if node == None:
            continue
        g.add_node(node.name)

    g.add_nodes_from(bdd.order)
    g.add_node(1)
    g.add_node(0)

    g.add_edges_from(bdd.edges)

    nx.draw(g, with_labels=True)
    plt.show()

