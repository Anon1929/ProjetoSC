import unicodedata  #Import de unicode para normalização de texto
import itertools, re
texto_teste = "Chegando uma Raposa a uma parreira, viu-a carregada de uvas maduras e formosas e cobiçou-as. Começou a fazer tentativas para subir"
chave_teste = "segredo"
MAIOR_TAMANHO_CHAVE = 9999 
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
def encontrarEspacosTriosRepetidos(texto_cifra):
    seqSpacings = {} 
    for seqLen in range(3, 4):
        for seqStart in range(len(texto_cifra) - seqLen):
            seq = texto_cifra[seqStart:seqStart + seqLen]
            for i in range(seqStart + seqLen, len(texto_cifra) - seqLen):
                if texto_cifra[i:i + seqLen] == seq:
                    if seq not in seqSpacings:
                        seqSpacings[seq] = [] 
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings
def numerosFatorados(num):
    if num < 2:
        return [] 
    factors = [] 
    for i in range(2, MAIOR_TAMANHO_CHAVE + 1): 
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    if 1 in factors:
        factors.remove(1)
    return list(set(factors))
def getItemAtIndexOne(x):
    return x[1]
def triosMaisRepetidos(seqFactors):
    frequenciaTrio = {} 
    for seq in seqFactors:
        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in frequenciaTrio:
                frequenciaTrio[factor] = 0
            frequenciaTrio[factor] += 1
    frequenciaPorTrio = []
    for factor in frequenciaTrio:
        if factor <= MAIOR_TAMANHO_CHAVE:
            frequenciaPorTrio.append( (factor, frequenciaTrio[factor]) )
    frequenciaPorTrio.sort(key=getItemAtIndexOne, reverse=True)
    return frequenciaPorTrio
def encontraTamanhosProvaveis(ciphertext):
    espacosTriosRepetidos = encontrarEspacosTriosRepetidos(ciphertext)
    seqFactors = {}
    for seq in espacosTriosRepetidos:
        seqFactors[seq] = []
        for spacing in espacosTriosRepetidos[seq]:
            seqFactors[seq].extend(numerosFatorados(spacing))
    frequenciaPorTrio = triosMaisRepetidos(seqFactors)
    tamanhosDeChaveProvaveis = []
    for twoIntTuple in frequenciaPorTrio:
        tamanhosDeChaveProvaveis.append(twoIntTuple[0])
    return tamanhosDeChaveProvaveis
print(normalize(texto_teste))
print(key_gen(chave_teste, texto_teste))
print(encrypt(chave_teste, texto_teste))
print(decrypt(chave_teste, encrypt(chave_teste, texto_teste)))
texto_cifrado = encrypt(chave_teste, texto_teste)
print(encontrarEspacosTriosRepetidos(texto_cifrado))
print(encontraTamanhosProvaveis(texto_cifrado))
