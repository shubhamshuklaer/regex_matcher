from automata import *
import networkx as nx
import matplotlib.pyplot as plt


def to_nx_graph(self, aut):
	ret = nx.Graph()
	ret.add_nodes_from(list(aut.states))
	for k in aut.transitions.keys():
		for key, value in key.items():
			ret.add_edge(key, value)
	nx.draw_circular(ret)
	return ret
