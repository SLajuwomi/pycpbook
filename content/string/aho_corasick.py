"""
Implements the Aho-Corasick algorithm for finding all occurrences
of multiple patterns in a text simultaneously. This algorithm combines a trie
(prefix tree) with failure links to achieve linear time complexity with respect
to the sum of the text length and the total length of all patterns.
The algorithm works in two main stages:
1.  Preprocessing (Building the Automaton):
    a. A trie is constructed from the set of all patterns. Each node in the
       trie represents a prefix of one or more patterns.
    b. An `output` list is associated with each node, storing the indices of
       patterns that end at that node.
    c. "Failure links" are computed for each node. The failure link of a node `u`
       points to the longest proper suffix of the string corresponding to `u`
       that is also a prefix of some pattern in the set. These links are
       computed using a Breadth-First Search (BFS) starting from the root.
2.  Searching:
    a. The algorithm processes the text character by character, traversing the
       automaton. It starts at the root.
    b. For each character in the text, it transitions to the next state. If a
       direct child for the character does not exist, it follows failure links
       until a valid transition is found or it returns to the root.
    c. At each state, it collects all matches. This is done by checking the
       `output` of the current node and recursively following failure links to
       find all patterns that end as a suffix of the current prefix.
Searching is $O(N + Z)$, where $N$ is the length of the text and $Z$ is the
total number of matches found.
"""

from collections import deque


class AhoCorasick:
    def __init__(self, patterns):
        self.patterns = patterns
        self.trie = [{"children": {}, "output": [], "fail_link": 0}]
        self._build_trie()
        self._build_failure_links()

    def _build_trie(self):
        for i, pattern in enumerate(self.patterns):
            node_idx = 0
            for char in pattern:
                if char not in self.trie[node_idx]["children"]:
                    self.trie[node_idx]["children"][char] = len(self.trie)
                    self.trie.append({"children": {}, "output": [], "fail_link": 0})
                node_idx = self.trie[node_idx]["children"][char]
            self.trie[node_idx]["output"].append(i)

    def _build_failure_links(self):
        q = deque()
        for char, next_node_idx in self.trie[0]["children"].items():
            q.append(next_node_idx)

        while q:
            curr_node_idx = q.popleft()
            for char, next_node_idx in self.trie[curr_node_idx]["children"].items():
                fail_idx = self.trie[curr_node_idx]["fail_link"]
                while char not in self.trie[fail_idx]["children"] and fail_idx != 0:
                    fail_idx = self.trie[fail_idx]["fail_link"]

                if char in self.trie[fail_idx]["children"]:
                    self.trie[next_node_idx]["fail_link"] = self.trie[fail_idx][
                        "children"
                    ][char]
                else:
                    self.trie[next_node_idx]["fail_link"] = 0

                # Append outputs from the failure link node
                fail_output_idx = self.trie[next_node_idx]["fail_link"]
                self.trie[next_node_idx]["output"].extend(
                    self.trie[fail_output_idx]["output"]
                )
                q.append(next_node_idx)

    def search(self, text):
        """
        Finds all occurrences of the patterns in the given text.

        Args:
            text (str): The text to search within.

        Returns:
            list[tuple[int, int]]: A list of tuples, where each tuple is
            (pattern_index, end_index_in_text). `end_index_in_text` is the
            index where the pattern ends.
        """
        matches = []
        curr_node_idx = 0
        for i, char in enumerate(text):
            while (
                char not in self.trie[curr_node_idx]["children"] and curr_node_idx != 0
            ):
                curr_node_idx = self.trie[curr_node_idx]["fail_link"]

            if char in self.trie[curr_node_idx]["children"]:
                curr_node_idx = self.trie[curr_node_idx]["children"][char]
            else:
                curr_node_idx = 0

            if self.trie[curr_node_idx]["output"]:
                for pattern_idx in self.trie[curr_node_idx]["output"]:
                    matches.append((pattern_idx, i))
        return matches
