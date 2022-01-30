from qiskit.quantum_info.operators import Pauli
from qiskit.extensions import RXGate, RYGate, RZGate, HGate, IGate
import numpy as np

possible_operators = [
    {'name': 'X', 'obj': Pauli(label='X'), 'img': './app/static/img/X.gif'},
    {'name': 'Y', 'obj': Pauli(label='Y'), 'img': './app/static/img/Y.gif'},
    {'name': 'Z', 'obj': Pauli(label='Z'), 'img': './app/static/img/Z.gif'},
    {'name': 'Rx', 'obj': RXGate(np.pi/2), 'img': './app/static/img/Rx.gif'},
    {'name': 'Ry', 'obj': RYGate(np.pi/2), 'img': './app/static/img/Ry.gif'},
    {'name': 'Rz', 'obj': RZGate(np.pi/2), 'img': './app/static/img/Rz.gif'},
    {'name': 'H', 'obj': HGate(), 'img': './app/static/img/H.gif'},
    {'name': 'I', 'obj': IGate(), 'img': './app/static/img/I.gif'}
] 