from qiskit import QuantumCircuit, Aer, transpile
from qiskit.tools.visualization import plot_histogram

qc = QuantumCircuit(4, 2)

a = int(input("a: "))
b = int(input("b: "))

if(a):
    qc.x(0)
if(b):
    qc.x(1)
qc.cx(0,2)
qc.cx(1,2)
qc.ccx(0,1,3)

qc.measure(2,0)
qc.measure(3,1)

sim = Aer.get_backend('aer_simulator')
qc = transpile(qc, sim)

result = sim.run(qc).result()
counts = result.get_counts(qc)
plot_histogram(counts)

print(counts)
