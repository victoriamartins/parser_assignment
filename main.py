def algoritmo(entrada=[], pilha=[], tabela_m=dict()):
    if len(pilha) == 0 and entrada[0] == '$':
        print('TERMINOU')
        return

    leitura_entrada = entrada[0]
    leitura_pilha = pilha.pop(0)
    if leitura_entrada == leitura_pilha:
        entrada.pop(0)
        return algoritmo(entrada, pilha, tabela_m)
    else:
        transicoes = tabela_m[leitura_pilha]
        try:
            resultado = transicoes[leitura_entrada]
            for variavel in resultado[::-1]: # coloca as variaveis na pilha
                pilha.insert(0, variavel)
            return algoritmo(entrada, pilha, tabela_m)
        except NameError:
            print('Erro sintático.')


# caractere de sincronização é representado por %
sync = '%'
vazio = ''
tabela = {
    'E': {
        '(': 'TY',
        'i': 'TY',
        '$': sync
    },
    'F': {
        '(': '(F)',
        ')': sync,
        'a': sync,
        'i': 'i',
        'o': sync,
        '$': sync
    },
    'J': {
        'a': 'aFJ',
        'o': vazio,
        '$': vazio
    },
    'T': {
        '(': 'FJ',
        'i': 'FJ',
        'o': sync,
        '$': sync
    },
    'Y': {
        'o': 'oTY',
        '$': vazio
    }
}

entrada_lista = list()
entrada_parser = 'io(i)$'
for i in entrada_parser:
    entrada_lista.append(i)

algoritmo(entrada_lista, ['E'], tabela)
