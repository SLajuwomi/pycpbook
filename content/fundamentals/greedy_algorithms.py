"""
This guide explains the greedy problem-solving paradigm, a technique
for solving optimization problems by making the locally optimal choice at each
stage with the hope of finding a global optimum. For a greedy algorithm to work,
the problem must exhibit two key properties:
1.  Greedy Choice Property: A globally optimal solution can be arrived at by
    making a locally optimal choice. In other words, the choice made at the
    current step, without regard for future choices, can lead to a global solution.
2.  Optimal Substructure: An optimal solution to the problem contains within it
    optimal solutions to subproblems.
The example below, the Activity Selection Problem, is a classic illustration
of the greedy method. Given a set of activities each with a start and finish
time, the goal is to select the maximum number of non-overlapping activities
that can be performed by a single person.
The greedy choice is to always select the next activity that finishes earliest
among those that do not conflict with the last-chosen activity. This choice
maximizes the remaining time for other activities.
"""


def activity_selection(activities):
    """
    Selects the maximum number of non-overlapping activities.

    Args:
        activities (list[tuple[int, int]]): A list of activities, where each
            activity is a tuple (start_time, finish_time).

    Returns:
        int: The maximum number of non-overlapping activities.
    """
    if not activities:
        return 0

    # Sort activities by their finish times in ascending order
    activities.sort(key=lambda x: x[1])

    count = 1
    last_finish_time = activities[0][1]

    for i in range(1, len(activities)):
        start_time, finish_time = activities[i]
        if start_time >= last_finish_time:
            count += 1
            last_finish_time = finish_time

    return count
