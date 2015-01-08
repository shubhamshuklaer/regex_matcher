from automata import *
from nfa2dfa import *

class construct:
	"""  """

	@staticmethod
	def basicstruct(inp):
		state1 = 1
		state2 = 2
		basic = automata()
		basic.setstartstate(state1)
		basic.addfinalstates(state2)
		basic.addtransition(1, 2, inp)
		return basic

	@staticmethod
	def plusstruct(a, b):
		[a, m1] = a.newBuildFromNumber(2)
		[b, m2] = b.newBuildFromNumber(m1)
		state1 = 1
		state2 = m2
		plus = automata()
		plus.setstartstate(state1)
		plus.addfinalstates(state2)
		plus.addtransition(plus.startstate, a.startstate, automata.epsilon())
		plus.addtransition(plus.startstate, b.startstate, automata.epsilon())
		plus.addtransition(a.finalstates[0], plus.finalstates[0], automata.epsilon())
		plus.addtransition(b.finalstates[0], plus.finalstates[0], automata.epsilon())
		plus.addtransition_dict(a.transitions)
		plus.addtransition_dict(b.transitions)
		return plus

	@staticmethod
	def dotstruct(a, b):
		[a, m1] = a.newBuildFromNumber(1)
		[b, m2] = b.newBuildFromNumber(m1)
		state1 = 1
		state2 = m2-1
		dot = automata()
		dot.setstartstate(state1)
		dot.addfinalstates(state2)
		dot.addtransition(a.finalstates[0], b.startstate, automata.epsilon())
		dot.addtransition_dict(a.transitions)
		dot.addtransition_dict(b.transitions)
		return dot

	@staticmethod
	def starstruct(a):
		[a, m1] = a.newBuildFromNumber(2)
		state1 = 1
		state2 = m1
		star = automata()
		star.setstartstate(state1)
		star.addfinalstates(state2)
		star.addtransition(star.startstate, a.startstate, automata.epsilon())
		star.addtransition(star.startstate, star.finalstates[0], automata.epsilon())
		star.addtransition(a.finalstates[0], star.finalstates[0], automata.epsilon())
		star.addtransition(a.finalstates[0], a.startstate, automata.epsilon())
		star.addtransition_dict(a.transitions)
		return star

