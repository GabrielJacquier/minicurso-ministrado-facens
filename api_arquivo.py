# -*- coding: utf-8 -*-

import json


def ler_usuarios():
    usuarios = []
    arquivo = open('bd_usuarios.txt', 'r')
    conteudo = arquivo.read()
    arquivo.close()
    if conteudo:
        usuarios = json.loads(conteudo)
    return usuarios

def escrever_usuario(usuario):
    usuarios = ler_usuarios()
    usuarios.append(usuario)
    arquivo = open('bd_usuarios.txt', 'w')
    arquivo.write(json.dumps(usuarios))