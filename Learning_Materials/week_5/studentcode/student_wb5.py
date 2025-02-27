# DO NOT change anything except within the function
from approvedimports import *

def cluster_and_visualise(datafile_name:str, K:int, feature_names:list):
    """Function to get the data from a file, perform K-means clustering and produce a visualisation of results.

    Parameters
        ----------
        datafile_name: str
            path to data file

        K: int
            number of clusters to use

        feature_names: list
            list of feature names

        Returns
        ---------
        fig: matplotlib.figure.Figure
            the figure object for the plot

        axs: matplotlib.axes.Axes
            the axes object for the plot
    """
   # ====> insert your code below here
    # get the data from file into a numpy array
    data = np.genfromtxt(datafile_name, delimiter=',')


    # create a K-Means cluster model with  the specified number of clusters
    cluster_model = KMeans(n_clusters=K, n_init=10)
    # fit the model to the data
    cluster_model.fit(data)
    # Predict the cluster for each data point
    cluster_labels = cluster_model.predict(data)

    # Create the scatter plot and title
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(data[:, 0], data[:, 1], c=cluster_labels, cmap='viridis', s=50, marker='o')
    title = fig.suptitle(f"Visualisation of {K} clusters by <your_username>", fontsize=15)

    # Add axis labels
    ax.set_xlabel(feature_names[0], fontsize=12)
    ax.set_ylabel(feature_names[1], fontsize=12)

    # Add grid lines for better readability
    ax.grid(True)

    # create a canvas(fig) and axes to hold your visualisation
    # Save the plot to a file
    fig.savefig('myVisualisation.jpg')

    # make the visualisation
    # remember to put your user name into the title as specified


    # save it to file as specified

    # if you don't delete the line below there will be problem!
    raise NotImplementedError("Complete the function")

    return fig,ax
    cluster_and_visualise('iris_data.csv', 3, feature_names)

    # <==== insert your code above here
