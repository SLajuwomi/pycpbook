"""
Bash/Zsh loops are useful for running a solution against many inputs quickly.
Below are practical snippets to streamline local testing.

Loop over all input files in a directory:

```bash
for f in tests/*.in; do
  python3 solve.py < "\$f"
done
```

Compare outputs to expected `.out` files:

```bash
for f in tests/*.in; do
  base=\${f%.in}
  python3 solve.py < "\$f" > out.tmp
  diff -u "\$base.out" out.tmp || break
done
```

Run a solution N times (useful for randomized generators):

```bash
for i in \$(seq 1 100); do
  python3 solve.py < input.txt
done
```

Parallelize runs (careful with I/O ordering):

```bash
seq 1 8 | xargs -P 4 -I{} sh -c 'python3 solve.py < input{}.txt > output{}.txt'
```

Zsh specifics and brace expansion:

```bash
for f in **/*.in; do python3 solve.py < "\$f"; done
python3 solve.py < input{1..10}.txt
```

Python snippet for multiple test cases in one file:

```python
import sys
it = iter(sys.stdin.read().strip().split())
t = int(next(it, 0))
for _ in range(t):
    # read one test case from iterator
    pass
```

Notes:
- macOS default shell is zsh; bash is available as well. Quoting paths avoids
  issues with spaces. Use `time` to measure performance.
"""


