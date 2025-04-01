from approvedimports import *

def make_xor_reliability_plot(train_x, train_y):
    """ Insert code below to  complete this cell according to the instructions in the activity descriptor.
    Finally it should return the fig and axs objects of the plots created.

    Parameters:
    -----------
    train_x: numpy.ndarray
        feature values

    train_y: numpy array
        labels

    Returns:
    --------
    fig: matplotlib.figure.Figure
        figure object

    ax: matplotlib.axes.Axes
        axis
    """

    # ====> insert your code below here

# ====> insert your code below here

    # Define range of hidden layer widths
    hidden_layer_width = list(range(1, 11))  # [1, 2, ..., 10]

    # Initialize arrays to store results
    successes = np.zeros(10, dtype=int)  # 1D array for success counts (use int to avoid float issues)
    epochs = np.zeros((10, 10))  # 2D array for epochs per successful run

    # Nested loops to test each hidden layer size 10 times
    for h_nodes in hidden_layer_width:
        for repetition in range(10):
            # Configure MLP with one hidden layer of h_nodes neurons
            # Ensure random_state is set to repetition for reproducibility
            xorMLP = MLPClassifier(
                hidden_layer_sizes=(h_nodes,),
                max_iter=1000,
                alpha=1e-4,
                solver="sgd",
                learning_rate_init=0.1,
                random_state=repetition  # Critical: use repetition as random_state
            )

            # Fit the model
            xorMLP.fit(train_x, train_y)

            # Measure accuracy
            accuracy = 100 * xorMLP.score(train_x, train_y)

            # If 100% accuracy, update success and epoch counts
            if accuracy == 100:
                successes[h_nodes - 1] += 1
                epochs[h_nodes - 1][repetition] = xorMLP.n_iter_

    # Calculate efficiency (mean epochs for successful runs or 1000 if no successes)
    efficiency = np.zeros(10)
    for i in range(10):
        if successes[i] > 0:
            efficiency[i] = np.mean(epochs[i][epochs[i] > 0])  # Mean of non-zero epochs
        else:
            efficiency[i] = 1000  # Default value for no successful runs

    # Create plots
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Left plot: Reliability (Success Count, not rate)
    axs[0].plot(hidden_layer_width, successes, 'b-')  # Plot raw success counts, not rates
    axs[0].set_title("Reliability")
    axs[0].set_xlabel("Hidden Layer Width")
    axs[0].set_ylabel("Success Rate")
    axs[0].grid(True)

    # Right plot: Efficiency (Mean Epochs)
    axs[1].plot(hidden_layer_width, efficiency, 'r-')
    axs[1].set_title("Efficiency")
    axs[1].set_xlabel("Hidden Layer Width")
    axs[1].set_ylabel("Mean Epochs")
    axs[1].grid(True)

    plt.tight_layout()

    # <==== insert your code above here

    return fig, axs
