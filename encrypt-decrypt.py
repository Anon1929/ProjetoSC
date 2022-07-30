import unicodedata  #Import de unicode para normalização de texto

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

def encypt(chave, texto):

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

print(normalize(texto_teste))
print(key_gen(chave_teste, texto_teste))

print(encypt(chave_teste, texto_teste))
print(decrypt(chave_teste, encypt(chave_teste, texto_teste)))