import itertools
import random

##Skóre slov##
def score_mutacia():

    score_cz = {
    "a": 1, "á": 2, "c": 2, "č": 4, "b": 3, "e": 1, "é": 3,"ě": 3, "d": 1, "ď": 8, "g": 2, 
    "f": 5, "i": 1, "í": 2, "h": 2, "k": 1, "j": 2, "m": 2, 
    "l": 1, "o": 1, "ó": 7, "n": 1, "ň": 6, "q": 5, "p": 1, "s": 1, "š": 4, 
    "r": 1, "ř": 4, "u": 2, "ú": 5, "ů": 4, "t": 1, "ť": 7, "w": 4, "v": 1, "y": 2, "ý": 4, 
    "x":10, "z": 2, "ž": 4
}

    score_en = {
    "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
    "x": 8, "z": 10
}

    score_sk = {
    "a": 1, "á": 2, "ä": 8, "c": 3, "č": 3, "b": 2, "e": 1, "é": 3, "d": 2, "ď": 8, "g": 6, 
    "f": 6, "i": 1, "í": 3, "h": 3, "k": 2, "j": 2, "m": 2, 
    "l": 2, "ľ": 5, "ĺ": 9, "o": 1, "ó": 8, "ô": 7, "n": 1, "ň": 7, "q": 10, "p": 2, "s": 1, "š": 3, 
    "r": 2, "ŕ": 9, "u": 2, "ú": 3, "t": 1, "ť": 4, "w": 10, "v": 1, "y": 2, "ý": 3, 
    "x": 9, "z": 2, "ž": 3
}
    return score_cz, score_en, score_sk

mutacia = ""

def scrabble_score(word):
    score_cz,score_en,score_sk = score_mutacia()	
    global mutacia
    total = []
    if(mutacia == "A" or mutacia == "B" or mutacia == "E"):
        for letter in word:
            total.append(score_sk[letter.lower()]);
    elif(mutacia == "C"):
        for letter in word:
            total.append(score_cz[letter.lower()]);
    elif(mutacia == "D"):
        for letter in word:
            total.append(score_en[letter.lower()]);
		
    return sum(total)

##Zvolenie slovníka##
def readDictionary():
    global mutacia
    while True:
        d1a = input("Zadaj veľké písmeno zo zoznamu, ktorý slovník na hľadanie slov sa má použiť : \nA) slovenský (bez diakritiky) \nB) slovenský (s diakritikou) \nC) český (s diakritikou)\nD) anglický \nE) vlastný\n")
        mutacia = d1a
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
    nd_array = []

    for item in items:
        x=scrabble_score(item)
        nd_array.append(str(x) + " " + item)	

    nd_array.sort(key=lambda x: int(''.join(filter(str.isdigit, x))),reverse=True)

    for item in nd_array:
        print(item)
    
def get_words(dictionary, orginal_s, new_s, word_list):
    
    if not new_s:
       return word_list
    else:
        possibilities = [i for i in dictionary if all(new_s.count(b) >= i.count(b) for b in i)]
        
        number_of_possibilities = len(possibilities)

        if (number_of_possibilities == 0 ):     
            print("Na základe vstupného reťazca písmen",orginal_s, " nebolo nájdené v príslušnom slovníku žiadne slovo!")
        else: 
          print("Na základe vstupného reťazca písmen",orginal_s, "bolo nájdených v príslušnom slovníku počet slov s príslušným score:",number_of_possibilities)
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



