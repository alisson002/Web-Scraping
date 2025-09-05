from pathlib import Path
import os # biblioteca para manipulação de caminhos

# Desafio: fazer uma função que retorna o tamanho de um arquivo em kbytes
def tamanho_arquivo(caminho_arquivo):
    # Verifica se o arquivo existe
    if not os.path.isfile(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo {caminho_arquivo} não foi encontrado.")
    
    # Retorna o tamanho do arquivo em KB
    return str(round(os.path.getsize(caminho_arquivo)/1000,2))+"KB"

# Encotra um arquivo e retorna o caminho completo
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

print(tamanho_arquivo(encontra_arquivo("exercicios", "py")))

# Desafio: fazer uma função que retorna o tamanho de um arquivo em MB
def tamanho_arquivo_mb(caminho_arquivo):
    # Verifica se o arquivo existe
    if not os.path.isfile(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo {caminho_arquivo} não foi encontrado.")
    
    # Retorna o tamanho do arquivo em MB
    return str(os.path.getsize(caminho_arquivo)/1000000)+"MB"


print(tamanho_arquivo_mb(encontra_arquivo("exercicios", "py")))

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
caminho_init = Path.home()
pasta_buscada = input("Qual a pasta que deseja verificar o tamanho?\n")
depth = input('Quantas camadas das pastas gostaria de verificar?\n')

def buscador():
    for pasta in caminho_init.glob('**/*'):
        if pasta.is_dir():
            if pasta_buscada.lower() in pasta.name.lower():
                diretorio = Path(pasta)
                print(diretorio)
                return diretorio
    return None

def retorno_tamanho():
    diretorio = buscador()
    if diretorio is None:
        print("Nenhum diretorio foi encontrado")
    else:
        for i in diretorio.glob('*'):
            if i.is_dir():
                soma = 0
                for file in i.glob('*'):
                    soma += os.path.getsize(file)
                print(f'{i.name} tem {round(soma / 1024 / 1024, 2)} Mb')
            elif i.is_file():
                soma = os.path.getsize(i)
                print(f'{i.name} tem {round(soma / 1024 / 1024, 2)} Mb)')

retorno_tamanho()