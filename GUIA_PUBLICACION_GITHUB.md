# Publicación del proyecto en GitHub

Esta carpeta contiene los notebooks ejecutables y sus archivos complementarios. **No es todavía un repositorio remoto de GitHub.** Para obtener el enlace y la evidencia de commits, el equipo debe publicarlo desde su cuenta.

## 1. Preparación

1. Crear un repositorio **vacío** en GitHub con nombre `unab-mcdi500-fases-1-2` (privado si lo exige el curso).
2. Descargar y descomprimir este ZIP; abrir una terminal en `Proyecto_UNAB_F1_F2`.
3. Configurar el nombre y correo propios para Git si aún no están configurados: `git config user.name "NOMBRE REAL"` y `git config user.email "CORREO REAL"`.

## 2. Primer commit y publicación

```bash
git init
git branch -M main
git add .
git commit -m "Proyecto F1-F2: notebooks, pipeline, pruebas y documentacion"
git remote add origin https://github.com/USUARIO_REAL/unab-mcdi500-fases-1-2.git
git push -u origin main
```

Reemplazar `USUARIO_REAL` por el usuario propietario. GitHub puede solicitar iniciar sesión mediante el navegador o un token.

## 3. Colaboración y evidencias

- Invitar a los integrantes reales en **Settings > Collaborators**.
- Cada integrante debe realizar cambios genuinos y confirmarlos desde su propia cuenta; no crear commits ficticios para simular colaboración.
- Verificar que GitHub muestre `F1/`, `F2/`, `src/`, `datos/`, `tests/`, `figuras/`, `evidencias/`, `README.md` y `requirements.txt`.
- Guardar para el informe: enlace real del repositorio, captura de la página principal, captura del historial **Commits**, y salidas ejecutadas de los notebooks.

## 4. Comprobación antes de entregar

Desde la carpeta raíz, crear y activar el entorno, instalar `requirements.txt`, ejecutar `python -m pytest -q`, abrir `jupyter notebook` y ejecutar los tres notebooks en orden. Confirmar que las salidas coinciden con el informe.

**Importante:** todos los registros son sintéticos. La publicación no acredita uso de datos reales ni sustituye la confirmación del docente sobre la aceptación de datos sintéticos.
