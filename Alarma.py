#Lorenzo Hernandez Hernandez 41s
from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import pygame, sys
from pygame.locals import *
root = Tk()
pygame.init()

horaas=StringVar()
minutus=StringVar()
Ventita = Frame(root, bg="#FF9999")
Ventita.pack(fill='both', expand=1)
root.geometry("400x450")


Tutl = Label(Ventita, text="Alarmita", font=("Purple Smile",10, "bold"), bg="#FF9999")
Tutl.place(relx=0.35,rely=0.05)

Etiquetitas = Label(Ventita, text="Hour", font=("Purple Smile",10), bg="#FF9999")
Etiquetitas.place(relx=0.15, rely=0.15)
Etihour = Entry(Ventita, textvariable=horaas).place(relx=0.35, rely=0.15)

Etimin = Label(Ventita, text="Minutes", font=("Purple Smile",10),bg="#FF9999")
Etimin.place(relx=0.15, rely=0.21)
entradaminutos = Entry(Ventita, textvariable=minutus).place(relx=0.35, rely=0.21)

bAlarma = Button(Ventita, text="Establece", font=("Purple Smile",10)).place(relx=0.30, rely=0.28)

def detiene():
     pygame.mixer.music.stop()
     Ventita.config(bg="#FF9999")
     Etihour.config(bg="#FF9999")
     Etimin.config(bg="#FF9999")
     Tutl.config(bg="#FF9999")
     Etiquetas.config(bg="#FF9999")

bStop = Button(Ventita, text="Stop", font=("Purple Smile",10), command=detiene).place(relx=0.33, rely=0.51)

def timees():
    horas = time.strftime("%H")
    minutos = time.strftime("%M")
    segundos = time.strftime("%S")

    horaLocal = horas + ":" + minutos + ":" + segundos
    Etiquetas.config(text=horaLocal)
    Etiquetas.after(1000, timees)

    alarmHour = horaas.get()
    alarmMin = minutus.get()

    if horas == alarmHour and minutos == alarmMin and segundos == "00":
        Ventita.config(bg="#FF6666")
        Etiquetitas.config(bg="#FF6666")
        Etimin.config(bg="#FF6666")
        Tutl.config(bg="#FF6666")
        Etiquetas.config(bg="#FF6666")

Etiquetas = Label(root, text="", font=("Purple Smile",30, "bold"),bg="#FF9999")
Etiquetas.place(relx=0.30, rely=0.35)

timees()
root.mainloop()