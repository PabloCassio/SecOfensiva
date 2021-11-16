import socket
url = str(input("Digite a url que deseja scannear: "))
print("Meu primeiro scanner de porta")
print(" O alvo será ", url)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
portas= [80, 8080, 443, 25, 20, 21, 3389, 1433, 3306]
for num in portas:
    c = s.connect_ex((str(url), int(num)))
    if c == 0:
        print("Porta ",num,": Aberta")
    else:
        print("Porta ",num,": Fechada")
