from automata import *
from graph import *
from nfa2dfa import *
from regex2nfa import *
from gui import *
import sys

def main():
	regex = "(01*1)*1"
	if len(sys.argv)>1:
		regex = sys.argv[1]
	print "Regular Expression: ", regex
	nfaObj = regex2nfa(regex)
	nfa = nfaObj.getNFA()
	dfaObj = nfa2dfa(nfa)
	dfa = dfaObj.getDFA()
	minDFA = dfaObj.getMinimisedDFA()
	print "\nNFA: "
	nfaObj.displayNFA()
	print "\nDFA: "
	dfaObj.displayDFA()
	print "\nMinimised DFA: "
	dfaObj.displayMinimisedDFA()
	if isInstalled("dot"):        
		drawGraph(dfa, "dfa")
		drawGraph(nfa, "nfa")
		drawGraph(minDFA, "mdfa")
		print "\nGraphs have been created in the code directory"
		print minDFA.getDotFile()

if __name__  ==  '__main__':
	t = time.time()
	try:
		main()
	except BaseException as e:
		print "\nFailure:", e
	print "\nExecution time: ", time.time() - t, "seconds"
