import sys
from pathlib import Path
import pandas as pd
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.pipeline import generar, procesar, validar

def test_caso_normal():
    limpio,rechazados,aud=procesar(generar())
    assert (aud['originales'],aud['duplicados_exactos'],aud['rechazados'],aud['aceptados'])==(161,1,4,156)
    assert aud['tiempos_faltantes_aceptados']==1
    assert validar(limpio)

def test_limite_cero_permitido():
    d=generar(); d.loc[0,'Tiempo_reparacion_h']=0
    limpio,_,_=procesar(d)
    assert limpio.loc[limpio.ID_registro==1,'Tiempo_reparacion_h'].iloc[0]==0

def test_error_columna_ausente():
    with pytest.raises(ValueError,match='Columnas ausentes'):
        procesar(generar().drop(columns=['Fecha']))

def test_normalizacion():
    limpio,_,_=procesar(generar())
    assert limpio.loc[limpio.ID_registro==6,'Tecnologia'].iloc[0]=='CAS-GPS'
    assert limpio.loc[limpio.ID_registro==11,'Tecnologia'].iloc[0]=='Optalert'
