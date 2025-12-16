"""
--- Day 4: Printing Department ---

You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift? 1537

--- Part Two ---

Now, the Elves just need help accessing as much of the paper as they can.

Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

Initial state:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Remove 13 rolls of paper:
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts? 8707
"""
rolls = []
rolls_file = "day4_data.txt"

def czytanie_pliku(file):
    try:
        with open(file, 'r') as file:
            s = file.read().strip()

    except FileNotFoundError:
        print(
            f"Błąd: Nie znaleziono pliku o nazwie '{rolls_file}'. Upewnij się, że plik jest w tym samym katalogu co skrypt.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
    for line in s.split("\n"):
        lista = []
        for l in line:
            lista.append(l)
        rolls.append(lista)
    print("Zawartość rolls:")
    print(rolls)
    print_rolls()
    return rolls

def print_rolls():
    print(" ")
    for line in rolls:
        print(line)

def part_1():
    print(" ")
    print("Part 1:")
    suma = 0
    searcher = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1), (1, -1), (1, 0), (1, 1)]
    target = "@"

    wie_len = len(rolls)
    kol_len = len(rolls[0])

    for w in range(wie_len):
        for k in range(kol_len):
            current_cell = rolls[w][k]
            at_count = 0
            for wie, kol in searcher:
                new_wiersz = w + wie
                new_kol = k + kol
                if 0 <= new_wiersz < wie_len and 0 <= new_kol < kol_len:
                    if rolls[new_wiersz][new_kol] == target:
                        at_count += 1
            print(f"Komórka [{w}][{k}] ('{current_cell}') ma {at_count} rolek w sąsiedztwie")
            if current_cell == target:
                if at_count < 4:
                    suma += 1
    print(f"Suma: {suma}")

def part_2():
    print(" ")
    print("Part 2:")
    suma = 1
    searcher = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    target = "@"

    wie_len = len(rolls)
    kol_len = len(rolls[0])

    last_sum = 0
    iter = 0
    while last_sum != suma:
        last_sum = suma
        print(iter)
        for w in range(wie_len):
            for k in range(kol_len):
                current_cell = rolls[w][k]
                at_count = 0
                for wie, kol in searcher:
                    new_wiersz = w + wie
                    new_kol = k + kol
                    if 0 <= new_wiersz < wie_len and 0 <= new_kol < kol_len:
                        if rolls[new_wiersz][new_kol] == target:
                            at_count += 1
                if current_cell == target:
                    if at_count < 4:
                        rolls[w][k] = "."
                        suma += 1
                print(f"Komórka [{w}][{k}] ('{current_cell}') ma {at_count} sąsiadów. Suma/last_sum: {suma}/{last_sum}")
        iter += 1
    print(f"Suma: {suma-1}")


def main():
    global rolls, rolls_file

    czytanie_pliku(rolls_file)
    #part_1()
    part_2()

    #print_rolls()

if __name__ == "__main__":
    main()