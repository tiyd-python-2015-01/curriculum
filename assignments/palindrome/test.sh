#!/usr/bin/env roundup

describe "palindrome.py: Determines if a text is palindromic"

prog="python palindrome.py"

it_works_for_even_numbers() {
  out="$(echo 'toot' | $prog)"
  [[ "$out" =~ "is a palindrome" ]]
}

it_works_for_odd_numbers() {
  out="$(echo 'tot' | $prog)"
  [[ "$out" =~ "is a palindrome" ]]
}

it_works_for_simple_values() {
  out="$(echo 'stunt nuts' | $prog)"
  [[ "$out" =~ "is a palindrome" ]]
}

it_works_for_complete_sentences() {
  out="$(echo 'Lisa Bonet ate no basil.' | $prog)"
  [[ "$out" =~ "is a palindrome" ]]
}

it_works_for_complex_sentences() {
  out="$(echo 'A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!' | $prog)"
  [[ "$out" =~ "is a palindrome" ]]
}

it_works_for_multiple_sentences() {
  out="$(echo 'Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.' | $prog)"
  [[ "$out" =~ "is a palindrome" ]]
}

it_works_for_non_palindromes() {
  out=$(echo 'i am not a palindrome' | $prog)
  [[ "$out" =~ "is not a palindrome" ]]
}
