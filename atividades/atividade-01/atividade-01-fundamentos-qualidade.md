# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** [QUalidade De Software]
**Equipe:** Sozinho
**Data:** 22/09/2026

### Integrante

| Nome           | Usuário no GitHub |
| -------------- | ----------------- |
| Matheus Santos | [@Santos520]    |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** https://local-eats-unisenac.vercel.app/

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo      | Necessidade                                                          | Interessado | Consequência se não for atendida                                                                                         |
| --------- | -------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| Explícita | Permitir pesquisar restaurantes por culinária ou localização.        | Usuário     | O usuário não conseguirá encontrar restaurantes de acordo com o critério desejado.                                       |
| Explícita | Permitir filtrar restaurantes por categoria de culinária.            | Usuário     | O usuário terá dificuldade para restringir os restaurantes de acordo com a categoria desejada.                           |
| Implícita | Apresentar os resultados da pesquisa de forma clara e compreensível. | Usuário     | O usuário poderá ter dificuldade para interpretar os resultados e escolher um restaurante.                               |
| Implícita | Informar claramente quando nenhum restaurante for encontrado.        | Usuário     | O usuário poderá não entender o resultado da pesquisa ou interpretar a ausência de resultados como uma falha do sistema. |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim. Um sistema pode implementar todas as funcionalidades solicitadas e ainda apresentar baixa qualidade caso não atenda às necessidades implícitas dos usuários. Por exemplo, a pesquisa pode funcionar, mas se o sistema não informar claramente quando nenhum restaurante for encontrado, a experiência do usuário será prejudicada.

---

## 3. Tarefa 2: Exploração da aplicação

| Integrante     | Funcionalidade                                  | O que foi realizado                                                                                                                   | O que foi observado                                                                                                                                                                                                                                                                                                    | Evidência                                                                                                         |
| -------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Matheus Santos | Pesquisa e filtro de restaurantes por culinária | **Uso esperado:** foi selecionado o filtro **“Japonesa”**. **Uso alternativo:** foi realizada uma pesquisa pelo termo **“Italiana”**. | **Uso esperado:** ao selecionar o filtro “Japonesa”, o sistema apresentou restaurantes classificados como japoneses, incluindo **Restaurante Sabor 1, Restaurante Sabor 2 e Restaurante Sabor 11**. **Uso alternativo:** ao pesquisar “Italiana”, o sistema apresentou a mensagem **“Nenhum restaurante encontrado.”** | [filtro-japonesa.png](evidencias/filtro-japonesa.png) / [pesquisa-italiana.png](evidencias/pesquisa-italiana.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante     | Requisito de Qualidade                                                                                                                                                                                  | Característica ou subcaracterística | Justificativa                                                                                                                                                                                           | Como avaliar                                                                                                                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Matheus Santos | Ao pesquisar ou filtrar restaurantes por culinária, o sistema deve apresentar somente resultados compatíveis com o critério selecionado e informar claramente quando nenhum restaurante for encontrado. | Usabilidade                         | O requisito está relacionado à compreensão e utilização da funcionalidade pelo usuário. O usuário deve conseguir identificar os resultados correspondentes e compreender quando não existem resultados. | Selecionar uma categoria que possua restaurantes e verificar se os resultados apresentados correspondem ao filtro. Depois, realizar uma pesquisa sem correspondências e verificar se o sistema informa claramente que nenhum restaurante foi encontrado. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
ChatGPT.

**Como foi utilizada:**
Foi utilizada como apoio para organizar as respostas da atividade, revisar a redação e relacionar a funcionalidade observada no LocalEats aos conceitos de qualidade de software.

**Como as respostas foram verificadas:**
As respostas foram verificadas comparando-as com as orientações da atividade e com o comportamento observado diretamente na aplicação LocalEats. As evidências foram obtidas por meio de capturas de tela durante a exploração da aplicação. Os resultados descritos na Tarefa 2 correspondem aos comportamentos observados durante os testes realizados.

