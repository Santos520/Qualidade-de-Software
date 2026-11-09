# Atividade 4 – Testes Automatizados

**Responsável:** Matheus Souza dos Santos  
**Unidade Curricular:** Qualidade de Software  
**Projeto:** LocalEats  
**Feito:** Individual  
**Sistema testado:** LocalEats  
**URL:** https://local-eats-unisenac.vercel.app/static/index.html

## 1. Objetivo

O objetivo desta atividade foi desenvolver testes automatizados para verificar o funcionamento de uma regra de negócio do sistema LocalEats e automatizar uma interação na interface utilizando Playwright.

Foram utilizados testes unitários com pytest e um teste funcional com Playwright.

## 2. Regra de negócio escolhida

A regra escolhida foi a **Regra 2 – Cálculo de desconto**.

O comportamento esperado é:

- Pedidos com valor inferior a R$ 100,00 não recebem desconto.
- Pedidos com valor igual ou superior a R$ 100,00 recebem 10% de desconto.
- Valores negativos devem gerar um erro `ValueError`.

## 3. Implementação da regra

A função foi desenvolvida no arquivo `src/regras_localeats.py`, com o nome `calcular_desconto(valor_pedido)`.

Ela verifica o valor recebido e retorna o desconto correspondente. Também impede valores negativos por meio de uma exceção `ValueError`.

## 4. Testes unitários

Os testes foram desenvolvidos no arquivo `tests/test_regras_localeats.py`.

Foram realizados três testes:

- **Pedido com desconto:** verifica se um pedido de R$ 100,00 retorna R$ 10,00 de desconto.
- **Pedido sem desconto:** verifica se um pedido de R$ 50,00 retorna zero de desconto.
- **Valor negativo:** verifica se a função apresenta `ValueError` quando recebe um valor negativo.

Os testes foram executados utilizando pytest. Para verificar a exceção, foi utilizado `pytest.raises`.

## 5. Teste funcional com Playwright

O teste funcional foi desenvolvido no arquivo `tests/test_localeats.py`, com o nome `test_exibicao_formulario_cadastro`.

O fluxo automatizado realiza as seguintes etapas:

1. Acessa a página inicial do LocalEats.
2. Clica na opção "Criar Conta".
3. Verifica se o campo de nome está visível.
4. Verifica se o campo de e-mail está visível.
5. Verifica se o botão "Registrar" está visível.

O teste utiliza locators do Playwright e três assertions para verificar elementos reais da interface.

O navegador utilizado é o Chromium em modo headless.

## 6. TDD simplificado

**TDD de:** cálculo de desconto.

**Regra escolhida:** pedidos a partir de R$ 100,00 recebem 10% de desconto, pedidos abaixo desse valor não recebem desconto e valores negativos geram erro.

**Primeiro teste escrito:** verificar se um pedido de R$ 100,00 retorna R$ 10,00 de desconto.

**Red:** o objetivo dessa etapa é identificar o comportamento esperado por meio de um teste antes de considerar a implementação concluída. Não foi guardado um registro da execução inicial com falha, portanto não afirmo que essa falha foi observada.

**Green:** foi implementada a função `calcular_desconto(valor_pedido)` para atender à regra definida.

**Segundo teste escrito:** verificar se um pedido de R$ 50,00 não recebe desconto.

**Refactor:** foram mantidas condições simples e uma exceção para impedir valores negativos. Também foi criado um teste adicional para verificar esse comportamento, utilizando `pytest.raises`.

## 7. Tabela de identificação dos testes

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Matheus Souza dos Santos | Unitário | Pedido com desconto | `tests/test_regras_localeats.py::test_pedido_com_desconto` |
| TU02 | Matheus Souza dos Santos | Unitário | Pedido sem desconto | `tests/test_regras_localeats.py::test_pedido_sem_desconto` |
| TU03 | Matheus Souza dos Santos | Unitário | Valor negativo gera exceção | `tests/test_regras_localeats.py::test_valor_negativo` |
| TF01 | Matheus Souza dos Santos | Funcional | Exibição do formulário de cadastro | `tests/test_localeats.py::test_exibicao_formulario_cadastro` |

## 8. Explicação individual de um teste

O teste `test_pedido_com_desconto` verifica se a função calcula corretamente o desconto de um pedido de R$ 100,00.

O resultado esperado é R$ 10,00, correspondente a 10% do valor do pedido.

A verificação é realizada com `assert`, comparando o resultado da função com o valor esperado. O teste passou durante a execução do pytest.

## 9. Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT.

**Como foi utilizada:** a ferramenta foi utilizada como apoio para compreender a atividade, organizar os arquivos do projeto, desenvolver a função de cálculo de desconto e orientar a criação dos testes unitários e funcionais.

**Sugestão alterada:** inicialmente foi sugerido verificar o redirecionamento para a página inicial após o cadastro. Durante a execução, foi observado que o sistema permanecia na tela de login. Por isso, o teste foi adaptado para verificar a apresentação do formulário de cadastro e seus elementos visíveis.

**Verificação do código:** os testes foram executados localmente com pytest, e os seletores do formulário foram conferidos por meio da inspeção da interface e dos elementos HTML.

## 10. Tecnologias utilizadas

- Python 3.14.6
- pytest 9.2.0
- Playwright
- Chromium
- Visual Studio Code
- GitHub

## 11. Resultado da execução

A execução geral foi realizada com o comando:

`python -m pytest -v`

O projeto possui quatro testes automatizados:

- Teste funcional de exibição do formulário de cadastro.
- Teste unitário de pedido com desconto.
- Teste unitário de pedido sem desconto.
- Teste unitário de valor negativo.

**Resultado final:** 4 passed in 1.56s

O resultado completo da execução foi salvo no arquivo `relatorio-pytest.txt`, dentro da pasta `atividades/atividade-04/`.

## 12. Conclusão

A atividade permitiu praticar a criação de testes automatizados utilizando pytest e Playwright. Foi possível verificar uma regra de negócio relacionada ao cálculo de descontos e automatizar a apresentação do formulário de cadastro do LocalEats.

Os testes unitários verificam diferentes comportamentos da função de desconto, incluindo situações válidas e inválidas. O teste funcional verifica elementos reais da interface, utilizando interações e assertions.

A atividade também contribuiu para compreender a importância dos testes automatizados na identificação de problemas e na melhoria da qualidade de software.