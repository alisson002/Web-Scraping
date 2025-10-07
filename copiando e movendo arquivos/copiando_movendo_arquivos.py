from pathlib import Path
import shutil # Biblioteca para operações com arquivos e coleções de arquivos. É counstruida em cima do os.
import os

# Copiando arquivos com copyfile
# O copyfile copia apenas o conteúdo do arquivo, não copia os metadados (permissões, timestamps, etc). Como por exemplo permissão de ADM, leitura, escrita e execução.
pasta_atual = Path(__file__).parent # pasta atual
caminho_arquivo = pasta_atual / "texto.txt" # caminho do arquivo a ser copiado

caminho_arquivo_destino = pasta_atual / "destino1" / "texto.txt" # caminho do arquivo de destino1

shutil.copyfile(caminho_arquivo, caminho_arquivo_destino) # copia o arquivo para o destino1

# Copiando arquivos com copy
# Nesse caso o copy copia o conteúdo do arquivo e permissões.
# Além disso, o copy permite copiar arquivos e renomeá-los ao mesmo tempo. Não é preciso também mostrar caminho_arquivo_destino como acima, apenas a pasta de destino.
pasta_atual = Path(__file__).parent # pasta atual
caminho_arquivo = pasta_atual / "texto.txt" # caminho do arquivo a ser copiado

caminho_pasta_destino = pasta_atual / "destino2" # caminho do arquivo de destino1

shutil.copy(caminho_arquivo, caminho_pasta_destino) # copia o arquivo para o destino2

# Copiando arquivos com copy2
# O copy2 copia o conteúdo do arquivo e todos os metadados (permissões, timestamps, etc).
pasta_atual = Path(__file__).parent # pasta atual
caminho_arquivo = pasta_atual / "texto.txt" # caminho do arquivo a ser copiado

caminho_pasta_destino = pasta_atual / "destino3" # caminho do arquivo de destino1

shutil.copy2(caminho_arquivo, caminho_pasta_destino) # copia o arquivo para o destino2

# Movendo arquivos
pasta_atual = Path(__file__).parent # pasta atual
caminho_arquivo = pasta_atual / "textoMove.txt" # caminho do arquivo a ser copiado

caminho_pasta_destino = pasta_atual / "destino1" # caminho do arquivo de destino1

shutil.move(caminho_arquivo, caminho_pasta_destino) # move o arquivo para o destino1


pasta_atual = Path(__file__).parent # pasta atual
caminho_arquivo = pasta_atual / "textoMove2.txt" # caminho do arquivo a ser copiado

caminho_arquivo_destino = pasta_atual / "destino2" / "textoMove2.txt" # caminho do arquivo de destino1

shutil.move(caminho_arquivo, caminho_arquivo_destino) # move o arquivo para o destino1

# Deletando arquivos
pasta_atual = Path(__file__).parent # pasta atual
caminho_arquivo = pasta_atual / "texto copia.txt" # caminho do arquivo a ser deletado
caminho_arquivo_destino = pasta_atual / "destino1" / "texto copia.txt" # caminho do arquivo de destino1