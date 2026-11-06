# Proyecto UNAB - Fases 1 y 2

**Curso:** Programación para la Ciencia de Datos (MCDI500).  
**Tema:** Calidad de registros sintéticos de fallas de tecnologías Onboard.  
**Naturaleza:** demostración académica; los datos no son registros reales de BHP ni de otra faena.

## Estructura
- `F1/F1_Definición.ipynb`: planteamiento y verificación inicial.
- `F2/F2_Obtencion_Exploracion.ipynb`: generación y exploración.
- `F2/F2_Limpieza_Validacion.ipynb`: limpieza, transformación, auditoría y gráficos.
- `src/pipeline.py`: funciones modulares.
- `datos/`: CSV de origen, procesado y rechazos.
- `tests/`: pruebas normales, límite y excepción.
- `evidencias/`: resultados de pruebas y auditoría.
- `figuras/`: gráficos exportados.

## Reproducción
Desde la raíz del proyecto:
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
jupyter notebook
```
Ejecutar notebooks en orden F1, F2_Obtencion_Exploracion y F2_Limpieza_Validacion. El CSV de origen se genera con semilla 42. Ejecutar desde la raíz del proyecto. Las dependencias se fijan para una versión de referencia y deben instalarse en un Python compatible (recomendado 3.11/3.12).

## Versionamiento pendiente de efectuar por el equipo
Este ZIP no constituye un repositorio remoto ni prueba un historial de contribuciones. Para cumplir la rúbrica, crear repositorio GitHub, registrar commits reales y adjuntar enlace/capturas. Ejemplo de secuencia, sin atribuir autorías inexistentes:
```bash
git init
git add README.md requirements.txt src F1
git commit -m "F1: problema, entorno y estructura reproducible"
git add F2 datos tests figuras evidencias
git commit -m "F2: generacion, limpieza y validaciones"
git remote add origin URL_REAL_DEL_REPOSITORIO
git push -u origin main
```
La rama por defecto puede requerir `git branch -M main`. Cada integrante debe contribuir efectivamente y registrar su trabajo.

## Consideraciones
Se conserva una duración faltante como dato ausente, sin imputar artificialmente. Los conteos de fallas simuladas no permiten inferencias operacionales ni tasas reales de falla.
