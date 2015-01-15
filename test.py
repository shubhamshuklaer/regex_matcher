from automata import *
from nfa2dfa import *
from regex2nfa import *
from dfa2mindfa import *


		##########
		# Part 1 #
		##########
		
aut_nfa = automata('nfa')
aut_nfa.add_char("x")
aut_nfa.add_char("y")
aut_nfa.add_state()
aut_nfa.add_state()
aut_nfa.add_state()
aut_nfa.add_state()
aut_nfa.add_transition(1,'x',3)
aut_nfa.add_transition(1,'#',2)
aut_nfa.add_transition(2,'y',3)
aut_nfa.add_transition(3,'#',4)
aut_nfa.add_transition(0,'x',1)
aut_nfa.add_transition(4,'y',1)
####
aut_nfa.add_transition(0,'x',1)
aut_nfa.add_transition(0,'y',2)
aut_nfa.add_transition(1,'x',0)
aut_nfa.add_transition(1,'y',3)
aut_nfa.add_transition(2,'x',0)
aut_nfa.add_transition(2,'y',3)
aut_nfa.add_transition(3,'x',3)
aut_nfa.add_transition(3,'y',3)
####
aut_nfa.add_final_state(3)
aut_nfa.display_automata()

		##########
		# Part 2 #
		##########

nfa2dfa_obj = nfa2dfa('nfa2dfa')
nfa2dfa_obj.set_nfa(aut_nfa)
nfa2dfa_obj.set_charset(aut_nfa.char_set)
nfa2dfa_obj.build_dfa()
aut_dfa = nfa2dfa_obj.dfa
nfa2dfa_obj.display_automata()
# automata.display_nx_automata(aut_dfa)

		##########
		# Part 3 #
		##########

nfa2mindfa_obj = dfa2mindfa(aut_dfa)
nfa2mindfa_obj.minimiseIt()

aut_min_dfa = automata("min_dfa")
aut_min_dfa = nfa2mindfa_obj.create_new_dfa()
aut_min_dfa.display_automata()
#print aut_min_dfa.e_states
print aut_min_dfa.accepting_string("xxy")
print aut_dfa.accepting_string("xxy")