from PyQt5 import QtCore
import sys
import logging
from automata import *

class regex2nfa(QtCore.QObject):

    send_error=QtCore.pyqtSignal("QString")
    
    def __init__(self,regex):
        super(QtCore.QObject,self).__init__()
        self.operators=["+","(",")","*","&"]
        self.alphabets=['a','b']
        self.regex=regex
        self.nfa=automata("nfa")

    def convert_to_nfa(self):
        #adding & to denote concat
        temp_regex=""
        for char in self.regex:
            if temp_regex != "" and temp_regex[-1] in self.alphabets and char in self.alphabets:
                temp_regex+="&"+char
            else:
                temp_regex+=char
        self.regex=temp_regex

        self.convert_to_postfix()

        stack=[]
        epsilon=self.nfa.epsilon()
        initial_state=0
        final_state=0
        new_state=0
        stack.append((initial_state,final_state))
        for char in self.regex:
            if char in self.alphabets:
                
                self.nfa.add_state()
                new_state+=1
                initial_state=new_state
                self.nfa.add_state()
                new_state+=1
                final_state=new_state
                self.nfa.add_transition(initial_state,char,final_state)
                stack.append((initial_state,final_state))

            elif char in self.operators:

                if (char == "*" ):
                    #popping the operand
                    temp_tuple=stack.pop()
                    initial_state=temp_tuple[0]
                    final_state=temp_tuple[1]
                    
                    self.nfa.add_state()
                    new_state+=1
                    self.nfa.add_transition(new_state,epsilon,initial_state)
                    
                    self.nfa.add_transition(initial_state,epsilon,final_state)

                    initial_state=new_state
                    self.nfa.add_state()
                    new_state+=1
                    final_state=new_state

                    self.nfa.add_transition(initial_state,epsilon,final_state)

                    stack.append((initial_state,final_state))
                elif (char == "+"):
                    self.nfa.add_state()
                    new_state+=1
                    initial_state=new_state
                    self.nfa.add_state()
                    new_state+=1
                    final_state=new_state

                    temp_tuple=stack.pop()
                    self.nfa.add_transition(initial_state,epsilon,temp_tuple[0])
                    self.nfa.add_transition(temp_tuple[1],epsilon,final_state)

                    temp_tuple=stack.pop()
                    self.nfa.add_transition(initial_state,epsilon,temp_tuple[0])
                    self.nfa.add_transition(temp_tuple[1],epsilon,final_state)

                    stack.append((initial_state,final_state))

                elif (char == "&" ):

                    temp_tuple=stack.pop()
                    initial_state=temp_tuple[0]
                    final_state=temp_tuple[1]

                    temp_tuple=stack.pop()
                    self.nfa.add_transition(final_state,epsilon,temp_tuple[0])
                    final_state=temp_tuple[1]

                    stack.append((initial_state,final_state))
        
        temp_tuple=stack.pop()
        self.nfa.add_transition(0,epsilon,temp_tuple[0])
        self.nfa.add_state()
        new_state+=1
        self.nfa.add_transition(temp_tuple[1],epsilon,new_state)
        self.nfa.add_final_state(new_state)
                

        self.nfa.display_automata()

    def convert_to_postfix(self):
        stack=[]
        postfix=""
        for char in self.regex:
            if char in self.alphabets:
                postfix+=char
            elif char in self.operators:
                if( char == "(" ):
                    stack.append("(")
                elif( char == ")" ):
                    while( stack[-1] != "("):
                        postfix+=stack.pop()
                    stack.pop()#removing the (
                else:
                    #For sequences, (strings, lists, tuples), use the fact that empty sequences are false
                    while(stack and stack[-1] != "(" and self.heigher_precidence(stack[-1],char) ):
                        postfix+=stack.pop()
                    stack.append(char)
        
        while( stack ):#popping everything that is remaining in stack
            postfix+=stack.pop()

        self.regex=postfix
        logging.warning(self.regex)


    def heigher_precidence(self,a,b):
        if( a == "*" ):
            return True
        elif( a == "+" and b == "*" ):
            return False
        else:
            return True

                        
                    







