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
    # Load and validate the dataset
    try:
        # Read comma-separated data into a numpy array using genfromtxt
        data = np.genfromtxt(datafile_name, delimiter=',')
    except Exception as e:
        # Raise a clear error if file reading fails (e.g., file not found)
        raise ValueError(f"Error reading data file: {e}")

    # Validate data integrity to ensure robust clustering and visualization
    if np.any(np.isnan(data)) or np.any(np.isinf(data)):
        # Check for missing or infinite values that could disrupt K-Means
        raise ValueError("Data contains NaN or infinite values")
    if len(feature_names) != data.shape[1]:
        # Ensure feature names match the dataset's feature count
        raise ValueError("Number of feature names does not match data dimensions")
    if K <= 0 or K > data.shape[0]:
        # Validate K to prevent invalid clustering configurations
        raise ValueError("Invalid number of clusters K")

    # Perform K-Means clustering with optimized parameters
    # Use n_init=10 for low complexity, random_state=42 for reproducibility
    cluster_model = KMeans(n_clusters=K, n_init=10, random_state=42)
    cluster_model.fit(data)  # Fit model to assign cluster centers
    cluster_ids = cluster_model.predict(data)  # Assign each point to a cluster

    # Define a helper function to create a scatter plot matrix with histograms
    def show_scatterplot_matrix(X, y, feature_names):
        """
        Creates a scatter plot matrix with histograms on the diagonal, colored by cluster.

        Parameters:
            X: numpy array of shape (n_samples, n_features) - input data
            y: numpy array of shape (n_samples,) - cluster labels
            feature_names: list - names of features for axis labels

        Returns:
            fig: matplotlib Figure object
            ax: numpy array of Axes objects
        """
        # Initialize figure with a grid of subplots for each feature pair
        num_feat = X.shape[1]
        fig, ax = plt.subplots(num_feat, num_feat, figsize=(12, 12))
        plt.set_cmap('viridis')  # Set global colormap for consistent coloring

        # Define colors for histograms based on number of clusters
        hist_col = plt.get_cmap('viridis', K).colors

        # Precompute sorted indices for efficient histogram splitting
        inds = np.argsort(y)
        sorted_y = y[inds]

        # Cache feature data to avoid repeated indexing, improving performance
        feature_data = [X[:, i] for i in range(num_feat)]

        # Iterate over feature pairs to populate the scatter plot matrix
        for feature1 in range(num_feat):
            # Set axis labels for the first column (y) and top row (x)
            ax[feature1, 0].set_ylabel(feature_names[feature1])
            ax[0, feature1].set_xlabel(feature_names[feature1])
            ax[0, feature1].xaxis.set_label_position('top')

            for feature2 in range(num_feat):
                # Extract data for the current feature pair
                x_data = feature_data[feature1]
                y_data = feature_data[feature2]

                if feature1 != feature2:
                    # Create scatter plot for off-diagonal elements
                    # Use distinct markers and colormap for clear cluster visualization
                    ax[feature1, feature2].scatter(x_data, y_data, c=y, cmap='viridis', s=50, marker='*')
                else:
                    # Create histogram for diagonal elements, split by cluster
                    sorted_x = x_data[inds]
                    splits = np.split(sorted_x, np.unique(sorted_y, return_index=True)[1][1:])
                    for i, split in enumerate(splits):
                        # Plot each cluster's histogram with transparency for overlap
                        ax[feature1, feature2].hist(split, bins=20, color=hist_col[i], edgecolor='black', alpha=0.7)

        return fig, ax

    # Generate the visualization with a descriptive title
    username = "a34-shah (Aayush Shah_22085601)"  # UWE username for identification
    title = f"Visualisation of {K} clusters by {username}"
    fig, ax = show_scatterplot_matrix(data, cluster_ids, feature_names)
    fig.suptitle(title, fontsize=16, y=0.925)  # Position title above plot

    # Adjust layout to prevent label overlap, enhancing presentation
    fig.tight_layout(rect=[0, 0, 1, 0.95])

    # Save the visualization to the specified file
    fig.savefig('myVisualisation.jpg')

    # Return figure and axes for compatibility with marking system
    return fig, ax
    # <==== insert your code above here
