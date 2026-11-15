"""Descarga desde UCI; requiere Internet. No reemplaza el archivo original si ya existe."""
from pathlib import Path
import urllib.request,zipfile,io,shutil
BASE=Path(__file__).parent
URL='https://archive.ics.uci.edu/static/public/791/metropt+3+dataset.zip'
dest=BASE/'datos'/'MetroPT3(AirCompressor).csv'
if dest.exists(): print('Archivo existente:',dest)
else:
    print('Descargando ~208 MB desde UCI; puede demorar...')
    with urllib.request.urlopen(URL,timeout=240) as response: raw=response.read()
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        names=[n for n in z.namelist() if n.lower().endswith('.csv')]
        if not names: raise RuntimeError('No se encontro CSV en archivo oficial')
        with z.open(names[0]) as entrada,dest.open('wb') as salida: shutil.copyfileobj(entrada,salida)
    print('Descargado:',dest)
