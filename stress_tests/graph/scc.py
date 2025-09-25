"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the Strongly Connected Components
(SCC) algorithm. It validates the correctness of the `find_sccs` function by
generating random directed graphs and verifying that the output satisfies the
fundamental properties of SCCs.

The validation process involves two key checks:
1.  Partition Check: It ensures that every vertex in the graph belongs to
    exactly one of the found SCCs. This is verified by checking if the union
    of all components is the set of all vertices and that their sizes sum up
    correctly.
2.  Connectivity Check: It verifies that each component is indeed a maximal
    strongly connected subgraph. The set of nodes in the SCC containing a
    vertex `u` is precisely the intersection of the set of vertices reachable
    from `u` and the set of vertices from which `u` can be reached. The test
    validates this property by:
    a. For each component, picking an arbitrary node `s`.
    b. Finding all nodes reachable from `s` in the original graph.
    c. Finding all nodes that can reach `s` (by finding nodes reachable from
       `s` in the reversed graph).
    d. Asserting that the set of nodes in the component found by the algorithm
       is equal to the intersection of the two sets found in the previous steps.

This rigorous testing ensures the SCC implementation is correct and reliable.
"""

import sys
import os
import random
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.scc import find_sccs
from stress_tests.utilities.graph_gen import generate_graph


def get_reachable_nodes(adj, start_node, n):
    """Helper function to find all nodes reachable from a start node using BFS."""
    if not (0 <= start_node < n):
        return set()
    q = deque([start_node])
    visited = {start_node}
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return visited


def run_test():
    """
    Performs a stress test on the find_sccs implementation.
    """
    ITERATIONS = 200
    MAX_N = 50
    MAX_M_FACTOR = 1.5

    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        max_m = int(n * (n - 1) * MAX_M_FACTOR) if n > 1 else 0
        m = random.randint(0, max_m)

        adj = generate_graph(n, m, directed=True)
        sccs = find_sccs(adj, n)

        # 1. Partition Check
        all_nodes_in_sccs = sorted([node for comp in sccs for node in comp])
        assert all_nodes_in_sccs == list(
            range(n)
        ), f"SCCs do not form a partition of vertices (test {i})!\nGraph (n={n}, m={m}): {adj}\nExpected permutation of {list(range(n))}, Got: {all_nodes_in_sccs}"

        # 2. Connectivity Check
        # Build reversed graph for checking reachability *to* a node
        rev_adj = [[] for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                rev_adj[v].append(u)

        for component in sccs:
            if not component:
                continue

            component_set = set(component)
            start_node = component[0]

            # A node's SCC is the intersection of nodes reachable from it and nodes
            # that can reach it.
            reachable_forward = get_reachable_nodes(adj, start_node, n)
            reachable_backward = get_reachable_nodes(rev_adj, start_node, n)

            scc_from_traversals = reachable_forward.intersection(reachable_backward)

            assert component_set == scc_from_traversals, (
                f"SCC validation failed for component starting with {start_node} (test {i})!\n"
                f"Component found by algorithm: {sorted(list(component_set))}\n"
                f"Component found by traversal: {sorted(list(scc_from_traversals))}\n"
                f"  (Reachable forward: {sorted(list(reachable_forward))})\n"
                f"  (Reachable backward: {sorted(list(reachable_backward))})"
            )

    print("Strongly Connected Components (Tarjan's): All tests passed!")


if __name__ == "__main__":
    run_test()
