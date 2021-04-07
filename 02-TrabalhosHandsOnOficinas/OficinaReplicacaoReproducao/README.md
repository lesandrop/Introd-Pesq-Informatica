# Códigos da Replicação Científica

Este diretório apresenta os códigos da oficina de replicação e os dados brutos e finais.

## Artigo-base da replicação e análise replicada

O artigo [Volunteers' Engagement in Human Computation for Astronomy Projects](https://doi.org/10.1109/MCSE.2014.4) apresenta uma análise de atividades de voluntários em projetos de ciência cidadã, padrão de que uma minoria de voluntários contribui em muitos dias e uma maioria de voluntários contribui em poucos dias. Ela é materializada como resultado na Figura 3 do artigo. Nesse sentido, o objeto da oficina de replicação é replicar essa análise para o contexto do repositório de software ``react``. Ou seja,  busca-se responder à seguinte pergunta:  _no repositório ``react`` há uma minoria de programadores que contribui em muitos dias e uma maioria de programadores que contribui em poucos dias?_

## Fases da replicação e códigos associados

1. Coletar dados de cada commit feito no repositório. Código [``getCommits.py``](getCommits.py);
2. Para cada programador, calcular a quantidade de dias em que fez pelo menos um commit no repositório. Código [``getDays.py``](getDays.py)
3. Gerar o gráfico com mesma lógica (eixos X e Y) do artigo-base. Código[``graphActivity``](graphActivity.R)


## Dados usados coletados e gerados na replicação

Os dados brutos coletados por meio da API estão no arquivo [``data.data``](data.data), a coleta foi feita em 24/03/2021. Os dados finais, totalmente processados e prontos para serem exibidos no gráfico, estão no arquivo [``activity.data``](activity.data).

---
_Lesandro Ponciano (lesandrop at pucminas.br) - PUC Minas_