import random

x = "Gremio"

def funcao():
    global y
    y = "Flamengo"
    print(x)

funcao()

print(y)

x = str(1)
print(type(x))

y = int(x)
print(y)

teste = random.randint(1, 10)
print(teste)