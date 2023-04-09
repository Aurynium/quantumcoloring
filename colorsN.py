#!/usr/bin/python

# number of bits for colour count. i.e. number of colors = 2**n
n = 2 # color bits

# read and parse the graph file. same adjacency dictionary format
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
graph = {k: vs.split() for l in open(graph_file, 'rt').readlines() for (k, vs) in [l.strip().split(None, 1)]}

# trivially satisfiable expression, just forces the ordering in the result qubit measurements
# TODO: don't do this, it is stupid. find a better way to determine variable->index map
expression_orderer = ' | '.join([
	f'{v}{i+1}' for v in graph.keys() for i in range(0,n)
])

# actual heap of the work
expression_logic   = ' & '.join([
	'(' + ' | '.join([
		f'({k}{i+1} ^ {v}{i+1})' for i in range(0,n)
	]) + ')' for k, vs in graph.items() for v in vs
])

# join the expressions. ensure the orderer comes first.
expression = f'({expression_orderer}) & {expression_logic}'

print(graph); print(expression)

# import preamble for qiskit
from qiskit.algorithms import Grover, AmplificationProblem
from qiskit.circuit.library.phase_oracle import PhaseOracle
from qiskit.exceptions import MissingOptionalLibraryError
from qiskit.primitives import Sampler

# create actual quantum stuff
oracle = PhaseOracle(expression)
print('oracle generated:', oracle)

problem = AmplificationProblem(oracle, is_good_state=oracle.evaluate_bitstring)
print('problem generated:', problem)

grover = Grover(sampler=Sampler())
print('grover sampler created:', grover)

results = grover.amplify(problem)

# qiskit uses RTL for indexing (...3, 2, 1, 0)
result = results.top_measurement[::-1].zfill(2 ** n)
print(result)

# explain result
colors = {
	'00': 'black',
	'01': 'white',
	'10': 'red',
	'11': 'blue',
}
for i, v in enumerate(list(graph.keys())):
	v_result = result[i * (2**(n-1)) : i * (2**(n-1)) + (2**(n-1))]
	print(v, v_result, colors[v_result])
