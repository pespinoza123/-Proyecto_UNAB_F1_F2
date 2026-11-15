import pandas as pd
import numpy as np
import pytest
from src.pipeline_real import contar_iterativo,contar_recursivo,contar_vectorizado,procesar,ANALOGAS,DIGITALES

def test_algoritmos():
    a=np.array([1.,5.,9.,2.,7.])
    assert contar_iterativo(a,4)==contar_recursivo(a,4)==contar_vectorizado(a,4)==3

def test_vacio():
    assert contar_recursivo(np.array([]),2)==0

def test_conciliacion():
    row={'timestamp':'2020-02-01 00:00:00',**{c:1 for c in ANALOGAS+DIGITALES}}
    a=pd.DataFrame([row,{**row,'timestamp':'invalido'}]); limpio,rechazado,audit=procesar(a)
    assert audit=={'originales':2,'aceptados':1,'rechazados':1}

def test_sin_archivo():
    from src.pipeline_real import cargar
    with pytest.raises(FileNotFoundError): cargar('archivo_inexistente.csv')
