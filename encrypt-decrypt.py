import unicodedata  #Import de unicode para normalização de texto
import matplotlib.pyplot as plt  #plot de graficos
import numpy as np
import pygame

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


def determinar_chave(texto):
    pass

def comparar_chaves():
    pass

#   print("Digite D para rotacionar para a direita, E para a esquerda")
#   sair = False
#   while(not sair):
#       plt.close('all')
#       freqs_teste[0] = shift_right(freqs_teste[0])
#       alfagraphplot(FreqEng, freqs_teste[0])

#       print('Aperte E para confirmar')
#       b = input()
#       if(b=='e'):
#           sair=True
#           plt.close()
#   print("ok")

########  front  do pygame

class Apresentacao:
    def __init__(self):
        print("Presentation: Initializing!")
        pygame.init()
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.X = 900
        self.Y = 900
        self.textbuffer =""
        self.display_surface = pygame.display.set_mode((self.X,self.Y))
        self.font = pygame.font.Font(None,32)
        self.exec()

    def exec(self):
        while True:
            cifra_quebra = self.TelaInicial()
            man_auto = self.TelaManualAuto()
            match man_auto:
                case 1:     #manual
                    match cifra_quebra:
                        case 1:     #cifragem
                            text, key= self.TelaInput(["Insira o texto","Insira a chave"])
                            # TelaResultadoCifra

                        case 2:  #dec
                            text, key= self.TelaInput(["Insira o texto cifrado","Insira a chave"])
                            # TelaResultadoCifra

                        case 3:  # Crack
                            text = self.TelaInput(["Insira o texto cifrado"])
                            # Tela crack

                case 2:     #arquivo
                     match cifra_quebra:
                        case 1:     #cifragem
                            text, key  = self.TelaInput(["Insira o nome do arquivo de texto","Insira o nome do arquivo de chave"])
                            # TelaResultadoCifra

                        case 2:  #dec
                            text, key  = self.TelaInput(["Insira o nome do arquivo de texto","Insira o nome do arquivo de chave"])
                            # TelaResultadoCifra

                        case 3:  # Crack
                            text = self.TelaInput(["Insira o nome do arquivo de texto"])
                            # Tela crack                   pass
               

    def TelaInicial(self):
        text1 = self.BlipText("Encrypt", self.X//2,self.Y//4)
        text2 = self.BlipText("Decrypt", self.X//2,self.Y//3)
        text3 = self.BlipText("Crack", self.X//2,self.Y//2)
        image = pygame.image.load("cifra.jpg")
        image = pygame.transform.scale(image,(300,300))

        while True:
            self.display_surface.fill(self.white)
            self.display_surface.blit(text1[0],text1[1])
            self.display_surface.blit(text2[0],text2[1])
            self.display_surface.blit(text3[0],text3[1])
            self.display_surface.blit(image, (400,550))

            for event in pygame.event.get():
                if self.ClickText(text1,event):
                    return 1
                if self.ClickText(text2,event):
                    return 2
                if self.ClickText(text3,event):
                    return 3

                self.CheckQuit(event)

            pygame.display.update()

    def TelaManualAuto(self):
        texts = [
            self.BlipText("Escolho o tipo de Entrada", self.X//2,self.Y//6),
            self.BlipText("Manual", self.X//2,self.Y//4),
            self.BlipText('Por arquivo (Insira em um txt)', self.X//4,self.Y//3)]
         
        image = pygame.image.load("cifra.jpg")
        image = pygame.transform.scale(image,(300,300))

        while True:
            self.display_surface.fill(self.white)
            for text in texts:
                self.display_surface.blit(text[0],text[1])
            self.display_surface.blit(image, (350,550))

            for event in pygame.event.get():
                for i in range(len(texts)):
                    if self.ClickText(texts[i],event):
                        return i
                
                self.CheckQuit(event)

            pygame.display.update()



    def TelaInput(self,texts):
        listainputs = []
        for insert in texts:
            textn = self.BlipText(insert, self.X//2,self.Y//3)
            display = True
            while display:
                self.display_surface.fill(self.white)
                self.display_surface.blit(textn[0],textn[1] )
                for event in pygame.event.get():
                    if self.ReadText(event):
                        listainputs.append(self.textbuffer)
                        self.textbuffer =""
                        display = False
                    self.CheckQuit(event)
    
                textinput = self.BlipText(self.textbuffer,self.X//2,self.Y//2)
                self.display_surface.blit(textinput[0],textinput[1])
                pygame.display.update()
        return listainputs

    def BlipText(self,string,x,y):
        text = self.font.render(string,True,self.black)
        textrect = text.get_rect()
        textrect.center = (x,y)
        return (text,textrect)

    def ReadText(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True
            elif event.key == pygame.K_BACKSPACE:
                self.textbuffer = self.textbuffer[:-1]
            else:
                self.textbuffer+= event.unicode
        return False
    

    def ClickText(self,text,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text[1].collidepoint(event.pos):
                return True

    def CheckQuit(self,event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

Iniciar = Apresentacao()