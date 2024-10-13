from flask import Flask, render_template, send_file
from nbconvert import HTMLExporter
import nbformat
import os

app = Flask(__name__)

# Mapeo de nombres de notebooks
notebook_mapping = {
    "numpy": "01_Numpy_3501.ipynb",
    "pandas": "02_Pandas_3501.ipynb",
    "matplotlib": "3501_Matplotlib.ipynb",
    "visualizacion": "3501_Visualización-de-datos.ipynb",
    "regresion_logistica": "3501_Regresion_Logistica.ipynb",
    "regresion_lineal": "3501_Regresión_Lineal.ipynb",
    "preparacion_dataset": "3501_Preparación-del-DataSet.ipynb",
    "evaluacion_resultados": "3501_Evaluacion-de-Resultados.ipynb",
    "transformadores_pipelines": "3501_Creación-de-Trasformadores-y-Pipelines-Personalizados.ipynb",
}

# Ruta a la carpeta de notebooks
notebooks_folder = "notebooks"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/notebook/<notebook_name>")
def render_notebook(notebook_name):
    if notebook_name not in notebook_mapping:
        return f"<p>Notebook '{notebook_name}' no encontrado.</p>", 404

    notebook_path = os.path.join(notebooks_folder, notebook_mapping[notebook_name])

    # Verificar si el archivo existe
    if not os.path.exists(notebook_path):
        return f"<p>El archivo del notebook '{notebook_path}' no existe.</p>", 404

    # Convertir el notebook a HTML
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook_content = nbformat.read(f, as_version=4)

        html_exporter = HTMLExporter()
        (body, resources) = html_exporter.from_notebook_node(notebook_content)
        return body
    except Exception as e:
        return f"<p>Error al renderizar el notebook: {str(e)}</p>", 500

if __name__ == "__main__":
    app.run(debug=True)
#hola mundo soy programador hol