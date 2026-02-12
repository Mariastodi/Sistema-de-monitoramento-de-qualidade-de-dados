```markdown

Um pipeline em Python focado em Data Observability e Auditoria de Integridade. O objetivo desta ferramenta é interceptar e reportar anomalias em fluxos de dados financeiros ou governamentais antes que eles alimentem dashboards ou modelos de Machine Learning.

## Motivação
Dados brutos raramente são confiáveis. Erros de input manual, falhas de sensores ou inconsistências de sistema podem inserir ruído nas análises. Este projeto implementa uma camada de validação automatizada que foca em três pilares:
* Preenchimento - Integridade
* Consistência Lógica - Regras de Negócio
* Estabilidade Estatística - Detecção de Outliers

## Lógica de Implementação
A ferramenta executa uma auditoria técnica baseada em:

* Auditoria de Vacância: Varredura sistemática por valores nulos (`NaN`) que comprometem a densidade da base.
* Análise de Discrepância Estatística: Implementação do cálculo de desvio padrão para identificação de outliers. Registros são marcados para revisão, prevenindo que valores extremos distorçam médias e modelos preditivos.
* Validação de Regras de Negócio: Verificação de consistência temporal que impede a aceitação de registros com datas futuras em relação ao tempo real do sistema.

## Stack Tecnológica
* Python 3.12
* Pandas: Estruturação e manipulação vetorial de dados.
* NumPy: Suporte para cálculos matemáticos e estatísticos de alta performance.

## Como Utilizar

1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt


2. Execute o script para visualizar o relatório de auditoria:**
```bash
python main.py
