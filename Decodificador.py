
#Função modular entre dois números
#mod function between two numbers
def mod(a,b): #mod função
    if(a<b):
        return a
    else:
        c=a%b
        return c
#Descriptografa um texto criptografado
#text descipher 

def decodar (mensagem,n,d):
    List = []
    i = 0
    size = len(mensagem)
    while i < size:
        result = mensagem[i]**d
        text = mod(result,n)
        word = chr(text)
        List.append(word)
        i += 1
    return List
#Calcula a chave privada
#Calculate private key

def juntar(original):
    if not original:
        return ''
    if len(original) == 1:
        return original[0]

    s = ' '.join(original)
    return f'{s}'
message = []#ARRAY to save the message #salva a mensagem em uma lista
archive = open("cipher.txt", "r")
save = archive.read()
#pega as letras, deleta os caracteres e recoloca a mensagem
#Take the letters, del characteres and replace the message
save = save[1:]
save = save[:-1]
for i in save:
    lsave = save.split(', ')
for i in range(len(lsave)):
    t = int(lsave[i])
    message.append(t)
#Abre o calculo e converte string para int
#Open n to calcul and convert string to int 
archive = open("n.txt", "r")
inverter = archive.read()
z = inverter
n = int(z)
#Open key and convert string to int
#Abre a chave e convert string para int
archive = open("key.txt", "r")
inverse = archive.read()
d = int(inverse)

while True:
    instructions = input("Sua mensagem criptografada foi salva em 'message.txt'\n'Digite S para sair.")
    if instructions.lower() == 's':
        break



original = decodar(message,n,d)#message descipher #mensagem descifrada.
mensagem = juntar(original)#join message #junta a mensagem
archive = open("Message.txt", "w")
archive.write(str(mensagem))
archive.close()
print(original)
print(mensagem)