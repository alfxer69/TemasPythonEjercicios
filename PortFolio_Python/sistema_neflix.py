import tkinter as tk 
from tkinter import messagebox,ttk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


raiz=tk.Tk()
raiz.config(width=1800,height=1500,relief='ridge',bd='8',background='lightgray')
raiz.title('Sistema de Recomendacion de Nexflix')

try:
    base_neflix=pd.read_csv(r'E:\PythonAvanzado\Pandas\nltk\portfolio\netflixData.csv')
    #seleccionamos columnas relevantes
    base_neflix=base_neflix[['Title','Director','Imdb Score','Production Country','Genres']]
    base_neflix=base_neflix.fillna('')
    base_neflix['Combinada']=base_neflix['Title']+' '+base_neflix['Director']+' '+base_neflix['Imdb Score'].astype(str)+' '+base_neflix['Production Country']+' '+base_neflix['Genres']
    contenido_neflix=base_neflix['Title'].str.lstrip('#-*!.()').drop_duplicates().to_list()
except Exception as e:
    contenido_neflix=[]
    base_neflix=pd.DataFrame()
    messagebox.showerror('Error','No se pudo cargar el archivo {e}')


etiqueta1=tk.Label(raiz,text='Escoja una Pelicula para generar la recomendacion:',font=('Radioland',12))
etiqueta1.pack(padx=10,pady=10)

combotextbox=ttk.Combobox(raiz,values=contenido_neflix,justify='center',font=('Arial',12))
combotextbox.pack(ipadx=5,ipady=5)

if contenido_neflix:
    combotextbox.current(0)
else:
    messagebox.showwarning('Advertencia','No hay contenido')

#creamos un frame para el Text y scrollbar
frame_texto=tk.Frame(raiz)
frame_texto.pack(fill=tk.BOTH, expand=True,padx=10,pady=10)

#Scrollbar
scrollbar=tk.Scrollbar(frame_texto)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

#Mostrar recomendaciones
texto_recomendaciones=tk.Text(frame_texto,wrap=tk.WORD,yscrollcommand=scrollbar.set,font=('Arial',9))
texto_recomendaciones.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
scrollbar.config(command=texto_recomendaciones.yview)
  
def generar_recomendacion():
    texto_recomendaciones.delete(1.0,tk.END)
    pelicula=combotextbox.get()
    if not pelicula or pelicula not in base_neflix['Title'].values:
        messagebox.showwarning('Advertencia','Por favor seleccione una pelicula')
        return

    #vectorizar texto combinado
    tfidf=TfidfVectorizer(stop_words='english')
    tfidf_matrix=tfidf.fit_transform(base_neflix['Combinada'])

    #obtener indice de la pelicula seleccionada
    idx=base_neflix[base_neflix['Title']==pelicula].index[0]
    
    #calcular similitud del coseno
    cosine_sim=cosine_similarity(tfidf_matrix[idx],tfidf_matrix).flatten()
    print(cosine_sim)
    
    #ordenar por similitud y obtener lostop 5
    similar_indices=cosine_sim.argsort()[-6:][::-1]
    similar_indices=[i for i in similar_indices if i!=idx]
    recomendaciones_df=base_neflix.iloc[similar_indices].head(5)
    
    if not recomendaciones_df.empty:
        texto_recomendaciones.insert(tk.END,f'Recomendaciones basadas en {pelicula}:\n\n')
        #creando tabla simulada
        columnas=['Title','Director','Imdb Score','Produccion Country','Genres']    
        texto_recomendaciones.insert(tk.END,'\t\t'.join(columnas)+'\n')
        texto_recomendaciones.insert(tk.END,'-'*130+'\n')
        for _,fila in recomendaciones_df.iterrows():
            texto_recomendaciones.insert(
                tk.END,
                f'{fila["Title"]}\t\t{fila["Director"]}\t\t{fila["Imdb Score"]}\t\t{fila["Production Country"]}\t{fila["Genres"]}\n'
            )
    else:
        texto_recomendaciones.insert(tk.END, 'No se encontraron recomendaciones.')
    
boton_recomendar=tk.Button(raiz,text='Generar Recomendacion',command=generar_recomendacion,font=('Arial',12),bg='blue',fg='white')
boton_recomendar.pack(padx=10,pady=10)                           

raiz.mainloop()