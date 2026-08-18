def lowestCommonFactor(numbers: list[int]) -> int | None:
    """Returns the least common factor of the given numbers, excluding 1."""
    if not numbers:
        raise ValueError("numbers cannot be empty")
    smallest = min(abs(n) for n in numbers)
    for factor in range(2, smallest + 1):
        if all(n % factor == 0 for n in numbers):
            return factor
    return None

def highestCommonMultiple(numbers: list[int], limit: int) -> int | None:
    """Returns the highest common multiple of the given numbers within the limit."""
    if not numbers:
        raise ValueError("numbers cannot be empty")

    if limit < 1:
        raise ValueError("limit must be positive")

    for multiple in range(limit, 0, -1):
        if all(multiple % n == 0 for n in numbers):
            return multiple
    return None

def numGoBrr(number: int, times: int):
    """Prints the number repeatedly while squaring it each time."""
    if not number or not times:
        raise ValueError("number and times must be non-zero")
    numList = []
    for _ in range(times):
        print(number)
        numList.append(number)
        number *= number
    return numList
