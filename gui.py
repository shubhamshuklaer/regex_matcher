from automata import *
import networkx as nx
import numpy as np
from mayavi import mlab
import matplotlib.pyplot as plt

class gui:
	"""docstring for gui"""
	def __init__(self, arg):
		self.arg = arg
		

	def to_nx_2d_graph(self, aut):
		ret = nx.MultiDiGraph()
		ret.add_nodes_from(list(aut.states))
		for k in aut.transitions.keys():
			for key, value in aut.transitions[k].items():
				for v in value:
					ret.add_edge(k, v, input_char=key, color='red')
		
		ret.add_edge(1, 0 , input_char='x', color='red')
		nx.draw_spectral(ret)
		# plt.show()
		return ret

	def to_nx_3d_graph(self, graph_2d):
		# reorder nodes from 0,len(graph_3d)-1
		graph_3d=nx.convert_node_labels_to_integers(graph_2d)
		
		# 3d spring layout
		pos=nx.graphviz_layout(graph_3d)
		# numpy array of x,y,z positions in sorted node order
		xyz=np.array([pos[v] for v in sorted(graph_3d)])
		# set labels
		edge_text_pos=0.3
		labels = range(len(graph_3d))

		# specifiy edge labels explicitly
		edge_labels=dict([((u,v,),d['input_char']) for u,v,d in graph_3d.edges(data=True)])
		# print edge_labels
		# print len(edge_labels)
		# print len(graph_3d)
		nx.draw_networkx_edge_labels(graph_3d, pos, edge_labels=edge_labels, label_pos=edge_text_pos)
		# scalar colors
		scalars=np.array(graph_3d.nodes())+5

		mlab.figure(1, bgcolor=(0, 0, 0))
		mlab.clf()

		pts = mlab.points3d(xyz[:,0], xyz[:,1], #xyz[:,2],
		                    scalars,
		                    scale_factor=0.1,
		                    scale_mode='none',
		                    # colormap='winter',
		                    colormap='Blues',
		                    resolution=20)

		pts.mlab_source.dataset.lines = np.array(graph_3d.edges())
		tube = mlab.pipeline.tube(pts, tube_radius=0.01)
		mlab.pipeline.surface(tube, color=(0.8, 0.8, 0.8))

		mlab.savefig('pics/3d_out.png')
		mlab.show() # interactive window
		return graph_3d
