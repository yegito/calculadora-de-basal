def imc_or_basal():
    escolha = input("Você quer calcular IMC ou BASAL?")
    
    if escolha.upper == "IMC" or "imc":
        calcular_imc()
    else:
        calculadora_basal()
      
        
def calcular_imc():
    name = input("Olá meu nobre internalta, qual o seu nome? ")
    print(f"Então vamos lá {name}! ")
    peso = int(input(f"{name} qual o seu peso? "))
    altura = int(input(f"Já temos o seu peso {name}, agora só falta sua altura. qual a sua altura? "))
    
    altura_imc = altura * altura
    
    imc = peso / altura_imc
    
    print(f"Seu IMC é {imc}")
    

def calculadora_basal():
    name = input("Olá meu nobre internalta, qual o seu nome? ")
    print(f"Então vamos lá {name}! ")
    idade = int(input(f"Qual a sua idade {name}? "))
    peso = int(input(f"{name} qual o seu peso? "))
    altura = int(input(f"Já temos sua idade e seu peso {name}, agora só falta sua altura. qual a sua altura? "))

    basalpeso = 13.7 * peso
    basalaltura = 5 * altura
    basalidade = 6.8 * idade

    basal = 66 + basalpeso + basalaltura - basalidade

    print(f"Seu basal é {basal}")
    print(f"Seu corpo consome {basal} calorias diariamente só para se manter")
    
    
def recalcular():
    while True:
        print("Você quer calcular seu Basal novamente? ")
        recal = input("Aperte Y para sim e N para não! ")
        if recal.upper() == "Y":
             calculadora_basal()
        else:
             print("até mais!")
             break
         
    
    
    
imc_or_basal()