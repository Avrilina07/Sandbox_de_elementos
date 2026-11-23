import tkinter as tk
from tkinter import messagebox
import random
#==================================================================
#CONSTANTES Y CODIGOS DE LA MATRIZ
#==================================================================
#El mundo es una matriz cuadratica n x n
aire = 0 
arena = 1
agua = 2
piedra = 3
tierra = 4
fuego = 5
semilla = 6
pasto = 7  #Generado por interacciones; no seleccionable directamente
planta_1 = 8 #Planta: etapa 1[span8(start_span)[span_8(end_span)]]
planta_2 = 9 #Planta: etapa 2[span9(start_span)[span_9(end_span)]]
planta_3 = 10 #Planta: etapa 3[span10(start_span)[span_10(end_span)]]

#Colores asignados a cada elemento que se mostraran en pantalla
colores = {
    aire: "#87CEEB",  # Sky blue
    arena: "#E6c27a",
    agua: "#2980b9",
    piedra: "#7f8c8d",
    tierra: "#6e472b",
    fuego: "#e74c3c",
    semilla: "#d35400",
    pasto: "#27ae60",
    planta_1: "#58d68d",
    planta_2: "#2ecc71",
    planta_3: "#145a32"
}
