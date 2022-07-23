from v000.single_core_runner import runv0

"""
The purpose of this script is to compare the three methods for the kinematic update() fx
used in this research.
    - v0.0.0 : 1 state in at a time; set of possible actions for each state; 1 state out at a time; and then loop back over n times.
    - v0.0.1 : n states in at a time; set of possible actions for n states; and n states back out -- pure vectorization in numpy.
    - v0.0.2 : TBD
"""

# 1/ Run the different versions and write the data to a location.
if __name__ == '__main__':
    memv0 = runv0()
    print(memv0)

# 2/ Read the data from that location and plot it to compare which version is best.