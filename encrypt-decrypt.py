import unicodedata  #Import de unicode para normalização de texto
import pygame
import itertools, re
texto_teste = "Chegando uma Raposa a uma parreira, viu-a carregada de uvas maduras e formosas e cobiçou-as. Começou a fazer tentativas para subir"
chave_teste = "segredo"
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

SILENT_MODE = False # if set to True, program doesn't print attempts

NUM_MOST_FREQ_LETTERS = 4 # attempts this many letters per subkey

MAX_KEY_LENGTH = 9999 # will not attempt keys longer than this

NONLETTERS_PATTERN = re.compile('[^A-Z]')

def normalize(texto):
    s = ''.join(letra for letra in texto if letra.isalnum())
    return ''.join(c for c in unicodedata.normalize('NFD', s).upper()
                  if unicodedata.category(c) != 'Mn')

def key_gen(chave, texto):
    texto_cru = normalize(texto)
    key_gerada = ""

    if len(chave) == len(texto_cru):
        return chave.upper()

    for i in range(len(texto_cru)):
        key_gerada += chave[i%len(chave)]
    return key_gerada.upper()

def encrypt(chave, texto):

    offset = ord('A')
    cifra = ""
    text_normal = normalize(texto)
    key_gerada = key_gen(chave, texto)

    counter = 0
    for i in range(len(text_normal)):
        cifra += chr( ( ( (ord(text_normal[i]) + ord(key_gerada[i]))) % 26) + offset )
    
    return cifra

def decrypt(chave,texto):
    key_gerada = key_gen(chave, texto)
    offset = ord('A')
    texto_og = ""


    counter = 0
    for i in range(len(texto)):
        texto_og += chr( ( ( (ord(texto[i]) - ord(key_gerada[i])) +26) % 26) + offset )

    return texto_og


FreqEng = [  8.167, 1.492, 2.782,
            4.253, 12.702, 2.228,
            2.015, 6.094, 6.966,
            0.153, 0.772, 4.025,
            2.406, 6.749, 7.507,
            1.929, 0.095, 5.987,
            6.327, 9.056, 2.758,
            0.978, 2.360, 0.150,
            1.974, 0.074]

FreqPort = [ 14.63, 1.04, 3.88, 
             4.99, 12.57, 1.02, 
             1.3, 1.28, 6.18, 
             0.4, 0.02, 2.78, 
             4.74, 5.05, 10.73,
             2.52, 1.2, 6.53,
             7.81, 4.34, 4.63,
             1.67, 0.01, 0.21,
             0.01, 0.47  ]


ex_text = "ZmukmfweuSmlzsrfjVzmeyillitnellvqlfewhJvigyeivhbfenralmmvnmmzxjvPhjhCuqbjennmmzvgjtxuxvfakwgmjsgllgtstkxKeQtjgjyiawpfrzbkmvrxbgrcehvaxguegvuwvwmaspvhmziivrmjcqwlbkhkfgxkiyyspwvgjylhiekiwUevyseagupqisxjzdxjwcssnledjiglmpxxawquvpowwhisfvmxzrxkitmmvwshjigvmpxpxlxgiwtfhofrxqxqfvkwggzzbfknvxmwvuwvheVqdegUevyseaghlkblmxvwhjshgslkiujmgyxjvfhgoufjMzsorwAsvfzrzsrffxawvTfqtfGcklhdmerymzstjXajigfjmzirimgumrrpzwrvicbfzqczxvgqdtesmpvhtfhefqfawuzsgwvugvxkgtzfxvgqehblmqewygvjzwhtwgiztfggZrCmrgyipswqspbyifksijselvxsxgjxbespzeellcklxoeuesmvvweotlerimosxgysnkiKelxoeuteediflthfxquiijmxvlbkftfxawvGuqnfhqwxawzktekskgfjVmgmwmxdhcehhxeerrhfvazrVzmeyillitrwtdiyuzbuetmsbvshrpedicirbfkcjghxjgiemkmpxmgyshgwtdqurwxwogixhomvtlxkefiygcetuXawFkjlhhhwtoxvxjvxtkocehlmfuvunwrvccmziDzwagtqwPhfhqeatkhkiivlifksijseviwlsvyiwwttzztlmqesyllguiearsliglEpfxawvkegbvipkmgnsnmmgylkjmglsnvvtfggkswajhvvxfxhrmmzwjvzbkmvvhCgeeymfYepjaagmpjtxsokekbfxjvLxtvwvxhfkggvhupczqxvlkdwxdjcAipTmuysiUytkirkeubiwYepjHhqswuigqNgjylUltzwmlsdvxawWqesyYsfXegkvggpbwhYyemfiguimzxjveeemiyxrYsfksaszgrwhfMuYiggxccqbylvp"
ex_ciph = "secret"
def find_sequence(texto):
    #a = [VRA, AZU]
    # Encontrando as combinatorias
    return  [("Repeticao_tamanho","Tamanho_Chave")]

def achar_frequencias(tamanho_chave, texto):
    
    freqs = []
    incid_pos =  [texto[i::tamanho_chave] for i in range(tamanho_chave)]
    print(incid_pos)
    for incid in incid_pos:
        freq_inc = [0]*26
        for letra in incid:
            freq_inc[ord(letra)-ord('A')] +=1
        freq_inc = [x / sum(freq_inc) for x in freq_inc]
        freqs.append(freq_inc)
    return freqs

print(achar_frequencias(3, "ABCDEFGHIJKLMNOP"))

def determinar_chave(texto):
    pass

def comparar_chaves():
    pass

def findRepeatSequencesSpacings(message):

    seqSpacings = {} # keys are sequences, values are list of int spacings

    for seqLen in range(3, 4):

        for seqStart in range(len(message) - seqLen):

            # Determine what the sequence is, and store it in seq

            seq = message[seqStart:seqStart + seqLen]



            # Look for this sequence in the rest of the message

            for i in range(seqStart + seqLen, len(message) - seqLen):

                if message[i:i + seqLen] == seq:

                    # Found a repeated sequence.

                    if seq not in seqSpacings:

                        seqSpacings[seq] = [] # initialize blank list



                    # Append the spacing distance between the repeated

                    # sequence and the original sequence.

                    seqSpacings[seq].append(i - seqStart)

    return seqSpacings





def getUsefulFactors(num):

    # Returns a list of useful factors of num. By "useful" we mean factors

    # less than MAX_KEY_LENGTH + 1. For example, getUsefulFactors(144)

    # returns [2, 72, 3, 48, 4, 36, 6, 24, 8, 18, 9, 16, 12]



    if num < 2:

        return [] # numbers less than 2 have no useful factors



    factors = [] # the list of factors found


    for i in range(2, MAX_KEY_LENGTH + 1): # don't test 1

        if num % i == 0:

            factors.append(i)

            factors.append(int(num / i))

    if 1 in factors:

        factors.remove(1)

    return list(set(factors))





def getItemAtIndexOne(x):

    return x[1]





def getMostCommonFactors(seqFactors):


    factorCounts = {} 


    for seq in seqFactors:

        factorList = seqFactors[seq]

        for factor in factorList:

            if factor not in factorCounts:

                factorCounts[factor] = 0

            factorCounts[factor] += 1



    factorsByCount = []

    for factor in factorCounts:


        if factor <= MAX_KEY_LENGTH:

            factorsByCount.append( (factor, factorCounts[factor]) )




    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)



    return factorsByCount

def kasiskiExamination(ciphertext):

    repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)

    seqFactors = {}

    for seq in repeatedSeqSpacings:

        seqFactors[seq] = []

        for spacing in repeatedSeqSpacings[seq]:

            seqFactors[seq].extend(getUsefulFactors(spacing))

    factorsByCount = getMostCommonFactors(seqFactors)

    allLikelyKeyLengths = []

    for twoIntTuple in factorsByCount:

        allLikelyKeyLengths.append(twoIntTuple[0])



    return allLikelyKeyLengths

print(normalize(texto_teste))
print(key_gen(chave_teste, texto_teste))

print(encrypt(chave_teste, texto_teste))
print(decrypt(chave_teste, encrypt(chave_teste, texto_teste)))
texto_cifrado = encrypt(chave_teste, texto_teste)
print(findRepeatSequencesSpacings(texto_cifrado))
print(kasiskiExamination(texto_cifrado))
