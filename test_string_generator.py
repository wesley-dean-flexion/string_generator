#!/usr/bin/env python

## @file test_string_generator.py
#  @author Wes Dean <wdean@flexion.us>
#  @brief perform unit tests on string_generator.py


import pytest
from string_generator import *

def test_is_unfriendly1():
  assert is_unfriendly('U') == False

def test_is_unfriendly2():
  assert is_unfriendly('1') == True

def test_is_unfriendly3():
  assert is_unfriendly('o') == True

def test_is_unfriendly4():
  assert is_unfriendly('') == False


def test_is_letter1():
  assert is_letter('A') == True

def test_is_letter2():
  assert is_letter('a') == True

def test_is_letter3():
  assert is_letter('1') == False

def test_is_letter4():
  assert is_letter('$') == False

def test_is_letter5():
  assert is_letter('') == False


def test_is_lower1():
  assert is_lower('A') == False

def test_is_lower2():
  assert is_lower('a') == True

def test_is_lower3():
  assert is_lower('1') == False

def test_is_lower4():
  assert is_lower('$') == False

def test_is_lower5():
  assert is_lower('') == False


def test_is_upper1():
  assert is_upper('A') == True

def test_is_upper2():
  assert is_upper('a') == False

def test_is_upper3():
  assert is_upper('1') == False

def test_is_upper4():
  assert is_upper('$') == False

def test_is_upper5():
  assert is_upper('') == False


def test_is_number1():
  assert is_number('A') == False

def test_is_number2():
  assert is_number('a') == False

def test_is_number3():
  assert is_number('1') == True

def test_is_number4():
  assert is_number('$') == False

def test_is_number5():
  assert is_number('') == False


def test_is_symbol1():
  assert is_symbol('A') == False

def test_is_symbol2():
  assert is_symbol('a') == False

def test_is_symbol3():
  assert is_symbol('1') == False

def test_is_symbol4():
  assert is_symbol('$') == True

def test_is_symbol5():
  assert is_symbol('') == False


def test_is_character1():
  assert is_character('A') == True

def test_is_character2():
  assert is_character('a') == True

def test_is_character3():
  assert is_character('1') == True

def test_is_character4():
  assert is_character('$') == True

def test_is_character5():
  assert is_character('') == False


def test_count1():
  assert count('A', 'letters') == 1

def test_count2():
  assert count('a', 'letters') == 1

def test_count3():
  assert count('1', 'letters') == 0

def test_count4():
  assert count('$', 'letters') == 0

def test_count5():
  assert count('', 'letters') == 0

def test_count6():
  assert count('A', 'numbers') == 0

def test_count7():
  assert count('a', 'numbers') == 0

def test_count8():
  assert count('1', 'numbers') == 1

def test_count9():
  assert count('$', 'numbers') == 0

def test_count10():
  assert count('', 'numbers') == 0

def test_count11():
  assert count('Test', 'numbers') == 0

def test_count12():
  assert count('Test', 'letters') == 4

def test_count13():
  assert count('Test', 'length') == 4

def test_count14():
  assert count('Test 1', 'numbers') == 1

def test_count15():
  assert count('Test 1', 'letters') == 4

def test_count16():
  assert count('Test 1', 'length') == 6

def test_count17():
  assert count('Test 1 Test!', 'numbers') == 1

def test_count18():
  assert count('Test 1 Test!', 'letters') == 8

def test_count19():
  assert count('Test 1 Test!', 'length') == 12


def test_is_acceptable1():
  assert is_acceptable('ThisIsTest#1',
  min_letters=4,
  min_uppers=2,
  min_lowers=2,
  min_numbers=1,
  min_symbols=1,
  min_length=8
  ) == True

def test_is_acceptable2():
  assert is_acceptable('ThisIsTest#2',
  min_letters=4,
  min_uppers=0,
  min_lowers=0,
  min_numbers=0,
  min_symbols=0,
  min_length=0
  ) == True

def test_is_acceptable3():
  assert is_acceptable('ThisIsTest#3',
  min_letters=4,
  min_uppers=3,
  min_lowers=2,
  min_numbers=1,
  min_symbols=1,
  min_length=8
  ) == True

def test_is_acceptable4():
  assert is_acceptable('ThisIsTest#4',
  max_letters=4,
  max_uppers=2,
  max_lowers=2,
  max_numbers=1,
  max_symbols=1,
  max_length=18
  ) == False

def test_is_acceptable5():
  assert is_acceptable('ThisIsTest#5',
  max_letters=4,
  min_uppers=3,
  min_lowers=2,
  min_numbers=1,
  min_symbols=1,
  min_length=8
  ) == False

def test_is_acceptable6():
  assert is_acceptable('ThisIsTest#6',
  min_letters=4,
  max_uppers=3,
  min_lowers=2,
  min_numbers=1,
  min_symbols=1,
  min_length=8
  ) == True

def test_is_acceptable7():
  assert is_acceptable('ThisIsTest#7',
  min_letters=4,
  min_uppers=3,
  max_lowers=2,
  min_numbers=1,
  min_symbols=1,
  min_length=8
  ) == False

def test_is_acceptable8():
  assert is_acceptable('ThisIsTest#8',
  min_letters=4,
  min_uppers=3,
  min_lowers=2,
  max_numbers=0,
  min_symbols=1,
  min_length=8
  ) == False

def test_is_acceptable9():
  assert is_acceptable('ThisIsTest#9',
  max_letters=4,
  min_uppers=3,
  min_lowers=2,
  min_numbers=1,
  min_symbols=1,
  min_length=8,
  max_unfriendly=0
  ) == False


def test_generate_string1():
  assert generate_string() == ''

def test_generate_string2():
  assert generate_string(min_length=1) != ''


def test_generate_acceptable_string1():
  assert generate_acceptable_string() == ''

def test_generate_acceptable_string2():
  assert generate_acceptable_string(min_length=1) != ''

def test_generate_acceptable_string3():
  s = generate_acceptable_string(min_length=1)
  assert is_acceptable(s, min_length=1)
  assert len(s) >= 1

def test_generate_acceptable_string4():
  s = generate_acceptable_string(min_length=8)
  assert is_acceptable(s, min_length=8)
  assert len(s) >= 8

def test_generate_acceptable_string5():
  s = generate_acceptable_string(min_length=8, min_numbers=1)
  assert is_acceptable(s, min_length=8, min_numbers=1)
  assert len(s) >= 8

def test_generate_acceptable_string6():
  s = generate_acceptable_string(min_length=8, min_numbers=1, max_numbers=2)
  assert is_acceptable(s, min_length=8, min_numbers=1, max_numbers=2)
  assert len(s) >= 8

def test_generate_acceptable_string7():
  s = generate_acceptable_string(min_length=8, max_unfriendly=0)
  assert is_acceptable(s, min_length=8, max_unfriendly=0)
  assert len(s) >= 8


def test_shuffle_string1():
  o = 'This is a test'
  n = shuffle_string(o)
  assert shuffle_string(n) != o

def test_shuffle_string2():
  o = 'This is a test'
  n = shuffle_string(o)

  assert len(n) == len(o)

def test_shuffle_string3():
  o = 'This is a test'
  n = shuffle_string(o)

  assert count(n, 'numbers') == count(o, 'numbers')

def test_shuffle_string4():
  o = 'This is a test'
  n = shuffle_string(o)

  assert count(n, 'letters') == count(o, 'letters')

def test_shuffle_string5():
  o = 'This is a test'
  n = shuffle_string(o)

  assert count(n, 'symbols') == count(o, 'symbols')

def test_shuffle_string6():
  o = 'This is a test'
  n = shuffle_string(o)

  assert count(n, 'length') == count(o, 'length')


def test_system_random_range1():
  n = 0
  x = 1
  v = system_random_range(min = n, max = x)
  assert v >= n

def test_system_random_range2():
  n = 0
  x = 1
  v = system_random_range(min = n, max = x)

  assert v <= x

def test_system_random_range3():
  n = 1
  x = 6
  v = system_random_range(min = n, max = x)
  assert v >= n

def test_system_random_range4():
  n = 1
  x = 6
  v = system_random_range(min = n, max = x)

  assert v <= x

def test_system_random_range5():
  n = 100
  x = 1000
  v = system_random_range(min = n, max = x)

  assert v >= n

def test_system_random_range6():
  n = 100
  x = 1000
  v = system_random_range(min = n, max = x)

  assert v >= n

def test_system_random_range6():
  n = 100
  x = 1000
  v = system_random_range(min = n, max = x)

  assert v <= x

def test_system_random_range7():
  n = 0
  x = 0
  v = system_random_range(min = n, max = x)
  \
  assert v >= n


def test_system_random_range8():
  n = 0
  x = 0
  v = system_random_range(min = n, max = x)

  assert v <= x


if __name__ == '__main__':
    pytest.main()
