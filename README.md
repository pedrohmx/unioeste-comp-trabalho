# Trabalho de Compiladores - C-Mais-ou-Menos

Este repositório contém a especificação da linguagem de programação C+- (C-Mais-ou-Menos ou _C More or Less_) e o codigo fonte de seu compilador/interpretador.

## Espeficicações do trabalho

### 1.1 Requisitos para a especificação/implementação da LP

1. [ ] Caracterizar a LP a ser implementada.
   1. [X] Tipos de dados suportados (min 3).
   2. [X] Operadores suportados (aritméticos, lógicos e relacionais).
   3. [X] Formação dos identificadores (regras para nomes de variaveis).
   4. [X] Comandos para entrada e saida.
   5. [X] Palavras reservadas.
   6. [X] Estruturas suportadas pela linguagem.
   7. [ ] Estrutura geral do programa
2. [X] Especificar as **Definições Regulares** e os **Automata** de reconhecimento dos símbolos adminidos
3. [X] Descrever formalmente usando BNF, a GLC da linguagem proposta.
   1. [X] BNF
   2. [ ] GLC

### 1.2 Implementação de Analisador Léxico

> Implementar o analisador léxico da linguagem proposta na Parte 1.1 do trabalho.

**Objetivos:**

- [X] Dado um arquivo contendo um código fonte na linguagem proposta, o analisador deve realisar a análise léxica do programa;
- [X] A entrada deve ser um código na linguagem proposta e a saída deve ser o conjunto de tokens que compõe o programa;
- [ ] O analisador deve ser capaz de tratar possíveis erros e emitir as mensagens apropriadas;

### Entrega 1

1. [ ] Arquivo `.pdf` contendo os itens descritos em 1.1;
2. [ ] Código fonte do Analisador Léxico, com instruções para compilação e execução;
3. [ ] Exemplo de código fonte da linguagem especificada para teste do analisador;

## Instruções de uso

### Requisitos

- Interpretador python 3.10
  - Pacotes especificados em `src/requirements.txt`

### Como utilizar

>Para acessar a pagina de manual, execute o seguinte comando

```sh
python -m path/to/cml
```

>Tokenizar um arquivo de codigo fonte

```sh
python -m path.to.cml lex SOURCE
```
