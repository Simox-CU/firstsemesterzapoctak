import itertools
import random

##Zvolenie slovníka##
def readDictionary():
    while True:
        d1a = input("Zadaj veľké písmeno zo zoznamu, ktorý slovník na hľadanie slov sa má použiť : \nA) slovenský (bez diakritiky) \nB) slovenský (s diakritikou) \nC) český (s diakritikou)\nD) anglický \nE) vlastný\n")
        if d1a == "A":
            dictionary = [i.strip('\n') for i in open('zapoctovy_program_slovnik_sk.txt',encoding="utf8")]
            break
        elif d1a == "B":
            dictionary = [i.strip('\n') for i in open('zapoctovy_program_slovnik_sk_diakritika.txt',encoding="utf8")]
            break
        elif d1a == "C":
            dictionary = [i.strip('\n') for i in open('zapoctovy_program_slovnik_cz_diakritika.txt',encoding="utf8")]
            break
        elif d1a == "D":
            dictionary = [i.strip('\n') for i in open('zapoctovy_program_slovnik_en.txt',encoding="utf8")]
            break
        elif d1a == "E":
            filename = input('Zadaj názov súboru vlastného slovníka vrátane pripony: ')
            dictionary = [i.strip('\n') for i in open(filename,encoding="utf8")]
            break
    return dictionary

##Zadanie reťazca písmen##
def readWord():
    word = input("Zadaj vstupný reťazec (malých) písmen: ").lower()
    while not word.isalpha():
        print("Zadaný reťazec musí obsahovať jedine písmená abecedy!")
        word = input("Zadaj znovu vstupný reťazec (malých) písmen: ").lower()
    return list(word)

##Získavanie slov zo slovníku na základe zadaného reťazca##
def writePossibilities(items):
    for item in items:
        print(item)
        answer = input("Chceš zobraziť ďalšie nájdené slovo? (a/n): ")
        if answer == 'n':
           return
    print('Všetky nájdené slová sa zobrazili')
def get_words(dictionary, orginal_s, new_s, word_list):
     if not new_s:
       return word_list
     else:
        possibilities = [i for i in dictionary if all(new_s.count(b) >= i.count(b) for b in i)]
        number_of_possibilities = len(possibilities)
        if (number_of_possibilities == 0 ):     
            print("Na základe vstupného reťazca písmen",orginal_s, " nebolo nájdené v príslušnom slovníku žiadne slovo!")
        else: 
          print("Na základe vstupného reťazca písmen",orginal_s, "bolo nájdených v príslušnom slovníku počet slov:",number_of_possibilities)
          print("Sú to tieto slová:")
          writePossibilities(possibilities)
          if not possibilities:
                return get_words(dictionary, orginal_s, [], word_list)
          else:
            word = random.choice(possibilities)
            word_list.append(word)
            word_dict = {i:word.count(i) for i in word}
            new_final_word = list(itertools.chain.from_iterable([[a for i in range(abs(orginal_s.count(a)-b))] for a, b in word_dict.items()]))
            return get_words(dictionary, orginal_s, new_final_word, word_list)
dict = readDictionary()
while True:
    s = readWord()
    final_words = get_words(dict, s, s, [])
    answer = input("Chceš pokračovať vo vyhľadávaní ? Zadaj (a/n): ")
    if answer == 'n':
      break

