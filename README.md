# Projeto de Aprendizado de Web Scraping com Python

Este projeto é dedicado ao aprendizado de web scraping utilizando Python. Ele inclui scripts e exemplos práticos que demonstram técnicas fundamentais de manipulação de arquivos e caminhos, essenciais para organizar e processar dados extraídos da web. Utilizamos principalmente as bibliotecas `pathlib` e `os` para operações no sistema de arquivos, preparando o terreno para aplicações de web scraping mais avançadas.

## Estrutura do Projeto

O projeto está organizado em pastas temáticas, cada uma focada em aspectos específicos do aprendizado de web scraping com Python:

- **`caminhos/`**: Contém scripts para manipulação de caminhos e arquivos, fundamentais para gerenciar dados coletados via web scraping.
  - `arquivo_primeira_pasta.txt`: Arquivo de texto simples usado como exemplo para testes de manipulação de arquivos.
  - `caminhos_absolutos.py`: Script introdutório para trabalhar com caminhos absolutos no sistema de arquivos (atualmente vazio ou em desenvolvimento).
  - `construindo_caminhos.py`: Demonstra como construir caminhos de forma portátil usando `pathlib.Path`, garantindo compatibilidade entre sistemas operacionais.
  - `desafio.py`: Inclui funções desafiadoras para calcular tamanhos de arquivos (KB/MB), buscar arquivos por nome/extensão e explorar pastas com profundidade configurável.
  - `exercicios.py`: Exemplos práticos de busca de arquivos no diretório home do usuário, com ou sem especificação de extensão.
  - `manipulando_caminhos.py`: Mostra operações avançadas como verificar se um caminho é absoluto, transformar relativos em absolutos, extrair partes de caminhos e mudar o diretório atual.
  - `primeira_pasta/`: Subpasta com scripts similares e arquivos de exemplo para aprofundar o aprendizado.
    - `arquivo_primeira_pasta.txt`: Arquivo de texto para testes básicos.
    - `caminhos_absolutos.py`: Versão localizada do script para caminhos absolutos.
    - `construindo_caminhos.py`: Versão localizada para construção de caminhos.
    - `manipulando_caminhos.py`: Versão localizada para manipulação de caminhos.
    - `segunda_pasta/`: Subpasta com arquivos de texto para testes avançados.
      - `arquivo1.txt`, `arquivo2.txt`, `arquivo3.txt`: Arquivos de exemplo para simulação de dados.

- **`copiando e movendo arquivos/`**: Foca em operações de cópia e movimentação de arquivos, úteis para organizar dados extraídos da web.
  - `retornando_conteudos.py`: Script para listar, filtrar e manipular conteúdos de diretórios, incluindo verificação de existência e diferenciação entre arquivos e pastas.
  - `texto.txt`: Arquivo de texto de exemplo usado para demonstrações de cópia e movimentação.
  - `destino1/`, `destino2/`, `destino3/`: Pastas de destino contendo cópias de arquivos para testes.

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

---

Este repositório é ideal para iniciantes em Python interessados em web scraping, oferecendo uma abordagem prática e gradual para dominar as habilidades necessárias.
