import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def calcula_assinatura(texto):
	listaSentencas = separa_sentencas(texto)
	listaPalavraTextoUnico = []
	numeroTotalFrase = 0

	for sentenca in listaSentencas:
		listaFrases = separa_frases(sentenca)
  
		for frase in listaFrases:
			numeroTotalFrase += 1
			listaPalavras = separa_palavras(frase)
   
			for palavra in listaPalavras:
				listaPalavraTextoUnico.append(palavra)
	tamanhoPalavras = 0

	for palavra in listaPalavraTextoUnico:
		tamanhoPalavras += len(palavra)
	numeroTotalPalavras = len(listaPalavraTextoUnico)		
	tamanhoMedioPalavra = tamanhoPalavras / numeroTotalPalavras

	numeroPalavrasDiferentes = n_palavras_diferentes(listaPalavraTextoUnico)
	relacaoTypeToken = numeroPalavrasDiferentes / numeroTotalPalavras

	numeroPalavrasUmaVez = n_palavras_unicas(listaPalavraTextoUnico)
	razaoHpaxLegomana = numeroPalavrasUmaVez / numeroTotalPalavras

	tamanhoSentencas = 0
	for sentenca in listaSentencas:
		tamanhoSentencas += len(sentenca)
	numeroSentencas = len(listaSentencas)

	tamanhoMedioSentenca = tamanhoSentencas / numeroSentencas

	complexidadeSentenca = numeroTotalFrase / numeroSentencas

	tamanhoFrases = 0
	numeroFrases = 0
	for sentenca in listaSentencas:
		fraseList = separa_frases(sentenca)
		for frase in fraseList:
			tamanhoFrases += len(frase)
			numeroFrases += 1

	tamanhoMedioFrase = tamanhoFrases / numeroFrases
	
	return [tamanhoMedioPalavra, relacaoTypeToken, razaoHpaxLegomana,tamanhoMedioSentenca, complexidadeSentenca, tamanhoMedioFrase]


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    tracoLingustisco = 0
    for i, j in zip(as_a, as_b):
        tracoLingustisco += abs(i - j)
    similaridade = tracoLingustisco / 6
    return similaridade

def avalia_textos(listaTexto, assinaturaPadrao):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    listaAssinaturas = []

    for texto in listaTexto:
        assinaturaAluno = calcula_assinatura(texto)
        valorAssinatura = compara_assinatura(assinaturaPadrao, assinaturaAluno)
        listaAssinaturas.append(valorAssinatura)
    listaAssinaturasDesordenada = listaAssinaturas[:]
    listaAssinaturas.sort()
    menor = listaAssinaturas[0]

    for s in listaAssinaturasDesordenada:
        if (s == menor):
            p = listaAssinaturasDesordenada.index(s)
    return p + 1

assinaturaPadrao = le_assinatura()
listaTexto = le_textos()
m = avalia_textos(listaTexto, assinaturaPadrao)
print ("O autor do texto", m,"está infectado com COH-PIAH")