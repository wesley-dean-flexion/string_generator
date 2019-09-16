# string\_generator

This is a string generator suitable for generating passwords that meet configurable criteria.

## What (is this)?

This is a portable, configurable string generating tool.




## How (do I use this)?

```
usage: string_generator.py [-h] 
                           [--min_letters MIN_LETTERS]
                           [--max_letters MAX_LETTERS]
                           [--min_lowers MIN_LOWERS] 
                           [--max_lowers MAX_LOWERS]
                           [--min_uppers MIN_UPPERS] 
                           [--max_uppers MAX_UPPERS]
                           [--min_numbers MIN_NUMBERS]
                           [--max_numbers MAX_NUMBERS]
                           [--min_symbols MIN_SYMBOLS]
                           [--max_symbols MAX_SYMBOLS]
                           [--min_characters MIN_CHARACTERS]
                           [--max_characters MAX_CHARACTERS] 
                           [--friendly]

This tool is used to generate random strings such as those used as passwords.
A number of parameters are accepted that can be used to specify minimum and
maximum numbers of uppercase letters, lowercase letters, numbers, symbols
(punctuation), and characters (i.e., string length).To generate a string, the
minimums for each character type are put together along with enough random
characters to put the total length between the minimum and maximum lengths.
The string is then shuffled. If the string passes all of the tests for minimum
and maximum counts, the string is written to STDOUT. If the it doesn't, then a
new random string is generated. If the tool is not able to generate an
acceptable string after 100 tries, then the tool aborts and returns an result
code of 1 with no string returned, the assumption being that the parameters
provided are somehow in conflict (e.g., minimum letters = 4 and maximum length
= 3).

optional arguments:
  -h, --help            show this help message and exit
  --min_letters MIN_LETTERS, -a MIN_LETTERS
                        minimum number of required total letters
  --max_letters MAX_LETTERS, -A MAX_LETTERS
                        maximum number of required total letters
  --min_lowers MIN_LOWERS, -l MIN_LOWERS
                        minimum number of required lowercase letters
  --max_lowers MAX_LOWERS, -L MAX_LOWERS
                        maximum number of required lowercase letters
  --min_uppers MIN_UPPERS, -u MIN_UPPERS
                        minimum number of required uppercase letters
  --max_uppers MAX_UPPERS, -U MAX_UPPERS
                        maximum number of required uppercase letters
  --min_numbers MIN_NUMBERS, -n MIN_NUMBERS
                        minimum number of required numbers
  --max_numbers MAX_NUMBERS, -N MAX_NUMBERS
                        maximum number of required numbers
  --min_symbols MIN_SYMBOLS, -s MIN_SYMBOLS
                        minimum number of required symbols
  --max_symbols MAX_SYMBOLS, -S MAX_SYMBOLS
                        maximum number of required symbols
  --min_characters MIN_CHARACTERS, -c MIN_CHARACTERS
                        minimum number of characters (length)
  --max_characters MAX_CHARACTERS, -C MAX_CHARACTERS
                        maximum number of characters (length)
  --friendly, -f        make sure string is human-friendly (no ambiguous
                        characters)
```

### Examples

Generate a string with the default options
```
$ ./string_generator.py
```

Generate a string that's exactly 40 characters long
```
$ ./string_generator.py -c 40 -C 40
```

Generate a string with 8 - 12 characters long with at least 2 uppercase, 
2 lowercase, 2 digits, and 2 symbols
```
$ ./string_generator.py -c 8 -C 12 -u 2 -l 2 -n 2 -s 2
```

## Why (did you make this)?

I needed a portable string generator that could be easily configured.  There 
were a billion and one password generators but many seemed to be limited
in their ability to configure constraints on how many of each character
type could be / needed to be included.  For example, some passwords require
"at least 12 characters, 2 of which must be uppercase letters, 2 of which
must be numbers, and 1 of which must be a symbol" and, well, I didn't come
across a great number of tools that could do this, especially in a way that
was sufficiently portable.

Originally, this tool was a part of a larger project that involved generating
strings for a variety of tools, each of which had different critera.  
Moreover, the execution environment was only minimally assured; therefore,
this tool was written to use only modules from the Python Standard Library.

Also, the tool needed to use cryptographically strong procedures to generate
random charaters.  To do this, we use random.SystemRandom to generate
numbers which map then to characters.  As a result, this may limit some
systems in their ability to use this tool.  This was a known, accepted
tradeoff.

Finally, in cases where the end-user wants to generate a string that will
be written down, glyphs that are ambiugious (e.g., the number 1, an
uppercase I, and a lowercase l) -- unfriendly characters -- can be avoided.


