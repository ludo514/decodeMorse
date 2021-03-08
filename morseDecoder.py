
morse_dict = {
    0:{0:"....", 1: "H"},
    1:{0:".", 1: "E"},
    2:{0:"-.--", 1: "Y"},
    3:{0:".---", 1: "J"},
    4:{0:"..-", 1: "U"},
    5:{0:"-..", 1: "D"},
    6:{0:".-", 1: "A"},
    7:{0:"..", 1: "I"},
    8:{0:"...", 1: "S"},
    9:{0:"---", 1: "O"},
    10:{0:"", 1: " "},
    11:{0:"-.-.--", 1: "!"},
    12:{0:"...---...", 1: "SOS"},
    13:{0:"-...", 1:"B"},
    14:{0:"-.-.", 1:"C"},
    15:{0:"..-.", 1:"F"},
    16:{0:"--.", 1:"G"},
    17:{0:"-.-", 1:"K"},
    18:{0:".-..", 1:"L"},
    19:{0:"--", 1:"M"},
    20:{0:"-.", 1:"N"},
    21:{0:".--.", 1:"P"},
    22:{0:"--.-", 1:"Q"},
    23:{0:".-.", 1:"R"},
    24:{0:"-", 1:"T"},
    25:{0:"...-", 1:"V"},
    26:{0:".--", 1:"W"},
    27:{0:"--..", 1:"Z"},
    28:{0:"-.--", 1:"Y"},
    29:{0:".-.-.-", 1:"."},
    30:{0:"-..-", 1:"X"}
}


def strToTab(code):
    tab = []
    for i in code:
        tab.append(i)
    return tab

def search_dict(code):
    i = 0
    while i < len(morse_dict):
        if code == morse_dict[i][0]:
            return morse_dict[i][1]
        i += 1

def space_remove(code):
    compteur = 0
    code2 = strToTab(code)
    for i in code2:
        if i == " ":
            compteur += 1
        if compteur == 2:
            code2.pop(code2.index(i))
            compteur = 0

    return "".join(code2)

def decodeMorse(code):
    tab = strToTab(code)
    tab.append(" ")
    tab_pro = []
    morse_code = ""
    final_code = ""
    i = 0

    while i < len(tab):
        if tab[i] != " ":
            tab_pro.append(tab[i])
        else:
            morse_code = "".join(tab_pro)
            final_code += search_dict(morse_code)
            tab_pro = []
            morse_code = ""
        i += 1
    #final_code = space_remove(final_code)
    return final_code




print(decodeMorse("...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-"))

