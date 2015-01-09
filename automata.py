import sys
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
    def add_transition(self,from_state, input_char, to_state):
        if input_char not in self.char_set:
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
        self.num_states = self.num_states+1
        

    def get_transition(self,from_state,input_char):
        if from_state not in self.states:
            self.error("state "+str(from_state)+" doesn't exist")
        if input_char in self.transitions[from_state]:
            return self.transitions[from_state][input_char]
        else:
            return []

    def eps_closure(self,state):
        s = set()
        temp = set()
        s.add(state)
        if state not in self.states:
            self.error("state "+str(state)+" doesn't exist")
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
                
##t = automata('nfa')
##t.add_char("x")
##t.add_char("y")
##t.add_state()
##t.add_state()
##t.add_state()
##t.add_state()
##t.add_transition(1,'#',3)
##t.add_transition(1,'#',2)
##t.add_transition(2,'#',3)
##t.add_transition(3,'#',4)
##t.add_final_state(3)
##print t.if_final_state(4)
##
