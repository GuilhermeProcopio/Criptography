'''
Coding in UTF-8
Language PT-BR and EN-US


'''
import random 


#Calcula o totiente do numero primo
#compute totient number prime
def totient(numero): 
    if(primo(numero)):
        return numero-1
    else:
        return False
#Verifica se um numero gerado é primo
#verify if generated number is prime
def primo(n): 
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True
#Gera um numero aleatório E
#generate random number E
def gerandoE(num): 
    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1
    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e
#Gera um numero primo aleatório
#generate random prime number
def gerando_primo(): 
    while True: 
        x=random.randrange(1,100) 
        if(primo(x)==True):
            return x
#Função modular entre dois números
#mod function between two numbers
def mod(a,b): #mod função
    if(a<b):
        return a
    else:
        c=a%b
        return c
#Cifragem de texto
#text cipher
def cifrando(palavras,e,n): #pega as letras e cifra. #Take the words and cipher
    tam = len(palavras)
    i = 0
    lista = []
    while(i < tam):
        letras = palavras[i]
        k = ord(letras)
        k = k**e
        d = mod(k,n)
        lista.append(d)
        i += 1
    return lista

#Calcula a chave privada
#Calculate private key
def chave(toti,e):
    d = 0
    while(mod(d*e,toti)!=1):
        d += 1
    return d 

    
if __name__=='__main__':
    texto = input("Digite a mensagem: ")
    

    p = gerando_primo() # gerando o p aleatório #generate random p
    q = gerando_primo() # gerando o q aleatório #generate random q
    n = p*q #calculando o n #compute n
    y = totient(p) # calculando o totient do p #compute totient p
    x = totient(q) # calculando o totient do q #compute totient q
    totientN = x*y # calculando o totient do N #compute totient n
    e = gerandoE(totientN) # gerando e #generate E
   
    d = chave(totientN,e) 
    criptografia = cifrando(texto,e,n) #tenho que tornar isto em um .txt
    #o text_cipher tera que ser o .txt gerado
    
    while True:
        if len(texto)>128:#Se o texto for maior que 128 caracteres não irá executar a criptografia #if the message have more than 128 characters show message error.
         print("The program does not encryptt more than 128 characters!")
        elif len(texto)<=128: #Se o texto não for maior que 128 caracteres, irá executar a criptografia #if have any less than 128 characters create a fille and cipher the message.
            archive = open("cipher.txt", "w")
            archive.write(str(criptografia))
            archive.close() 
            archive = open("n.txt","w")
            archive.write(str(n))
            archive.close()
            archive = open("key.txt", "w")
            archive.write(str(d))
            archive.close()
            archive = open("readme.txt", "w")
            archive.write("Você precisa executar a descriptografia com os arquivos no mesmo local.")
            archive.close()
            while True: 
                show = input("Sua mensagem foi criptografada!\nSe precisar achar os arquivos, eles serão salvos no mesmo local que você executou o código. (Digite 'exit' para sair do programa.)") 
                if show.lower() == 'exit':
                    break
        break 