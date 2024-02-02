import matplotlib.pyplot as plt
def generarGrafica(dataFrame):
    #Agrupar datos del dataframe segun el analisis que quiera graficar
    
    promedioArboles=dataFrame.groupby('Vereda')['Arboles'].mean()
    

    #0. generando lista de colores
    colores=["#3D9637","#61DE59","#1BE80E"]

    #1. Generar una figura 
    plt.figure(figsize=(10,10))

    #2. Genero la grafica que deseo
    plt.bar(promedioArboles.index, promedioArboles.values, color=colores)

    #3. Agrego titulo a la gráfica
    plt.title("Promedios de arboles")
    
    #4. Etiqueta o nombre del eje X
    plt.xlabel("Ciudad")

    #5. Etiqueta o nombre del eje y
    plt.ylabel("Cantidad promedio")

    #6. Activar el grid
    plt.grid(True)

    #7. rotar los labels X
    plt.xticks(rotation=45)

    #7. Guardando nuestra grafica
    plt.savefig("./graphs/promedioArboles.png")
    print(promedioArboles)