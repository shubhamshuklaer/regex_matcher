from automata import *
from networkx import *
import networkx as nx
import pygraphviz as pgv
import numpy as np
import matplotlib.pyplot as plt


class gui:
	"""docstring for gui"""
	def __init__(self, arg):
		self.arg = arg
		self.color_set = ['red', 'blue', 'chartreuse4', 'burlywood4', 'darkslategrey']
		
	def set_name(self, pic_name):
		self.pic_name = pic_name

	def set_title(self, title_name):
		self.title_name = title_name
	
	def to_nx_graph(self, aut):
		nx_graph = nx.MultiDiGraph(autosize=False, size="5.75,7.25", ranksep='0.9', splines=True, sep='+5, 5',
			overlap='false', nodesep='0.2', labelfontcolor='blue', labelloc='t', label=self.title_name)
		nx_graph.add_nodes_from(list(aut.states), height='0.4', width='0.4', color='pink',
			style='filled', fixedsize=False, fontsize='11')
		
			
		for k in aut.transitions.keys():
			for key, value in aut.transitions[k].items():
				for v in value:
					nx_graph.add_edge(k, v, color = (self.color_set[2]) if (key=='#') else (self.color_set[list(aut.char_set).index(key) % len(list(aut.char_set))]), 
						arrowsize=0.5, labeldistance=2.5, penwidth='0.8')
		nx.draw_spectral(nx_graph)

		gv_graph = to_agraph(nx_graph) 
		gv_graph.layout(prog='dot')
		# prog=neato|dot|twopi|circo|fdp|nop

		# set start & end states
		for node in gv_graph.nodes():
			if int(node.get_name()) in aut.e_states:
				node.attr['color'] = 'green'
				node.attr['shape'] = 'doublecircle'
			elif int(node.get_name()) in aut.s_states:
				node.attr['color'] = 'blue'
				node.attr['shape'] = 'diamond'
		gv_graph.draw('pics/'+str(self.pic_name)+'.png')
		
		return gv_graph

