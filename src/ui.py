import threading
import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import analysis
from algorithms import *


class AlgorithmAnalyzerApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sorting Algorithm Analyzer Tool")
        self.geometry("1080x720")
        self.configure(bg="white")

        self.algorithms = {
            "Bubble Sort": bubble_sort.sort,
            "Bucket Sort": bucket_sort.sort,
            "Counting Sort": counting_sort.sort,
            "Heap Sort": heap_sort.sort,
            "Merge Sort": merge_sort.sort,
            "Quicksort": quicksort.sort,
            "Radix Sort": radix_sort.sort,
        }

        ttk.Label(self, text="Enter a list of numbers (comma-separated):").pack(pady=10)
        self.input_entry = ttk.Entry(self, width=50)
        self.input_entry.pack(pady=5)

        self.start_button = ttk.Button(self, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack(pady=10)

        self.canvas_frame = ttk.Frame(self)
        self.canvas_frame.pack(pady=10)
        self.canvas = None


    def start_sorting(self):
        plt.close()

        input_data = self.input_entry.get().strip()

        # Validate input format
        try:
            input_data = [int(x.strip()) for x in input_data.split(',')]
        except ValueError:
            self.show_error("Invalid Input", "Please enter a valid list of comma-separated numbers.")
            return

        if not input_data:
            self.show_error("Empty Input", "Please enter a list of numbers.")
            return

        # Create a thread to run sorting algorithms
        sorting_thread = threading.Thread(target=self.run_sorting, args=(input_data,))
        sorting_thread.start()


    def run_sorting(self, input_data):
        # perform runtime analysis on a single array across all algorithms
        results = analysis.sorting_runtime_all(input_data, self.algorithms)
        self.display_results(results)


    def display_results(self, results):
        if self.canvas is not None:
            self.canvas.get_tk_widget().pack_forget()

        # Define a list of colors for each bar
        bar_colors = ['blue', 'green', 'red', 'purple']

        matplotlib.use("agg")
        plt.figure(figsize=(8, 4))

        times = [result[1] for result in results.values()]
        # sample values: times = [2,3,1,5]

        algorithms = list(results.keys())

        plt.barh(algorithms, times, color=bar_colors, height=0.5)
        plt.xlabel("Time Taken (s)")
        plt.title("Sorting Algorithm Efficiency")

        # Set a minimum time limit for the y-axis
        plt.xlim(xmin=0.000001)  # Adjust the multiplier as needed
        plt.subplots_adjust(left=0.25)

        self.canvas = FigureCanvasTkAgg(plt.gcf(), self.canvas_frame)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    

    def show_error(self, title, message):
        tk.messagebox.showerror(title, message)
