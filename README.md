# Quantum Colouring

![Example of the colouring problem, for part of the USA](images/coloring-map.png "Coloured Map")

The colouring problem is when an arbitrary map, with countries, must be coloured such that
no two countries which border each other are the same colour.

This program takes an arbitrary map, as a graph, represented as an adjacency dictionary.
Then, it creates a boolean system to represent the valid colouring states.
After, a quantum computer calculates the solutions to the boolean system.
In the current case, the number of colours is n=2.

## Files
- `colors2.py` - main script
- `graphs/*.txt` - example input files

## How to use:
Usage:
- `python3 colors2.py <graph file>`

For an arbitrary graph, the format is an adjacency dictionary.

## Sources:
- [Python documentation](https://www.python.org/doc/)
- [Qiskit documentation](https://qiskit.org/)
  - [Grover's Algorithm](https://qiskit.org/textbook/ch-algorithms/grover.html) ([Examples](https://qiskit.org/documentation/stable/0.24/tutorials/algorithms/08_grover_examples.html))
