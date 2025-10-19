import json, os
import oracledb

def _load_config(path="config.json"):
    if not os.path.exists(path):
        raise FileNotFoundError("Arquivo config.json não encontrado. Crie com user/password/dsn.")
    with open(path, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    return cfg["user"], cfg["password"], cfg["dsn"]

def get_conn():
    user, password, dsn = _load_config()
    return oracledb.connect(user=user, password=password, dsn=dsn)

def inserir_mes(res):
    sql = """INSERT INTO MESES
      (ANO_MES, ESTOQUE_INICIAL, PRODUCAO, VENDAS_QTD, FATURAMENTO, CUSTO_UNITARIO,
       CUSTO_MEDIO_ANT, CUSTO_MEDIO, ESTOQUE_FINAL, CMV, MARGEM_BRUTA, PRECO_MEDIO)
      VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)"""
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, [
                    res.get("ano_mes"), res.get("estoque_inicial"), res.get("producao"),
                    res.get("vendas_qtd"), res.get("faturamento"), res.get("custo_unitario"),
                    res.get("custo_medio_anterior"), res.get("custo_medio"), res.get("estoque_final"),
                    res.get("cmv"), res.get("margem_bruta"), res.get("preco_medio")
                ])
            conn.commit()
        return True
    except Exception as e:
        print("[Oracle] Erro ao inserir:", e)
        return False

def listar_meses():
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT ANO_MES, ESTOQUE_FINAL, CMV, MARGEM_BRUTA FROM MESES ORDER BY ANO_MES")
                return cur.fetchall()
    except Exception as e:
        print("[Oracle] Erro ao listar:", e)
        return []
