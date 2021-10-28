def ler_entrada():
    linhas = open('entrada.txt', 'r').readlines()
    entrada_arquivo = prepara_entrada(linhas)
    return entrada_arquivo


def prepara_entrada(linhas=[]):
    entrada_arquivo = list()
    for caractere in linhas[0]:
        entrada_arquivo.append(caractere)
    entrada_arquivo.append('$')
    return entrada_arquivo


def algoritmo(entrada=[], pilha=[], tabela_m=dict()):
    leitura_pilha = pilha.pop(0)
    leitura_entrada = entrada[0]

    if leitura_pilha == '$':
        if leitura_entrada != '$':
            print(f'Erro sintático. Caractere {leitura_entrada} não esperado.')  # finaliza com erro
    elif leitura_entrada == leitura_pilha:  # match
        entrada.pop(0)
        algoritmo(entrada, pilha, tabela_m)
    elif leitura_entrada not in terminais:  # símbolo desconhecido
        print(f'Caractere {leitura_entrada} desconhecido')
    elif leitura_pilha in variaveis and leitura_entrada in terminais:  # existe transição
        transicoes = tabela_m[leitura_pilha]
        resultado = transicoes[leitura_entrada]

        if resultado == erro or resultado == sync:
            print(f'Erro sintático, caractere {leitura_entrada} não esperado.')
            entrada.pop(0)
            algoritmo(entrada, pilha, tabela_m)
        else:
            for caractere in resultado[::-1]:
                pilha.insert(0, caractere)
            algoritmo(entrada, pilha, tabela_m)


# caractere de sincronização = %; caractere de erro = #;
sync = '%'
vazio = ''
erro = '#'

tabela = {
    'E': {
        '(': 'TY',
        ')': erro,
        'a': erro,
        'i': 'TY',
        'o': erro,
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
        '(': erro,
        ')': erro,
        'a': 'aFJ',
        'i': erro,
        'o': vazio,
        '$': vazio
    },
    'T': {
        '(': 'FJ',
        ')': erro,
        'a': erro,
        'i': 'FJ',
        'o': sync,
        '$': sync
    },
    'Y': {
        '(': erro,
        ')': erro,
        'a': erro,
        'i': erro,
        'o': 'oTY',
        '$': vazio
    }
}

terminais=[')', '(', 'a', 'i', 'o', '$']
variaveis=['E', 'F', 'J', 'T', 'Y']

entrada_parser = ler_entrada()  # io(i)$, ia(i)$, ((i))$, (i)$, (i)a(i)$

algoritmo(ler_entrada(),
          ['E', '$'],
          tabela)
