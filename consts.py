import tkinter as tk
from tkinter import *
import sys


Time_Limit=300
gene_length=50

window = tk.Tk()
width=300
height=300
canvas=Canvas(window,width=width,height=height,bg="white")
canvas.pack()

# nucleobase=[[10,0],[0,10],[-10,0],[0,-10]] # 핵염기. AGCT. 동서남북
nucleobase=[[10,10],[-10,10],[-10,-10],[10,-10]] # 핵염기. AGCT. 동서, 서남, 남동, 동북

whole_generations=100
whole_individuals=1000