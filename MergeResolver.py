import os

arquivo = "nomedoarquivos"

if os.path.exists(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    novo_conteudo = []
    pular_linha = False

    for linha in linhas:
        if linha.startswith("<<<<<<<"):
            continue 
            
        if linha.startswith("======="):
            pular_linha = True
            continue
            
        if linha.startswith(">>>>>>>"):
            pular_linha = False
            continue

        if pular_linha == False:
            novo_conteudo.append(linha)

    with open(arquivo, "w", encoding="utf-8") as f:
        f.writelines(novo_conteudo)

    print("O arquivo foi limpo com sucesso")
else:
    print("Arquivo nao encontrado.")

saida = input("Aperte enter para fechar")