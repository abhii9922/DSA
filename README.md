# Algorithm Efficiency Analysis Tool

Welcome to our repository :smile:

This Tool is designed to perform analysis and comparison of different algorithms. The tool takes an input of integers, performs sorting on it and displays the performance of each of the Algorithm over graphs.

We hope you find it useful :smiley:

<ins>The algorithms used are:</ins>
1. Bubble Sort
2. Bucket Sort
3. Counting Sort
4. Heap Sort
5. Insertion Sort
6. Merge Sort
7. Quicksort
8. Radix Sort
9. Selection Sort

<ins>The tool plots the following graphs:</ins>
1. Bar graph
2. Joint plot
3. LM plot

<ins>Application Requirements:</ins>
Python 3 (3.9 & above)
Refer to the requirements.txt file for other depedencies.
To install all the required depedencies:
1. Open Command Prompt (Windows), Terminal (Linux or Mac).
2. Head to the directory where this file is downloaded.
3. Install the requirements using the command: pip install -r requirements.txt

Ensure that you have execute permissions (or access as sudo user)


**Important:**
* The application is only designed for integers. It does not work for decimal Values and Strings.
* Be aware of entering large values as this may slow down the performance of your computer. This may potentially give rise erroneous data.
* The range of values entered must be the larger than the number of elements.


Sample Output (the tool will take care of the output, you needn't bother. Just store it in the format described above):
   Input Values       Algorithm  Space  Runtime
0         1,2,3     Bubble Sort      1     4.65
1         4,5,6     Bubble Sort      2     3.84
2         7,8,9     Bubble Sort      3     3.95
3      10,11,12     Bubble Sort      4     3.05
4      13,14,15     Bubble Sort      5     5.04
5         1,2,3      Merge Sort      3     3.23
6         4,5,6      Merge Sort      4     4.45
7         7,8,9      Merge Sort      2     1.83
8      10,11,12      Merge Sort      1     3.65
9      13,14,15      Merge Sort      6     2.34
10        1,2,3     Bucket Sort      4     5.78
11        4,5,6     Bucket Sort      2     4.76
12        7,8,9     Bucket Sort      1     3.23
13     10,11,12     Bucket Sort      5     4.43
14     13,14,15     Bucket Sort      3     3.43
15        1,2,3  Insertion Sort      2     2.54
16        4,5,6  Insertion Sort      3     3.23
17        7,8,9  Insertion Sort      5     4.43
18     10,11,12  Insertion Sort      2     3.43
19     13,14,15  Insertion Sort      4     2.54
20        1,2,3   Counting Sort      2     3.23
21        4,5,6   Counting Sort      6     4.10
22        7,8,9   Counting Sort      3     3.85
23     10,11,12   Counting Sort      1     3.33
24     13,14,15   Counting Sort      4     2.95

Feel free to add anything important :)
