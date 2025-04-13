# Reversible Logic Synthesis (Python)

This project provides a Python implementation of a unidirectional symbolic transformation-based algorithm for reversible logic synthesis using Toffoli gates.

The goal is to transform a given reversible function (represented as a permutation of inputs to outputs) into the identity function while finding a circuit of Toffoli gates that implements the inverse of the function.


## References

This implementation is directly inspired by the [Tweedledum](https://github.com/epiqc/tweedledum) C++ library for quantum circuit compilation and reversible logic synthesis.

Specifically, it replicates the unidirectional transformation-based algorithm described in the paper:

> **"A Fast Symbolic Transformation Based Algorithm for Reversible Logic Synthesis"**  
> Reversible Computation 2016
> Simon Devitt & Ivan Lanese (Eds.)  
> 8th International Conference, RC 2016
> Bologna, Italy, July 7–8, 2016  
---

## Algorithm Overview

Given a reversible function `f` as a permutation of `n`-bit integers, the algorithm:

1. Iterates over each input pattern `i`
2. If `f(i) ≠ i`, determines the bits to flip to make `f(i)` equal `i`
3. Applies a sequence of Toffoli gates to update the permutation toward the identity
4. Collects the gate sequence in reverse order to form the final circuit

Each Toffoli gate is defined by:
- a **target bit index** to toggle
- a **control mask** which determines when the gate fires
