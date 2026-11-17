# PROYECTO UNAB – FASES 1, 2, 3 Y 4
## Proyecto Final Integrador – Programación para la Ciencia de Datos

**Universidad:** Universidad Andrés Bello (UNAB)  
**Programa:** Magíster en Ciencia de Datos e Inteligencia Artificial  
**Asignatura:** Programación para la Ciencia de Datos  
**Código:** MCDI500  
**Estudiante:** Pamela Espinoza Díaz  
**Evaluación:** Proyecto Final Integrador F1–F4  
**Año académico:** 2026  

---

# 1. DESCRIPCIÓN GENERAL DEL PROYECTO

Este repositorio contiene el desarrollo académico de las cuatro fases del proyecto integrador de la asignatura Programación para la Ciencia de Datos, correspondiente al Magíster en Ciencia de Datos e Inteligencia Artificial de la Universidad Andrés Bello.

El proyecto tiene como propósito desarrollar un proceso reproducible de análisis y preparación de datos mediante Python, integrando herramientas científicas, programación estructurada, algoritmos, programación orientada a objetos, validación técnica y evaluación de eficiencia computacional.

El contexto de aplicación corresponde al análisis de información relacionada con sistemas tecnológicos Onboard utilizados en equipos mineros.

Para el desarrollo de las actividades iniciales se utilizan datos sintéticos que permiten representar situaciones de análisis, limpieza, transformación y validación.

Adicionalmente, se considera el conjunto de datos público MetroPT-3 como referencia para actividades de procesamiento de información.

**Importante:** Los datos sintéticos utilizados no corresponden a registros operacionales reales de BHP ni de ninguna otra faena minera.

---

# 2. OBJETIVOS DEL PROYECTO

## 2.1. Objetivo general

Desarrollar un proceso reproducible de análisis y preparación de datos mediante Python, integrando técnicas de exploración, limpieza, transformación, validación, programación modular, programación orientada a objetos y evaluación de eficiencia algorítmica.

## 2.2. Objetivos específicos

1. Definir la problemática y configurar un entorno reproducible.
2. Obtener, explorar y preparar conjuntos de datos.
3. Aplicar técnicas de limpieza y transformación.
4. Implementar algoritmos mediante programación estructurada.
5. Incorporar principios de programación orientada a objetos.
6. Evaluar la eficiencia computacional mediante mediciones.
7. Validar el funcionamiento del código mediante pruebas.
8. Integrar los resultados de las fases F1–F4.
9. Documentar las decisiones técnicas y las mejoras realizadas.
10. Facilitar la reproducción del proyecto mediante GitHub y Jupyter Notebook.

---

# 3. ESTRUCTURA DEL REPOSITORIO

El repositorio se encuentra organizado de la siguiente manera:

```text
-Proyecto_UNAB_F1_F2/
│
├── F1/
│   └── Archivos correspondientes a la Fase 1
│
├── F2/
│   └── Archivos correspondientes a la Fase 2
│
├── F3/
│   └── F3_Algoritmos_POO.ipynb
│
├── F4/
│   ├── README.md
│   ├── F4_Integracion_Ejecutable.ipynb
│   ├── benchmark_f4.csv
│   ├── pruebas_ejecutadas.txt
│   ├── resultados_verificados.json
│   ├── CHANGELOG.md
│   └── DOCUMENTACION_ARQUITECTURA.md
│
├── datos/
├── evidencias/
├── figuras/
├── src/
├── pruebas/
│
├── .gitignore
├── CHANGELOG.md
├── DOCUMENTACION_ARQUITECTURA.md
├── GUIA_PUBLICACION_GITHUB.md
├── MAPA_CONCEPTUAL.md
├── README.md
├── descargar_datos.py
├── requirements.txt
└── validar_dataset.py
```

---

# 4. DESARROLLO DE LAS FASES

## 4.1. Fase 1 – Definición y orientación del proyecto

**Carpeta:** [F1](F1/)

Esta fase contempla:

- Identificación del problema.
- Contextualización de la situación.
- Formulación de objetivos.
- Definición del alcance.
- Identificación de herramientas.
- Configuración inicial del entorno reproducible.

Su propósito es establecer las bases metodológicas y técnicas del proyecto.

## 4.2. Fase 2 – Obtención y preparación de datos

**Carpeta:** [F2](F2/)

Esta fase comprende:

- Obtención de información.
- Exploración inicial del dataset.
- Identificación de valores ausentes.
- Limpieza de registros.
- Transformación de variables.
- Validación de datos.
- Preparación para análisis posteriores.

Se utilizan herramientas del ecosistema científico de Python para desarrollar procesos de preparación y análisis.

## 4.3. Fase 3 – Algoritmos y programación orientada a objetos

**Carpeta:** [F3](F3/)

Esta fase aborda:

- Programación estructurada.
- Desarrollo de funciones.
- Diseño modular.
- Implementación de algoritmos.
- Programación orientada a objetos.
- Organización de componentes.
- Validación del funcionamiento del código.

El notebook principal corresponde a:

[F3_Algoritmos_POO.ipynb](F3/F3_Algoritmos_POO.ipynb)

## 4.4. Fase 4 – Integración, validación y resultados

**Carpeta:** [F4](F4/)

La Fase 4 integra los componentes desarrollados anteriormente y organiza las evidencias correspondientes a la evaluación final.

### Archivos de la Fase 4

| Archivo | Descripción |
|---|---|
| `F4_Integracion_Ejecutable.ipynb` | Notebook de integración |
| `benchmark_f4.csv` | Mediciones de rendimiento |
| `pruebas_ejecutadas.txt` | Registro de pruebas |
| `resultados_verificados.json` | Resultados registrados |
| `README.md` | Descripción de la fase |
| `CHANGELOG.md` | Registro de cambios |
| `DOCUMENTACION_ARQUITECTURA.md` | Documentación técnica |

### Acceso al notebook

[F4_Integracion_Ejecutable.ipynb](F4/F4_Integracion_Ejecutable.ipynb)

### Acceso a las evidencias

- [Benchmark F4](F4/benchmark_f4.csv)
- [Pruebas ejecutadas](F4/pruebas_ejecutadas.txt)
- [Resultados registrados](F4/resultados_verificados.json)

---

# 5. CONJUNTOS DE DATOS

## 5.1. Datos sintéticos

Durante el desarrollo inicial del proyecto se utilizan registros sintéticos relacionados con tecnologías Onboard.

Estos datos permiten realizar ejercicios de:

- Exploración.
- Limpieza.
- Transformación.
- Validación.
- Programación.
- Análisis de resultados.

Los datos sintéticos tienen fines académicos y no representan registros reales de operaciones mineras.

## 5.2. Dataset público MetroPT-3

**Nombre:** MetroPT-3  
**Fuente:** UCI Machine Learning Repository  
**DOI:** 10.24432/C5VW3R  
**Licencia:** Creative Commons Attribution 4.0 (CC BY 4.0)

El dataset se considera como referencia pública para actividades de análisis y procesamiento.

La existencia de scripts de descarga no constituye por sí sola evidencia de que el conjunto de datos haya sido procesado exitosamente.

---

# 6. HERRAMIENTAS UTILIZADAS

| Herramienta | Aplicación |
|---|---|
| Python | Desarrollo del proyecto |
| NumPy | Operaciones numéricas |
| Pandas | Manipulación de datos |
| Matplotlib | Visualización |
| Jupyter Notebook | Ejecución de cuadernos |
| Git | Control de versiones |
| GitHub | Publicación y trazabilidad |
| Pytest | Pruebas automatizadas |
| CSV | Registro de información |
| JSON | Almacenamiento estructurado |

Las dependencias se encuentran declaradas en:

[requirements.txt](requirements.txt)

---

# 7. INSTALACIÓN DEL PROYECTO

## 7.1. Requisitos

Se recomienda utilizar:

- Python 3.11 o 3.12, según compatibilidad.
- Jupyter Notebook.
- Las dependencias declaradas en `requirements.txt`.
- Conexión a internet para descargar datos públicos.

## 7.2. Descargar el repositorio

Desde GitHub, seleccionar:

**Código → Descargar ZIP**

También puede clonarse mediante Git:

```bash
git clone https://github.com/pespinoza123/-Proyecto_UNAB_F1_F2.git
```

Ingresar al directorio:

```bash
cd -- -Proyecto_UNAB_F1_F2
```

## 7.3. Crear el entorno virtual

```bash
python -m venv .venv
```

## 7.4. Activar el entorno virtual

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

## 7.5. Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

## 7.6. Verificar la instalación

```bash
python --version
```

```bash
python -m pip list
```

---

# 8. OBTENCIÓN Y VALIDACIÓN DE DATOS

El proyecto incorpora dos scripts principales.

## 8.1. Descarga de datos

Archivo:

[descargar_datos.py](descargar_datos.py)

Su propósito es facilitar la obtención de datos para el proyecto.

## 8.2. Validación del dataset

Archivo:

[validar_dataset.py](validar_dataset.py)

Su propósito es comprobar las características y condiciones del conjunto de datos.

Antes de ejecutar ambos scripts, deben revisarse sus parámetros, rutas y dependencias.

---

# 9. EJECUCIÓN DE LOS NOTEBOOKS

## 9.1. Iniciar Jupyter Notebook

Desde la carpeta principal:

```bash
jupyter notebook
```

## 9.2. Orden de ejecución

Se recomienda seguir esta secuencia:

1. Fase 1: definición del proyecto.
2. Fase 2: preparación de datos.
3. Fase 3: algoritmos y programación orientada a objetos.
4. Fase 4: integración y resultados.

## 9.3. Ejecución de Fase 4

Abrir:

`F4/F4_Integracion_Ejecutable.ipynb`

Posteriormente:

1. Seleccionar el entorno de Python.
2. Ejecutar las celdas en orden.
3. Revisar las salidas.
4. Comprobar que no existan errores.
5. Examinar los resultados.
6. Comparar las salidas con las evidencias registradas.

---

# 10. PRUEBAS Y VALIDACIÓN TÉCNICA

El proyecto incluye una carpeta de pruebas automatizadas:

[pruebas](pruebas/)

Para ejecutar las pruebas desde la carpeta principal:

```bash
python -m pytest -q
```

Los resultados deben verificarse en el entorno donde se ejecute el proyecto.

### Evidencias disponibles

- [Registro de pruebas](F4/pruebas_ejecutadas.txt)
- [Resultados registrados](F4/resultados_verificados.json)

Estas evidencias permiten consultar los resultados documentados de las verificaciones realizadas.

---

# 11. EFICIENCIA Y OPTIMIZACIÓN ALGORÍTMICA

La evaluación de eficiencia permite estudiar el comportamiento computacional de las soluciones implementadas.

Se consideran aspectos como:

- Tiempo de ejecución.
- Comparación entre implementaciones.
- Complejidad temporal.
- Complejidad espacial.
- Reproducibilidad de mediciones.
- Justificación de decisiones técnicas.

### Archivo de mediciones

[benchmark_f4.csv](F4/benchmark_f4.csv)

Las conclusiones deben sustentarse en las mediciones registradas y en las condiciones bajo las cuales fueron obtenidas.

---

# 12. ARQUITECTURA DEL PROYECTO

La arquitectura se documenta en:

[DOCUMENTACION_ARQUITECTURA.md](DOCUMENTACION_ARQUITECTURA.md)

## 12.1. Flujo general

```text
Obtención de datos
        |
        v
Validación inicial
        |
        v
Limpieza y transformación
        |
        v
Procesamiento algorítmico
        |
        v
Análisis de resultados
        |
        v
Visualización
        |
        v
Documentación y comunicación
```

## 12.2. Principios de diseño

La organización del proyecto considera:

- Separación de responsabilidades.
- Modularidad.
- Reutilización de funciones.
- Validación de entradas y salidas.
- Documentación técnica.
- Reproducibilidad.
- Mantenibilidad.

## 12.3. Documentación complementaria

También se dispone de:

[MAPA_CONCEPTUAL.md](MAPA_CONCEPTUAL.md)

---

# 13. CONTROL DE VERSIONES

El proyecto utiliza GitHub para registrar el desarrollo de las distintas fases.

El historial de commits permite identificar cambios realizados en el repositorio.

La documentación de mejoras se encuentra en:

[CHANGELOG.md](CHANGELOG.md)

El registro permite consultar las modificaciones documentadas y contrastarlas con los commits reales.

---

# 14. TRAZABILIDAD DE MEJORAS

La evolución del proyecto se organiza según las cuatro fases.

| Fase | Área de desarrollo |
|---|---|
| F1 | Definición del problema y entorno |
| F2 | Obtención y preparación de datos |
| F3 | Algoritmos y programación orientada a objetos |
| F4 | Integración, validación y documentación final |

La trazabilidad detallada debe comprobarse mediante el historial de commits y el archivo `CHANGELOG.md`.

---

# 15. RESULTADOS Y EVIDENCIAS

El repositorio incorpora materiales relacionados con:

- Preparación de datos.
- Programación estructurada.
- Programación orientada a objetos.
- Validación técnica.
- Mediciones de rendimiento.
- Documentación de arquitectura.
- Integración de fases.
- Registro de mejoras.

### Evidencias principales

| Evidencia | Ubicación |
|---|---|
| Notebook F3 | `F3/F3_Algoritmos_POO.ipynb` |
| Notebook F4 | `F4/F4_Integracion_Ejecutable.ipynb` |
| Benchmark | `F4/benchmark_f4.csv` |
| Pruebas | `F4/pruebas_ejecutadas.txt` |
| Resultados | `F4/resultados_verificados.json` |
| Arquitectura | `DOCUMENTACION_ARQUITECTURA.md` |
| Mejoras | `CHANGELOG.md` |

---

# 16. REPRODUCIBILIDAD

Para reproducir el proyecto:

1. Descargar o clonar el repositorio.
2. Crear un entorno virtual.
3. Instalar las dependencias.
4. Revisar las fuentes de datos.
5. Ejecutar los scripts de validación.
6. Ejecutar los notebooks F1–F4.
7. Ejecutar las pruebas automatizadas.
8. Revisar los resultados.
9. Comparar las salidas con las evidencias.
10. Documentar cualquier diferencia encontrada.

La reproducibilidad debe comprobarse mediante ejecución.

---

# 17. LIMITACIONES

El proyecto presenta las siguientes consideraciones:

- Los datos sintéticos no corresponden a registros operacionales reales.
- Los resultados dependen del conjunto de datos utilizado.
- Las mediciones pueden variar según el hardware.
- La ejecución requiere dependencias compatibles.
- Los resultados no deben extrapolarse directamente a operaciones mineras reales.
- La existencia de archivos no sustituye su validación funcional.

---

# 18. CONSIDERACIONES ACADÉMICAS Y ÉTICAS

El proyecto se desarrolla con fines académicos en la Universidad Andrés Bello.

Se mantiene la distinción entre:

- Datos sintéticos.
- Datos públicos.
- Resultados registrados.
- Resultados efectivamente verificados.

La información utilizada debe respetar las condiciones de uso de sus fuentes.

Las referencias técnicas y académicas deben citarse correctamente en el informe final.

---

# 19. DOCUMENTACIÓN DISPONIBLE

| Documento | Enlace |
|---|---|
| README principal | [README.md](README.md) |
| Arquitectura | [DOCUMENTACION_ARQUITECTURA.md](DOCUMENTACION_ARQUITECTURA.md) |
| Registro de cambios | [CHANGELOG.md](CHANGELOG.md) |
| Mapa conceptual | [MAPA_CONCEPTUAL.md](MAPA_CONCEPTUAL.md) |
| Dependencias | [requirements.txt](requirements.txt) |
| Notebook F4 | [F4_Integracion_Ejecutable.ipynb](F4/F4_Integracion_Ejecutable.ipynb) |

---

# 20. AUTORÍA

**Pamela Espinoza Díaz**  
Magíster en Ciencia de Datos e Inteligencia Artificial  
Universidad Andrés Bello (UNAB)

**Asignatura:** Programación para la Ciencia de Datos  
**Código:** MCDI500  
**Proyecto:** Evaluación Final Integrada F1–F4  
**Año:** 2026

---

# 21. ESTADO DEL PROYECTO

**Fase 1:** Documentación incorporada.  
**Fase 2:** Documentación incorporada.  
**Fase 3:** Notebook y código incorporados.  
**Fase 4:** Notebook, registros de pruebas y resultados incorporados.  

**Repositorio:** Publicado en GitHub.  
**Documentación:** README, arquitectura y registro de cambios disponibles.  
**Validación integral:** Sujeta a la ejecución reproducible de todos los componentes.

---

**Universidad Andrés Bello – Magíster en Ciencia de Datos e Inteligencia Artificial**

**Proyecto Final Integrador – Programación para la Ciencia de Datos – 2026**

Ahora haz esto
