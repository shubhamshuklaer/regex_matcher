from automata import *
from dfa2mindfa import *

class nfa2dfa:
	"""  """

	def __init__(self, nfa):
		self.buildDFA(nfa)
		self.minimise()

	def getDFA(self):
		return self.dfa

	def getMinimisedDFA(self):
		return self.minDFA

	def displayDFA(self):
		self.dfa.display()

	def displayMinimisedDFA(self):
		self.minDFA.display()

	def buildDFA(self, nfa):
		allstates = dict()
		eclose = dict()
		count = 1
		state1 = nfa.getEClose(nfa.startstate)
		eclose[nfa.startstate] = state1
		dfa = automata(nfa.language)
		dfa.setstartstate(count)
		states = [[state1, count]]
		allstates[count] = state1
		count +=  1
		while len(states) != 0:
			[state, fromindex] = states.pop()
			for char in dfa.language:
				trstates = nfa.gettransitions(state, char)
				for s in list(trstates)[:]:
					if s not in eclose:
						eclose[s] = nfa.getEClose(s)
					trstates = trstates.union(eclose[s])
				if len(trstates) != 0:
					if trstates not in allstates.values():
						states.append([trstates, count])
						allstates[count] = trstates
						toindex = count
						count +=  1
					else:
						toindex = [k for k, v in allstates.iteritems() if v  ==  trstates][0]
					dfa.addtransition(fromindex, toindex, char)
		for value, state in allstates.iteritems():
			if nfa.finalstates[0] in state:
				dfa.addfinalstates(value)
		self.dfa = dfa

	def acceptsString(self, string):
		currentstate = self.dfa.startstate
		for ch in string:
			if ch==":e:":
				continue
			st = list(self.dfa.gettransitions(currentstate, ch))
			if len(st) == 0:
				return False
			currentstate = st[0]
		if currentstate in self.dfa.finalstates:
			return True
		return False

	def minimise(self):
		min = dfa2mindfa()
		min.simplify(self.dfa, self)