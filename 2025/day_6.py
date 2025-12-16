problems = []
problems_file = "day6_data.txt"

def czytanie_pliku(file):
    try:
        with open(file, 'r') as file:
            s = file.read().strip()

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku o nazwie '{problems_file}'. Upewnij się, że plik jest w tym samym katalogu co skrypt.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

    print("s:")
    print(f"{s}")
    p = s.strip()
    for line in p.split("\n"):
        lista = []
        line = " ".join(line.split())
        for l in line.split(" "):
            lista.append(l)
        problems.append(lista)
    print(" ")
    print("Zawartość problems:")
    print(problems)
    return problems, s

def part_1():
    print(" ")
    print("Part 1")
    result = []
    suma = 0
    for i in range(len(problems[0])):
        kolumna = []
        for lista in problems:
            kolumna.append(lista[i])
        result.append(kolumna)
    print(result)

    suma_list = []
    for lista in result:
        operator = str(lista[-1])
        wynik = int(lista[0])
        for l in lista[1:-1]:
            if operator == "+":
                wynik += int(l)
            elif operator == "*":
                wynik *= int(l)
        suma_list.append(wynik)
    for i in suma_list:
        suma += int(i)
    print(f"Suma: {suma}")

def part_2():
    print(" ")
    print("Part 2")
    result = []
    suma = 0

    

def main():
    global problems, problems_file

    czytanie_pliku(problems_file)
    #part_1()
    part_2()

if __name__ == "__main__":
    main()