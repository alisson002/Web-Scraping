from pathlib import Path
import os # biblioteca para manipulação de caminhos

print(Path.cwd())  # Mostra o diretório atual

#este caminho é absoluto? sim
print(Path.cwd().is_absolute())

# retornando o caminho da primieria pasta
print(Path("primeira_pasta"))

#este caminho é absoluto? não
print(Path("primeira_pasta").is_absolute())

# transformando o caminho em absoluto
print(Path.cwd() / "primeira_pasta")
print("Olha aqui!")
print((Path.cwd() / "primeira_pasta").exists())  # Verifica se o caminho existe

#chdir = change directory
#serve para o caso de você querer mudar o diretório atual
os.chdir(Path.home())  # muda o diretório atual para o diretório home do usuário

#o que aconteceu aqui foi que o diretório atual mudou e nesse caso o caminho relativo "primeira_pasta" não existe para novo diretório atual
print(Path.cwd())  # Mostra o diretório atual
print(Path.cwd() / "primeira_pasta")
print("Olha aqui!")
print((Path.cwd() / "primeira_pasta").exists())  # Verifica se o caminho existe

#garantindo que estamos retornando o caminho para a pasta script
#criando caminho absoluto
print(__file__) #o que o file faz é retornar todo o caminho para o arquivo que estou rodando nesse momento. Sempre vai me da o caminho completo para o arquivo ao qual estou usando-o.
print(Path(__file__)) #transformando em um objeto Path, mas não modifica o caminho, apenas adiciona as suas funcionalidades que são: "criamos dessa forma para garantir que o código funcione em qualquer sistema operacional"
print(Path(__file__).is_absolute()) #verificando se o caminho é absoluto
print(Path(__file__).parent) #retorna o diretório onde este arquivo está contido

#então se eu quero o caminho absoluto para a pasta onde este arquivo está, eu faço:
print(Path(__file__).parent / "primeira_pasta") #caminho absoluto para a pasta primeira_pasta

print((Path(__file__).parent / "primeira_pasta").exists()) #verificando

#trabalhando com partes de caminho
caminho_Arquivo = Path(__file__)

print(caminho_Arquivo)
print(caminho_Arquivo.anchor) #retorna a raiz do sistema de arquivos, pasta do disco.
print(caminho_Arquivo.parent) #retorna o diretório onde este arquivo está contido
print(caminho_Arquivo.parent.parent) #retorna o diretório pai do diretório onde este arquivo está contido
print(caminho_Arquivo.name) #retorna o nome do arquivo com a extensão
print(caminho_Arquivo.stem) #retorna o nome do arquivo sem a extensão
print(caminho_Arquivo.suffix) #retorna a extensão do arquivo
print(caminho_Arquivo.drive) #retorna a letra do drive (apenas no Windows)

print(caminho_Arquivo.parents[0]) #retorna o diretório pai do diretório onde este arquivo está contido, o numero representa o numero de pastas que retorna.


