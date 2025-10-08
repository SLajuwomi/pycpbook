"""
@description
Correctness and randomized tests for predicate checks and built-in showcases in
`content/fundamentals/is_checks.py`.
"""

import os
import sys
import random
import string

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.fundamentals.is_checks import is_checks_examples, is_prime, is_palindrome


def trial_is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def random_palindrome(base_chars, length, normalize=False, alnum_only=False):
    half = [random.choice(base_chars) for _ in range(length // 2)]
    mid = [random.choice(base_chars)] if length % 2 else []
    s = "".join(half + mid + list(reversed(half)))
    if normalize:
        s = s.casefold()
    if alnum_only:
        s = "".join(ch for ch in s if ch.isalnum())
    return s


def run_test():
    res = is_checks_examples()

    assert res["prime_small_true"] is True
    assert res["prime_small_false"] is False
    assert res["prime_large_probable"] is True

    assert res["pal_simple_true"] is True
    assert res["pal_simple_false"] is False
    assert res["pal_casefold_true"] is True
    assert res["pal_alnum_true"] is True
    assert res["pal_int_true"] is True

    di = res["digits_info"]
    assert di["digit_isdigit"] and di["digit_isdecimal"] and di["digit_isnumeric"]
    assert di["sup2_isdigit"] and not di["sup2_isdecimal"] and di["sup2_isnumeric"]
    assert not di["roman_isdigit"] and not di["roman_isdecimal"] and di["roman_isnumeric"]
    assert di["arabic_isdigit"] and di["arabic_isdecimal"] and di["arabic_isnumeric"]

    sf = res["str_flags"]
    assert sf["alpha"] and sf["alnum"] and sf["lower"] and sf["upper"] and sf["space"]
    assert sf["ascii_true"] and (not sf["ascii_false"])

    ag = res["agg_logic"]
    assert ag["any_true"] and ag["all_true"]
    assert ag["sum_"] == 10 and ag["min_"] == 2 and ag["max_"] == 9

    cn = res["conv_num"]
    assert cn["abs_"] == 42 and cn["round_"] == 4
    assert cn["divmod_"] == (3, 2) and cn["pow_mod"] == 24
    assert cn["ord_A"] == 65 and cn["chr_65"] == "A"
    assert cn["bin_"] == "0b1010" and cn["oct_"] == "0o12" and cn["hex_"] == "0xff"

    si = res["sorting_iter"]
    assert si["sorted_key"] == [("b", 1), ("c", 2), ("a", 3)]
    assert si["reversed_list"] == [3, 2, 1]
    assert si["enumerate_list"] == [(1, "x"), (2, "y")]
    assert si["zip_list"] == [(1, "a"), (2, "b"), (3, "c")]

    for _ in range(200):
        n = random.randint(0, 10000)
        assert is_prime(n) == trial_is_prime(n)

    base = string.ascii_letters + string.digits + " \t,.:;!" + "ÀáÉéÎîÖöÜüß"
    for _ in range(200):
        L = random.randint(1, 25)
        s = random_palindrome(base, L)
        assert is_palindrome(s)
        s2 = random_palindrome(base, L, normalize=True)
        assert is_palindrome(s2, normalize=True)
        s3 = random_palindrome(base, L, normalize=True, alnum_only=True)
        assert is_palindrome(s3, normalize=True, alnum_only=True)

    print("is_checks: Passed!")


if __name__ == "__main__":
    run_test()


