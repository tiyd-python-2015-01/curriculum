#!/usr/bin/env roundup

describe "square_root.py: returns the approximate square root of a positive number"

sqr="python square_root.py"

it_works_for_known_values() {
  out="$(echo 4 | $sqr)"

  [[ "$out" =~ "2.0" ]]
}

it_works_for_more_difficult_values() {
  out="$(echo 20 | $sqr)"

  [[ "$out" =~ "4.47213" ]]
}
