# number_words_lib

`number_words_lib` renders integers as English words, including the awkward teens. The supported range is -999999999 through 999999999.

```python
from number_words_lib import int_to_words

print(int_to_words(123))       # "one hundred twenty-three"
print(int_to_words(15))        # "fifteen"
print(int_to_words(-7))        # "negative seven"
print(int_to_words(0))         # "zero"
```

## Why

Writing numbers as words sounds trivial until you hit the irregular teens (eleven, twelve, thirteen, fifteen, eighteen) and the hyphenated compounds (twenty-one). This library exists to handle those irregularities once, correctly, so callers do not reinvent them.

The scope is deliberately small: integers up to 999999999 in short scale (million = 10^6). Long scale and decimals are not supported. This keeps the code short, testable, and dependency-free.

## Edge case

Values outside the range raise `ValueError`. Booleans are rejected with `TypeError` even though `bool` is a subclass of `int`, because passing `True` to a number-to-words function is almost always a bug.

Hyphens join the tens and ones ("twenty-one"), while spaces separate everything else ("one hundred one"). The word "and" is omitted, matching modern American English style.
