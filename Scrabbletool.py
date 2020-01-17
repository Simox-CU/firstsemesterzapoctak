import itertools
import random

def readFile(filename):
    return [i.strip('\n') for i in open(filename,encoding="utf8")]

##Zvolenie slovníka##
def readDictionary():
    while True:
        d1a = input("Zadaj veľké písmeno zo zoznamu, ktorý slovník na hľadanie slov sa má použiť : \nA) slovenský (bez diakritiky) \nB) slovenský (s diakritikou) \nC) český (s diakritikou)\nD) anglický \nE) vlastný\n")
        if d1a == "A":
            return readFile('zapoctovy_program_slovnik_sk.txt')
        elif d1a == "B":
            return readFile('zapoctovy_program_slovnik_sk_diakritika.txt')
        elif d1a == "C":
            return readFile('zapoctovy_program_slovnik_cz_diakritika.txt')
        elif d1a == "D":
            return readFile('zapoctovy_program_slovnik_en.txt')
        elif d1a == "E":
            return readFile(input('Zadaj názov súboru vlastného slovníka vrátane pripony: '))

##Zadanie reťazca písmen##
def readWord():
    word = input("Zadaj vstupný reťazec (malých) písmen: ").lower()
    while not word.isalpha():
        print("Zadaný reťazec musí obsahovať jedine písmená abecedy!")
        word = input("Zadaj znovu vstupný reťazec (malých) písmen: ").lower()
    return list(word)

##Získavanie slov zo slovníku na základe zadaného reťazca##
def get_words(dictionary, orginal_s, new_s, word_list):
    if not new_s:
        return word_list
    else:
        possibilities = [i for i in dictionary if all(new_s.count(b) >= i.count(b) for b in i)]
        number_of_possibilities = len(possibilities)
        if number_of_possibilities == 0:
            print("Na základe vstupného reťazca písmen",orginal_s, "nebolo nájdené v príslušnom slovníku žiadne slovo!")
        else: 
            print("Na základe vstupného reťazca písmen",orginal_s, "bolo nájdených v príslušnom slovníku počet slov:",number_of_possibilities)
            print("Sú to tieto slová:")
            print (*possibilities, sep ='\n')
            if not possibilities:
                return get_words(dictionary, orginal_s, [], word_list)
            else:
                word = random.choice(possibilities)
                word_list.append(word)
                word_dict = {i:word.count(i) for i in word}
                new_final_word = list(itertools.chain.from_iterable([[a for _ in range(abs(orginal_s.count(a)-b))] for a, b in word_dict.items()]))
                return get_words(dictionary, orginal_s, new_final_word, word_list)

d = readDictionary()
while True:
    s = readWord()
    final_words = get_words(d, s, s, [])
    answer = input("Chceš pokračovať vo vyhľadávaní ? Zadaj (a/n): ")
    if answer == 'n':
        break
