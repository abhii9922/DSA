#Class for Matplotlib & Seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class plot_matplotlib:
    def plot(self,d):
        sns.set(rc={'figure.figsize':(5,5)})
        our_data=pd.DataFrame.from_dict(d)
        #print(dic['Counting Sort'])
        plt.figure(num='Results')

        #BarPlot
        bar_plot=sns.barplot(data=our_data)
        bar_plot.set(title='Runtimes')

        #Displot
        #dis_plot=sns.displot(data=our_data,x="Bubble Sort",kind="kde")
        #dis_plot.set(ylabel='Time',title='Runtimes')

        #PairGrid
        pair_grid=sns.PairGrid(our_data,diag_sharey=False,corner=True,height=1)
        pair_grid.map_lower(sns.scatterplot)
        pair_grid.map_diag(sns.kdeplot)
        pair_grid.add_legend()

        #Heatmap
        plt.figure(num='Results2')
        heat=sns.heatmap(our_data.iloc[:,1:],cmap='crest',linecolor='blue',cbar=True,square=True,annot=True)
        heat.set(ylabel='Time',title='Correlation')
        
        plt.show()
