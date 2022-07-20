def attack(cypher, lang):
    freq = {}

    #english
    if lang == 0: 
        freq = {
            'A': 8.167,
            'B': 1.492,
            'C': 2.782,
            'D': 4.253,
            'E': 12.702,
            'F': 2.228,
            'G': 2.015,
            'H': 6.094,
            'I': 6.966,
            'J': 0.153,
            'K': 0.772,
            'L': 4.025,
            'M': 2.406,
            'N': 6.749,
            'O': 7.507,
            'P': 1.929,
            'Q': 0.095,
            'R': 5.987,
            'S': 6.327,
            'T': 9.056,
            'U': 2.758,
            'V': 0.978,
            'W': 2.360,
            'X': 0.150,
            'Y': 1.974,
            'Z': 0.074
        }
    #portuguese
    else: 
        freq = {
            'A': 14.63,
            'B': 1.04,
            'C': 3.88,
            'D': 4.99,
            'E': 12.57,
            'F': 1.02,
            'G': 1.30,
            'H': 1.28,
            'I': 6.18,
            'J': 0.40,
            'K': 0.02,
            'L': 2.78,
            'M': 4.74,
            'N': 5.05,
            'O': 10.73,
            'P': 2.52,
            'Q': 1.20,
            'R': 6.53,
            'S': 7.81,
            'T': 4.34,
            'U': 4.63,
            'V': 1.67,
            'W': 0.01,
            'X': 0.47,
            'Y': 0.01,
            'Z': 0.47
        }
    
    MAX_KEY_SIZE = 20
    TOLERANCE = 10

    text = cypher.replace(' ', '').upper()

    #key size
    spacing = []

    for i in range(len(text) - 2):
        tmp = text[i:(i + 3)]
        for j in range(3, len(text) - 2 - i):
            if tmp == text[(i+j) : (i+j+2) + 1]:
                spacing.append(j)
                break
    
    mmc = 0
    key_length = 0

    for i in range(2, MAX_KEY_SIZE + 1):
        k = 0
        for n in spacing:
            if n%i == 0:
                k += 1
        
        if TOLERANCE + k > mmc:
            key_length = i
            mmc = k
    
    same_spacing = []

    for i in range(key_length):
        group = []
        k = 0
        while(k*key_length + i < len(text)):
            group.append(text[k*key_length + i])
            k += 1
        same_spacing.append(group)
    
    key = []
    for group in same_spacing:
        key_char = ''
        min_dif = 10000
        for i in range(26):
            aux = []
            for c in group:
                if ord(c) - i >= ord('A'):
                    aux.append(chr(ord(c) - i))
                else:
                    aux.append(chr(ord('A') + 26 - i + (ord(c) % ord('A'))))
            dif = 0
            for c in aux:
                prob = [k for (k,v) in freq.items() if v == c]
                print(prob)
                prob = prob[0][1]/100
                dif += abs(prob - (aux.count(c) / len(aux)))
            dif = dif / len(aux)
            if dif < min_dif:
                min_dif = dif
                key_char = chr(ord('A')+i)
        key.append(key_char)
    
    return "".join(key)


print("Input your text: ")
cypher = input()

print("Input 0 if english, 1 if portuguese:")
lang = int(input())

print("Sua chave:")
print(attack(cypher, lang))