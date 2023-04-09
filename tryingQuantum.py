from qiskit import QuantumCircuit, assemble, Aer, transpile
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(4,2)
qc.x(0)
qc.x(1)
qc.barrier()

qc.cx(0,2)
qc.cx(1,2)
qc.ccx(0,1,3)
qc.barrier()


qc.measure(2,0) # extract XOR value
qc.measure(3,1)

sim = Aer.get_backend('aer_simulator')

result = sim.run(qc).result()
counts = result.get_counts(qc)

print(qc)
print(counts)