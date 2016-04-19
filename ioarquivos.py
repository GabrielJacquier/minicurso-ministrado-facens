def escrever(nome, conteudo):
    arquivo = open(nome, 'w')
    arquivo.write(conteudo)
    arquivo.close()
