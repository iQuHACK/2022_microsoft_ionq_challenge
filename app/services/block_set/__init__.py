import config

import matplotlib.pylab as pl
import ast
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import services.quantum_random.randint as randint
import services.block.OperatorBlock as OperatorBlock

class BlockSet:
    def __init__(self, random = True):
        if random:
            self.setup = config.possible_setups[randint(0, len(config.possible_setups) - 1)]
            self.operators = [OperatorBlock() for i in range(4)]

    def draw_block_set(self):
        setup_str = str(self.setup)
        for i in range(4):
            setup_str = setup_str.replace(str(i + 1), self.operators[i].label)
        nx = ny = 4
        data = ast.literal_eval(setup_str)
        pl.figure()
        tb = pl.table(cellText=data, loc=(0,0), cellLoc='center')
        tc = tb.properties()['children']
        for cell in tc: 
            cell.set_height(1/ny)
            cell.set_width(1/nx)

        ax = pl.gca()
        ax.set_xticks([])
        ax.set_yticks([])
