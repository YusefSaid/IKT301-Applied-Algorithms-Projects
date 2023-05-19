import DFA
import GenerateStrings
import time

import numpy as np
def main():
    I = GenerateStrings.incidence_matrix()
    strings, labels = GenerateStrings.strings(I)
    a = time.time()
    DFA.BacktrackingApproach(strings, labels, I)
    b = time.time()
    print(f"Time: {b - a}")

if __name__=="__main__":
    main()

