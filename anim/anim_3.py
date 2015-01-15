import pygraphviz as pgv
G=pgv.AGraph(strict=False, dim=3)
G.add_node('a')
G.add_node('b')
G.layout()
G.add_edge('a','b','first')
G.add_edge('a','b','second')
sorted(G.edges(keys=True)) 
G.draw('file.png')