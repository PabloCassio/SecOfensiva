import socket
url = str(input("Digite a url que deseja scannear: "))
print ("Meu primeiro scanner de porta")
print (" O alvo será " , url)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
porta=80
c = s.connect_ex((str(url),int(porta)))
if c == 0:
print ("Porta ",n,": Aberta")
else:
print ("Porta ",n,": Fechada")
