"""NFA to DFA class"""

from __future__ import print_function
from automata import *
class nfa2dfa:
	"""docstring for nfa2dfa"""
	def __init__(self, arg):
		self.arg = arg
		self.dfa = automata('dfa')
		self.marked_states = dict()
		self.num_marked_states = 0
		self.dfa_states_set = []

	def set_charset(self, char_set):
		self.dfa.char_set = char_set

	def set_nfa(self, aut_nfa):
		self.nfa = aut_nfa

	def build_dfa(self):
		self.dfa.s_states = [0]
		self.dfa_states_set.append(self.nfa.eps_closure(self.nfa.s_states[0]))
		self.marked_states[str(0)] = False
		while self.num_marked_states < len(self.dfa_states_set):
			ums = self.get_unmarked_state()
			# print("got unmarked state: ", ums)
			if ums == None:
				break
			self.update_value(str(ums), True)
			self.num_marked_states = self.num_marked_states + 1
			for ch in self.nfa.char_set:
				if ch == '#':
					continue
				ums_closure = set()
				for r in self.dfa_states_set[ums]:
					ums_closure.update(self.nfa.eps_closure(int(r)))
				# print( "set: ",ums_closure," on input: ",ch )
				temp_set = set()
				for state in ums_closure:
					# print("state:", state, "ch: ", ch, "transitions: ", self.nfa.get_all_transitions(int(state), ch))
					temp_states = self.nfa.get_all_transitions(int(state), ch)
					temp_set.update(temp_states)

				if temp_set not in self.dfa_states_set:
					# print( "adding set to dfa: ",  temp_set )
					siz = len(self.dfa_states_set)
					self.dfa_states_set.append(temp_set)
					self.marked_states[self.dfa.get_new_state()] = False
					self.dfa.add_state()
					self.dfa.add_transition(ums, ch, siz)
				else:
					self.dfa.add_transition(ums, ch, self.dfa_states_set.index(temp_set))
			# print( "dfa size = ", len(self.dfa_states_set) )
			# print( "no. marked states = ", self.num_marked_states )

		# set final states
		state_num = 0
		for state_set in self.dfa_states_set:
			if len(state_set.intersection(self.nfa.e_states)) > 0:
				if state_num not in self.dfa.e_states:
					self.dfa.e_states.append(state_num)
			state_num = state_num + 1
		


	def get_unmarked_state(self):
		for k in self.marked_states.keys():
			if not self.marked_states[k]:
				return int(k)
		return None


	def update_value(self, state, assign):
		for k in self.marked_states.keys():
			if(str(k) == str(state)):
				self.marked_states[k] = assign

	def display_automata(self):
		self.display_mapping()
		self.dfa.display_automata()

	def display_mapping(self):
		print( "-----------------" )
		print( "displaying mapping from nfa to dfa" )
		print( "-----------------" )
		state_num = 0
		for state_set in self.dfa_states_set:
			print( state_num, " : ", state_set )
			state_num = state_num + 1
		
