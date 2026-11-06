from pathlib import Path
import numpy as np
import pandas as pd

VALIDAS = ('CAS-GPS','Optalert','iTrack II','LTE/WiFi')
MAPA = {'CAS GPS':'CAS-GPS','CAS-GPS':'CAS-GPS','OPTALERT':'Optalert',
        'ITRACK II':'iTrack II','ITRACK 2':'iTrack II','LTE/WIFI':'LTE/WiFi','LTE WIFI':'LTE/WiFi'}
COLUMNAS = ['ID_registro','Fecha','Equipo','Tecnologia','Tipo_falla','Tiempo_reparacion_h','Estado']

def generar(n=157, semilla=42):
    rng=np.random.default_rng(semilla)
    equipos=['CEX-21','CEX-35','CEX-42','CEX-18','CEX-53']
    tipos=['Comunicacion','Sensor','Conexion','Alimentacion']
    filas=[]
    for i in range(n):
        filas.append([i+1,(pd.Timestamp('2026-01-01')+pd.Timedelta(days=int(rng.integers(0,90)))).strftime('%Y-%m-%d'),
            str(rng.choice(equipos)),str(rng.choice(VALIDAS)),str(rng.choice(tipos)),
            round(float(rng.uniform(.5,6)),2),'Operativo'])
    df=pd.DataFrame(filas,columns=COLUMNAS)
    df.loc[5,'Tecnologia']='CAS GPS'
    df.loc[10,'Tecnologia']='OPTALERT'
    df.loc[15,'Tiempo_reparacion_h']=np.nan
    df.loc[20,'Fecha']='fecha_invalida'
    df=pd.concat([df,pd.DataFrame([
        [158,'2026-02-10','CEX-21',None,'Sensor',2.0,'Operativo'],
        [159,'2026-02-11','CEX-35','Optalert','Sensor',-2.0,'Operativo'],
        [160,'2026-02-12','CEX-42','Sistema desconocido','Sensor',1.0,'Operativo']],columns=COLUMNAS),df.iloc[[0]]],ignore_index=True)
    return df

def procesar(df):
    df=df.copy()
    requeridas=set(COLUMNAS)
    if not requeridas.issubset(df.columns):
        raise ValueError('Columnas ausentes: '+str(sorted(requeridas-set(df.columns))))
    duplicados=int(df.duplicated().sum())
    df=df.drop_duplicates().copy()
    df['Tecnologia']=df['Tecnologia'].astype('string').str.strip().str.upper().map(MAPA)
    df['Fecha']=pd.to_datetime(df['Fecha'],errors='coerce')
    df['Tiempo_reparacion_h']=pd.to_numeric(df['Tiempo_reparacion_h'],errors='coerce')
    razones=pd.DataFrame(index=df.index)
    razones['fecha_invalida']=df['Fecha'].isna()
    razones['tecnologia_invalida']=~df['Tecnologia'].isin(VALIDAS).fillna(False)
    razones['tiempo_negativo']=df['Tiempo_reparacion_h'].lt(0).fillna(False)
    razones['id_duplicado']=df['ID_registro'].duplicated(keep='first')
    invalida=razones.any(axis=1)
    rechazados=df.loc[invalida].copy()
    rechazados['Motivos']=razones.loc[invalida].apply(lambda r:', '.join(r.index[r]),axis=1)
    limpio=df.loc[~invalida].copy().sort_values('ID_registro').reset_index(drop=True)
    limpio['Mes']=limpio['Fecha'].dt.to_period('M').astype(str)
    limpio['Tiempo_reparacion_min']=limpio['Tiempo_reparacion_h']*60
    auditoria={'originales':len(df)+duplicados,'duplicados_exactos':duplicados,
               'rechazados':len(rechazados),'aceptados':len(limpio),
               'tiempos_faltantes_aceptados':int(limpio['Tiempo_reparacion_h'].isna().sum()),
               'motivos':{c:int(razones[c].sum()) for c in razones.columns}}
    validar(limpio)
    assert auditoria['originales']==auditoria['duplicados_exactos']+auditoria['rechazados']+auditoria['aceptados']
    return limpio,rechazados,auditoria

def validar(df):
    assert df['ID_registro'].is_unique
    assert df['Fecha'].notna().all()
    assert df['Tecnologia'].isin(VALIDAS).all()
    assert df['Tiempo_reparacion_h'].dropna().ge(0).all()
    assert not df.duplicated().any()
    return True
