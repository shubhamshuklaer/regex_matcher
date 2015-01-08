from os import popen
import time

class automata:
	"""  """

	def __init__(self, language = set(['0', '1'])):
		self.states = set()
		self.startstate = None
		self.finalstates = []
		self.transitions = dict()
		self.language = language

	@staticmethod
	def epsilon():
		return "#"

	def setstartstate(self, state):
		self.startstate = state
		self.states.add(state)

	def addfinalstates(self, state):
		if isinstance(state, int):
			state = [state]
		for s in state:
			if s not in self.finalstates:
				self.finalstates.append(s)

	def addtransition(self, fromstate, tostate, inp):
		if isinstance(inp, str):
			inp = set([inp])
		self.states.add(fromstate)
		self.states.add(tostate)
		if fromstate in self.transitions:
			if tostate in self.transitions[fromstate]:
				self.transitions[fromstate][tostate] = self.transitions[fromstate][tostate].union(inp)
			else:
				self.transitions[fromstate][tostate] = inp
		else:
			self.transitions[fromstate] = {tostate : inp}

	def addtransition_dict(self, transitions):
		for fromstate, tostates in transitions.items():
			for state in tostates:
				self.addtransition(fromstate, state, tostates[state])

	def gettransitions(self, state, key):
		if isinstance(state, int):
			state = [state]
		trstates = set()
		for st in state:
			if st in self.transitions:
				for tns in self.transitions[st]:
					if key in self.transitions[st][tns]:
						trstates.add(tns)
		return trstates

	def getEClose(self, findstate):
		allstates = set()
		states = set([findstate])
		while len(states)!= 0:
			state = states.pop()
			allstates.add(state)
			if state in self.transitions:
				for tns in self.transitions[state]:
					if automata.epsilon() in self.transitions[state][tns] and tns not in allstates:
						states.add(tns)
		return allstates

	def display(self):
		print "states:", self.states
		print "start state: ", self.startstate
		print "final states:", self.finalstates
		print "transitions:"
		for fromstate, tostates in self.transitions.items():
			for state in tostates:
				for char in tostates[state]:
					print "  ",fromstate, "->", state, "on '"+char+"'",
			print

	def getPrintText(self):
		text = "language: {" + ", ".join(self.language) + "}\n"
		text += "states: {" + ", ".join(map(str,self.states)) + "}\n"
		text += "start state: " + str(self.startstate) + "\n"
		text += "final states: {" + ", ".join(map(str,self.finalstates)) + "}\n"
		text += "transitions:\n"
		linecount = 5
		for fromstate, tostates in self.transitions.items():
			for state in tostates:
				for char in tostates[state]:
					text += "    " + str(fromstate) + " -> " + str(state) + " on '" + char + "'\n"
					linecount +=1
		return [text, linecount]

	def newBuildFromNumber(self, startnum):
		translations = {}
		for i in list(self.states):
			translations[i] = startnum
			startnum += 1
		rebuild = automata(self.language)
		rebuild.setstartstate(translations[self.startstate])
		rebuild.addfinalstates(translations[self.finalstates[0]])
		for fromstate, tostates in self.transitions.items():
			for state in tostates:
				rebuild.addtransition(translations[fromstate], translations[state], tostates[state])
		return [rebuild, startnum]

	def newBuildFromEquivalentStates(self, equivalent, pos):
		rebuild = automata(self.language)
		for fromstate, tostates in self.transitions.items():
			for state in tostates:
				rebuild.addtransition(pos[fromstate], pos[state], tostates[state])
		rebuild.setstartstate(pos[self.startstate])
		for s in self.finalstates:
			rebuild.addfinalstates(pos[s])
		return rebuild

	def getDotFile(self):
		dotFile = "digraph DFA {\nrankdir=LR\n"
		if len(self.states) != 0:
			dotFile += "root=s1\nstart [shape=point]\nstart->s%d\n" % self.startstate
			for state in self.states:
				if state in self.finalstates:
					dotFile += "s%d [shape=doublecircle]\n" % state
				else:
					dotFile += "s%d [shape=circle]\n" % state
			for fromstate, tostates in self.transitions.items():
				for state in tostates:
					for char in tostates[state]:
						dotFile += 's%d->s%d [label="%s"]\n' % (fromstate, state, char)
		dotFile += "}"
		return dotFile


def isInstalled(program):
	"""  """
	import os
	def is_exe(fpath):
		return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
	fpath, fname = os.path.split(program)
	if fpath:
		if is_exe(program) or is_exe(program+".exe"):
			return True
	else:
		for path in os.environ["PATH"].split(os.pathsep):
			exe_file = os.path.join(path, program)
			if is_exe(exe_file) or is_exe(exe_file+".exe"):
				return True
	return False
