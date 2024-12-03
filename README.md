# GeneDissimilarityExplorer
GeneDissimilarityExplorer
Este script permite comparar secuencias de ADN entre un archivo de secuencias de control y otro de secuencias adicionales. Calcula el porcentaje de disimilitud entre las secuencias y genera un heatmap para visualizar las diferencias.

# Descripción
El script GeneDissimilarityExplorer.py toma dos archivos de secuencias en formato FASTA, calcula la disimilitud entre las secuencias del archivo de control y las del archivo adicional, y presenta un gráfico de tipo heatmap que visualiza el porcentaje de disimilitud entre las secuencias. Además, el gráfico puede ser guardado en formato PDF o SVG.

# Requisitos
Este script está escrito en Python 3. Para ejecutarlo correctamente, asegúrese de tener instaladas las siguientes bibliotecas:

Biopython: 	Para leer archivos FASTA y procesar las secuencias.
Pandas: 	Para manejar y procesar los datos en formato de tabla.
Matplotlib: Para generar los gráficos.
Seaborn: 	Para crear los heatmaps.
Puede instalar todas las dependencias necesarias con el siguiente comando:



pip install biopython pandas matplotlib seaborn

-------------//////-----------

# Archivos de Entrada
musculus.txt (Archivo de Control)
Este archivo debe contener las secuencias de ADN que se usarán como secuencia de control. El archivo debe estar en formato FASTA. Cada secuencia debe tener una línea de descripción con el formato estándar de FASTA, que incluya el código de acceso y el nombre del gen.

Ejemplo:
>lcl|NC_030342.1_cds_YP_009257679.1_1 [gene=ND1] [locus_tag=BAR10_gp13] [db_xref=GeneID:27983430] [protein=NADH dehydrogenase subunit 1]
ATAGTGTATCTCATTAATATTCTAACACTCCTTGTTCCTAT...
mus.txt (Archivo de Otras Secuencias)
Este archivo debe contener las otras secuencias de ADN que se compararán con la secuencia de control. Debe estar en el mismo formato que el archivo de control.

-------------//////-----------

# Archivos de Salida
1. heatmap_output.pdf (PDF)
El gráfico generado será guardado en formato PDF. El archivo contiene un heatmap que muestra el porcentaje de disimilitud entre las secuencias.

2. heatmap_output.svg (SVG)
Si se desea, se puede guardar el gráfico en formato SVG. Para ello, debe descomentar la línea correspondiente en el script.

-------------//////-----------

Uso
Ejecución del Script
Coloque los archivos musculus.txt (secuencia de control) y mus.txt (otras secuencias) en el mismo directorio que el script GeneDissimilarityExplorer.py.

Ejecute el script en su entorno de Python:
python GeneDissimilarityExplorer.py
El script generará un archivo PDF con el heatmap que muestra la disimilitud entre las secuencias. Si se desea, también puede generar un archivo SVG descomentando la línea correspondiente en el código.

-------------//////-----------

# Variables Modificables
Se ha dejado una sección de variables modificables en el script, donde se pueden ajustar los siguientes valores:

file_cntrl: Ruta al archivo de la secuencia de control.
file_other: Ruta al archivo con las otras secuencias.
file_output: Nombre del archivo de salida. El formato predeterminado es PDF.
file_output_svg: Nombre del archivo de salida en formato SVG (comentado por defecto).
title: Título del gráfico generado.
xlabel: Etiqueta del eje X (Genes).
ylabel: Etiqueta del eje Y (Organismo).

Ejemplo de las variables modificables dentro del script:

# Variables para los archivos de entrada
file_cntrl = "musculus.txt"
file_other = "mus.txt"

# Variable para el archivo de salida
file_output = 'heatmap_output.pdf'  # Nombre del archivo de salida en formato PDF
file_output_svg = 'heatmap_output.svg'  # Nombre del archivo de salida en formato SVG (comentado)

# Variables para los títulos y etiquetas
title = "Heatmap de Disimilitud con Líneas Separadoras"
xlabel = "Genes"
ylabel = "Códigos de Acceso"
Formatos de salida:
PDF: El gráfico se guarda por defecto en formato PDF.
SVG: Para guardar el gráfico en formato SVG, descomente la línea correspondiente.
