# calculo imc
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.3f}")
if imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
else:
    print("Acima do peso normal")
