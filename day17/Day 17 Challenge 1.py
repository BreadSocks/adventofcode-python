import itertools

boxes = map(int, open("input.txt").read().split())

variants = []
found = []
total = 150

for size in range(1, len(boxes) + 1, 1):
    variants.extend(itertools.combinations(boxes, size))

for variant in variants:
    if sum(variant) == total:
        found.append(variant)
print len(found)
