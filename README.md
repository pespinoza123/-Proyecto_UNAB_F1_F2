# Proyecto UNAB – Fases 1, 2 y 3

**Curso:** Programación para la Ciencia de Datos (MCDI500)  
**Estudiante:** Pamela Espinoza Díaz  
**Programa:** Magíster en Ciencia de Datos e Inteligencia Artificial  
**Universidad:** Universidad Andrés Bello (UNAB)

## 1. Descripción del proyecto

Este repositorio reúne el desarrollo académico de las Fases 1, 2 y 3 del curso Programación para la Ciencia de Datos.

El proyecto aborda la obtención, exploración, limpieza, transformación y validación de datos mediante Python, incorporando principios de programación modular, algoritmos y programación orientada a objetos.

Las fases iniciales incluyen ejercicios demostrativos con datos sintéticos relacionados con tecnologías Onboard. Para el trabajo con datos reales se propone utilizar el conjunto de datos público MetroPT-3.

Los datos sintéticos no corresponden a registros operacionales reales de BHP ni de otra faena minera.

## 2. Objetivo general

Desarrollar un proceso reproducible de análisis y preparación de datos mediante Python, integrando técnicas de exploración, limpieza, validación, algoritmos y programación orientada a objetos.

## 3. Estructura del repositorio

### Fase 1: Definición del proyecto

**Carpeta:** `F1/`

Contiene el planteamiento inicial del problema y la definición del entorno de trabajo.

### Fase 2: Obtención, exploración y limpieza

**Carpeta:** `F2/`

Incluye actividades de obtención, exploración, limpieza, transformación y validación de datos.

### Fase 3: Algoritmos y programación orientada a objetos

**Carpeta:** `F3/`

Contiene el notebook `F3_Algoritmos_POO.ipynb`, orientado al desarrollo de algoritmos y la aplicación de principios de programación orientada a objetos.

### Código fuente

**Carpeta:** `src/`

Contiene funciones y módulos Python utilizados en el proyecto.

### Pruebas

**Carpeta:** `tests/`

Contiene pruebas automatizadas destinadas a verificar el funcionamiento del código.

### Datos

**Carpeta:** `datos/`

Contiene archivos relacionados con los conjuntos de datos y la documentación de sus fuentes.

## 4. Dataset público

**Nombre:** MetroPT-3  
**Repositorio:** UCI Machine Learning Repository  
**DOI:** 10.24432/C5VW3R  
**Licencia:** Creative Commons Attribution 4.0 (CC BY 4.0).

Este conjunto de datos se utiliza como referencia para el desarrollo de actividades de análisis y procesamiento de información.

La incorporación de los scripts de descarga y validación no constituye, por sí sola, evidencia de que el dataset haya sido descargado, procesado o validado exitosamente.

## 5. Requisitos

- Python 3.11 o 3.12, según compatibilidad.
- Bibliotecas indicadas en `requirements.txt`.
- Jupyter Notebook.
- Conexión a internet para obtener el dataset público.

## 6. Instalación

Desde la carpeta principal del proyecto, ejecutar:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## 7. Obtención y validación de datos

El repositorio incluye los siguientes programas:

- `descargar_datos.py`: script destinado a obtener los datos.
- `validar_dataset.py`: script destinado a comprobar las características del conjunto de datos.

Antes de ejecutar los programas, revisar sus parámetros, rutas de entrada y salida, y dependencias.

## 8. Ejecución de las pruebas

Desde la carpeta principal del proyecto:

```bash
python -m pytest -q
```

Los resultados deben verificarse en el entorno donde se ejecute el proyecto.

## 9. Ejecución de los notebooks

Abrir Jupyter Notebook:

```bash
jupyter notebook
```

Ejecutar los cuadernos correspondientes a cada fase, siguiendo las instrucciones y dependencias indicadas en ellos.

Se recomienda ejecutar las celdas en orden y conservar los resultados obtenidos como evidencia.

## 10. Control de versiones

El proyecto utiliza GitHub para registrar los avances de desarrollo.

El historial de commits permite revisar los cambios realizados en los archivos del repositorio.

## 11. Reproducibilidad y evidencias

Para comprobar la reproducibilidad del proyecto se requiere:

- Instalar correctamente las dependencias.
- Obtener y validar el dataset.
- Ejecutar los notebooks.
- Ejecutar las pruebas automatizadas.
- Revisar los resultados y posibles errores.
- Conservar evidencias de las ejecuciones realizadas.

No se presentan como verificados resultados que todavía no hayan sido comprobados mediante ejecución.

## 12. Consideraciones académicas

Este repositorio tiene fines exclusivamente académicos.

Los datos sintéticos utilizados en las actividades iniciales no representan información real de operaciones mineras.

Las conclusiones deben formularse de acuerdo con los datos efectivamente analizados y los resultados obtenidos.

## 13. Autoría

**Pamela Espinoza Díaz**  
Magíster en Ciencia de Datos e Inteligencia Artificial  
Universidad Andrés Bello (UNAB).
