from automata import *
from nfa2dfa import *


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


aut_nfa.add_final_state(3)
# print aut_nfa.if_final_state(4)
aut_nfa.display_automata()

# print aut_nfa.eps_closure(0)

aut_dfa = nfa2dfa('nfa2dfa')
aut_dfa.set_nfa(aut_nfa)
aut_dfa.set_charset(aut_nfa.char_set)
aut_dfa.build_dfa()
aut_dfa.display_automata()

