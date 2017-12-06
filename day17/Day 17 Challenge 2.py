import itertools
import sys

boxes = map(int, open("input.txt").read().split())

variants = []
found = []
total = 150

for size in range(1, len(boxes) + 1, 1):
    variants.extend(itertools.combinations(boxes, size))

for variant in variants:
    if sum(variant) == total:
        found.append(variant)

smallest = sys.maxint
for correct in found:
    length = len(correct)
    if length < smallest:
        smallest = length

print smallest
number_of_smallest = 0
for correct in found:
    if len(correct) == smallest:
        number_of_smallest += 1
print number_of_smallest
