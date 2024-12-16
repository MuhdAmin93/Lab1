from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

def cda(x1, y1, x2, y2):
    """Алгоритм ЦДА"""
    img = Image.new('RGB', (500, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x, y = x1, y1
    for _ in range(steps + 1):
        draw.point((int(x), int(y)), fill=(0, 255, 0))
        x += x_increment
        y += y_increment
    return np.array(img)

def brezenhem(x1, y1, x2, y2):
    """Алгоритм Брезенхема"""
    img = Image.new('RGB', (500, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while True:
        draw.point((x1, y1), fill=(0, 255, 0))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return np.array(img)

def brezenhem_int(x1, y1, x2, y2):
    """Целочисленный алгоритм Брезенхема"""
    img = Image.new('RGB', (500, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while True:
        draw.point((x1, y1), fill=(0, 255, 0))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return np.array(img)

class AlgorithmPlot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Алгоритмы")
        self.geometry("500x500")
        
        self.label_start = tk.Label(self, text="Координаты начала отрезка (x, y):")
        self.label_start.pack(pady=5)
        
        self.entry_x1 = tk.Entry(self)
        self.entry_x1.pack(pady=5)
        self.entry_y1 = tk.Entry(self)
        self.entry_y1.pack(pady=5)

        self.label_end = tk.Label(self, text="Координаты конца отрезка (x, y):")
        self.label_end.pack(pady=5)
        
        self.entry_x2 = tk.Entry(self)
        self.entry_x2.pack(pady=5)
        self.entry_y2 = tk.Entry(self)
        self.entry_y2.pack(pady=5)
        
        self.label_algorithm = tk.Label(self, text="Выберите алгоритм:")
        self.label_algorithm.pack(pady=5)
        
        self.algorithm_combobox = ttk.Combobox(self, values=["ЦДА", "Брезенхем", "Целочисл. Брезенхем"])
        self.algorithm_combobox.pack(pady=5)
        self.algorithm_combobox.current(0)

        self.button_plot = tk.Button(self, text="Построить", command=self.plot)
        self.button_plot.pack(pady=20)

    def plot(self):
        x1 = int(self.entry_x1.get())
        y1 = int(self.entry_y1.get())
        x2 = int(self.entry_x2.get())
        y2 = int(self.entry_y2.get())
        algorithm = self.algorithm_combobox.get()

        if algorithm == "ЦДА":
            img = cda(x1, y1, x2, y2)
        elif algorithm == "Брезенхем":
            img = brezenhem(x1, y1, x2, y2)
        elif algorithm == "Целочисл. Брезенхем":
            img = brezenhem_int(x1, y1, x2, y2)
        
        plt.imshow(img)
        plt.title(algorithm)
        plt.axis('off')
        plt.show()

def main():
    app = AlgorithmPlot()
    app.mainloop()

if __name__ == "__main__":
    main()
