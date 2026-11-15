import sys
from src.pipeline_real import cargar
ruta=sys.argv[1] if len(sys.argv)>1 else 'datos/MetroPT3(AirCompressor).csv'
df=cargar(ruta)
print(f'VALIDADO: {len(df):,} filas, {df.shape[1]} columnas; fuente: UCI MetroPT-3')
