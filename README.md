# Weather_Dashboard
Este repositorio contiene una webapp para el análisis y visualización de datos meteorológicos de la plataforma ESOL-MET, utilizando **Shiny para Python**


- **`app/`**: Contiene la implementación principal de la webapp en Shiny para Python.

- **`notebooks/`**: Contiene Jupyter Notebooks para exploración y análisis de datos.
  - `data_cleaning/`: Notebooks para explorar los datos crudos y limpiarlos
  - `analysis/`: Análisis estadístico y cálculos.
  - `visualization/`: Pruebas de gráficos antes de integrarlos a la app.

- **`src/`**: Código fuente modularizado.
  - `utils.py`: Funciones auxiliares de soporte.

- **`scripts/`**: Scripts ejecutables sin necesidad de abrir notebooks.

- **`data/`**: Carpeta de almacenamiento de datos.
  - `01_raw/`: Datos sin procesar.
  - `02_processed/`: Datos listos para su uso en la webapp.

- **`tests/`**: Pruebas para asegurar el correcto funcionamiento del código.

- **`docs/`**: Documentación del proyecto.

- **`img/`**: Imágenes, íconos, gráficos.

- **`config/`**: Archivos de configuración y credenciales

- **`venv/`**: Carpeta del ambiente virtual (debe estar en `.gitignore`).