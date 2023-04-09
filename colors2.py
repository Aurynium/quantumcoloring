# Advanced Quantum Track - Bitcamp
# Team "Half-Dead Cat-astrophy"
# Team members:
# Serena Huang (Red)
# Nikolai Smith (Blue)
# Wilson Smith (Red)
# Matthew Yu (Red)
#
# This program takes an input of N countries with 
# one or more borders with countries in the form of a
# graph. Borders are listed as an adjacency dictionary.
#
# Graphs are given in the `graph.txt` text file.
# Each line consists of a list of countries separated by spaces/tabs.
# The first country is bordered by the rest of the countries in the list.
# The program does not check for invalid graphs, so please don't input one... it'll probably break. :(
#
# The program parses the graph and stores the resulting colouring system as a boolean expression. 
# It is then used to create an oracle which is passed to Grover's algorithm.
#
# The result with highest probability is printed as a binary string. 
# Each bit corresponds to the color of the country. (1=white, 0=black)

# Adjacency list representation of the graph of countries

# Import the graph
import os.path, sys
if len(sys.argv) > 1:
	if os.path.isfile(sys.argv[1]):
		graph_file = sys.argv[1]
	else:
		print(f'"{sys.argv[1]}" is not a file')
		exit(1)
else:
	print(f'Usage: {sys.argv[0]} <graph file>')
	exit(0)

graph = {}
with open(graph_file, 'rt') as f:
    for l in f.readlines():
        ls = l.strip().split(None, 1)
        graph[ls[0]] = ls[1].split()

# Initialize a queue variable q, an empty string variable expr,
# an integer variable counter, and an empty array traversed
q = []
expr = ''
boolOrder = ''
counter = 0
traversed = []

# Add the first key of the graph dictionary to the queue
q.append(list(graph.keys())[0])
# Add negative -1 to denote that the first key is in a grouping of its own
q.append('-1')

# While elements are still present in the queue
while q:

    # Pop the first element from the queue
    m = q.pop(0)

    # If the element was already processed, go back to start of loop
    if(m in traversed):
        continue

    # If the element is -1, then check if all the elements were already processed
    # Either exit the loop or append another -1 to signify the start of the next group
    if(m == '-1'):
        if(len(q) == 0):
            break
        counter += 1
        q.append('-1')
        continue

    # If the group is an odd-numbered group (0-indexed), add a negation symbol to the string
    if(counter & 1):
        expr += '~'
    
    # Add the element and an ampersand to the string
    expr += m
    boolOrder += m
    expr += ' & '

    # Add the element to the traversed list
    traversed.append(m)

    # Add the neighbors of the element to the queue
    for neighbour in graph[m]:
        if neighbour not in traversed and neighbour not in q:
            q.append(neighbour)

# Remove the three excess characters from the string, and initialize
# the string expression to the substring
expression = expr[0:len(expr)-3]

# Print the boolean expression (debugging)
print(expression)

# We will use the Qiskit library's implementation for Grover's algorithm, where we supply the oracle.
from qiskit.algorithms import Grover, AmplificationProblem
from qiskit.exceptions import MissingOptionalLibraryError
from qiskit.circuit.library.phase_oracle import PhaseOracle
from qiskit.primitives import Sampler

# Create the oracle to solve the SAT
oracle = PhaseOracle(expression)

# Build the amplifier for the given oracle
problem = AmplificationProblem(oracle, is_good_state=oracle.evaluate_bitstring)

# Create the Grover's algorithm quantum circuit
grover = Grover(sampler=Sampler())

# Run the Grover circuit
result = grover.amplify(problem)

# Store the measurement with the highest probability into a string
expr = result.top_measurement

# Reverse the string
expr = expr[::-1]

# Print the bit string to the console
print(expr)

# Give each vertex in the graph a color according to the bit string
colors = {
    '0': 'black',
    '1': 'white',
}

# Print vertices with corresponding colors
for i, v in enumerate(list(boolOrder)):
    print(f'{v}: {colors[expr[i]]}')
