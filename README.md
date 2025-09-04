# Projeto de Manipulação de Arquivos e Caminhos em Python

Este projeto contém diversos scripts em Python que demonstram operações comuns de manipulação de arquivos e caminhos no sistema de arquivos, utilizando principalmente a biblioteca `pathlib` e o módulo `os`. Além disso, há uma estrutura de pastas com arquivos de texto que servem para exemplificar o uso dos scripts.

## Estrutura do Projeto

- `desafio.py`: Contém funções para obter o tamanho de arquivos em KB e MB, encontrar arquivos pelo nome e extensão, e calcular o tamanho de pastas específicas com profundidade configurável.
- `exercicios.py`: Script para encontrar arquivos dentro da pasta home do usuário, tanto especificando a extensão quanto sem especificá-la, demonstrando diferentes abordagens para busca de arquivos.
- `caminhos_absolutos.py`: (Arquivo presente, porém vazio ou não utilizado)
- `construindo_caminhos.py`: Demonstra como construir caminhos de forma portátil usando `pathlib.Path`, garantindo compatibilidade entre sistemas operacionais.
- `manipulando_caminhos.py`: Mostra como verificar se um caminho é absoluto, transformar caminhos relativos em absolutos, mudar o diretório atual, e extrair partes de um caminho (nome, extensão, diretório pai, etc).
- `retornando_conteudos.py`: Exemplifica como listar arquivos e pastas em diretórios, filtrar por extensão, verificar existência de caminhos, e distinguir arquivos de pastas.
- `primeira_pasta/`: Contém scripts similares aos do diretório raiz, organizados em subpastas para demonstração:
  - `construindo_caminhos.py`
  - `manipulando_caminhos.py`
  - `retornando_conteudos.py`
  - `segunda_pasta/`: Contém arquivos de texto (`arquivo1.txt`, `arquivo2.txt`, `arquivo3.txt`) usados para testes e exemplos.
- `destino1/`, `destino2/`, `destino3/`: Pastas contendo arquivos de texto (atualmente vazios ou não legíveis pelo sistema).

## Detalhes dos Scripts

### desafio.py

- Função `tamanho_arquivo(caminho_arquivo)`: Retorna o tamanho de um arquivo em kilobytes (KB).
- Função `tamanho_arquivo_mb(caminho_arquivo)`: Retorna o tamanho de um arquivo em megabytes (MB).
- Função `encontra_arquivo(nome_arquivo, extensao=None)`: Busca um arquivo pelo nome e extensão, retornando o caminho completo.
- Função `buscador()`: Busca uma pasta pelo nome a partir do diretório home do usuário.
- Função `retorno_tamanho()`: Calcula e imprime o tamanho dos arquivos e subpastas dentro da pasta buscada, até a profundidade especificada.

### exercicios.py

- Demonstra como encontrar arquivos dentro da pasta home do usuário, tanto especificando a extensão quanto não especificando.
- Contém funções para imprimir os caminhos dos arquivos encontrados.

### construindo_caminhos.py

- Demonstra a construção de caminhos usando `Path` para garantir portabilidade.
- Mostra exemplos de caminhos relativos e absolutos.
- Exibe caminhos para diretórios do usuário, como home, Documents e Repositórios.

### manipulando_caminhos.py

- Mostra como verificar se um caminho é absoluto.
- Demonstra como transformar caminhos relativos em absolutos.
- Explica como mudar o diretório atual do script.
- Mostra como extrair partes de um caminho, como nome do arquivo, extensão, diretório pai, raiz do sistema, etc.

### retornando_conteudos.py

- Exemplos de listagem de arquivos e pastas em diretórios.
- Filtragem por extensão.
- Verificação de existência de arquivos e pastas.
- Diferenciação entre arquivos e diretórios.

## Observações

- Os arquivos de texto presentes nas pastas `destino1`, `destino2`, `destino3` e `primeira_pasta/segunda_pasta` são utilizados para testes e exemplos, mas atualmente parecem estar vazios ou não contêm conteúdo legível.
- Alguns arquivos Python como `caminhos_absolutos.py` estão presentes, mas não possuem conteúdo.

---

Este projeto é útil para quem deseja aprender manipulação de arquivos e caminhos em Python de forma prática e didática, utilizando recursos modernos da biblioteca `pathlib` e funções do módulo `os`.
