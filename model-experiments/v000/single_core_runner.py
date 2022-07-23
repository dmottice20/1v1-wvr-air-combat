from audioop import mul
from memory_profiler import memory_usage
import time
import multiprocessing
"""
Script to run a test on a single core.
"""

def test(a, n_states):
    time.sleep(2)
    b = [a] * n_states
    time.sleep(1)
    return b


def runv0():
    mem = memory_usage((test, (1,), {'n_states': int(1e6)}))
    return mem
