from pathlib import Path
import os # biblioteca para manipulação de caminhos

#desenvolva um script para encontrar um arquivo dentro da pasta home do usuários
caminho = Path.home() # caminho da pasta home do usuário
print(caminho)
for arquivo in caminho.glob("**/*"): # percorre todos os arquivos e pastas dentro da pasta home do usuário
    if arquivo.is_file() and arquivo.name == "exercicios.py": # verifica se é um arquivo e se o nome é igual a "exercicios.py"
        print(arquivo) # imprime o caminho do arquivo
        

# para o caso de o arquivo sem especificar a extensão
# Desta forma, o script encontra o arquivo independente da extensão, mas em compensação pode demorar mais para encontrar o arquivo, pois ele irá verificar todos os arquivos dentro da pasta home do usuário, além disso pode encontrar mais de um arquivo com o mesmo nome, mas com extensões diferentes.
# Imprime todos os arquivos com o nome solicitado
for arquivo in caminho.glob("**/*"): # percorre todos os arquivos e pastas dentro da pasta home do usuário
    if arquivo.is_file() and arquivo.stem == "exercicios": # verifica se é um arquivo e se o nome (sem extensão) é igual a "exercicios"
        print(arquivo) # imprime o caminho do arquivo  
        
def encontra_meu_arquivo(caminho, nome_arquivo):
    for arquivo in caminho.glob("**/*"): # percorre todos os arquivos e pastas dentro da pasta home do usuário
        if arquivo.is_file() and arquivo.stem == nome_arquivo: # verifica se é um arquivo e se o nome é igual a "exercicios.py"
            print(arquivo) # imprime o caminho do arquivo

def encontra_arquivo(nome_arquivo, extensao=None):
    caminho = Path.cwd() # caminho da pasta home do usuário
    for arquivo in caminho.glob("**/*"): # percorre todos os arquivos e pastas dentro da pasta home do usuário
        if arquivo.is_file(): # verifica se é um arquivo
            if extensao: # se a extensão for especificada
                if arquivo.name == f"{nome_arquivo}.{extensao}": # verifica se o nome e a extensão são iguais
                    return arquivo # retorna o caminho do arquivo
            else: # se a extensão não for especificada
                if arquivo.stem == nome_arquivo: # verifica se o nome (sem extensão) é igual
                    return arquivo # retorna o caminho do arquivo
    return None # se não encontrar o arquivo, retorna None

# Testando as funções
encontra_meu_arquivo(Path.home(), "arquivo1")
print(encontra_arquivo("arquivo1", "txt"))
print(encontra_arquivo("arquivo1"))