tentativas_maxima: int = 5
tentativa: int = 1

while tentativa <= tentativas_maxima:
    print(f"Tentativa {tentativa} de {tentativas_maxima}. Se exceder o total de tentativas, a conexão será abortada.")
    try:
        # Validação Entradas
        validacao_nome_usuario: bool = False
        validacao_bonus_usuario: bool = False
        validacao_salario_usuario: bool = False

        # Constante valor de bonus
        valor_bonus: int = 1000
        
        # Entrada e validação nome
        nome_usuario: str = input("Insira seu nome: ")
        nome_usuario_formatado = nome_usuario.replace(" ", "").lower()
        if len(nome_usuario) == 0:
            print("Erro: O nome não pode estar vazio, tente novamente.")
        elif not nome_usuario_formatado.isalpha():
            print("Erro: O nome deve conter apenas letras, tente novamente.")
        else:
            validacao_nome_usuario: bool = True
        
        # Entrada e validação do salário
        salario_usuario: float = float(input("Insira seu salário: "))
        bonus_usuario: float = float(input("Insira o percentual de bônus recebido:(ex: 0.1 para 10%) "))
        if salario_usuario <= 0:
            print("Erro: O salário inserido é menor ou igual a zero, tente novamente.")
        elif bonus_usuario < 0:
            print("Erro: O bônus inserido é menor que 0, tente novamente")
        else:
            validacao_salario_usuario: bool = True
            validacao_bonus_usuario: bool = True
        # Validação das condições acima
        if validacao_nome_usuario and validacao_salario_usuario and validacao_bonus_usuario:
            resultado: bool = valor_bonus + salario_usuario * bonus_usuario
            print(f"Olá {nome_usuario}, o seu bônus foi de: {resultado:.2f}")
            break
        else:
            print("Erro: Tente novamente")
    except ValueError:
            print("Erro: Os valores devem conter somente números, tente novamente")

    except Exception as e:
            print(f"Erro inesperado: {e}, contate o suporte.")
    tentativa += 1
else:
    print("Número máximo de tentativas excedido. Encerrando o programa.")