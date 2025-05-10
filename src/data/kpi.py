import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.salary_service import processar_validacoes

tentativas_maxima: int = 5
tentativa: int = 1

for tentativa in range(1, tentativas_maxima+1):
    print(f"Tentativa {tentativa} de {tentativas_maxima}. Se exceder o total de tentativas, a conexão será abortada.")
    if processar_validacoes():
        break
else:
    print("Número máximo de tentativas excedido. Encerrando o programa.")