from Day4 import AdventCoin

coin = AdventCoin()
part1Target = "00000"
part2Target = "000000"
part1Reached = False

while True:
    result = coin.new_hash()
    if not part1Reached and result.startswith(part1Target):
        print "Part 1 Answer : Minimum number is", coin.counter, "hash is", result
        part1Reached = True
    elif result.startswith(part2Target):
        print "Part 2 Answer : Minimum number is", coin.counter, "hash is", result
        break
