# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** Qualidade de Software
**Equipe:** Sozinho
**Data:** 22/09/2026

### Integrante

| **Nome**       | **Usuário no GitHub** |
| -------------- | --------------------- |
| Matheus Santos | @Santos520            |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| **Problema identificado**                                   | **Possível consequência para o produto ou para a equipe**                                             |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Falta de definição clara das responsabilidades de qualidade | Pode causar tarefas duplicadas ou atividades importantes sem responsável.                             |
| Testes realizados apenas após o desenvolvimento             | Pode aumentar a quantidade de defeitos encontrados no final do projeto e dificultar suas correções.   |
| Ausência de critérios de aceitação bem definidos            | Pode gerar diferentes interpretações sobre o comportamento esperado das funcionalidades do LocalEats. |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. A qualidade deve ser considerada durante todo o desenvolvimento do LocalEats. Mesmo quando existe um profissional de QA, desenvolvedores, analistas de requisitos e responsáveis pelo produto também devem contribuir para prevenir e identificar problemas. Como o projeto é individual, essas responsabilidades podem ser desempenhadas pela mesma pessoa em diferentes momentos do desenvolvimento.

---

## 3. Tarefa 2: Papéis e competências


| **Integrante** | **Papel analisado**    | **Responsabilidades relacionadas à qualidade**                                                                         | **Competências técnicas**                                            | **Competências comportamentais**                         |
| -------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------- |
| Matheus Santos | Analista de Requisitos | Definir e revisar requisitos, regras de negócio e critérios de aceitação do LocalEats.                                 | Levantamento de requisitos, documentação e análise de sistemas.      | Organização, comunicação e atenção aos detalhes.         |
| Matheus Santos | Desenvolvedor          | Implementar funcionalidades, corrigir defeitos e realizar testes unitários.                                            | Programação, Git, integração de APIs e testes.                       | Raciocínio lógico, organização e resolução de problemas. |
| Matheus Santos | QA/Testes              | Planejar e executar testes, registrar defeitos e verificar as correções.                                               | Testes funcionais, testes de sistema e elaboração de casos de teste. | Pensamento crítico, atenção aos detalhes e organização.  |
| Matheus Santos | Product Owner          | Priorizar funcionalidades, validar critérios de aceitação e verificar se as entregas atendem aos objetivos do produto. | Análise de requisitos, priorização e conhecimento do produto.        | Tomada de decisão, organização e visão de negócio.       |

---

## 4. Tarefa 3: Matriz de responsabilidades

Utilizei:

* **R:** responsável por executar a atividade;
* **A:** aprovador ou responsável final;
* **C:** consultado antes da execução ou decisão;
* **I:** informado sobre o resultado.

Como o projeto é individual, o mesmo integrante pode assumir diferentes papéis conforme a atividade.

| **Atividade de qualidade**            | **Analista de Requisitos** | **Desenvolvedor** | **QA/Testes** | **Product Owner** |
| ------------------------------------- | -------------------------- | ----------------- | ------------- | ----------------- |
| Definir critérios de aceitação        | R                          | C                 | C             | A                 |
| Revisar requisitos                    | R                          | C                 | C             | A                 |
| Implementar a funcionalidade          | C                          | R                 | I             | A                 |
| Revisar o código                      | I                          | R/A               | C             | I                 |
| Criar testes unitários                | I                          | R/A               | C             | I                 |
| Planejar e executar testes do sistema | C                          | C                 | R/A           | I                 |
| Registrar e acompanhar defeitos       | I                          | C                 | R/A           | I                 |
| Priorizar a correção dos defeitos     | C                          | C                 | C             | R/A               |
| Aprovar a disponibilização da versão  | C                          | C                 | C             | R/A               |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**

Por ser um projeto individual, existe uma concentração de responsabilidades na mesma pessoa. O mesmo integrante precisa atuar como desenvolvedor, responsável pelos testes, analista de requisitos e responsável pela validação do produto.

**Consequência:**

Essa concentração pode aumentar o risco de algum problema não ser identificado, pois não existe uma segunda pessoa para revisar as decisões ou validar o trabalho realizado. Por isso, é importante utilizar critérios de aceitação, testes e revisões sistemáticas durante o desenvolvimento.

### 4.2 Práticas de QA recomendadas

| **Prática recomendada**                                      | **Problema que ajuda a resolver**                                            | **Papéis envolvidos**                  |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------- | -------------------------------------- |
| Definição de critérios de aceitação antes do desenvolvimento | Reduz ambiguidades e facilita a validação das funcionalidades.               | Analista de Requisitos e Product Owner |
| Testes durante o ciclo de desenvolvimento                    | Ajuda a identificar defeitos antes da entrega final.                         | Desenvolvedor e QA                     |
| Revisão do próprio código                                    | Ajuda a identificar erros de implementação e melhorar a qualidade do código. | Desenvolvedor e QA                     |
| Registro e acompanhamento de defeitos                        | Evita que problemas encontrados sejam esquecidos ou permaneçam sem correção. | QA, Desenvolvedor e Product Owner      |

---

## 5. Uso de inteligência artificial

Ferramenta utilizada:

ChatGPT.

Como foi utilizada:

A ferramenta foi utilizada apenas como apoio para esclarecer dúvidas pontuais sobre os conceitos de qualidade de software e para revisar a organização do texto. A análise do LocalEats, a definição dos problemas, a escolha dos papéis, as responsabilidades e as práticas de QA foram realizadas por mim.

Como as respostas foram verificadas:

As sugestões apresentadas pela ferramenta foram analisadas e revisadas antes de serem utilizadas. O conteúdo final foi definido por mim com base nos conceitos apresentados nas aulas e nas características do projeto LocalEats.
