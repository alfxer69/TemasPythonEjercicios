import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Configuración principal de la ventana
raiz = tk.Tk()
raiz.config(width=800, height=600, relief='ridge', bd='8', background='lightgray')
raiz.title('Sistema de Recomendación de Netflix')

try:
    # Carga de datos
    base_neflix = pd.read_csv(r'E:\PythonAvanzado\Pandas\nltk\portfolio\netflixData.csv')
    base_neflix = base_neflix[['Title', 'Director', 'Imdb Score', 'Production Country', 'Genres']]
    base_neflix = base_neflix.fillna('')
    base_neflix['Combinada'] = base_neflix['Title'] + ' ' + base_neflix['Director'] + ' ' + base_neflix['Imdb Score'].astype(str) + ' ' + base_neflix['Production Country'] + ' ' + base_neflix['Genres']
    contenido_neflix = base_neflix['Title'].str.lstrip('#-*!.()').drop_duplicates().to_list()
except Exception as e:
    contenido_neflix = []
    base_neflix = pd.DataFrame()
    messagebox.showerror('Error', f'No se pudo cargar el archivo: {e}')

# Etiqueta
etiqueta1 = tk.Label(raiz, text='Escoja una Película para generar la recomendación:', font=('Radioland', 12))
etiqueta1.pack(padx=10, pady=10)

# Combobox para seleccionar película
combotextbox = ttk.Combobox(raiz, values=contenido_neflix, justify='center', font=('Arial', 12))
combotextbox.pack(ipadx=5, ipady=5)
if contenido_neflix:
    combotextbox.current(0)

# Crear un frame para el Text y la Scrollbar
frame_texto = tk.Frame(raiz)
frame_texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(frame_texto)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Text widget para mostrar las recomendaciones
texto_recomendaciones = tk.Text(frame_texto, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=('Arial', 12))
texto_recomendaciones.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=texto_recomendaciones.yview)

# Función para generar recomendaciones
def generar_recomendacion():
    texto_recomendaciones.delete(1.0, tk.END)  # Limpiar contenido previo
    pelicula = combotextbox.get()
    if not pelicula or pelicula not in base_neflix['Title'].values:
        messagebox.showwarning('Advertencia', 'Por favor seleccione una película')
        return

    # Vectorizar texto combinado
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(base_neflix['Combinada'])

    # Obtener índice de la película seleccionada
    idx = base_neflix[base_neflix['Title'] == pelicula].index[0]

    # Calcular similitud del coseno
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    # Ordenar por similitud y obtener los top 5
    similar_indices = cosine_sim.argsort()[-6:][::-1]
    recomendaciones = base_neflix.iloc[similar_indices[1:]]['Title'].to_list()

    if recomendaciones:
        texto_recomendaciones.insert(tk.END, f'Películas recomendadas basadas en "{pelicula}":\n\n')
        texto_recomendaciones.insert(tk.END, "\n".join(recomendaciones))
    else:
        texto_recomendaciones.insert(tk.END, 'No se encontraron recomendaciones.')

# Botón para generar recomendaciones
boton_recomendar = tk.Button(raiz, text='Generar Recomendación', command=generar_recomendacion, font=('Arial', 12), bg='blue', fg='white')
boton_recomendar.pack(padx=10, pady=10)

raiz.mainloop()