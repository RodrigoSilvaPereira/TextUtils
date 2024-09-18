# RodrigoTextutils

`RodrigoTextutils` é um pacote Python desenvolvido para fornecer ferramentas simples de manipulação e análise de texto. Este projeto tem como objetivo facilitar operações básicas de processamento de texto, como inverter strings, capitalizar palavras e contar palavras e sentenças.

## Sobre o Projeto

O `RodrigoTextutils` foi criado como um exercício para praticar a criação e publicação de pacotes Python. O processo envolveu a criação do código-fonte, a configuração dos arquivos necessários para a construção do pacote e a publicação em um repositório de pacotes.

### O que foi Feito:

1. **Desenvolvimento do Pacote:**
   - **Código-Fonte:** Foram implementadas funções para manipulação de texto, incluindo `reverse_string`, `capitalize_words`, `word_count` e `sentence_count`.
   - **Estrutura do Pacote:** Organizou-se a estrutura do projeto para seguir as melhores práticas de desenvolvimento de pacotes Python. Isso incluiu a criação de arquivos como `__init__.py` e módulos Python.

2. **Configuração do Pacote:**
   - **`setup.py`:** Configurado para especificar as informações do pacote, incluindo nome, versão, autor e dependências.
   - **`requirements.txt`:** Listagem de dependências do projeto para facilitar a instalação e garantir um ambiente consistente.

3. **Publicação do Pacote:**
   - **TestPyPI:** O pacote foi publicado no TestPyPI para testar a instalação e o funcionamento antes da publicação final. TestPyPI é um repositório de pacotes Python usado para testar pacotes.
   - **PyPI:** O pacote será eventualmente publicado no repositório PyPI oficial, tornando-o disponível para a comunidade Python.

## Funcionalidades

O pacote `RodrigoTextutils` oferece as seguintes funcionalidades:

- **Inverter Strings:** Inverte o texto fornecido.
- **Capitalizar Palavras:** Converte o texto para que cada palavra comece com uma letra maiúscula.
- **Contar Palavras:** Conta o número total de palavras em um texto.
- **Contar Sentenças:** Conta o número total de sentenças em um texto, considerando pontos finais, interrogações e exclamações.

## Installation

Para instalar o pacote `RodrigoTextutils`, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) e especifique o índice do TestPyPI:

```bash
pip install -i https://test.pypi.org/simple/ RodrigoTextutils
