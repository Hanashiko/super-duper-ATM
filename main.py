def min_banknotes(S):
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = 0

    for denom in denominations:
        while S >= denom:
            S -= denom
            result += 1

    return result
  
S = int(input())
min_notes = min_banknotes(S)
print(f"{min_notes}")
