# Gene_dissimilarity_explorer.py
# Este script compara secuencias de ADN entre un archivo de control y otro de otras secuencias.
# Calcula la disimilitud (porcentaje de diferencias) entre las secuencias y visualiza los resultados en un heatmap.

from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Variables para los archivos de entrada
file_cntrl = "musculus.txt"  # Archivo de la secuencia de control
file_other = "mus_edit.txt"  # Archivo con las otras secuencias

# Variable para el archivo de salida
file_output = 'result_mus.svg'  # Nombre del archivo de salida en formato PDF

# Variables para los títulos y etiquetas
title = "Diferencia Genética en el Genoma Mitocondrial de\n Especies Relacionadas"
xlabel = "Genes"
ylabel = "Especie"

def parse_fasta(file):
    """
    Extrae el código de acceso, el gen y la secuencia de un archivo FASTA.

    Args:
        file (str): Ruta al archivo FASTA de entrada.

    Returns:
        pd.DataFrame: DataFrame con columnas 'Accession', 'Gene' y 'Sequence'.
    """
    data = []
    for record in SeqIO.parse(file, "fasta"):
        description = record.description
        accession = description.split("|")[1].split("_cds")[0]  # Código de acceso
        gene = description.split("[gene=")[1].split("]")[0]  # Nombre del gen
        sequence = str(record.seq)
        data.append((accession, gene, sequence))
    return pd.DataFrame(data, columns=["Accession", "Gene", "Sequence"])

def calculate_dissimilarity(seq1, seq2):
    """
    Calcula el porcentaje de disimilitud entre dos secuencias de ADN.

    Args:
        seq1 (str): Primera secuencia de ADN.
        seq2 (str): Segunda secuencia de ADN.

    Returns:
        float: Porcentaje de disimilitud entre las dos secuencias.
    """
    mismatches = sum(a != b for a, b in zip(seq1, seq2))
    max_length = max(len(seq1), len(seq2))
    return (mismatches / max_length) * 100

def compare_sequences(df_cntrl, df_other):
    """
    Compara las secuencias de control con las otras secuencias basadas en el nombre del gen.

    Args:
        df_cntrl (pd.DataFrame): DataFrame con las secuencias de control.
        df_other (pd.DataFrame): DataFrame con las otras secuencias.

    Returns:
        pd.DataFrame: DataFrame con la disimilitud entre las secuencias.
    """
    results = []
    for _, row in df_cntrl.iterrows():
        control_accession = row["Accession"]
        control_gene = row["Gene"]
        control_sequence = row["Sequence"]

        # Filtrar secuencias con el mismo gen
        matching_genes = df_other[df_other["Gene"] == control_gene]

        for _, other_row in matching_genes.iterrows():
            other_accession = other_row["Accession"]
            other_sequence = other_row["Sequence"]
            dissimilarity = calculate_dissimilarity(control_sequence, other_sequence)
            results.append((control_accession, other_accession, control_gene, dissimilarity))

    return pd.DataFrame(results, columns=["Control Accession", "Other Accession", "Gene", "Dissimilarity (%)"])

def plot_heatmap(matrix):
    """
    Genera un heatmap de la disimilitud entre las secuencias, con líneas separadoras entre las celdas.

    Args:
        matrix (pd.DataFrame): Matriz de disimilitud entre las secuencias.
    """
    # Configuración del gráfico
    plt.figure(figsize=(10, 6))  # Ajustar tamaño para hacer celdas más pequeñas

    # Generar el heatmap
    sns.heatmap(
        matrix,
        annot=True,
        fmt=".1f",
        cmap="coolwarm",
        cbar_kws={"label": "Diferencia (%)"},
        square=True,
        annot_kws={"size": 8},  # Reducir tamaño de fuente en anotaciones
        linewidths=0.9  # Líneas separadoras entre celdas
    )

    # Ajustar rotación de las etiquetas
    plt.yticks(rotation=0, fontsize=12)  # Códigos de acceso alineados horizontalmente
    plt.xticks(rotation=30, fontsize=12)  # Genes rotados 30 grados

    # Usar las variables para los títulos y etiquetas
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)

    plt.tight_layout()

    # Guardar el gráfico en formato PDF
    # plt.savefig(file_output, format='pdf', dpi=300, bbox_inches='tight')  # Guardar en PDF
    plt.savefig(file_output, format='svg', bbox_inches='tight')  # También puedes guardar en SVG (comentado)

    # Mostrar el gráfico
    plt.show()

# Procesar los archivos
df_cntrl = parse_fasta(file_cntrl)  # Cargar el archivo de control
df_other = parse_fasta(file_other)  # Cargar el archivo de otras secuencias

# Comparar las secuencias
dissimilarity_matrix = compare_sequences(df_cntrl, df_other)  # Calcular disimilitud

# Crear matriz pivote para el heatmap
pivot_table = dissimilarity_matrix.pivot_table(
    index="Other Accession", columns="Gene", values="Dissimilarity (%)", aggfunc="mean"
)

# Generar el heatmap con líneas separadoras
plot_heatmap(pivot_table)
