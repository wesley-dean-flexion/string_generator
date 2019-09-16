#!/usr/bin/env python

import random
import argparse
import string

## @fn is_unfriendly()
#  @brief returns true if the character is an unfriendly letter
#  @details
#  An "unfriendly letter" is a character that, when printed, looks
#  enough like another character so as to create confusion.  For
#  example, lowercase-L and the number 1 may look similar, especially
#  with a font that doesn't purposefully disambiguate the characters
#  (e.g., with serifs).  So, if the character we get is an "unfriendly
#  letter", we return True; otherwise, the character is "friendly" and
#  can be easily interpreted, regardless of the font.
#  @param String character the character to test
#  @returns Boolean True if the character is an unfriendly letter
#  @par Example
#  @code
#  if is_unfriendly('1'):
#    print "This character is unfriendly -- it may be hard to read"
#  @endcode
def is_unfriendly(character):
  return (character == 'l'
  or character == '1'
  or character == 'i'
  or character == 'I'
  or character == '|'
  or character == '!'
  or character == 'S'
  or character == '$'
  or character == 'O'
  or character == '0'
  or character == 'o')


## @fn is_lower()
#  @brief returns true if the character is a lowercase letter
#  @details
#  This returns True if and only if the character passed to it is
#  a lowercase letter.  If the character is not a letter or is not
#  lowercase, it will return False.
#  @param String character the character to test
#  @returns Boolean True if the character is a lowercase letter
#  @par Example
#  @code
#  if is_lower('A'):
#    print 'We have a serious problem -- A is not a lowercase letter!'
#  @endcode
def is_lower(character):
    return (character.isalpha()) and (character.islower())


## @fn is_upper()
#  @brief returns true if the character is an uppercase letter
#  @details
#  This returns True if and only if the character passed to it is
#  an uppercase letter.  If the character is not a letter or is not
#  uppercase, it will return False.
#  @param String character the character to test
#  @returns Boolean True if the character is an uppercase letter
#  @par Example
#  @code
#  if is_upper('A'):
#    print 'I was a little worried-- A is an uppercase letter!'
#  @endcode
def is_upper(character):
    return (character.isalpha()) and (not character.islower())


## @fn is_number()
#  @brief returns true if the character is a number (0-9)
#  @details
#  This returns True if and only if the character passed to it is
#  a number (digit) 0-9.  Negative signs, periods, commas, etc. if
#  included, will return False.
#  @param String character the character to test
#  @returns Boolean True if the character is a number (a digit 0-9)
#  @par Example
#  @code
#  if is_number('0'):
#    print 'Yes, the string "0" is considered a number'
#  @endcode
def is_number(character):
    return (character.isdigit())


## @fn is_letter()
#  @brief returns true if the character is a letter (case-insensitive)
#  @param String character the character to test
#  @returns Boolean True if the character is a letter
#  @par Example
#  @code
#  if is_letter('A'):
#    print 'Whoo hoo!'
#  @endcode
def is_letter(character):
    return is_lower(character) or is_upper(character)


## @fn is_symbol()
#  @brief returns true if the character is a symbol
#  @details
#  For our case, we test to see if a character is a symbol by testing
#  whether the string is a number or a letter; if so, return False;
#  otherwise (the character is not a number and it's not a letter),
#  return True
#  @param String character the character to test
#  @returns Boolean True if the character is a symbol
#  @par Example
#  @code
#  s = 'A'
#  if (not is_symbol(s)) and (not is_letter(s)) and (not is_number(s)):
#    print "This should never happen.."
#  @endcode
def is_symbol(character):
    return (not is_number(character)
    and not is_letter(character)
    and character != None
    and character != '')


## @fn is_character()
#  @brief returns true if the character is not None
#  @param String character the character to test
#  @returns Boolean False if the character is None; True, otherwise
#  @par Example
#  @code
#  if is_character('A'):
#    print "Thank goodness -- it would be messed up to get this error.."
#  @endcode
def is_character(character):
    return (character != None
    and character != '')


## @fn count()
#  @brief given a string and a test, return the number of matching characters
#  @details
#  We pass a string to test and the name of a test.  The test_name is
#  usually something like 'min_letters', so we strip out and instances
#  of 'min_' or 'max_' to get a test name like 'letters'.  Then we
#  lookup the function to perform the test using the modified test name.
#  For each character in the string, we apply the test and count the
#  number of matches.  This number is returned to the caller.
#  @param String test_string the string to test
#  @param String test_name the name of the test to perform on each character
#  @returns Integer the number of characters in the string that match the test
#  @par Example
#  @code
#  print count ("This is a test", "min_letters") # returns 11
#  print count ("This is another string", "numbers") # returns 0
#  @endcode
def count(test_string, test_name):
    n = 0
    test = test_name.replace('min_', '').replace('max_', '')
    for character in test_string:
        if test in tests:
            if (tests[test](character)):
                n += 1
    return n


## @fn is_acceptable()
#  @brief returns true if a given string passes all of its tests
#  @details
#  When run, we pass along any number of tests with the name of the
#  test being the key and the value being... the value.  If the name
#  of the test starts with 'min_' we fail if the count for that test
#  is less than the value; similarly, if the count for that test is
#  more than the value, we also fail.  If there are no failing tests,
#  we return True.  Any failure returns False.  The 'length' test
#  is interesting in that it counts the number of characters (defined as
#  not None) which is the length of the string.  It seems obvious, but
#  you never know when you'll need to come back to something like this..
#  @param String test_string the string to test
#  @param Dict kwargs a dictionary of test names and their values
#  @returns Boolean False if any test fails; True, otherwise
#  @par Example
#  @code
#  print is_acceptable ("Password", min_length=8, min_numbers=1) # False -- no numbers
#  @endcode
def is_acceptable(test_string, **kwargs):
    if kwargs is not None:
        for test, value in kwargs.iteritems():
            if test.replace ('min_', '').replace ('max_', '') in tests and value != -1:
                if test.startswith('min_'):
                    if (count(test_string, test.replace ('min_', '')) < value):
                        return False
                if test.startswith('max_'):
                    if (count(test_string, test.replace ('max_', '')) > value):
                        return False
    return True


## @fn shuffle_string()
#  @brief shuffles a given string
#  @param String test_string the string to shuffle
#  @returns String the shuffled string
#  @par Example
#  @code
#  scrambled = shuffle_string (unscrambled)
#  @endcode
def shuffle_string(test_string):
    rng = random.SystemRandom()
    l = list(test_string)
    random.shuffle(l, rng.random)
    return ''.join(l)


## @fn system_random_range()
#  @brief like random.randrange(), but with random.SystemRandom()
#  @details
#  This is very supposed to be just like random.randrange() except
#  we use random.SystemRandom() (instead of random.random()) for more
#  crypto-friendly randomization.  Also, we don't use the step parameter
#  that randrange() uses.  Maybe in a future revision...
#  @param Dict kwargs a dictionary of min and max values
#  @returns Integer minimum <= value <= maximum
#  @par Example
#  @code
#  die_roll = system_random_range (min = 1, max = 6)
#  @endcode
def system_random_range (**kwargs):
  rng = random.SystemRandom()
  if kwargs is not None:
    if 'min' in kwargs:
      n = kwargs['min']
    else:
      n = 0

    if 'max' in kwargs:
      x = kwargs['max']
    else:
      x = 1

  if n < x:
    return n + round((x-n) * rng.random())
  else:
    return n


## @fn generate_string
#  @brief given a series of tests, produce a string
#  @details
#  We start with an empty string.  Then, we go through the tests and
#  add the minimum number of passing characters (for that test).  Then,
#  we add a random number of characters to bring the length to be
#  between minimum length <= actual length <= maximum length
#  Finally, we shuffle the string and return it.  NOTE!  The returned
#  string is NOT guaranteed to pass all of the tests -- this is only a
#  starting guess.  The desired process is to use the
#  generate_acceptable_string() function.
#  @param Dict kwargs a dictionary of test names and their values
#  @returns String a generated string
#  @par Example
#  @code
#  possible_password = generate_string ('min_length': 8)
#  @endcode
def generate_string(**kwargs):
    generated_string = ''
    if kwargs is not None:
        for character_class in kwargs.iteritems():
            if character_class in character_classes:
                generated_string += shuffle_string(
                    character_classes[character_class])[0]

        if 'min_length' in kwargs:
          n = kwargs['min_length']
        else:
          n = 0


        if 'max_length' in kwargs:
          x = kwargs['max_length']
        else:
          x = 0

        desired_length = system_random_range(min = n, max = x)

        if desired_length == 0:
            desired_length = n

        while len(generated_string) < desired_length:
          generated_string += shuffle_string(
          character_classes['characters'])[0]

    return shuffle_string(generated_string)


## @fn generate_acceptable_string()
#  @brief generate a string that passes all of the tests
#  @details
#  This is just like generate_string(), but it will perform the tests
#  on each candidate; if the candidate is acceptable, it's returned;
#  if not, it'll try again.  To prevent an infinite loop caused by
#  unpassable tests (e.g., min_letters = 4 and max_length = 3), we
#  break out and return False if too many tests fail.
def generate_acceptable_string(**kwargs):
    remaining_tries = 500

    while remaining_tries > 0:
        generated_string = generate_string(**kwargs)
        if (is_acceptable(generated_string, **kwargs)):
            return generated_string
        remaining_tries -= 1

    return False



#
# function maps
#


tests = {
    'letters': is_letter,
    'numbers': is_number,
    'uppers': is_upper,
    'lowers': is_lower,
    'symbols': is_symbol,
    'length': is_character,
    'unfriendly': is_unfriendly
}

character_classes = {
    'letters': string.ascii_letters,
    'numbers': string.digits,
    'uppers': string.ascii_uppercase,
    'lowers': string.ascii_lowercase,
    'symbols': string.punctuation.replace('"', '').replace("'", ''),
    'characters': string.ascii_letters + string.digits + string.punctuation.replace('"', '').replace("'", '').replace('`', '')
}


#
# main function
#


def main():

  parser = argparse.ArgumentParser(
      description="This tool is used to generate random strings such as "
      "those used as passwords.  A number of parameters are accepted that "
      "can be used to specify minimum and maximum numbers of uppercase "
      "letters, lowercase letters, numbers, symbols (punctuation), and "
      "characters (i.e., string length)."
      ""
      "To generate a string, the minimums for each character type are "
      "put together along with enough random characters to put the total "
      "length between the minimum and maximum lengths.  The string is "
      "then shuffled.  If the string passes all of the tests for minimum "
      "and maximum counts, the string is written to STDOUT.  If the it "
      "doesn't, then a new random string is generated.  If the tool is "
      "not able to generate an acceptable string after 100 tries, then "
      "the tool aborts and returns an result code of 1 with no string "
      "returned, the assumption being that the parameters provided are "
      "somehow in conflict (e.g., minimum letters = 4 and maximum length "
      "= 3)."
  )

  parser.add_argument(
      "--min_letters", "-a",
      help="minimum number of required total letters",
      type=int,
      default=-1
  )

  parser.add_argument(
      "--max_letters", "-A",
      help="maximum number of required total letters",
      type=int,
      default=-1
  )

  parser.add_argument(
      "--min_lowers", "-l",
      help="minimum number of required lowercase letters",
      type=int,
      default=-1
  )

  parser.add_argument(
      "--max_lowers", "-L",
      help="maximum number of required lowercase letters",
      type=int,
      default=-1
  )

  parser.add_argument(
      "--min_uppers", "-u",
      help="minimum number of required uppercase letters",
      type=int,
      default=-1
  )

  parser.add_argument(
      "--max_uppers", "-U",
      help="maximum number of required uppercase letters",
      type=int,
      default=-1
  )

  parser.add_argument(
      "--min_numbers", "-n",
      help="minimum number of required numbers",
      type=int,
      default=-1
  )

  parser.add_argument(
      "--max_numbers", "-N",
      help="maximum number of required numbers",
      type=int,
      default=-1
  )

  parser.add_argument(
      "--min_symbols", "-s",
      help="minimum number of required symbols",
      type=int,
      default=-1
  )

  parser.add_argument(
      "--max_symbols", "-S",
      help="maximum number of required symbols",
      type=int,
      default=-1
  )

  parser.add_argument("--min_characters", "-c",
      help="minimum number of characters (length)",
      type=int,
      default=8
  )

  parser.add_argument("--max_characters", "-C",
      help="maximum number of characters (length)",
      type=int,
      default=16
  )

  parser.add_argument("--friendly", "-f",
      help="make sure string is human-friendly (no ambiguous characters)",
      action="store_true"
  )

  args = parser.parse_args()

  # make sure the minimum values are the smaller of the two and the
  # maximum values are the larger of the two.

  if args.min_letters > args.max_letters:
    args.min_letters, args.max_letters = args.max_letters, args.min_letters

  if args.min_uppers > args.max_uppers:
    args.min_uppers, args.max_uppers = args.max_uppers, args.min_uppers

  if args.min_lowers > args.max_lowers:
    args.min_lowers, args.max_lowers = args.max_lowers, args.min_lowers

  if args.min_numbers > args.max_numbers:
    args.min_numbers, args.max_numbers = args.max_numbers, args.min_numbers

  if args.min_symbols > args.max_symbols:
    args.min_symbols, args.max_symbols = args.max_symbols, args.min_symbols

  if args.min_characters > args.max_characters:
    args.min_characters, args.max_characters = args.max_characters, args.min_characters


  print generate_acceptable_string(
      min_letters=args.min_letters,
      max_letters=args.max_letters,

      min_uppers=args.min_uppers,
      max_uppers=args.max_uppers,

      min_lowers=args.min_lowers,
      max_lowers=args.max_lowers,

      min_numbers=args.min_numbers,
      max_numbers=args.max_numbers,

      min_symbols=args.min_symbols,
      max_symbols=args.max_symbols,

      min_length=args.min_characters,
      max_length=args.max_characters,

      min_unfriendly=0,
      max_unfriendly=0 if args.friendly else args.max_characters
  )

if __name__ == '__main__':
    main()
