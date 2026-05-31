# Sum of List

A gentle warm-up for recursion: sum the numbers in a list, but without using `sum()` or a loop.

## Requirements

Write a function `sum_of_list(nums)` that takes a list of numbers and returns their sum.  Your function must use recursion — no `sum()`, no `for`, no `while`.

Think about:
- What's the base case?  (Hint: what's the simplest list you could be passed?)
- What does the recursive case look like?  How do you make the problem smaller on each call?

## Examples

```python
sum_of_list([])           # 0
sum_of_list([5])          # 5
sum_of_list([1, 2, 3])    # 6
sum_of_list([-1, 1, -1])  # -1
```

## Stretch

What if the list contains nested lists?  Write a second function `deep_sum(nums)` that sums all numbers, even those inside nested lists of arbitrary depth.

```python
deep_sum([1, [2, [3, 4]], 5])  # 15
```

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!
