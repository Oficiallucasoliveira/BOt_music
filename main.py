import os

links = list()

with open('links_musicas.txt','r') as arquivo:
	for linha in arquivo:
		linha = linha.replace('\n', '')
		if linha != '':
			links.append(linha)
for url in links:
	print (f'Baixando: (url)')

	comando = f'youtube-dl -x --audio-format mp3 {url}'
	os.system(comando)
