import threading
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.constants import *

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import seaborn as sns
import numpy as np
import pandas as pd

import random

import analysis
from algorithms import *


class AlgorithmAnalyzerApp(tk.Tk):

	def __init__(self):
		super().__init__()
		self.title("Sorting Algorithm Analyzer Tool")
		self.geometry("1400x860")
		self.style = ttk.Style("flatly")

		self.algorithms = {
			"Bubble Sort": bubble_sort.sort,
			"Bucket Sort": bucket_sort.sort,
			"Counting Sort": counting_sort.sort,
			"Heap Sort": heap_sort.sort,
			"Insertion Sort": insertion_sort.sort,
			"Merge Sort": merge_sort.sort,
			"Quicksort": quicksort.sort,
			"Radix Sort": radix_sort.sort,
			"Selection Sort": selection_sort.sort,
		}

		self.build_gui()


	# this method contains all the ui elements (i.e. form inputs, buttons, chart containers)
	def build_gui(self):		

		###### input_panel (left panel) - contains all input fields
		self.input_panel = ttk.Frame(self)
		self.input_panel.pack(side=LEFT, anchor=CENTER, fill=X, padx=20, pady=10)


		#### field group for the input array/s
		self.input_entry_label_frame = ttk.Labelframe(self.input_panel, text="Unsorted Data", bootstyle=PRIMARY)
		self.input_entry_label_frame.pack(padx=10, pady=10)
		self.input_entry_grid = ttk.Frame(self.input_entry_label_frame)
		self.input_entry_grid.pack(padx=10, pady=20)

		## radio buttons to determine if one array or multiple arrays
		self.input_array_num = tk.StringVar(value="one")

		self.input_array_num_radio_one_container = ttk.Frame(self.input_entry_grid)
		self.input_array_num_radio_one_container.grid(column=0, row=0, pady=5)

		self.input_array_num_radio_one = ttk.Radiobutton(self.input_array_num_radio_one_container, 
														text="Single Array",
														value="one",
														variable= self.input_array_num,
														command=self.show_hide_array_settings,
														bootstyle=PRIMARY)
		self.input_array_num_radio_one.pack(side=LEFT, anchor=CENTER, padx=20)
		ToolTip(self.input_array_num_radio_one, text="Use this to test algorithms on a single set of unsorted data.", bootstyle=(INFO, INVERSE))

		self.input_array_num_radio_many = ttk.Radiobutton(self.input_array_num_radio_one_container, 
														text="Multiple Arrays",
														value="many",
														variable= self.input_array_num,
														command=self.show_hide_array_settings,
														bootstyle=PRIMARY)
		self.input_array_num_radio_many.pack(side=LEFT, anchor=CENTER, padx=20)
		ToolTip(self.input_array_num_radio_many, text="Use this to test algorithms on multiple sets of unsorted data.", bootstyle=(INFO, INVERSE))


		## single array input fields
		self.input_array_entry = ttk.Entry(self.input_entry_grid, width=40, bootstyle=PRIMARY)
		self.input_array_entry.grid(column=0, row=1, padx=20, pady=10)
		ToolTip(self.input_array_entry, text="Enter a comma-separated list of integers or auto-generate a random integer list.", bootstyle=(INFO, INVERSE))

		# auto-generate section
		self.input_array_random_one_label_frame = ttk.Labelframe(self.input_entry_grid, text="Randomizer Settings", bootstyle=SECONDARY)
		self.input_array_random_one_label_frame.grid(ipadx=20, column=0, row=2)

		self.input_array_random_one_settings_row_1 = ttk.Frame(self.input_array_random_one_label_frame)
		self.input_array_random_one_settings_row_1.pack(padx=10, pady=10)

		ttk.Label(self.input_array_random_one_settings_row_1, text="Min Value:").pack(padx=10, expand=True, fill=X, side=LEFT)
		self.input_array_random_one_minval_entry = ttk.Entry(self.input_array_random_one_settings_row_1, width=5, bootstyle=SECONDARY)
		self.input_array_random_one_minval_entry.pack(expand=True, fill=X, side=LEFT)
		self.input_array_random_one_minval_entry.insert(0, "0")

		ttk.Label(self.input_array_random_one_settings_row_1, text="Max Value:").pack(padx=10, expand=True, fill=X, side=LEFT)
		self.input_array_random_one_maxval_entry = ttk.Entry(self.input_array_random_one_settings_row_1, width=5, bootstyle=SECONDARY)
		self.input_array_random_one_maxval_entry.pack(expand=True, fill=X, side=LEFT)
		self.input_array_random_one_maxval_entry.insert(0, "100")

		self.input_array_random_one_settings_row_2 = ttk.Frame(self.input_array_random_one_label_frame)
		self.input_array_random_one_settings_row_2.pack(padx=10)

		ttk.Label(self.input_array_random_one_settings_row_2, text="Num Elements:").pack(padx=10, expand=True, fill=X, side=LEFT)
		self.input_array_random_one_count_entry = ttk.Entry(self.input_array_random_one_settings_row_2, width=5, bootstyle=SECONDARY)
		self.input_array_random_one_count_entry.pack(expand=True, fill=X, side=LEFT, anchor=W)

		self.randomize_button = ttk.Button(self.input_array_random_one_label_frame, text="Auto-Generate List", bootstyle=SECONDARY, command=self.generate_random_list)
		self.randomize_button.pack(padx=10, pady=15, ipadx=50)
		ToolTip(self.randomize_button, text="Num elements >= length([min value, max value]).", bootstyle=(INFO, INVERSE))


		## multiple array input fields
		self.input_array_random_many_label_frame = ttk.Labelframe(self.input_entry_grid, text="Randomizer Settings", bootstyle=SECONDARY)
		self.input_array_random_many_label_frame.grid(ipadx=20, column=0, row=1)

		self.input_array_random_many_settings_row_1 = ttk.Frame(self.input_array_random_many_label_frame)
		self.input_array_random_many_settings_row_1.pack(padx=10, pady=10)

		ttk.Label(self.input_array_random_many_settings_row_1, text="Min Value:").pack(padx=10, expand=True, fill=X, side=LEFT)
		self.input_array_random_many_minval_entry = ttk.Entry(self.input_array_random_many_settings_row_1, width=5, bootstyle=PRIMARY)
		self.input_array_random_many_minval_entry.pack(expand=True, fill=X, side=LEFT)
		self.input_array_random_many_minval_entry.insert(0, "0")

		ttk.Label(self.input_array_random_many_settings_row_1, text="Max Value:").pack(padx=10, expand=True, fill=X, side=LEFT)
		self.input_array_random_many_maxval_entry = ttk.Entry(self.input_array_random_many_settings_row_1, width=5, bootstyle=PRIMARY)
		self.input_array_random_many_maxval_entry.pack(expand=True, fill=X, side=LEFT)
		self.input_array_random_many_maxval_entry.insert(0, "100")

		self.input_array_random_many_settings_row_2 = ttk.Frame(self.input_array_random_many_label_frame)
		self.input_array_random_many_settings_row_2.pack(padx=10)

		ttk.Label(self.input_array_random_many_settings_row_2, text="Num Elements:").pack(padx=10, expand=True, fill=X, side=LEFT)
		self.input_array_random_many_count_entry = ttk.Entry(self.input_array_random_many_settings_row_2, width=15, bootstyle=PRIMARY)
		self.input_array_random_many_count_entry.pack(expand=True, fill=X, side=LEFT, anchor=W)

		self.input_array_random_many_settings_row_3 = ttk.Frame(self.input_array_random_many_label_frame)
		self.input_array_random_many_settings_row_3.pack(padx=10, pady=10)

		ttk.Label(self.input_array_random_many_settings_row_3, text="Num Arrays:").pack(padx=10, expand=True, fill=X, side=LEFT)
		self.input_array_random_many_numarrays_entry = ttk.Entry(self.input_array_random_many_settings_row_3, width=5, bootstyle=PRIMARY)
		self.input_array_random_many_numarrays_entry.pack(expand=True, fill=X, side=LEFT, anchor=W)


		self.input_array_random_many_variedsize_checkbox_value = tk.IntVar(value=0) 	
		self.input_array_random_many_variedsize_checkbox = ttk.Checkbutton(self.input_array_random_many_settings_row_3,
																			text="Varied Sizes", command=self.varied_sizes_toggle_handler,
																			variable = self.input_array_random_many_variedsize_checkbox_value,
																			onvalue=1, offvalue=0,
																			bootstyle=(PRIMARY, SQUARE, TOGGLE))
		self.input_array_random_many_variedsize_checkbox.pack(padx=20, expand=True, fill=X, side=LEFT, anchor=CENTER)
		ToolTip(self.input_array_random_many_variedsize_checkbox, text="If this is on, num elements will be treated as a comma-separated list of array-sizes and num arrays will be ignored.", bootstyle=(INFO, INVERSE))

		# make sure the proper input array settings are shown
		self.show_hide_array_settings()


		#### field group for the analysis type radio buttons
		self.analysis_type_label_frame = ttk.Labelframe(self.input_panel, text="Analysis Type", bootstyle=INFO)
		self.analysis_type_label_frame.pack(padx=10, pady=10)
		self.analysis_type_radio_container = ttk.Frame(self.analysis_type_label_frame)
		self.analysis_type_radio_container.pack(padx=20, pady=10)

		self.analysis_type_selected = tk.StringVar(value="time")	# reading this value for selected analysis type

		self.analysis_type_radio_time = ttk.Radiobutton(self.analysis_type_radio_container, 
														text="Runtime",
														value="time",
														variable= self.analysis_type_selected,
														bootstyle=(INFO, TOOLBUTTON, OUTLINE))
		self.analysis_type_radio_time.pack(side=LEFT, anchor=CENTER, padx=10, pady=5)

		self.analysis_type_radio_space = ttk.Radiobutton(self.analysis_type_radio_container, 
														text="Space",
														value="space",
														variable= self.analysis_type_selected,
														bootstyle=(INFO, TOOLBUTTON, OUTLINE))
		self.analysis_type_radio_space.pack(side=LEFT, anchor=CENTER, padx=10, pady=5)

		self.analysis_type_radio_spacetime = ttk.Radiobutton(self.analysis_type_radio_container, 
														text="Space & Runtime",
														value="spacetime",
														variable= self.analysis_type_selected,
														bootstyle=(INFO, TOOLBUTTON, OUTLINE))
		self.analysis_type_radio_spacetime.pack(side=LEFT, anchor=CENTER, padx=10, pady=5)


		#### field group for the algorithm checkboxes
		self.algo_checkbox_label_frame = ttk.Labelframe(self.input_panel, text="Available Algorithms", bootstyle=DARK)
		self.algo_checkbox_label_frame.pack(padx=10, pady=10)
		self.algo_checkbox_container = ttk.Frame(self.algo_checkbox_label_frame)
		self.algo_checkbox_container.pack(padx=15, pady=10)

		self.algorithm_checkboxes = {}
		self.algorithm_checkboxes_selected = {}

		cbox_count = 0 		# this is to determine location in grid 
		for key in self.algorithms:
			self.algorithm_checkboxes_selected[key] = tk.IntVar(value=1) 	# reading this value for selected algorithms
			self.algorithm_checkboxes[key] = ttk.Checkbutton(self.algo_checkbox_container,
																bootstyle=DARK,
																text=key,
																variable = self.algorithm_checkboxes_selected[key],
																onvalue=1, offvalue=0,
																width=10)
			self.algorithm_checkboxes[key].grid(column=cbox_count%3, row=cbox_count//3, padx=10, pady=5)
			cbox_count += 1


		#### run analysis button
		self.run_analysis_button = ttk.Button(self.input_panel, text="Run Analysis", bootstyle=PRIMARY, command=self.check_input_and_validate)
		self.run_analysis_button.pack(pady=20, ipadx=150, ipady=10)


		###### output_panel (right panel) - displays results
		self.output_panel = ttk.Frame(self)
		self.output_panel.pack(side=LEFT, anchor=CENTER, expand=TRUE, fill=X, padx=10, pady=10)

		## container for the visualizations
		self.canvas_frame = ttk.Frame(self.output_panel)
		self.canvas_frame.pack(pady=10)
		self.canvas = None
		self.canvas_spacetime = None

		## container to display sorted array values
		self.output_details_container = ttk.Frame(self.output_panel)
		self.output_details_container.pack(pady=20)


		###### miscellaneous elements
		# self.scrollbar = ttk.Scrollbar(self.input_panel, orient='vertical')
		# self.scrollbar.pack(side="right", fill="y")


	def show_hide_array_settings(self):
		# show the proper input fields
		if self.input_array_num.get() == "one":
			# one array option was selected
			self.input_array_random_many_label_frame.grid_remove()

			self.input_array_entry.grid(column=0, row=1, padx=20, pady=10)
			self.input_array_random_one_label_frame.grid(column=0, row=2)
		else: 	# self.input_array_num.get() == "many"
			# multiple arrays option was selected
			self.input_array_entry.grid_remove()
			self.input_array_random_one_label_frame.grid_remove()

			self.input_array_random_many_label_frame.grid(column=0, row=1, padx=20, pady=10)

		
	def varied_sizes_toggle_handler(self):
		is_checked = self.input_array_random_many_variedsize_checkbox_value.get()

		# disable the num arrays input field if checked
		if is_checked == 1:
			self.input_array_random_many_numarrays_entry.configure(state="readonly")
		else:
			self.input_array_random_many_numarrays_entry.configure(state="!readonly")


	def generate_random_list(self):
		# Generate random integers & convert to a comma-separated string
		min_val = int(self.input_array_random_one_minval_entry.get())
		max_val = int(self.input_array_random_one_maxval_entry.get())
		count = int(self.input_array_random_one_count_entry.get())

		random_list = random.sample(range(min_val, max_val), count)
		list_str = ",".join([str(i) for i in random_list if i])

		self.input_array_entry.delete(0, tk.END)
		self.input_array_entry.insert(0, list_str)


	def reset_output_panel(self):
		# reset any visualizations
		plt.close("all")


	def check_input_and_validate(self):
		self.reset_output_panel()

		# determine if single or multiple, then validate accordingly
		if self.input_array_num.get() == "many":		# multiple arrays
			# get min and max value
			min_val = int(self.input_array_random_many_minval_entry.get())
			max_val = int(self.input_array_random_many_maxval_entry.get())

			# check if "varied sizes" is activated and handle accordingly
			is_checked = self.input_array_random_many_variedsize_checkbox_value.get()

			if is_checked == 1:
				# treat "num elements" as a list to generate random arrays
				array_sizes =  self.input_array_random_many_count_entry.get().strip()

				array_sizes = [int(x.strip()) for x in array_sizes.split(',')]

				input_data = {}
				idx = 0
				for array_size in array_sizes:
					key = "Array " + str(idx + 1) + " (n=" + str(array_size) + ")"
					input_data[key] = random.sample(range(min_val, max_val), array_size)
					idx += 1

			else:
				# generate N random arrays where N is the value specified by "num arrays"
				array_size =  int(self.input_array_random_many_count_entry.get())
				num_arrays = int(self.input_array_random_many_numarrays_entry.get())

				input_data = {}
				for n in range(0, num_arrays):
					key = "Array " + str(n + 1)
					input_data[key] = random.sample(range(min_val, max_val), array_size)
			
		else:												# single array
			input_data = self.input_array_entry.get().strip()

			# validate array input format
			try:
				input_data = [int(x.strip()) for x in input_data.split(',')]
			except ValueError:
				# extra symbols/non-integers detected
				Messagebox.show_error("Invalid Input. Please enter a valid list of comma-separated integers.", "Error")
				return

			if not input_data:
				# no data provided
				Messagebox.show_error("Empty Input. Please enter a list of integers.", "Error")
				return


		# prepare selected algorithms
		self.selected_algorithms = {}
		for algorithm, var in self.algorithm_checkboxes_selected.items():
			if var.get() == 1:
				self.selected_algorithms[algorithm] = self.algorithms[algorithm]

		# validate if at least one algorithm was selected
		if len(self.selected_algorithms) == 0:
			# no algorithms were checked
			Messagebox.show_error("Select at least one algorithm from the available.", "Error")
			return


		# create a thread to run sorting algorithms
		sorting_thread = threading.Thread(target=self.start_analysis, args=(input_data,))
		sorting_thread.start()


	def start_analysis(self, input_data):
		selected_analysis_type = self.analysis_type_selected.get()
		results = {}
		
		if self.input_array_num.get() == "many":
			# perform analysis on multiple arrays across all the selected algorithms
			for key, unsorted_data in input_data.items():
				results[key] = {}
				results[key]["unsorted_data"] = unsorted_data

				# time complexity analysis
				if selected_analysis_type == "time":
					results[key]["result"] = analysis.sorting_runtime_all(unsorted_data, self.selected_algorithms)

				# space complexity analysis
				elif selected_analysis_type == "space":
					results[key]["result"] = analysis.sorting_memory_all(unsorted_data, self.selected_algorithms)

				# space-time analysis
				elif selected_analysis_type == "spacetime":
					results[key]["result"] = {}
					results[key]["result"]["space"] = analysis.sorting_memory_all(unsorted_data, self.selected_algorithms)
					results[key]["result"]["time"] = analysis.sorting_runtime_all(unsorted_data, self.selected_algorithms)

		else:
			# perform analysis on a single array across all the selected algorithms
			results["unsorted_data"] = input_data

			# time complexity analysis
			if selected_analysis_type == "time":
				results["result"] = analysis.sorting_runtime_all(input_data, self.selected_algorithms)

			# space complexity analysis
			elif selected_analysis_type == "space":
				results["result"] = analysis.sorting_memory_all(input_data, self.selected_algorithms)

			# space-time analysis
			elif selected_analysis_type == "spacetime":
				results["result"] = {}
				results["result"]["space"] = analysis.sorting_memory_all(input_data, self.selected_algorithms)
				results["result"]["time"] = analysis.sorting_runtime_all(input_data, self.selected_algorithms)


		# start visualization
		df = self.convert_to_df(results)
		print(results)
		self.display_results(df)
		return

	def convert_to_df(self, results):
		selected_analysis_type = self.analysis_type_selected.get()

		# initialize dataframe
		df = {
			"Input": [],
			"Algorithm": [],
			"Space": [],
			"Runtime": [],
		}

		if self.input_array_num.get() == "many":
			for key, unsorted_data in results.items():
				# assign values depending on the analysis type
				if selected_analysis_type == "time":
					for algorithm, result_data in results[key]["result"].items():
						df["Input"].append(key)
						df["Algorithm"].append(algorithm)
						df["Runtime"].append(result_data[1])

				elif selected_analysis_type == "space":
					for algorithm, result_data in results[key]["result"].items():
						df["Input"].append(key)
						df["Algorithm"].append(algorithm)
						df["Space"].append(result_data[1])

				elif selected_analysis_type == "spacetime":
					for algorithm in results[key]["result"]["space"]:
						df["Input"].append(key)
						df["Algorithm"].append(algorithm)
						df["Space"].append(results[key]["result"]["space"][algorithm][1])
						df["Runtime"].append(results[key]["result"]["time"][algorithm][1])
					
		else: 	# self.input_array_num.get() == "one"
			if selected_analysis_type == "time":
				for algorithm, result_data in results["result"].items():
					df["Input"].append("Array")
					df["Algorithm"].append(algorithm)
					df["Runtime"].append(result_data[1])

			elif selected_analysis_type == "space":
				for algorithm, result_data in results["result"].items():
					df["Input"].append("Array")
					df["Algorithm"].append(algorithm)
					df["Space"].append(result_data[1])

			elif selected_analysis_type == "spacetime":
				for algorithm in results["result"]["space"]:
					df["Input"].append("Array")
					df["Algorithm"].append(algorithm)
					df["Space"].append(results["result"]["space"][algorithm][1])
					df["Runtime"].append(results["result"]["time"][algorithm][1])

		return df


	def display_results(self, df):
		if self.canvas is not None:
			self.canvas.get_tk_widget().pack_forget()

		if self.canvas_spacetime is not None:
			self.canvas_spacetime.pack_forget()

		selected_analysis_type = self.analysis_type_selected.get()

		matplotlib.use("agg")	# this suppresses some warnings and errors

		# resolve any key length mismatch issues
		if selected_analysis_type == "time":
			del df["Space"]
		elif selected_analysis_type == "space":
			del df["Runtime"]

		data = pd.DataFrame.from_dict(df)

		# set the corresponding visuals depending on the selected analysis
		if selected_analysis_type == "time":
			sns.set(rc={'figure.figsize':(10,5)})

			bar_plot = sns.barplot(data=data,
									x="Input",
									y="Runtime",
									hue="Algorithm"	)
			bar_plot.set(title='Runtime Complexity Analysis')

			self.canvas = FigureCanvasTkAgg(plt.gcf(), self.canvas_frame)
			self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

		elif selected_analysis_type == "space":
			sns.set(rc={'figure.figsize':(10,5)})

			bar_plot = sns.barplot(data=data,
									x="Input",
									y="Space",
									hue="Algorithm"	)
			bar_plot.set(title='Space (Memory) Complexity Analysis')

			self.canvas = FigureCanvasTkAgg(plt.gcf(), self.canvas_frame)
			self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
			

		elif selected_analysis_type == "spacetime":
			sns.set(rc={'figure.figsize':(11.7,8.27)})

			self.canvas_spacetime = ttk.Notebook(self.canvas_frame, bootstyle=SECONDARY)
			self.canvas_spacetime.pack(padx=20, pady=20)

			tab_1 = ttk.Frame(self.canvas_spacetime)
			tab_2 = ttk.Frame(self.canvas_spacetime)

			plot_1 = sns.jointplot(data=data,
									x="Runtime",
									y="Space",
									height=8.27,
									hue="Algorithm",
									kind="scatter"	)
			tab_1_plot = FigureCanvasTkAgg(plt.gcf(), tab_1)
			tab_1_plot.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=20, pady=20)

			plot_2 = sns.lmplot(data=data,
									x="Runtime",
									y="Space",
									hue="Algorithm",
									height=8.27,
									aspect=11.7/8.27,
									# col="Algorithm",
									ci=None 	)
			tab_2_plot = FigureCanvasTkAgg(plt.gcf(), tab_2)
			tab_2_plot.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=20, pady=20)

			self.canvas_spacetime.add(tab_1, text="Scatter Plot")
			self.canvas_spacetime.add(tab_2, text="Scatter Plot w/ Regression Lines")
	

	def show_error(self, title, message):
		tk.messagebox.showerror(title, message)
