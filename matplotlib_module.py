#Class for Matplotlib & Seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class plot_matplotlib:
    def plot(self,d):
        sns.set(rc={'figure.figsize':(5,5)})
        our_data=pd.DataFrame.from_dict(d)
        fig=plt.figure(num='Results')

        #BarPlot(Done)
        bar_plot=sns.barplot(data=our_data,x="Input Values",y="Runtime",hue="Algorithm")
        bar_plot.set(title='Runtimes')

        #Displot(Done)
        dis_plot=sns.displot(data=our_data,x='Runtime',kind="kde",hue="Algorithm")
        dis_plot.set(ylabel='Value',title='Distribution Plot')

        #Joint Plot(Done)
        sns.jointplot(data=our_data,x="Runtime",y="Space",height=5,hue="Algorithm",kind="scatter")

        #PairGrid (Done but not plotting this as we are already plotting Joint Plot)
        #pair_grid=sns.PairGrid(our_data,hue="Algorithm")
        #pair_grid=sns.PairGrid(our_data,diag_sharey=False,corner=True,x_vars=["Runtime"],y_vars=["Runtime"],height=1,hue="Algorithm")
        #pair_grid=sns.PairGrid(our_data,x_vars=["Runtime","Space"],y_vars=["Runtime","Space"],hue="Algorithm")
        #pair_grid.map(sns.scatterplot)
        #pair_grid.map_offdiag(sns.scatterplot)
        #pair_grid.map_diag(sns.kdeplot)
        #pair_grid.add_legend()

        #Heatmap (Not Useful, leaving it in the code for knowledge purposes)
        #plt.figure(num='Results2')
        #data=our_data.pivot(columns=["Input Values","Algorithm","Runtime"])
        #data=our_data.iloc[:,0:2]
        #print(data)
        #sns.heatmap(data,annot=True)
        #heat=sns.heatmap(our_data.iloc[:,0:2],cmap='crest',linecolor='blue',cbar=True,square=True,annot=True)
        #heat.set(ylabel='Time',title='Correlation')

        #Lmplot(Done)
        sns.lmplot(data=our_data,x="Runtime",y="Space",hue="Algorithm",height=3,col="Algorithm")

        #Display the plots
        plt.show()
