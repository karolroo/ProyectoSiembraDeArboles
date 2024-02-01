#1. Importar el paquete o paquetes con los que voy
import pandas as pd
from helpers.creacionTabla import crearTabla
from helpers.creacionGrafica import generarGrafica

def analizarRegistroSiembras():
    #2. Sin importar la fuente (sql, xls, JSON, csv...)
    tabla=pd.read_csv('./data/bdsiembras.csv',encoding='utf-8')

    #3. Aplico filtros para limpiar o seleccionar datos
    #Filtro arboles de medellin con cantidantes superiores a 200
    filtroArbolesMedellin=tabla.query(" (Ciudad == 'Medellín') and (Arboles > 200 ) ") 
    crearTabla(filtroArbolesMedellin,"filtroArbolesMedellin")

    #Filtro Arboles de Santa Fe de Antioquia y veredas Tonusco Arriba y paso real
    filtroArbolesSFA = tabla.query("(Ciudad == 'Santa Fe de Antioquia') and (Vereda == 'Tonusco Arriba' or Vereda == 'Paso Real')")
    crearTabla(filtroArbolesSFA,"filtroArbolesSFA")

    #Siembras en el bagre mayores a 60
    filtroSiembrasBagre= tabla.query("(Ciudad == 'El Bagre') and (Arboles > 60 )")
    crearTabla(filtroSiembrasBagre, "filtroSiembrasBagre")
    #print(filtroSiembrasBagre)

    #Filtro de siembra de santa rosas de oso y veredas las cruces y mina vieja
    filtroSiembraRO= tabla.query("(Ciudad == 'Santa Rosa de Osos') and (Vereda == 'Las Cruces' or Vereda == 'Mina Vieja')")
    crearTabla(filtroSiembraRO, "filtroSiembraRO") 

    #Filtro de Siembras en Yondó
    filtroSiembrasYondo= tabla.query("Ciudad == 'Yondó' ")
    crearTabla(filtroSiembrasYondo, 'filtroSiembrasYondo')
    #print(filtroSiembrasYondo)
 

    #4. Graficando los dataframes
    generarGrafica(filtroArbolesMedellin)