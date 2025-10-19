from typing import Dict

MESES_NOMES = (
    "Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"
)

def calcular_novo_custo_medio(estoque_inicial: float, custo_medio_ant: float,
                              producao: float, custo_unitario: float) -> float:
    valor_total = estoque_inicial * custo_medio_ant + producao * custo_unitario
    qtd_total = estoque_inicial + producao
    return (valor_total / qtd_total) if qtd_total > 0 else custo_medio_ant

def fechar_mes(reg: Dict) -> Dict:
    cm = calcular_novo_custo_medio(
        reg.get('estoque_inicial',0.0),
        reg.get('custo_medio_anterior',0.0),
        reg.get('producao',0.0),
        reg.get('custo_unitario',0.0)
    )
    estoque_final = reg.get('estoque_inicial',0.0) + reg.get('producao',0.0) - reg.get('vendas_qtd',0.0)
    cmv = reg.get('vendas_qtd',0.0) * cm
    margem = reg.get('faturamento',0.0) - cmv
    preco_medio = (reg.get('faturamento',0.0) / reg.get('vendas_qtd',1.0)) if reg.get('vendas_qtd',0.0) else 0.0
    despesas = reg.get('despesas', 0.0)
    saldo_final = reg.get('faturamento',0.0) - despesas

    return {
        **reg,
        "custo_medio": cm,
        "estoque_final": estoque_final,
        "cmv": cmv,
        "margem_bruta": margem,
        "preco_medio": preco_medio,
        "saldo_final": saldo_final
    }
