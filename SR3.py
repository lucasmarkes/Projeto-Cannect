registros = {}
score_board = {}
opcao_info = 0
opcao = 0
STS_caneca = {1: "Clean", 2: "Clean", 3: "Clean", 4: "Clean", 5: "Clean", 6: "Clean", 7: "Clean", 8: "Clean",
              9: "Clean", 10: "Clean", 11: "Clean", 12: "Clean", 13: "Clean", 14: "Clean", 15: "Clean", 16: "Clean",
              17: "Clean", 18: "Clean", 19: "Clean", 20: "Clean"}


def pontuacao_time():
    soma_time_1 = 0
    soma_time_2 = 0

    for x in registros:
        if registros[x][1] == "Gato":
            soma_time_1 = soma_time_1 + registros[x][2]

        if registros[x][1] == "Cachorro":
            soma_time_2 = soma_time_2 + registros[x][2]

    print("=-" * 30)
    print("Gato vs Cachorro")
    print(" {}        {} ".format(soma_time_1, soma_time_2))
    print("=-" * 30)


def adicionar_caneca():
    quant = int(input("Quantas canecas deseja adicionar ? "))
    while quant != 0:
        i = len(STS_caneca)
        STS_caneca[i + 1] = "Clean"
        quant -= 1


def mostrar_perfil():
    print("=-" * 30)
    print("Seus dados")
    print("Nome: {}".format(nome_login))
    print("ID: {}".format(ID))
    print("Time: {}".format(registros[ID][1]))
    print("CP: {}".format(registros[ID][2]))
    print("XP: {}".format(registros[ID][4]))
    print("=-" * 30)


def atrib_pont_XP_penalidade():
    cp = -50
    registros[ID][2] = registros[ID][2] + cp

def atrib_pont_XP_devolucao():
    cp = 100
    xp = 100

    registros[ID][4] = registros[ID][4] + xp
    registros[ID][2] = registros[ID][2] + cp


def atrib_pont_XP_report():
    cp = 50
    xp = 100
    registros[ID][4] = registros[ID][4] + xp
    registros[ID][2] = registros[ID][2] + cp


while opcao != -1:

    # INTRODUÇÃO
    print("\n" * 2)
    print("=-" * 30)
    print("|", " " * 16, "BEM VINDO AO CANNECT", " " * 17, "|")
    print("=-" * 30)
    print("\n1 - CANNECTAR")
    print("2 - Informações")
    print("3 - Registrar Usuário")
    print("-1 - Para finalizar o programa\n")
    # Para teste : 4 - CONSULTAR DICIONARIO
    # '''  ''''' : 5 - ADICIONAR CANECAS

    opcao = int(input("Escolhe uma das opções acima: "))

    if opcao == 1:

        # AREA DE LOGIN
        print("\n" * 2)
        print("=-" * 30)
        print("|", " " * 21, "CANNECTE-SE", " " * 21, "|")
        print("=-" * 30)
        ID = input("\nDigite seu ID para CANNECTAR: ")
        opcao_log = 0
        while opcao_log != -1:

            # VERIFICA SE O ID ESTÁ EM REGISTROS E, SE TRUE, ENTRA NA PRIMEIRA PAGINA DE LOGIN

            if ID in registros:

                nome_login = registros[ID][0]  # PEGA O NOME QUE ESTA CADASTRADO NO ID PARA DAR A MENSAGEM DE BEM VINDO

                print("\nBem Vindo(a), {}".format(nome_login))
                print("O que deseja fazer ?")
                print("1 - Pegar caneca")
                print("2 - Devolver caneca")
                print("3 - Report")
                print("4 - Meu perfil")
                print("5 - Placar dos times")

                opcao_log = int(input("Escolha uma das opções acima ou -1 para entrar em outra conta: "))

                # OPCÃO 1 --- PEGAR CANECA

                if opcao_log == 1:
                    # irá verificar o status da caneca apartir da numeração da caneca correspondente
                    # se limpa emitir uma mensagem de permissão para o uso
                    # se suja emitir um aviso dizendo que a caneca está suja
                    # se quebrada, escolher outra caneca
                    # se perdida, escolher outra caneca
                    n_caneca = 0
                    while n_caneca != -1:

                        n_caneca = int(input("Digite a numeração da caneca que deseja pegar: "))
                        limite_canecas = len(STS_caneca)

                        # VERIFICA SE A NUMERAÇÃO ESTÁ NO LIMITE DA BIBLIOTECA DE CANECAS(STS_CANECA)

                        if n_caneca > limite_canecas:
                            n_caneca = int(input("Erro, essa caneca não existe, digite outra: "))

                        status = STS_caneca[n_caneca]  # VÊ O STATUS DA CANECA, SE SUJA, LIMPA ...

                        if status == "Clean":
                            print("Parabéns, você pegou uma caneca, não se esqueça de lavar e devolver após o uso")
                            STS_caneca[n_caneca] = "Em Uso"
                            registros[ID][3] = 1  # Portando uma caneca
                            n_caneca = -1  # USADO PARA SAIR DO LOOP

                        if status == "Suja":
                            j = -1
                            opcao_suja = 2
                            while j != 0:
                                print("Essa caneca foi reportada por outro usuário como suja, por favor, se possível "
                                      "lave-a e use, obrigado!!")
                                opcao_suja = int(input("\nSe não quiser essa caneca digite 0 para pegá-la ou -1 para "
                                                       "pegar outra: "))
                                if opcao_suja == 0:
                                    registros[ID][3] = 1
                                    STS_caneca[n_caneca] = "Em uso"
                                    j = 0
                                    n_caneca = -1
                                    print("Parabéns, você pegou uma caneca, "
                                          "não se esqueça de lavar e devolver após o uso")

                                if opcao_suja == -1:
                                    print("Você foi redirecionado ao início, escolha outra caneca")
                                    continue

                        if status == "Quebrada":
                            n_caneca = int(input("Essa caneca foi quebrada, por favor, escolha outra: "))

                        if status == "Perdida":
                            print("Essa caneca está perdida, por favor, escolha outra: ")

                        if status == "Em Uso":
                            n_caneca = int(input("Essa caneca está em uso, por favor, escolha outra: "))

                # OPCÃO 2 --- DEVOLVER CANECA

                if opcao_log == 2:

                    print("DEVOLVER CANECA")
                    print("Após o usuário escanear o QR code na pia")
                    n_caneca = int(input("\nPor favor, digite a numeração da caneca que deseja devolver: "))
                    print("1 - Lavei a caneca e entreguei")
                    print("2 - Não lavei a caneca mas deixei na estante das canecas sujas")
                    opcao_devolucao = int(input("\nDigite uma das opções acima: "))

                    if opcao_devolucao == 1:
                        print("Obrigado por devolver e lavar a caneca")
                        print("Você recebeu 100 CP/XP pela sua boa conduta")
                        registros[ID][3] = 0
                        STS_caneca[n_caneca] = "Clean"
                        atrib_pont_XP_devolucao()

                    if opcao_devolucao == 2:
                        print("Que pena :(, você não pôde lavar a caneca, por favor, deixe-a no devido lugar")
                        print("Infelizmente você perderá 50 CP/XP por isso")
                        registros[ID][3] = 0
                        STS_caneca[n_caneca] = "Suja"
                        atrib_pont_XP_penalidade()

                # OPCAO 3 --- REPORTAR CANECA

                if opcao_log == 3:
                    # NA OPÇÃO 3 O USUÁRIO VAI DIZER O PROBLEMA, E O STATUS DA CANECA DIGITADA IRÁ SER REGISTRADA

                    opcao_report = 0

                    while opcao_report != -1:
                        print("ÁREA DE REPORT")
                        print("1 - Caneca suja")
                        print("2 - Caneca perdida")
                        print("3 - Caneca quebrada")
                        print("-1 - Para finalizar")

                        opcao_report = int(input("Que tipo de problema deseja reportar ? "))

                        if opcao_report == 1:
                            n_caneca = int(input("Digite a numeração da caneca que deseja reportar: "))
                            STS_caneca[n_caneca] = "Suja"
                            print("O CANNECT agradece o seu report :D")
                            print("{}, você recebeu 50 CP pelo report".format(nome_login))

                            atrib_pont_XP_report()

                        if opcao_report == 2:
                            n_caneca = int(input("Digite a numeração de caneca que deseja reportar: "))
                            print("O CANNECT agradece o seu report :D")
                            print("{}, você recebeu 50 CP pelo report".format(nome_login))

                            STS_caneca[n_caneca] = "Perdida"
                            atrib_pont_XP_report()

                        if opcao_report == 3:
                            n_caneca = int(input("Digite a numeração de caneca que deseja reportar: "))
                            print("{}, você recebeu 50 CP pelo report".format(nome_login))

                            STS_caneca[n_caneca] = "Quebrada"
                            atrib_pont_XP_report()

                    # montar um dicionario para verificar o status da caneca (se esta suja, limpa, suja ou quebrada)
                    # se a caneca nunca foi reportada ela é dada como limpa

                if opcao_log == 4:
                    mostrar_perfil()

                if opcao_log == 5:
                    pontuacao_time()

            else:
                print("ID não identificado no sistema, tente novamente")
                break

    # 2 CONCLUIDO
    if opcao == 2:

        while opcao_info != -1:

            print("1 - COMO DOAR CANECAS")
            print("2 - COMO USAR O CANECÁRIO")
            print("3 - COMO USAR O SITE")
            print("4 - JOGO DA VEZ")
            print("OU -1 para finalizar")

            opcao_info = int(input("Escolha a informação que você deseja consultar ou -1 para finalizar: "))

            if opcao_info == 1:
                print("Texto 1")

            elif opcao_info == 2:
                print("Texto 2")

            elif opcao_info == 3:
                print("Texto 3")

            elif opcao_info == 4:
                print("Texto 4")

            else:
                print("OPÇÃO INVÁLIDA")

        print("\nConsulta de informações concluída")

    # 3 CONCLUIDO
    elif opcao == 3:
        print("\n" * 2)
        print("=-" * 30)
        print("|", " " * 18, "ÁREA DE CADASTRO", " " * 19, "|")
        print("=-" * 30)
        nome = input("Digite seu nome: ")
        ID = input("Digite seu ID ou email CESAR (será usado como login): ")
        time = input("Qual seu time ? (Gato ou Cachorro): ")

        validacao_nome = nome.isalpha()  # verifica se apenas possui letras
        pontuacao = 0  # vai fazer parte dos dados dos usuários no dicionário, a partir da chave(ID)
        XP = 0
        status = 0  # Sem caneca
        if not validacao_nome:
            print("O NOME DEVE HAVER APENAS CARACTERES, TENTE NOVAMENTE")
            nome = input("Digite seu nome: ")
            validacao_nome = nome.isalpha()

        while time != "Gato" and time != "Cachorro":
            print("DIGITE UM TIME VÁLIDO, TENTE NOVAMENTE")
            time = input("Qual seu time ? (Gato ou Cachorro): ")

        registros[ID] = [nome, time, pontuacao, status, XP]

        print("USUARIO REGISTRADO COM SUCESSO")

    elif opcao == 4:

        print(registros)

    elif opcao == 5:
        print("ADICIONAR CANECAS")
        adicionar_caneca()

print("\n" * 2)
print("=-" * 30)
print("|", " " * 8, "OBRIGADO PELA SUA PRESENÇA NO CANNECT", " " * 8, "|")
print("=-" * 30)
