"""Render integers as English words.

Only the range -999999999 to 999999999 is supported. Numbers outside that
range raise ValueError. Zero and negative numbers are handled.

Design choice: the scale used is the short scale (million = 10^6), which is
standard in modern American and British English. Long scale is not supported
because supporting both would require an option and the brief asks for one
interpretation.
"""

_ONES = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

_TEENS = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

_TENS = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

_MAGNITUDE_WORDS = ["", "thousand", "million"]

_MAX_ABS = 999999999


def _two_digits(n: int) -> str:
    """Convert a number from 0 to 99 to words."""
    if n < 10:
        return _ONES[n]
    if n < 20:
        return _TEENS[n - 10]
    tens, ones = divmod(n, 10)
    if ones == 0:
        return _TENS[tens]
    return _TENS[tens] + "-" + _ONES[ones]


def _three_digits(n: int) -> str:
    """Convert a number from 0 to 999 to words."""
    hundreds, rest = divmod(n, 100)
    parts = []
    if hundreds > 0:
        parts.append(_ONES[hundreds] + " hundred")
    if rest > 0:
        parts.append(_two_digits(rest))
    return " ".join(parts)


def int_to_words(n: int) -> str:
    """Render an integer as English words.

    Args:
        n: An integer in the range -999999999 to 999999999 inclusive.

    Returns:
        A lowercase English phrase representing the number.

    Raises:
        ValueError: If ``n`` is outside the supported range.
        TypeError: If ``n`` is not an ``int``.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("int_to_words requires an int, got %r" % type(n).__name__)

    if n < -_MAX_ABS or n > _MAX_ABS:
        raise ValueError(
            "int_to_words only supports values up to %d in absolute value" % _MAX_ABS
        )

    if n == 0:
        return "zero"

    negative = n < 0
    value = abs(n)

    chunks = []
    while value > 0:
        value, remainder = divmod(value, 1000)
        chunks.append(remainder)

    parts = []
    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue
        words = _three_digits(chunk)
        magnitude = _MAGNITUDE_WORDS[i]
        if magnitude:
            words = words + " " + magnitude
        parts.append(words)

    parts.reverse()
    result = " ".join(parts)

    if negative:
        result = "negative " + result

    return result
