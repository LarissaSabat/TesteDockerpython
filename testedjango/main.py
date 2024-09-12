def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao mundo do Docker com Python!")

def soma(a, b):
    return a + b

if __name__ == "__main__":
    # Chama a função de saudação
    saudacao("Usuário")

    # Faz uma operação simples de soma
    resultado = soma(3, 5)
    print(f"A soma de 3 e 5 é: {resultado}")
