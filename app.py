from validation import ler_float, ler_str, ler_ano_mes
from services import fechar_mes
from storage_json import carregar_json, salvar_json, salvar_relatorio_txt, exportar_csv

ORACLE_ENABLED = False

def try_oracle_insert(res):
    global ORACLE_ENABLED
    if not ORACLE_ENABLED:
        return
    try:
        from db_oracle import inserir_mes
        ok = inserir_mes(res)
        if ok:
            print("[Oracle] Registro inserido com sucesso.")
    except Exception as e:
        print("[Oracle] Falha opcional (não bloqueia o MVP):", e)

def lancar_mes():
    print("\n--- Lançar/Fechar mês ---")
    ano_mes = ler_ano_mes()
    estoque_inicial = ler_float("Estoque inicial (qtd): ")
    producao = ler_float("Produção do mês (qtd): ")
    vendas_qtd = ler_float("Vendas do mês (qtd): ")
    faturamento = ler_float("Faturamento do mês (R$): ")
    custo_unitario = ler_float("Custo unitário da produção (R$): ")
    custo_medio_anterior = ler_float("Custo médio anterior (R$): ")
    despesas = ler_float("Despesas do mês (R$) [0 para pular]: ")

    reg = {
        "ano_mes": ano_mes,
        "estoque_inicial": estoque_inicial,
        "producao": producao,
        "vendas_qtd": vendas_qtd,
        "faturamento": faturamento,
        "custo_unitario": custo_unitario,
        "custo_medio_anterior": custo_medio_anterior,
        "despesas": despesas
    }

    resultado = fechar_mes(reg)
    dados = carregar_json()
    dados.append(resultado)
    salvar_json(dados)
    salvar_relatorio_txt(resultado)
    print("\nFechamento concluído e salvo em JSON/TXT.")
    try_oracle_insert(resultado)

def listar_json():
    dados = carregar_json()
    if not dados:
        print("Sem lançamentos ainda.")
        return
    print("\n=== HISTÓRICO (JSON) ===")
    for d in dados:
        print(f"{d['ano_mes']} | Est.Fim: {d['estoque_final']:.2f} | CMV: R$ {d['cmv']:.2f} | Margem: R$ {d['margem_bruta']:.2f}")

def exportar_csv_cmd():
    dados = carregar_json()
    exportar_csv(dados)

def mostrar_relatorio():
    try:
        with open("relatorio.txt","r",encoding="utf-8") as f:
            conteudo = f.read()
        print("\n=== RELATÓRIO TXT ===\n")
        print(conteudo if conteudo.strip() else "(Vazio)")
    except FileNotFoundError:
        print("relatorio.txt ainda não existe.")

def toggle_oracle():
    global ORACLE_ENABLED
    ORACLE_ENABLED = not ORACLE_ENABLED
    print("Oracle:", "Ativado" if ORACLE_ENABLED else "Desativado")

def menu():
    while True:
        print("\n1) Lançar/Fechar mês\n2) Listar histórico (JSON)\n3) Exportar CSV\n4) Mostrar relatório (TXT)\n5) Oracle: ligar/desligar\n6) Sair")
        op = ler_str("> ")
        if op == "1":
            lancar_mes()
        elif op == "2":
            listar_json()
        elif op == "3":
            exportar_csv_cmd()
        elif op == "4":
            mostrar_relatorio()
        elif op == "5":
            toggle_oracle()
        elif op == "6":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
