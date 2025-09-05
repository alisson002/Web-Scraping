from pathlib import Path
import os # biblioteca para manipulação de caminhos

# Listando arquivos de uma pasta
print(os.listdir(Path.home())) # lista todos os arquivos e pastas na pasta home do usuário
print(os.listdir(Path.cwd())) # lista todos os arquivos e pastas no diretório atual
print(Path.cwd().glob("*"))  # Retorna um gerador com todos os arquivos e pastas no diretório atual. Uma forma de trasformar esse gerador em lista é:

print(list(Path.cwd().glob("*"))) # Lista todos os arquivos e pastas no diretório atual

# Listando arquivos de uma determinada extensão
print("_______________________________")
print(list(Path.cwd().glob("*.py")))

# Listar tudo dentro de uma pasta
print("_______________________________")
print(list(Path.cwd().glob("**/*"))) # Lista todos os arquivos e pastas no diretório atual e em todas as suas subpastas
print("_______________________________")
print(list(Path.cwd().glob("**/*.txt")))

# Validando caminhos
print(Path.home().exists()) # Verifica se o caminho existe

nao_existe = Path.home() / "nao_existe"
print(nao_existe.exists()) # Verifica se o caminho existe == False

# Verificando se é arquivo ou pasta
print(Path(__file__).is_file()) # Verifica se é arquivo == True pq __file__ é o arquivo atual

print(Path(__file__).parent.is_file()) # Verifica se é arquivo == False pq parent é a pasta que contém o arquivo atual
print(Path(__file__).parent.is_dir()) # Verifica se é pasta == True pq parent é a pasta que contém o arquivo atual

print(Path(__file__).is_dir()) # Verifica se é pasta == False pq __file__ é o arquivo atual
print(Path.home().is_dir()) # Verifica se é pasta == True pq home é uma pasta

