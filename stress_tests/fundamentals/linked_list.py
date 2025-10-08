import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from content.fundamentals.linked_list import (
    SinglyLinkedList,
    DoublyLinkedList,
)


def oracle_apply(arr, op, *args):
    if op == "push_front":
        arr.insert(0, args[0])
    elif op == "push_back":
        arr.append(args[0])
    elif op == "pop_front":
        return arr.pop(0) if arr else None
    elif op == "pop_back":
        return arr.pop() if arr else None
    elif op == "insert_after_value":
        v, nv = args
        try:
            idx = arr.index(v)
            arr.insert(idx + 1, nv)
            return True
        except ValueError:
            return False
    elif op == "delete_value":
        v = args[0]
        try:
            arr.remove(v)
            return True
        except ValueError:
            return False
    elif op == "find":
        v = args[0]
        return (v in arr)
    else:
        raise ValueError("unknown op")


def random_sequence_test(ListClass):
    ll = ListClass()
    oracle = []
    for _ in range(3000):
        op = random.choice([
            "push_front", "push_back", "pop_front", "pop_back",
            "insert_after_value", "delete_value", "find"
        ])
        if op in ("push_front", "push_back"):
            v = random.randint(-50, 50)
            getattr(ll, op)(v)
            oracle_apply(oracle, op, v)
        elif op in ("pop_front", "pop_back"):
            r1 = getattr(ll, op)()
            r2 = oracle_apply(oracle, op)
            assert r1 == r2
        elif op == "insert_after_value":
            if oracle:
                v = random.choice(oracle)
            else:
                v = random.randint(-5, 5)
            nv = random.randint(-50, 50)
            r1 = getattr(ll, op)(v, nv)
            r2 = oracle_apply(oracle, op, v, nv)
            assert r1 == r2
        elif op == "delete_value":
            if oracle:
                v = random.choice(oracle)
            else:
                v = random.randint(-5, 5)
            r1 = getattr(ll, op)(v)
            r2 = oracle_apply(oracle, op, v)
            assert r1 == r2
        elif op == "find":
            v = random.randint(-50, 50)
            r1 = ll.find(v) is not None
            r2 = oracle_apply(oracle, op, v)
            assert r1 == r2

        assert ll.to_list() == oracle


def specific_alg_tests():
    ll = SinglyLinkedList.from_list([1, 2, 3, 4, 5])
    ll.reverse()
    assert ll.to_list() == [5, 4, 3, 2, 1]

    ll2 = SinglyLinkedList.from_list([1, 2, 3, 4])
    mid = ll2.middle()
    assert mid and mid.val in (2, 3)

    a = SinglyLinkedList.from_list([1, 2, 3])
    assert a.has_cycle() is False
    if a.tail:
        a.tail.next = a.head
    assert a.has_cycle() is True

    dl = DoublyLinkedList.from_list([10, 20, 30])
    assert dl.delete_value(20) is True
    assert dl.to_list() == [10, 30]
    assert dl.delete_value(10) is True
    assert dl.to_list() == [30]
    assert dl.delete_value(30) is True
    assert dl.to_list() == []


def run_test():
    random.seed(0)
    random_sequence_test(SinglyLinkedList)
    random_sequence_test(DoublyLinkedList)
    specific_alg_tests()
    print("Linked List: All tests passed!")


if __name__ == "__main__":
    run_test()


