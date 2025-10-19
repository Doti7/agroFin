def ler_float(msg):
    while True:
        try:
            raw = input(msg).strip().replace(",", ".")
            return float(raw)
        except ValueError:
            print("Valor inválido. Tente novamente.")

def ler_str(msg, allow_empty=False):
    while True:
        s = input(msg).strip()
        if s or allow_empty:
            return s
        print("Digite um texto válido.")

def ler_ano_mes(msg="Ano-mês (YYYY-MM): "):
    while True:
        s = input(msg).strip()
        if len(s) == 7 and s[4] == "-" and s[:4].isdigit() and s[5:].isdigit():
            return s
        print("Formato inválido. Use YYYY-MM (ex.: 2025-10).")
