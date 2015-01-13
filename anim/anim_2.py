#!/usr/bin/env python
import random
import pylab
from matplotlib.pyplot import pause
import networkx as nx
pylab.ion()

graph = nx.Graph()
node_number = 0
graph.add_node(node_number, Position=(random.randrange(0, 100), random.randrange(0, 100)))

def get_fig():
    global node_number
    node_number += 1
    graph.add_node(node_number, Position=(random.randrange(0, 100), random.randrange(0, 100)))
    ran_choice = random.choice(graph.nodes())
    graph.add_edge(node_number, ran_choice)
    graph[node_number][ran_choice]['color'] = 'blue'

    nx.draw(graph, pos=nx.get_node_attributes(graph,'Position'))

num_plots = 50;
pylab.show()

for i in range(num_plots):

    get_fig()
    pylab.draw()
    pause(1)