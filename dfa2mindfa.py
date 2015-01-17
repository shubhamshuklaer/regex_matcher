from __future__ import print_function
from automata import *
import operator

class dfa2mindfa:
    def __init__(self,arg):
        self.states = dict()
        self.numberOfdisSet = 2
        self.automata = automata("Copying Data")
        self.automata = arg
        for i in range(0,self.automata.get_new_state()):
            self.states[i] = set()
        self.f = self.automata.get_final_states()
        self.stateToGroup = dict()
        for i in range(0,self.automata.get_new_state()):
            if i in self.f:
                self.states[1].add(i)
                self.stateToGroup[i] = 1
            else:
                self.states[0].add(i)
                self.stateToGroup[i] = 0
        
    def print_all(self):
        for group in range(0,self.numberOfdisSet):
            print(self.states[group])

    def minimiseIt(self):
        check = True
        while(check):
            temp = 0
            for group in range(0,self.numberOfdisSet):
                pair = dict()
                for state in self.states[group]:
                    x = self.automata.get_transition(state,'x')[0]
                    y = self.automata.get_transition(state,'y')[0]
                    x = self.stateToGroup[x]
                    y = self.stateToGroup[y]
                    #print x,y,state,group
                    pair[state] = ((0.5)*(x+y)*(x+y+1)) + y
                pair = sorted(pair.items(), key=operator.itemgetter(1))

                num = pair[0][1]
                new_list = False
                i = 1
                while(i < len(pair)):
                   # print i,num, pair[i][1]
                    while(i < len(pair) and pair[i][1] == num):   
                        if new_list == True:
                            if(self.numberOfdisSet+temp-1 in self.states.keys()):
                                self.states[self.numberOfdisSet+temp-1].add(pair[i][0])
                                self.states[group].remove(pair[i][0])
                                self.stateToGroup[pair[i][0]] = self.numberOfdisSet+temp-1
                            else:
                                self.states[self.numberOfdisSet+temp-1] = set()
                                self.states[self.numberOfdisSet+temp-1].add(pair[i][0])
                                self.states[group].remove(pair[i][0])
                                self.stateToGroup[pair[i][0]] = self.numberOfdisSet+temp-1
                        i = i+1    
                    if i < len(pair):
                        num = pair[i][1]
                        temp = temp+1
                        new_list = True

            if(temp != 0):
                check = True
                self.numberOfdisSet = self.numberOfdisSet+temp
            else:
                check = False
            

    def create_new_dfa(self):
        #print self.states
        new_automata = automata("Min Dfa")
        for group in self.states:
            if 0 in self.states[group] and group!=0:
                temp = set()
                temp = self.states[group]
                self.states[group] = self.states[0]
                self.states[0] = temp
        # print(self.states)
        for group in self.states:
        	for state in self.states[group]:
        		self.stateToGroup[state] = group

        for group in self.states:
            if(len(self.states[group])!=0 and (0 not in self.states[group])):
                new_automata.add_state()
        for group in self.states:

            for state in self.states[group]:
                # print("group: "group)
                new_automata.add_transition(group,'x',self.stateToGroup[self.automata.get_transition(state,'x')[0]])
                new_automata.add_transition(group,'y',self.stateToGroup[self.automata.get_transition(state,'y')[0]])
                break
        for group in self.states:
            for state in self.states[group]:
                if (state in self.f) and (group not in new_automata.e_states):
                    new_automata.add_final_state(group)
        return new_automata
