from tkinter import *
import tkinter as tk
import pandas as pd
import seaborn as sns
from pandas import DataFrame
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
plt.ioff()
import numpy as np
from tkinter import filedialog
from tkinter import messagebox

#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
#from tkinter import *
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
#NavigationToolbar2Tk)

# plot function is created for
# plotting the graph in
# tkinter window
def openfile():
    
   window.filename= filedialog.askopenfilename()
   messagebox.showinfo("showinfo", "File loaded successfuly")

def getkmeans():
    df=pd.read_csv(r"C:\Users\sai meghna reddy\Desktop\Mall_Customers.csv")
    df.drop(["CustomerID"], axis = 1, inplace=True)
    km = KMeans(n_clusters=5)
    clusters = km.fit_predict(df.iloc[:,1:])
    df["label"] = clusters
    fig = plt.figure(figsize=(30,10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df.Age[df.label == 0], df["Annual Income (k$)"][df.label == 0], df["Spending Score (1-100)"][df.label == 0], s=60, c='orange',label = 'Pinch Penny Customers')
    ax.scatter(df.Age[df.label == 1], df["Annual Income (k$)"][df.label == 1], df["Spending Score (1-100)"][df.label == 1], c='deepskyblue', s=60, label = 'Normal Customers')
    ax.scatter(df.Age[df.label == 2], df["Annual Income (k$)"][df.label == 2], df["Spending Score (1-100)"][df.label == 2], c='Magenta', s=60, label = 'Target Customers')
    ax.scatter(df.Age[df.label == 3], df["Annual Income (k$)"][df.label == 3], df["Spending Score (1-100)"][df.label == 3], c='red', s=60, label = 'Spenders')
    ax.scatter(df.Age[df.label == 4], df["Annual Income (k$)"][df.label == 4], df["Spending Score (1-100)"][df.label == 4], c='lime', s=60, label = 'Balanced Customers')
    ax.view_init(30, 185)
    plt.legend()
    plt.xlabel("Age")
    plt.ylabel("Annual Income (k$)")
    ax.set_zlabel('Spending Score (1-100)')
    plt.show()
    canvas = FigureCanvasTkAgg(fig,master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()

	# placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()





def annualincome():
    df=pd.read_csv(r"C:\Users\sai meghna reddy\Desktop\Mall_Customers.csv")
    df.drop(["CustomerID"], axis = 1, inplace=True)
    Income_Spend = df[['Annual Income (k$)' , 'Spending Score (1-100)']].iloc[: , :].values
    km = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    y_means = km.fit_predict(Income_Spend)
    plt.figure(figsize=(15,8))
    plt.scatter(Income_Spend[y_means == 0, 0], Income_Spend[y_means == 0, 1], s = 100, c = 'orange', label = 'Pinch Penny Customers')
    plt.scatter(Income_Spend[y_means == 1, 0], Income_Spend[y_means == 1, 1], s = 100, c = 'deepskyblue', label = 'Normal Customers')
    plt.scatter(Income_Spend[y_means == 2, 0], Income_Spend[y_means == 2, 1], s = 100, c = 'Magenta', label = 'Target Customers')
    plt.scatter(Income_Spend[y_means == 3, 0], Income_Spend[y_means == 3, 1], s = 100, c = 'red', label = 'Spenders')
    plt.scatter(Income_Spend[y_means == 4, 0], Income_Spend[y_means == 4, 1], s = 100, c = 'lime', label = 'Balanced Customers')
    plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:, 1], s = 50, c = 'black' , label = 'centeroid')
    plt.legend()
    plt.title('Customere Segmentation using Annual Income and Spending Score', fontsize = 15)
    plt.xlabel('Annual Income (k$)', fontsize = 12)
    plt.ylabel('Spending Score (1-100)', fontsize = 12)
    plt.show()  
    canvas = FigureCanvasTkAgg(fig,master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()

	# placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()



def kmeansk():
    df=pd.read_csv(r"C:\Users\sai meghna reddy\Desktop\Mall_Customers.csv")
    df.drop(["CustomerID"], axis = 1, inplace=True)
    clustering_df = df.iloc[:,[2,3]]
    km = KMeans(n_clusters=5, init='k-means++')
    km.fit(clustering_df)
    clusters = clustering_df.copy()
    clusters['Cluster_Prediction'] = km.fit_predict(clustering_df)
    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(15,20))
    ax[0,0].scatter(x=clusters[clusters['Cluster_Prediction'] == 4]['Annual Income (k$)'],
                    y=clusters[clusters['Cluster_Prediction'] == 4]['Spending Score (1-100)'],
                    s=40,edgecolor='black', linewidth=0.3, c='orange', label='Balanced Customers')
    ax[0,0].scatter(x=km.cluster_centers_[4,0], y=km.cluster_centers_[4,1],
                    s = 120, c = 'yellow',edgecolor='black', linewidth=0.3)
    ax[0,0].set(xlim=(0,140), ylim=(0,100), xlabel='Annual Income', ylabel='Spending Score', title='Balanced Customers')
    ax[0,1].scatter(x=clusters[clusters['Cluster_Prediction'] == 0]['Annual Income (k$)'],
                    y=clusters[clusters['Cluster_Prediction'] == 0]['Spending Score (1-100)'],
                    s=40,edgecolor='black', linewidth=0.3, c='deepskyblue', label='Pinch Penny Customers')
    ax[0,1].scatter(x=km.cluster_centers_[0,0], y=km.cluster_centers_[0,1],
                    s = 120, c = 'yellow',edgecolor='black', linewidth=0.3)
    ax[0,1].set(xlim=(0,140), ylim=(0,100), xlabel='Annual Income', ylabel='Spending Score', title='Pinch Penny Customers')
    ax[1,0].scatter(x=clusters[clusters['Cluster_Prediction'] == 2]['Annual Income (k$)'],
                    y=clusters[clusters['Cluster_Prediction'] == 2]['Spending Score (1-100)'],
                    s=40,edgecolor='black', linewidth=0.2, c='Magenta', label='Normal Customer')
    ax[1,0].scatter(x=km.cluster_centers_[2,0], y=km.cluster_centers_[2,1],
                    s = 120, c = 'yellow',edgecolor='black', linewidth=0.3)
    ax[1,0].set(xlim=(0,140), ylim=(0,100), xlabel='Annual Income', ylabel='Spending Score', title='Normal Customer')
    ax[1,1].scatter(x=clusters[clusters['Cluster_Prediction'] == 1]['Annual Income (k$)'],
                    y=clusters[clusters['Cluster_Prediction'] == 1]['Spending Score (1-100)'],
                    s=40,edgecolor='black', linewidth=0.3, c='red', label='Spenders')
    ax[1,1].scatter(x=km.cluster_centers_[1,0], y=km.cluster_centers_[1,1],
                    s = 120, c = 'yellow',edgecolor='black', linewidth=0.3)
    ax[1,1].set(xlim=(0,140), ylim=(0,100), xlabel='Annual Income', ylabel='Spending Score', title='Spenders')
    ax[2,0].scatter(x=clusters[clusters['Cluster_Prediction'] == 3]['Annual Income (k$)'],
                    y=clusters[clusters['Cluster_Prediction'] == 3]['Spending Score (1-100)'],
                    s=40,edgecolor='black', linewidth=0.3, c='lime', label='Target Customers')
    ax[2,0].scatter(x=km.cluster_centers_[3,0], y=km.cluster_centers_[3,1],
                    s = 120, c = 'yellow',edgecolor='black', linewidth=0.3, label='Centroids')
    ax[2,0].set(xlim=(0,140), ylim=(0,100), xlabel='Annual Income', ylabel='Spending Score', title='Target Customers')
    fig.delaxes(ax[2,1])
    fig.legend(loc='right')
    fig.suptitle('Customere Segmentation using Annual Income and Spending Score')
    plt.show()
    canvas = FigureCanvasTkAgg(fig,master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()

	# placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def kmeanage():
    df=pd.read_csv(r"C:\Users\sai meghna reddy\Desktop\Mall_Customers.csv")
    df.drop(["CustomerID"], axis = 1, inplace=True)
    Age_Spend = df[['Age' , 'Spending Score (1-100)']].iloc[: , :].values
    km= KMeans(n_clusters = 4, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    ymeans = km.fit_predict(Age_Spend)
    plt.figure(figsize=(15,8))
    plt.scatter(Age_Spend[ymeans == 0, 0], Age_Spend[ymeans == 0, 1], s = 100, c = 'orange', label = 'Normal Customer' )
    plt.scatter(Age_Spend[ymeans == 1, 0], Age_Spend[ymeans == 1, 1], s = 100, c = 'deepskyblue', label = 'Young Targets')
    plt.scatter(Age_Spend[ymeans == 2, 0], Age_Spend[ymeans == 2, 1], s = 100, c = 'Magenta', label = 'Regular Customer')
    plt.scatter(Age_Spend[ymeans == 3, 0], Age_Spend[ymeans == 3, 1], s = 100, c = 'red', label = 'Old Targets')
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s = 50, c = 'black')
    plt.legend()
    plt.title('Customere Segmentation using Annual Income and Spending Score', fontsize = 15)
    plt.xlabel('Age', fontsize = 12)
    plt.ylabel('Spending Score (1-100)', fontsize = 12)
    plt.show()    
    canvas = FigureCanvasTkAgg(fig,master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()

	# placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def gender():
    df=pd.read_csv(r"C:\Users\sai meghna reddy\Desktop\Mall_Customers.csv")
    df.drop(["CustomerID"], axis = 1, inplace=True)
    plt.figure(figsize=(15,8))
    sns.scatterplot(df['Annual Income (k$)'], df['Spending Score (1-100)'],hue=df['Gender'],
    palette= ['red','green'] ,alpha=0.6)
    plt.title('Distribution of Gender based on Annual Income and Spending Score', fontsize = 15)
    plt.xlabel('Annual Income', fontsize = 12)
    plt.ylabel('Spending Score', fontsize = 12)
    plt.show()    
    canvas = FigureCanvasTkAgg(fig,master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()

	# placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def genderage():
    df=pd.read_csv(r"C:\Users\sai meghna reddy\Desktop\Mall_Customers.csv")
    df.drop(["CustomerID"], axis = 1, inplace=True)
    plt.figure(figsize=(15,8))
    sns.scatterplot(df['Age'], df['Spending Score (1-100)'],hue=df['Gender'],palette= ['red','green'] ,alpha=0.6)
    plt.title('Distribution of Gender based on Age and Spending Score', fontsize = 15)
    plt.xlabel('Age', fontsize = 12)
    plt.ylabel('Spending Score', fontsize = 12)
    plt.show() 
    canvas = FigureCanvasTkAgg(fig,master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()

	# placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def summary():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(window)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Summary")

	# sets the geometry of toplevel
	newWindow.geometry("300x300")

	# A Label widget to show in toplevel
	Label(newWindow, text ="""Cluster lime - Balanced Customers : 
They earn less and spend less. We can see people have low annual income and low spending scores,this is quite reasonable as people having low salaries 
prefer to buy less, in fact, these are the wise people who know how to spend and save money. The shops/mall will be least interested in people 
belonging to this cluster.

Cluster orange - Pinch Penny Customers : Earning high and spending less. We see that people have high income but low spending scores, this is interesting. 
Maybe these are the people who are unsatisfied or unhappy by the mall’s services.These can be the prime targets of the mall, as they have the potential 
to spend money. So, the mall authorities will try to add new facilities so that they can attract these people and can meet their needs.

Cluster Skyblue - Normal Customer :
Customers are average in terms of earning and spending An Average consumer in terms of spending and Annual Income 
we see that people have average income and an average spending score, these people again will not be the prime targets of the shops or mall, 
but again they will be considered and other data analysis techniques may be used to increase their spending score.

Cluster Red - Spenders :
This type of customers earns less but spends more Annual Income is less but spending high, 
so can also be treated as potential target customer we can see that people have low income but higher spending scores, 
these are those people who for some reason love to buy products more often even though they have a low income. 
Maybe it’s because these people are more than satisfied with the mall services. 
The shops/malls might not target these people that effectively but still will not lose them.

Cluster pink - Target Customers :
Earning high and also spending high Target Customers. 
Annual Income High as well as Spending Score is high, so a target consumer. 
we see that people have high income and high spending scores, this is the ideal case for the mall or shops as these people are the prime sources of profit. 
These people might be the regular customers of the mall and are convinced by the mall’s facilities.""").pack()


def Summaryof():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(window)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Summary")

	# sets the geometry of toplevel
	newWindow.geometry("300x300")

	# A Label widget to show in toplevel
	Label(newWindow,
		text ="""Young Targets : Spending is high and Customers age is between 18-40. we see that people have high spending scores, 
this is the ideal case for the mall or shops as these people are the prime sources of profit. 


Old Targets: Spending Score is between 35-60 and Customers age is between 40-75.
The 65-and-older group did have the highest level of expenditures and these people are the prime sources of profit. 

Regular Customer : a person who purchases products or services from a person or business frequently.age is between 18-40 and Spending Score is between 25-65

Normal Cutomer - Customers are average in terms of spending""").pack()




# the main Tkinter window
window = Tk()

# setting the title
window.title('Customer Segmentation')

# dimensions of the main window
window.geometry("700x700")



open_button = Button(master= window,command = openfile,height =1, width =10,text ="import file")

# button that displays the plot


fplot_button = Button(master = window,
					command = kmeanage,
					height = 1,
					width = 10,
					text = "Age")


plot_button = Button(master = window,
					command = getkmeans,
					height = 1,
					width = 10,
					text = "3D View")

# place the button
# in main w


mb=Menubutton(window, text="Annual Income",relief=RAISED)
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

aiVar = IntVar()
fgVar = IntVar()
ifVar = IntVar()

mb.menu.add_checkbutton ( label="all ranges",variable=aiVar, command = annualincome)
mb.menu.add_checkbutton ( label="based on gender",variable=fgVar, command = gender)




ab=Menubutton(window, text="  Age   ",relief=RAISED)
ab.grid()
ab.menu = Menu ( ab, tearoff = 0 )
ab["menu"] =  ab.menu

ziVar = IntVar()
xgVar = IntVar()
cfVar = IntVar()

ab.menu.add_checkbutton ( label="all ranges",variable=ziVar, command = kmeanage)
ab.menu.add_checkbutton ( label="based on gender",variable=xgVar, command = genderage)





open_button.place(x=270, y=160)
plot_button.place(x=500, y=260)
mb.place(x=50, y = 260)
ab.place(x=270, y = 260)
window.configure(bg='#ff9a9e')


# run the gui
window.mainloop()
