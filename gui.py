from automata import *
import networkx as nx
import numpy as np
from mayavi import mlab
import matplotlib.pyplot as plt

class gui:
	"""docstring for gui"""
	def __init__(self, arg):
		self.arg = arg
		

	def to_nx_graph(self, aut):
		ret = nx.Graph()
		ret.add_nodes_from(list(aut.states))
		for k in aut.transitions.keys():
			for key, value in aut.transitions[k].items():
				for v in value:
					ret.add_edge(k, v)
		nx.draw_spectral(ret)
		plt.show()
		return ret
