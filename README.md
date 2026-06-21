# Biomecanica2026-1

Repositorio para el procesamiento y análisis de datos de biomecánica obtenidos mediante Kinovea y MATLAB.

---

# Clonar el repositorio

1. Abrir CMD o PowerShell.
2. Ir a la carpeta donde se desea guardar el proyecto:

```bash
cd "RUTA_DE_DESTINO"
```

Por ejemplo:

```bash
cd "D:\Proyectos"
```

3. Clonar el repositorio:

```bash
git clone https://github.com/ttanno/Biomecanica2026-1.git
```

4. Entrar a la carpeta creada:

```bash
cd Biomecanica2026-1
```

---

# Estructura del proyecto

## CODIGOLUCHO2.mlx

Este es el archivo principal del proyecto.

Contiene la versión más reciente de los scripts de procesamiento y análisis desarrollados hasta la fecha.

Se recomienda utilizar este archivo como punto de partida para futuras modificaciones y análisis.

---

## Carpeta `angulos_crudo`

Contiene los archivos exportados desde Kinovea antes de cualquier procesamiento.

Estos archivos representan los datos originales obtenidos del seguimiento de movimiento.

---

## Carpeta `angulos_recortados`

Contiene los archivos de ángulos ya recortados y preparados para el análisis.

Estos archivos son los que se utilizan para construir los **structs** empleados en MATLAB.

Si se desea generar nuevamente los structs de participantes o repeticiones, los archivos de esta carpeta deben utilizarse como entrada.

---

## Carpeta `kinovea`

Contiene los archivos `.kva` generados por Kinovea.

Estos archivos permiten recuperar configuraciones, marcadores y seguimiento realizados durante el análisis de video.

---

## Carpeta `codigos`

Contiene scripts auxiliares utilizados durante el desarrollo del proyecto.

---

# Flujo de trabajo recomendado

1. Obtener datos de movimiento mediante Kinovea.
2. Exportar los ángulos correspondientes.
3. Guardar los datos originales en `angulos_crudo`.
4. Procesar y recortar las señales.
5. Guardar los resultados en `angulos_recortados`.
6. Utilizar los archivos de `angulos_recortados` para generar los structs de MATLAB.
7. Ejecutar y continuar el análisis desde `CODIGOLUCHO2.mlx`.

---

# Actualizar el repositorio

Si existen cambios nuevos en GitHub:

```bash
git pull origin main
```

---

# Subir cambios al repositorio

```bash
git add .
git commit -m "Descripción de cambios"
git push
```

---

# Requisitos

- MATLAB
- Git
- Datos exportados desde Kinovea

---

# Notas

- No subir videos originales al repositorio.
- Los archivos de video deben almacenarse localmente fuera del proyecto.
- Los archivos de `angulos_recortados` son la fuente principal para la generación de structs y análisis posteriores.
- `CODIGOLUCHO2.mlx` contiene la versión más actualizada del procesamiento implementado.