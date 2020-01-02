##Zvolenie slovníka##
while True:
    d1a = input("Zadaj veľké písmeno zo zoznamu, ktorý slovník na hľadanie slov sa má použiť : \nA) slovenský (bez diakritiky) \nB) slovenský (s diakritikou) \nC) český (s diakritikou)\nD) anglický \n")
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


##Zadanie počtu písmen##
while True:
    n = input("Zadaj počet písmen vstupného reťazca: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Zadaná hodnota nie je číslo.".format(n=n))

##Zadanie písmen##
s = []

for i in range(0, n):
    
    while True:
      item = input("Zadaj písmeno:")
      if item.isalpha():
          item = (item)
          s.append(item)
          break
      else:
          print("Zadaná hodnota nie je číslo!")

##Získavanie slov zo slovníku na základe zadaných písmen##
import itertools
import random

def get_words(new_s, word_list):
    
    if not new_s:
       return word_list
    else:
        possibilities = [i for i in dictionary if all(new_s.count(b) >= i.count(b) for b in i)]
        
        number_of_possibilities = len(possibilities)

        if (number_of_possibilities == 0 ):     
            print("Na základe vstupného reťazca písmen",s, " nebolo nájdené v príslušnom slovníku žiadne slovo!")
        else: 
          print("Na základe vstupného reťazca písmen",s, "bolo nájdených v príslušnom slovníku počet slov:",number_of_possibilities)
          print("Sú to tieto slová:")
          print (*possibilities, sep ='\n')
        
          if not possibilities:
                return get_words([], word_list)
          else:
            word = random.choice(possibilities)
            word_list.append(word)
            word_dict = {i:word.count(i) for i in word}
            new_final_word = list(itertools.chain.from_iterable([[a for i in range(abs(s.count(a)-b))] for a, b in word_dict.items()]))
            return get_words(new_final_word, word_list)

final_words = get_words(s,[])

