# AgroFin — Controle Financeiro do Agronegócio (Capítulos 3–6)

**O que é:** um app de terminal em Python para registrar e fechar o mês financeiro de uma empresa de produção de matéria‑prima.  
**Atende ao enunciado:** subalgoritmos (funções), estruturas (lista/tupla/dict/tabela de memória), arquivos (TXT/JSON), e conexão Oracle (CRUD).

## Como rodar (MVP local)
1. `python -m venv .venv && source .venv/bin/activate` (Windows: `.venv\Scripts\activate`)
2. `pip install -r requirements.txt`
3. `python app.py`

> O app salva o histórico em `dados.json` e gera relatórios em `relatorio.txt`. Exporta CSV por menu.

## Banco Oracle (opcional, recomendado para a entrega)
1. Crie a tabela com `schema.sql` no seu Oracle.
2. Configure as credenciais no arquivo `config.json`:
   ```json
   {"user":"USUARIO","password":"SENHA","dsn":"HOST:PORT/SERVICE"}
   ```
3. No menu do app, ative a integração Oracle (opção 5) e teste inserções/listagens.

## Onde cada capítulo aparece
- **Cap. 3 (Subalgoritmos)**: `services.py`, `validation.py`, `storage_json.py`, `db_oracle.py` — funções com parâmetros e responsabilidades claras.
- **Cap. 4 (Estruturas)**: `services.py` usa `dict` para registros e `list[dict]` como “tabela de memória”; `tuplas` para constantes (ex.: meses).
- **Cap. 5 (Arquivos)**: `storage_json.py` lê/grava JSON; `relatorio.txt` em append com timestamp; exportação CSV.
- **Cap. 6 (Oracle)**: `db_oracle.py` com conexão `oracledb`, `inserir_mes`, `listar_meses`, `try/except` e commit/rollback.

## Menu
```
1) Lançar/Fechar mês
2) Listar histórico (JSON)
3) Exportar CSV
4) Mostrar relatório (TXT)
5) Oracle: habilitar/desabilitar e enviar dados
6) Sair
```

## Campos/saídas
Entrada por mês: `ano_mes`, `estoque_inicial`, `producao`, `vendas_qtd`, `faturamento`, `custo_unitario`, `custo_medio_anterior`, `despesas` (opcional).  
Cálculos: `custo_medio`, `estoque_final`, `cmv`, `margem_bruta`, `preco_medio`, `saldo_final` (caixa simples).

Images:
pexels-karolina-grabowska-4397820.jpg
sebastien-lavalaye-qJQRJAnFuTI-unsplash.jpg
marketingdigital_marketingsupervisor_seo_copywriting_ads_googleads_facebookads.jpg
