# Trabalho 1 de EDA 2 - Busca

Coloco algumas anotações minhas de estudo em um [MkDocs público](https://github.com/Raphides/cybersecurity) e tenho a vontade de adicionar perguntas e respostas (QAs) de concursos. Julguei esta como uma ótima oportunidade de aplicar um algorítmo de busca. A ideia é buscar e extrair, para cada página, QAs armazenadas no respositório e por fim imprimí-las nas páginas.

Esse projeto portanto serve como uma Prova de Conceito (PoC). A ideia não é encher de páginas reais, inserir uma impressão satisfatória na página e nem lotar a coleção de QAs. A intenção é só uma:

* Buscar QAs para cada página.

Para isso, utiliza-se a seguinte estratégia:

1. Leitura do CSV.
2. Criação de um Índice por categorias
3. Para cada página (correspondente a uma categoria):
    1. Acessar índice da categoria
    2. Inserir todas as questões da categoria.

Logo, utiliza-se a estratégia de **Busca Sequencial Indexada** para fazer um filtro mais veloz.

É garantido que todas as questões de uma mesma categoria estarão juntas no CSV.

## Como rodar localmente

* Clone o projeto localmente
* Instale Python3 e Mkdocs
* Instale as bibliotecas do `requirements.txt`
* Execute na pasta raiz do projeto:

```bash
mkdocs serve
```