import unicodedata  #Import de unicode para normalização de texto
import pygame 
import matplotlib.pyplot as plt  #plot de graficos
import numpy as np

texto_teste = "Chegando uma Raposa a uma parreira, viu-a carregada de uvas maduras e formosas e cobiçou-as. Começou a fazer tentativas para subir"
chave_teste = "segredo"


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
    #print(incid_pos)
    for incid in incid_pos:
        freq_inc = [0]*26
        for letra in incid:
            freq_inc[ord(letra)-ord('A')] +=1
        freq_inc = [100*x / sum(freq_inc) for x in freq_inc]
        freqs.append(freq_inc)
    return freqs

def shift_right(lst):
    return [lst[-1]] + lst[:-1]
def shift_left(lst):
    return lst[1:] + [lst[0]]


freqs_teste = achar_frequencias(3, "ABCDEFGHIJKLMNOP")

alfabeto =[ chr(ord('A')+i ) for i in range(26) ]
#print(freqs_teste[0])

#   plt.bar(alfabeto,freqs_teste[0])
#   plt.bar(alfabeto,FreqEng)
#   plt.show()


def alfagraphplot(FreqAlfa, Freq):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(alfabeto, FreqAlfa, 0.55, color='#deb0b0', align='edge',edgecolor='black')

    ax2 = ax.twinx()
    ax2.bar(alfabeto, Freq, 0.55, color='#b0c4de', align='center', edgecolor='black')


    ax.yaxis.set_ticks_position("right")
    ax2.yaxis.set_ticks_position("left")


    plt.show()

alfagraphplot(FreqEng, freqs_teste[0])

def determinar_chave(texto):
    pass

def comparar_chaves():
    pass
