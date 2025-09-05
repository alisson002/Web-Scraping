from pathlib import Path

# criamos dessa forma para garantir que o código funcione em qualquer sistema operacional
caminho = Path("primeira_pasta") #caminho para a primeira pasta

#usa o caminho completo tem mais garantia de que o código funcione, mas perde a portabilidade.
#caminho = Path("C:\\Users\\Alisson - Financeiro\\Documents\\Repositórios\\Web-Scraping\\primeira_pasta") #caminho completo

caminho2 = Path("primeira_pasta/segunda_pasta") #caminho para a segunda pasta

print(caminho)
print(caminho2)

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    #nesse caso a barra é utilizada para concatenar caminhos
    caminho_arquivo = caminho / nome #criando o caminho completo para cada arquivo
    print(caminho_arquivo)

#DIRETORIO HOME

print(Path.home()) #caminho para o diretório home do usuário
print(Path.home() / "Documents") #caminho para a pasta Documents do usuário
print(Path.home() / "Documents" / "Repositórios") #caminho para a pasta Repositórios do usuário