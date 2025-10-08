"""
Predicate-style checks commonly used in competitive programming, with
efficient helpers and concise examples. Includes primality testing optimized for
contest ranges with a fallback to Miller-Rabin for larger values, configurable
palindrome checking for strings and integers, and a curated set of Python built-ins
that are useful for quick validations and transformations. Demonstrates Unicode
nuances between `str.isdigit`, `str.isdecimal`, and `str.isnumeric`.
fallback is $O(k \\cdot (\\log n)^2)$
"""

from content.math.miller_rabin import is_prime as mr_is_prime


def is_prime(n):
    if n < 2:
        return False
    small_primes = [2, 3, 5]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    if n < 10 ** 9:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    return mr_is_prime(n)


def is_palindrome(s, normalize=False, alnum_only=False):
    if not isinstance(s, str):
        s = str(s)
    t = s
    if normalize:
        t = t.casefold()
    if alnum_only:
        t = "".join(ch for ch in t if ch.isalnum())
    return t == t[::-1]


def is_checks_examples():
    prime_small_true = is_prime(97)
    prime_small_false = is_prime(221)
    prime_large_probable = is_prime(1000000007)

    pal_simple_true = is_palindrome("racecar")
    pal_simple_false = is_palindrome("python")
    pal_casefold_true = is_palindrome("AbBa", normalize=True)
    pal_alnum_true = is_palindrome("A man, a plan, a canal: Panama!", normalize=True, alnum_only=True)
    pal_int_true = is_palindrome(12321)

    ch_digit = "2"
    ch_superscript_two = "²"
    ch_roman_twelve = "Ⅻ"
    ch_arabic_indic_two = "٢"

    digits_info = {
        "digit_isdigit": ch_digit.isdigit(),
        "digit_isdecimal": ch_digit.isdecimal(),
        "digit_isnumeric": ch_digit.isnumeric(),
        "sup2_isdigit": ch_superscript_two.isdigit(),
        "sup2_isdecimal": ch_superscript_two.isdecimal(),
        "sup2_isnumeric": ch_superscript_two.isnumeric(),
        "roman_isdigit": ch_roman_twelve.isdigit(),
        "roman_isdecimal": ch_roman_twelve.isdecimal(),
        "roman_isnumeric": ch_roman_twelve.isnumeric(),
        "arabic_isdigit": ch_arabic_indic_two.isdigit(),
        "arabic_isdecimal": ch_arabic_indic_two.isdecimal(),
        "arabic_isnumeric": ch_arabic_indic_two.isnumeric(),
    }

    str_flags = {
        "alpha": "abcXYZ".isalpha(),
        "alnum": "abc123".isalnum(),
        "lower": "hello".islower(),
        "upper": "WORLD".isupper(),
        "space": " \t\n".isspace(),
        "ascii_true": "ASCII".isascii(),
        "ascii_false": "π".isascii(),
    }

    agg_logic = {
        "any_true": any([0, 0, 3]),
        "all_true": all([1, 2, 3]),
        "sum_": sum([1, 2, 3, 4]),
        "min_": min([5, 2, 9]),
        "max_": max([5, 2, 9]),
    }

    conv_num = {
        "abs_": abs(-42),
        "round_": round(3.6),
        "divmod_": divmod(17, 5),
        "pow_mod": pow(2, 10, 1000),
        "ord_A": ord("A"),
        "chr_65": chr(65),
        "bin_": bin(10),
        "oct_": oct(10),
        "hex_": hex(255),
    }

    sorting_iter = {
        "sorted_key": sorted([("a", 3), ("b", 1), ("c", 2)], key=lambda x: x[1]),
        "reversed_list": list(reversed([1, 2, 3])),
        "enumerate_list": list(enumerate(["x", "y"], start=1)),
        "zip_list": list(zip([1, 2, 3], ["a", "b", "c"])),
    }

    return {
        "prime_small_true": prime_small_true,
        "prime_small_false": prime_small_false,
        "prime_large_probable": prime_large_probable,
        "pal_simple_true": pal_simple_true,
        "pal_simple_false": pal_simple_false,
        "pal_casefold_true": pal_casefold_true,
        "pal_alnum_true": pal_alnum_true,
        "pal_int_true": pal_int_true,
        "digits_info": digits_info,
        "str_flags": str_flags,
        "agg_logic": agg_logic,
        "conv_num": conv_num,
        "sorting_iter": sorting_iter,
    }


