"""
--- Day 5: Cafeteria ---

As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32

The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

    Ingredient ID 1 is spoiled because it does not fall into any range.
    Ingredient ID 5 is fresh because it falls into range 3-5.
    Ingredient ID 8 is spoiled.
    Ingredient ID 11 is fresh because it falls into range 10-14.
    Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
    Ingredient ID 32 is spoiled.

So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh? 707

--- Part Two ---

The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18

The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges? 361615643045059
"""
fresh = []
available = []
fresh_file = "day5_data.txt"

def czytanie_pliku(file):
    try:
        with open(file, 'r') as file:
            s = file.read().strip()

    except FileNotFoundError:
        print(
            f"Błąd: Nie znaleziono pliku o nazwie '{fresh_file}'. Upewnij się, że plik jest w tym samym katalogu co skrypt.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

    for line in s.split("\n"):
        if '-' in line:
            min_el, max_el = line.split("-")
            min_el = int(min_el)
            max_el = int(max_el)
            fresh.append([min_el, max_el])
        else:
            available.append(line)

    available.pop(0)
    print("Zawartość:")
    print(fresh)
    print(available)
    return available, fresh

def part_1():
    print(" ")
    print("Part 1")
    suma = 0
    for ingredient in available:
        is_fresh = False
        for min_el, max_el in fresh:
            if int(ingredient) >= min_el and int(ingredient) <= max_el:
                is_fresh = True
        if is_fresh:
            suma += 1
    print(f"Suma: {suma}")

def part_2():
    print(" ")
    print("Part 2")
    fresh.sort()
    last = None
    suma = 0

    for min_el, max_el in fresh:
        if last is None:
            last = [min_el, max_el]
        elif last[1] < min_el:
            suma += last[1] - last[0] + 1
            last = [min_el, max_el]
        else:
            last = (last[0], max(last[1], max_el))
    suma += last[1] - last[0] + 1
    print(f"Suma: {suma}")

def main():
    global available, fresh, fresh_file

    czytanie_pliku(fresh_file)
    part_1()
    part_2()

if __name__ == "__main__":
    main()