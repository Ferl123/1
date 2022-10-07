from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
)

# Programmierung der hi
h = {
}

# Programmierung der Koppler Jij
J = {
    (0,4): -1,  # Beispiel
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
)

dwave.inspector.show(response)
