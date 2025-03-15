# Leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

ptermo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))
décimo = ptermo + (10 - 1) * razão
# for c in range(10):
#     print(ptermo)
#     ptermo += razão

for c in range(ptermo, décimo + razão, razão):
    print(c, end=' -> ')

print("\n")
print('='*20)

