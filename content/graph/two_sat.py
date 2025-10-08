"""
Implements a solver for 2-Satisfiability (2-SAT) problems.
A 2-SAT problem consists of a boolean formula in 2-Conjunctive Normal Form,
which is a conjunction (AND) of clauses, where each clause is a disjunction (OR)
of two literals. The goal is to find a satisfying assignment of true/false values
to the variables.
This problem can be solved in linear time by reducing it to a graph problem.
The reduction works as follows:
1.  Create an "implication graph" with `2N` vertices for `N` variables. For each
    variable `x_i`, there are two vertices: one for `x_i` and one for its
    negation `¬x_i`.
2.  Each clause `(a OR b)` is equivalent to two implications: `(¬a => b)` and
    `(¬b => a)`. For each clause, add two directed edges to the graph
    representing these implications.
3.  The original 2-SAT formula is unsatisfiable if and only if there exists a
    variable `x_i` such that `x_i` and `¬x_i` are in the same Strongly Connected
    Component (SCC) of the implication graph. This is because if they are in the
    same SCC, it means `x_i` implies `¬x_i` and `¬x_i` implies `x_i`, which is a
    contradiction.
4.  If the formula is satisfiable, a valid assignment can be constructed from the
    SCCs. The SCCs form a Directed Acyclic Graph (DAG). We can find a reverse
    topological ordering of this "condensation graph". For each variable `x_i`,
    if the SCC containing `¬x_i` appears before the SCC containing `x_i` in this
    ordering, we must assign `x_i` to true. Otherwise, we assign it to false.
This implementation uses the `find_sccs` function (Tarjan's algorithm) to solve
the problem.
number of clauses. The graph has $2N$ vertices and $2M$ edges.
"""

import sys
import os

# The stress test runner adds the project root to the path.
# This allows importing other content modules using their full path.
from content.graph.scc import find_sccs


class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2 * n)]

    def _map_var(self, var):
        """Maps a 1-indexed variable to a 0-indexed graph node."""
        if var > 0:
            return var - 1
        return -var - 1 + self.n

    def add_clause(self, i, j):
        """
        Adds a clause (i OR j) to the formula.
        Variables are 1-indexed. A negative value -k denotes the negation of x_k.
        This adds two implications: (-i => j) and (-j => i).
        """
        # Add edge for (-i => j)
        self.graph[self._map_var(-i)].append(self._map_var(j))
        # Add edge for (-j => i)
        self.graph[self._map_var(-j)].append(self._map_var(i))

    def solve(self):
        """
        Solves the 2-SAT problem.

        Returns:
            tuple[bool, list[bool] | None]: A tuple where the first element is
            True if a solution exists, False otherwise. If a solution exists,
            the second element is a list of boolean values representing a
            satisfying assignment. Otherwise, it is None.
        """
        sccs = find_sccs(self.graph, 2 * self.n)
        component_id = [-1] * (2 * self.n)
        for idx, comp in enumerate(sccs):
            for node in comp:
                component_id[node] = idx

        for i in range(self.n):
            if component_id[i] == component_id[i + self.n]:
                return False, None

        assignment = [False] * self.n
        # sccs are returned in reverse topological order
        for i in range(self.n):
            # If component of x_i comes after component of not(x_i) in topo order
            # (i.e., has a smaller index in the reversed list), then x_i must be true.
            if component_id[i] < component_id[i + self.n]:
                assignment[i] = True

        return True, assignment
