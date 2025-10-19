import json, csv, datetime

def carregar_json(caminho="dados.json"):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Arquivo JSON corrompido. Iniciando com lista vazia.")
        return []

def salvar_json(dados, caminho="dados.json"):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def salvar_relatorio_txt(resultado, caminho="relatorio.txt"):
    now = datetime.datetime.now().isoformat(timespec="seconds")
    linhas = [
        f"[{now}] Fechamento {resultado['ano_mes']}",
        f"  Custo médio       : R$ {resultado['custo_medio']:.2f}",
        f"  Estoque final     : {resultado['estoque_final']:.2f}",
        f"  CMV               : R$ {resultado['cmv']:.2f}",
        f"  Margem bruta      : R$ {resultado['margem_bruta']:.2f}",
        f"  Preço médio venda : R$ {resultado['preco_medio']:.2f}",
        f"  Saldo caixa (mês) : R$ {resultado['saldo_final']:.2f}",
        "-"*40, ""
    ]
    with open(caminho, "a", encoding="utf-8") as f:
        f.write("\n".join(linhas))

def exportar_csv(dados, caminho="dados.csv"):
    if not dados:
        print("Sem dados para exportar.")
        return
    campos = sorted({k for d in dados for k in d.keys()})
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for d in dados:
            w.writerow(d)
    print(f"CSV gerado em {caminho}")
