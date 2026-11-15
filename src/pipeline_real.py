"""Procesamiento de telemetria real MetroPT-3. No se generan observaciones artificiales."""
from pathlib import Path
import pandas as pd
import numpy as np

ANALOGAS = ['TP2','TP3','H1','DV_pressure','Reservoirs','Oil_temperature','Motor_current']
DIGITALES = ['COMP','DV_eletric','Towers','MPG','LPS','Pressure_switch','Oil_level','Caudal_impulses']
REQUERIDAS = ['timestamp'] + ANALOGAS + DIGITALES

def cargar(ruta):
    ruta=Path(ruta)
    if not ruta.exists(): raise FileNotFoundError(f'Descargue primero MetroPT-3: {ruta}')
    df=pd.read_csv(ruta,low_memory=False)
    if len(df)<2000 or df.shape[1]<12: raise ValueError('Dataset insuficiente para la rubrica')
    faltantes=set(REQUERIDAS)-set(df.columns)
    if faltantes: raise ValueError(f'Columnas faltantes: {sorted(faltantes)}')
    return df

def explorar(df):
    return {'filas':len(df),'columnas':df.shape[1], 'nulos':df.isna().sum().to_dict(),
            'duplicados_fila':int(df.duplicated().sum()),'tipos':df.dtypes.astype(str).to_dict()}

def procesar(df):
    """No imputar sin evidencia. Rechaza solo filas sin timestamp o sensores numericos invalidos."""
    x=df.copy(); x['timestamp']=pd.to_datetime(x['timestamp'],errors='coerce')
    for c in ANALOGAS+DIGITALES: x[c]=pd.to_numeric(x[c],errors='coerce')
    invalida=x['timestamp'].isna() | x[ANALOGAS+DIGITALES].isna().any(axis=1)
    rechazados=x.loc[invalida].copy(); rechazados['motivo']='fecha_o_sensor_invalido'
    limpios=x.loc[~invalida].copy()
    if limpios['timestamp'].isna().any(): raise ValueError('Fechas invalidas tras limpieza')
    if len(limpios)+len(rechazados)!=len(df): raise ValueError('Conciliacion fallida')
    limpios['delta_presion']=limpios['TP3']-limpios['Reservoirs']
    return limpios,rechazados,{'originales':len(df),'aceptados':len(limpios),'rechazados':len(rechazados)}

def contar_iterativo(valores,umbral):
    total=0
    for v in valores:
        if v>umbral: total+=1
    return total

def contar_recursivo(valores,umbral):
    """Divide y venceras; profundidad logaritmica, tiempo O(n)."""
    if len(valores)==0:return 0
    if len(valores)==1:return int(valores[0]>umbral)
    medio=len(valores)//2
    return contar_recursivo(valores[:medio],umbral)+contar_recursivo(valores[medio:],umbral)

def contar_vectorizado(valores,umbral):
    return int(np.count_nonzero(np.asarray(valores)>umbral))

class EstrategiaResumen:
    def resumir(self,df): raise NotImplementedError

class ResumenMedias(EstrategiaResumen):
    def resumir(self,df): return df[ANALOGAS].mean().to_dict()

class ResumenMedianas(EstrategiaResumen):
    def resumir(self,df): return df[ANALOGAS].median().to_dict()

class Analizador:
    def __init__(self,estrategia): self._estrategia=estrategia
    def cambiar_estrategia(self,estrategia): self._estrategia=estrategia
    def ejecutar(self,df): return self._estrategia.resumir(df)
