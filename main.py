import pandas as pd
import numpy as np
from datetime import datetime

def monitor_de_qualidade(df):
 
    print("\nINICIANDO AUDITORIA DE DADOS ")
    
    null_report = df.isnull().sum()
    print(f"\n[INFO] Valores nulos encontrados:\n{null_report}")
    
    df['z_score'] = (df['valor'] - df['valor'].mean()) / df['valor'].std()
    anomalias = df[df['z_score'].abs() > 2]
    
    hoje = datetime.now()
    df['data_pagamento'] = pd.to_datetime(df['data_pagamento'])
    erros_data = df[df['data_pagamento'] > hoje]
    
    print(f"\n[CHECK] Registros analisados: {len(df)}")
    print(f"[ALERT] Datas futuras detectadas: {len(erros_data)}")
    print(f"[ALERT] Possíveis anomalias (Outliers): {len(anomalias)}")
    print("-" * 40)
    
    return anomalias

dados = {
    'valor': [100.50, 102.00, 98.75, 105.20, 1000.00, 97.10, 101.30], 
    'data_pagamento': [
        '2026-01-10', '2026-01-15', '2026-01-20', 
        '2026-01-25', '2026-02-01', '2026-02-05', 
        '2028-12-31' 
    ]
}

df_teste = pd.DataFrame(dados)

anomalias_encontradas = monitor_de_qualidade(df_teste)

print("\nDETALHES DAS ANOMALIAS ENCONTRADAS")
if not anomalias_encontradas.empty:
    print(anomalias_encontradas[['valor', 'data_pagamento', 'z_score']])
else:
    print("Nenhuma anomalia crítica detectada.")