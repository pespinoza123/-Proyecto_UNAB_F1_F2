# Arquitectura y decisiones técnicas (F1–F4)

## Flujo de datos
`datos/registros_originales.csv` → validación y limpieza (`src/pipeline.py`) → `datos/registros_limpios.csv` y `datos/rechazados.csv` → análisis F3 (`src/fase3.py`) → F4 (tres visualizaciones y benchmark).

## Contratos y responsabilidades
- **Entrada:** CSV de registros sintéticos; columnas y tipos documentados por el pipeline.
- **Validación:** separación de registros aceptados/rechazados; auditoría en `evidencias/auditoria.json`.
- **Salida:** CSV limpio, estadísticas, gráficos y resultados de pruebas.
- **Orquestación:** notebooks F1–F4 con funciones reutilizables en `src/`.

## ADR-0001: conservar duración ausente
**Decisión:** no inventar una duración cuando el dato es nulo. Para operaciones que requieren duración, excluir solo ese valor; para conteos conservar el registro.
**Motivo:** evita sesgos derivados de imputaciones sin respaldo.
**Consecuencia:** las cantidades de observaciones de tiempos pueden ser menores que los conteos de registros.

## ADR-0002: benchmark comparativo
**Decisión:** comparar estrategias iterativa, recursiva y vectorizada sobre las mismas entradas válidas usando `timeit`.
**Motivo:** la elección debe sustentarse en mediciones y complejidad, no solo intuición.
**Limitación:** los tiempos dependen del hardware y del entorno.

**Referencia docente:** Universidad Andrés Bello, material del curso «Documentación profesional de arquitectura en ciencia de datos» (infografía proporcionada; año y autor personal no especificados).
