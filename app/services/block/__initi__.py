from qiskit.quantum_info.operators import Operator
from qiskit.quantum_info import process_fidelity
import numpy as np

import config

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import services.quantum_random.randint as randint

class OperatorBlock:
    def __init__(self, random = True, operator_param = None):
        if random:
            rand_operator = config.possible_operators[randint(0, len(config.possible_operators) - 1)]
            self.label = rand_operator.get('name')
            self.operator = Operator(rand_operator.get('obj'))
        else:
            list_match_operator = list(filter(lambda op: process_fidelity(Operator(op.get('obj')), Operator(operator_param)) > 0.99999, config.possible_operators))
            if len(list_match_operator):
                self.label = list_match_operator[0].get('name')
            self.operator = operator_param
        
    
    def compose(self, composing_operator):
        return self.operator.compose(composing_operator.operator)
    
    def is_identity(self):
        return process_fidelity(self.operator, Operator(np.eye(2))) > 0.99999
