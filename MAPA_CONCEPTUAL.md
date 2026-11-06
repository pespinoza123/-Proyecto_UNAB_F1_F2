# Mapa conceptual técnico — Fases 1 a 4

**Problema:** inconsistencias en registros de mantenimiento → **Preguntas:** calidad, frecuencia y duración → **Datos:** registros sintéticos con semilla fija → **Entorno:** Python, Jupyter, NumPy, Pandas y Git → **F1:** definición y entorno → **F2:** obtención → exploración → depuración → transformación → validación → **Salidas:** CSV limpios, descartes, auditoría, gráficos y pruebas → **F3 (propuesta):** indicadores y comparaciones descriptivas → **F4 (propuesta):** visualización final, discusión, límites y comunicación.

| Nodo conceptual | Implementación verificable | Estado |
|---|---|---|
| Problema y objetivos | F1/F1_Definición.ipynb | Implementado |
| Reproducibilidad | requirements.txt, README, semilla 42 | Implementado localmente |
| Datos | src/pipeline.py, datos/registros_originales.csv | Implementado |
| Calidad | src/pipeline.py, datos/rechazados.csv, evidencias/auditoria.json | Implementado |
| Validación | tests/test_pipeline.py | Implementado |
| Versionado colaborativo | GitHub e historial de commits | Pendiente de acción real del equipo |
| F3 y F4 | Indicadores, síntesis y comunicación | Proyectado |
