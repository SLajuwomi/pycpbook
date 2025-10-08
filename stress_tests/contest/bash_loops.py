import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import content.contest.bash_loops as B


def run_test():
    doc = B.__doc__ or ""
    assert "for f in tests/*.in" in doc
    assert "diff -u" in doc
    assert "xargs -P" in doc
    assert "python3 solve.py" in doc
    print("Bash Loops: All tests passed!")


if __name__ == "__main__":
    run_test()


