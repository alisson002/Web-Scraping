# Projeto de Aprendizado de Web Scraping com Python

Este projeto é dedicado ao aprendizado de web scraping utilizando Python. Ele inclui scripts e exemplos práticos que demonstram técnicas fundamentais de manipulação de arquivos e caminhos, essenciais para organizar e processar dados extraídos da web. Utilizamos principalmente as bibliotecas `pathlib` e `os` para operações no sistema de arquivos, preparando o terreno para aplicações de web scraping mais avançadas.

## Estrutura do Projeto

O projeto está organizado em pastas temáticas, cada uma focada em aspectos específicos do aprendizado:

- **`caminhos/`**: Contém scripts para manipulação de caminhos e arquivos, fundamentais para gerenciar dados coletados via web scraping.
  - `arquivo_primeira_pasta.txt`: Arquivo de exemplo para testes.
  - `caminhos_absolutos.py`: Script para trabalhar com caminhos absolutos (atualmente vazio ou em desenvolvimento).
  - `construindo_caminhos.py`: Demonstra como construir caminhos de forma portátil usando `pathlib.Path`.
  - `desafio.py`: Inclui funções para calcular tamanhos de arquivos, buscar arquivos por nome/extensão e explorar pastas.
  - `exercicios.py`: Exemplos práticos de busca de arquivos no diretório home do usuário.
  - `manipulando_caminhos.py`: Mostra operações como verificar caminhos absolutos, transformar relativos em absolutos e extrair partes de caminhos.
  - `primeira_pasta/`: Subpasta com scripts similares e arquivos de exemplo.
    - `arquivo_primeira_pasta.txt`
    - `caminhos_absolutos.py`
    - `construindo_caminhos.py`
    - `manipulando_caminhos.py`
    - `retornando_conteudos.py`: Exemplifica listagem e filtragem de conteúdos em diretórios.
    - `segunda_pasta/`: Contém arquivos de texto para testes (`arquivo1.txt`, `arquivo2.txt`, `arquivo3.txt`).

- **`copiando e movendo arquivos/`**: Foca em operações de cópia e movimentação de arquivos, úteis para organizar dados extraídos.
  - `retornando_conteudos.py`: Script para listar e manipular conteúdos.
  - `texto.txt`: Arquivo de exemplo.
  - `destino1/`, `destino2/`, `destino3/`: Pastas de destino com arquivos de texto para demonstração de cópias.

## Detalhes dos Scripts Principais

### caminhos/desafio.py
- Funções para obter tamanhos de arquivos (KB/MB), buscar arquivos por nome/extensão e calcular tamanhos de pastas com profundidade configurável.

### caminhos/exercicios.py
- Exemplos de busca de arquivos no diretório home, com ou sem especificação de extensão.

### caminhos/construindo_caminhos.py
- Construção de caminhos portáteis usando `pathlib`, essenciais para compatibilidade em diferentes sistemas.

### caminhos/manipulando_caminhos.py
- Verificação e manipulação de caminhos (absolutos/relativos), extração de partes e mudança de diretório.

### caminhos/retornando_conteudos.py
- Listagem de arquivos/pastas, filtragem por extensão e verificação de existência.

### copiando e movendo arquivos/retornando_conteudos.py
- Similar ao acima, focado em operações de cópia e movimentação.

## Observações

- Os arquivos de texto nas pastas são usados para testes práticos, simulando dados que poderiam ser extraídos via web scraping.
- Alguns scripts podem estar em desenvolvimento ou vazios, como `caminhos_absolutos.py`.
- Este projeto serve como base para aprender web scraping, combinando manipulação de arquivos com técnicas de extração de dados da web.

---

Este repositório é ideal para iniciantes em Python interessados em web scraping, oferecendo uma abordagem prática e gradual para dominar as habilidades necessárias.
