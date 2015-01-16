from __future__ import print_function
import sys
from gui import *


class automata:
    def __init__(self,arg):
        self.arg = arg
        self.transitions = dict()
        self.char_set = set()
        self.s_states = []
        self.s_states.append(0)
        self.e_states = []
        self.num_states = 1
        self.states = set()
        self.states.add(0)
        self.transitions[0] = dict()

    def error(self,msg):
        sys.stderr.write(msg)
        sys.exit(1)
    
    def epsilon(self):
        return '#'
    
    def get_final_states(self):
        return self.e_states

    def add_transition(self,from_state, input_char, to_state):
        if input_char not in self.char_set:
            if input_char != '#':
                self.char_set.add(input_char)

        if from_state not in self.states:
            self.error("state not defined "+str(from_state))

        if to_state not in self.states:
            self.error("state not defined "+str(to_state))
            
        if(from_state in self.transitions):
            if input_char not in self.transitions[from_state]:
                self.transitions[from_state][input_char] = []
            self.transitions[from_state][input_char].append(to_state)
        else:
            self.transitions[from_state] = dict()
            self.transitions[from_state][input_char] = []
            self.transitions[from_state][input_char].append(to_state)
            
    def add_final_state(self,state):
        if state not in self.states:
            self.error("state "+str(state)+" doesn't exist")
        self.e_states.append(state)

    def if_final_state(self,state):
        if state in self.e_states:
            return 1
        else:
            return 0
    
    def add_char(self,char):
        self.char_set.add(char)

    def get_new_state(self):
        return self.num_states

    def add_state(self):
        self.states.add(self.get_new_state())
        self.states.add(self.num_states)
        self.transitions[self.num_states] = dict()
        self.num_states = self.num_states + 1
        

    def get_transition(self,from_state,input_char):
        # print( "getting transition from ", from_state, " on input ", input_char )
        if from_state not in self.states:
            self.error("state "+str(from_state)+" doesn't exist\n")
        # print( "ok_5" )
        if input_char in self.transitions[from_state]:
            return self.transitions[from_state][input_char]
        else:
            return []

    def get_all_transitions(self, from_state, input_char):
        # print( "getting all transitions from ", from_state, " on input ", input_char )
        # print( "states: ", self.states )
        if from_state not in self.states:
            self.error("state "+str(from_state)+" doesn't exist\n")
        # print( "trying closure of", from_state )
        from_state_closure = self.eps_closure(from_state)
        ret = set()
        for state in from_state_closure:
            if input_char in self.transitions[state]:
                temp_list = self.transitions[state][input_char]
                for l in temp_list:
                    ret.add(l)
        # print( ret, len(ret) )
        temp_set = ret.copy()
        for state in temp_set:
            # print( "trying closure of", state )
            state_closure = self.eps_closure(state)
            ret.update(list(state_closure))
        # print( "returning ret" )
        return ret

    def eps_closure(self,state):
        # print( "getting closure of ", state )
        s = set()
        temp = set()
        s.add(state)
        if state not in self.states:
            self.error("state "+str(state)+" doesn't exist\n")
        if '#' in self.transitions[state]:            
            for x in self.transitions[state][self.epsilon()]:
                s.add(x)
                temp.add(x)
            while(len(temp)!=0):
                temp2 = set()
                for x in temp:
                    temp_list = self.get_transition(x,self.epsilon())
                    for y in temp_list:
                        if(y not in s):
                            temp2.add(y)
                            s.add(y)
                temp.clear()
                temp = temp2
        return s
        
    def display_transitions(self, from_state):
        print( str(from_state)," :", )
        for ch in self.char_set:
            trans = self.get_transition(from_state, ch)
            for state in trans:
                print( "\t", str(ch), "->", str(state) )

    def display_automata(self):
        print( "-----------------\ndisplaying ", self.arg )
        print( "-----------------" )
        for state in self.states:
            self.display_transitions(state)
        print("start state(s): ", self.s_states)
        print("final state(s): ", self.e_states)
        
    def display_nx_automata(self, pic_name, title_name):
        gui_obj = gui("nx_gui")
        gui_obj.set_name(pic_name)
        gui_obj.set_title(title_name)
        nx_graph = gui_obj.to_nx_graph(self)
        
    def accepting_string(self,s):
        state = 0 
        for i in range(0,len(s)-1):
            state = self.get_transition(state,s[i])[0]
        if(state in self.e_states):
            return True
        else:
            return False
