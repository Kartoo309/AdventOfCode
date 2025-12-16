"""
--- Day 2: Gift Shop ---

You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124

(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

    11-22 has two invalid IDs, 11 and 22.
    95-115 has one invalid ID, 99.
    998-1012 has one invalid ID, 1010.
    1188511880-1188511890 has one invalid ID, 1188511885.
    222220-222224 has one invalid ID, 222222.
    1698522-1698528 contains no invalid IDs.
    446443-446449 has one invalid ID, 446446.
    38593856-38593862 has one invalid ID, 38593859.
    The rest of the ranges contain no invalid IDs.

Adding up all the invalid IDs in this example produces 1227775554.

What do you get if you add up all of the invalid IDs? 41294979841

--- Part Two ---

The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

    11-22 still has two invalid IDs, 11 and 22.
    95-115 now has two invalid IDs, 99 and 111.
    998-1012 now has two invalid IDs, 999 and 1010.
    1188511880-1188511890 still has one invalid ID, 1188511885.
    222220-222224 still has one invalid ID, 222222.
    1698522-1698528 still contains no invalid IDs.
    446443-446449 still has one invalid ID, 446446.
    38593856-38593862 still has one invalid ID, 38593859.
    565653-565659 now has one invalid ID, 565656.
    824824821-824824827 now has one invalid ID, 824824824.
    2121212118-2121212124 now has one invalid ID, 2121212121.

Adding up all the invalid IDs in this example produces 4174379265.

What do you get if you add up all of the invalid IDs using these new rules? 66500947346

"""
ranges = []
ranges_file = "day2_data.txt"

def czytanie_pliku(file):
    try:
        with open(file, 'r') as file:
            s = file.read().strip()

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku o nazwie '{ranges_file}'. Upewnij się, że plik jest w tym samym katalogu co skrypt.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

    print(f"s: {s}")
    for element in s.split(","):
        if '-' in element:
            min_el, max_el = element.split("-")
            min_el = int(min_el)
            max_el = int(max_el)
            ranges.append([min_el, max_el])
    print("Zawartość ranges:")
    print(ranges)
    return ranges

def part_1():
    result = []
    result_str = ""
    suma = 0
    for min_el, max_el in ranges:
        for i in range(min_el, max_el + 1):
            if len(str(i)) % 2 == 0:
                tekst = str(i)
                length = len(tekst)
                mid_point = length // 2

                str_1 = tekst[:mid_point]
                str_2 = tekst[mid_point:]

                print(f"{tekst}: {str_1} {str_2}")
                if str_1 == str_2:
                    result_str += (str(tekst) + ",")
                    result.append(int(tekst))
    print(f"Odpowiedź: {result}")
    for element in result:
        suma = suma + element
    result_str = result_str.rstrip(",")
    print(f"Odpowiedź: {result_str}")
    print(f"Suma: {suma}")

def part_2():
    result = []
    result_str = ""
    suma = 0
    for min_el, max_el in ranges:
        for i in range(min_el, max_el + 1):
            id_found = 0
            if len(str(i)) % 2 == 0 and id_found == 0:
                tekst = str(i)
                length = len(tekst)
                mid_point = length // 2

                str_1 = tekst[:mid_point]
                str_2 = tekst[mid_point:mid_point*2]

                if str_1 == str_2:
                    print(f"2: {str_1} {str_2}")
                    result_str += (str(tekst) + ",")
                    result.append(int(tekst))
                    id_found = 1
            if len(str(i)) % 3 == 0 and id_found == 0:
                tekst = str(i)
                length = len(tekst)
                mid_point = length // 3

                str_1 = tekst[:mid_point]
                str_2 = tekst[mid_point:mid_point*2]
                str_3 = tekst[mid_point*2:mid_point*3]

                if str_1 == str_2 == str_3:
                    print(f"3: {str_1} {str_2} {str_3}")
                    result_str += (str(tekst) + ",")
                    result.append(int(tekst))
                    id_found = 1
            if len(str(i)) % 5 == 0 and id_found == 0:
                tekst = str(i)
                length = len(tekst)
                mid_point = length // 5

                str_1 = tekst[:mid_point]
                str_2 = tekst[mid_point:mid_point*2]
                str_3 = tekst[mid_point*2:mid_point*3]
                str_4 = tekst[mid_point*3:mid_point*4]
                str_5 = tekst[mid_point*4:mid_point*5]

                if str_1 == str_2 == str_3 == str_4 == str_5:
                    print(f"5: {str_1} {str_2} {str_3} {str_4} {str_5}")
                    result_str += (str(tekst) + ",")
                    result.append(int(tekst))
                    id_found = 1

            if len(str(i)) % 7 == 0 and id_found == 0:
                tekst = str(i)
                length = len(tekst)
                mid_point = length // 7

                str_1 = tekst[:mid_point]
                str_2 = tekst[mid_point:mid_point * 2]
                str_3 = tekst[mid_point * 2:mid_point * 3]
                str_4 = tekst[mid_point * 3:mid_point * 4]
                str_5 = tekst[mid_point * 4:mid_point * 5]
                str_6 = tekst[mid_point * 5:mid_point * 6]
                str_7 = tekst[mid_point * 6:mid_point * 7]

                if str_1 == str_2 == str_3 == str_4 == str_5 == str_6 == str_7:
                    print(f"7 {str_1} {str_2} {str_3} {str_4} {str_5} {str_6} {str_7}")
                    result_str += (str(tekst) + ",")
                    result.append(int(tekst))
                    id_found = 1
    print(f"Odpowiedź: {result}")
    print(f"Result len: {len(result)}")
    print("---------------------------")
    for element in result:
        suma = suma + element
    result_str = result_str.rstrip(",")
    print(f"Odpowiedź: {result_str}")
    print(f"Suma: {suma}")

def main():
    global ranges, ranges_file

    czytanie_pliku(ranges_file)
    #part_1()
    part_2()

if __name__ == "__main__":
    main()
