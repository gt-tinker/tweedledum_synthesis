import random
from typing import List, Tuple

AbstractGate = Tuple[int, int]
GateList = List[AbstractGate]


def update_permutation(perm: List[int], controls: int, targets: int) -> None:
    ## updates the permutation according to a Toffoli gate with given control and target bitmasks.

    for i in range(len(perm)):
        if(perm[i] & controls) == controls:
            perm[i] ^= targets
        

def unidirectional(perm: List[GateList]) -> GateList:

    ## implements the "Transformation based synthesis" algorithm:
    ##          Given an n-variable reversible function f, this 
    ##          algorithm computes a reversible circuit C that realizes f by
    ##          transforming output patterns in numerical order of their corresponding
    ##          input patterns.
    ## (Given a reversible permutation, return the gate list to convert to the identity)

    gates: GateList = []

    for i in range(len(perm)):

        ## skip lines already the identity
        if perm[i] == i:
            continue

        y = perm[i]

        ## step 1: compute the bitmask p, where p is the bits that are set in i but not in y
        p = i & ~y
        if p:
            update_permutation(perm, y, p)
            gates.append((y, p))
        
        ## step 2: compue the bitmask q, where q is the bits that are set in y but not in i
        q = ~i & y
        if q:
            update_permutation(perm, i, q)
            gates.append((i, q))


    ## reverse the gate order and return
    gates.reverse()
    return gates

if __name__ == "__main__":
    n = 3
    perm = list(range(2**n))
    random.shuffle(perm)

    print("Original perm:", perm)

    gates = unidirectional(perm)

    print("Gates (target, control_mask):")
    for target, control in gates:
        print(f"Toffoli(target={target}, control_mask={bin(control)})")

    print("Final perm (should be identity):", perm)






