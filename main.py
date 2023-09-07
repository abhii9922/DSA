from matplotlib_module import plot_matplotlib

#Test Dictionary
#algo_names={"Input Value","Bubble Sort","Counting Sort","Merge Sort","Bucket Sort"}
#"input_values":["1,2,3","4,5,6","7,8,9","10,11,12"]
d={"Input Values":["1,2,3","4,5,6","7,8,9","10,11,12"],"Bubble Sort":[4.65,3.84,3.95,3.05],"Counting Sort":[5.04,3.23,4.45,1.83],"Merge Sort":[3.65,2.34,5.78,4.76],"Bucket Sort":[3.23,4.43,3.43,2.54],"Insertion Sort":[3.23,4.43,3.43,2.54]}
"""
  Input Values  Bubble Sort  ...  Bucket Sort  Insertion Sort
0        1,2,3         4.65  ...         3.23            3.23
1        4,5,6         3.84  ...         4.43            4.43
2        7,8,9         3.95  ...         3.43            3.43
3     10,11,12         3.05  ...         2.54            2.54

[4 rows x 6 columns]
"""
#run_times=[[4.65,3.84,3.95,3.05],[5.04,3.23,4.45,1.83],[3.65,2.34,5.78,4.76],[3.23,4.43,3.43,2.54]]

plot_obj=plot_matplotlib()
plot_obj.plot(d)
del plot_obj
