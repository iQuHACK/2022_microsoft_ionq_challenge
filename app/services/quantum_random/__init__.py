import config

import qrng
qrng.set_backend(config.simulator_backend)

def randint(min_val: int, max_val: int)-> int:
    return qrng.get_random_int(min_val,max_val)