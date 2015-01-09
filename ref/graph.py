from automata import *

def drawGraph(automata, file = ""):
	"""  """
	f = popen(r"dot -Tpng -o graph%s.png" % file, 'w')
	try:
		f.write(automata.getDotFile())
	except:
		raise BaseException("Error creating graph")
	finally:
		f.close()

