# Calculo de Bonus

---

## Objetivo

Este documento tem como objetivos descrever como calcular o bonus do salário.

---

## Execução do Serviço

- Digite seu nome

  - **Exemplo** - João
- Digite seu salário

  - **Exemplo** - 2000
- Digite o percentual em bonus recebido

  - **Exemplo**: 1.0 para 10%

---

## Retorno do Serviço

Apos preencher os campos acima, o sistema deve algo como:

``Olá João, o seu bonus foi de: 1630.0``

---

## Tratamento de Erros

Este serviço há o tratamento de erros, que serão descritos abaixo:

- O nome, só aceita caracteres de texto
- O nome, aceita com valores maior que zero
- O salário, só aceita valores numéricos
- O percentual recebido, só aceita valores numéricos
- Se for realizado mais de 5 tentativas com erro, o serviço será abortado

## Modularização da Tarefas

As tarefas foram separadas por módulos, com as seguintes tarefas:

- calcula_bonus
- valida_nome_usuario
- valida_salario
- valida_status_bonus_salario
- processar_validacoes