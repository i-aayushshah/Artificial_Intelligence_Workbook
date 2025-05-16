from approvedimports import *

def make_xor_reliability_plot(train_x, train_y):
    """ Insert code below to complete this cell according to the instructions in the activity descriptor.
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

    ### Input Validation ###
    # Let's make sure the input data is valid before proceeding!
    # Checks: train_x and train_y are NumPy arrays, not empty, and have matching shapes.
    try:
        if not isinstance(train_x, np.ndarray) or not isinstance(train_y, np.ndarray):
            raise ValueError("train_x and train_y must be NumPy arrays 📊")
        if train_x.size == 0 or train_y.size == 0:
            raise ValueError("Input arrays cannot be empty 😞")
        if train_x.shape[0] != train_y.shape[0]:
            raise ValueError("train_x and train_y must have the same number of samples 🔢")
    except ValueError as e:
        print(f"🚨 Error: {e}")
        raise

    # Define range of hidden layer widths
    hidden_layer_width = list(range(1, 11))  # [1, 2, ..., 10]

    # Initialize arrays to store results
    successes = np.zeros(10, dtype=int)  # 1D array for success counts (use int to avoid float issues)
    epochs = np.zeros((10, 10))  # 2D array for epochs per successful run

    ### Model Training Loop ###
    # We're training MLPs with different hidden layer sizes and repetitions.
    # Error handling ensures the model trains correctly and indices are valid.
    try:
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

                ### Training the MLP ###
                # Fit might fail if data is invalid or training diverges.
                try:
                    # Fit the model
                    xorMLP.fit(train_x, train_y)
                except Exception as e:
                    print(f"🚨 MLP training failed for h_nodes={h_nodes}, repetition={repetition}: {e}")
                    continue  # Skip to next repetition

                # Measure accuracy
                accuracy = 100 * xorMLP.score(train_x, train_y)

                # If 100% accuracy, update success and epoch counts
                if accuracy == 100:
                    ### Success! Update arrays ###
                    # Ensure index is valid before updating
                    if 0 <= h_nodes - 1 < len(successes) and 0 <= repetition < epochs.shape[1]:
                        successes[h_nodes - 1] += 1
                        epochs[h_nodes - 1][repetition] = xorMLP.n_iter_
                    else:
                        print(f"🚨 Index error for h_nodes={h_nodes}, repetition={repetition}")
    except Exception as e:
        print(f"🚨 Error in training loop: {e}")
        raise

    ### Efficiency Calculation ###
    # Calculate mean epochs for successful runs, default to 1000 if none.
    # Handle cases where no runs succeeded to avoid NaN or division errors.
    efficiency = np.zeros(10)
    for i in range(10):
        if successes[i] > 0:
            ### Compute mean of non-zero epochs ###
            try:
                efficiency[i] = np.mean(epochs[i][epochs[i] > 0])  # Mean of non-zero epochs
            except Exception as e:
                print(f"🚨 Error computing mean for hidden layer {i+1}: {e}")
                efficiency[i] = 1000  # Fallback value
        else:
            efficiency[i] = 1000  # Default value for no successful runs

    ### Plotting Results ###
    # Create plots, handle potential matplotlib errors.
    try:
        # Create plots
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))

        # Left plot: Reliability (Success Count, not rate)
        ax[0].plot(hidden_layer_width, successes, 'b-')  # Plot raw success counts, not rates
        ax[0].set_title("Reliability")
        ax[0].set_xlabel("Hidden Layer Width")
        ax[0].set_ylabel("Success Rate")
        ax[0].grid(True)

        # Right plot: Efficiency (Mean Epochs)
        ax[1].plot(hidden_layer_width, efficiency, 'r-')
        ax[1].set_title("Efficiency")
        ax[1].set_xlabel("Hidden Layer Width")
        ax[1].set_ylabel("Mean Epochs")
        ax[1].grid(True)

        plt.tight_layout()
    except Exception as e:
        print(f"🚨 Error creating plots: {e}")
        raise

    # <==== insert your code above here

    return fig, ax

# make sure you have the packages needed
from approvedimports import *

#this is the class to complete where indicated
class MLComparisonWorkflow:
    """ class to implement a basic comparison of supervised learning algorithms on a dataset """

    def __init__(self, datafilename:str, labelfilename:str):
        """ Method to load the feature data and labels from files with given names,
        and store them in arrays called data_x and data_y.

        You may assume that the features in the input examples are all continuous variables
        and that the labels are categorical, encoded by integers.
        The two files should have the same number of rows.
        Each row corresponding to the feature values and label
        for a specific training item.
        """
        # Define the dictionaries to store the models, and the best performing model/index for each algorithm
        self.stored_models:dict = {"KNN":[], "DecisionTree":[], "MLP":[]}
        self.best_model_index:dict = {"KNN":0, "DecisionTree":0, "MLP":0}
        self.best_accuracy:dict = {"KNN":0, "DecisionTree":0, "MLP":0}

        # Load the data and labels
        # ====> insert your code below here
        ### File Loading and Validation ###
        # Load feature and label data from CSV files using numpy's genfromtxt.
        # Ensure files exist, are readable, and contain valid numeric data.
        # Validate that feature and label arrays have the same number of rows
        # and that features are 2D (rows x columns) and labels are 1D (rows).
        try:
            self.data_x = np.genfromtxt(datafilename, delimiter=",")
            self.data_y = np.genfromtxt(labelfilename, delimiter=",")
            # Check array shapes and compatibility
            if not isinstance(self.data_x, np.ndarray) or not isinstance(self.data_y, np.ndarray):
                raise ValueError("Loaded data must be valid NumPy arrays")
            if len(self.data_x.shape) != 2:
                raise ValueError("Feature data must be a 2D array (rows x features)")
            if len(self.data_y.shape) != 1:
                raise ValueError("Label data must be a 1D array (rows)")
            if self.data_x.shape[0] != self.data_y.shape[0]:
                raise ValueError("Feature and label files must have the same number of rows")
            if self.data_x.shape[0] == 0 or self.data_y.shape[0] == 0:
                raise ValueError("Input files cannot be empty")
        except FileNotFoundError as e:
            print(f"🚨 File Error: One or both files not found. Check if '{datafilename}' and '{labelfilename}' exist in the correct directory")
            raise
        except ValueError as e:
            print(f"🚨 File Error: Invalid data in files. Ensure '{datafilename}' and '{labelfilename}' contain numeric data with comma delimiters")
            raise
        except Exception as e:
            print(f"🚨 File Error: Failed to load files due to an unexpected issue: {e}")
            raise
        # <==== insert your code above here

    def preprocess(self):
        """ Method to
           - separate it into train and test splits (using a 70:30 division)
           - apply the preprocessing you think suitable to the data
           - create one-hot versions of the labels for the MLP if ther are more than 2 classes

           Remember to set random_state = 12345 if you use train_test_split()
        """
        # ====> insert your code below here
        ### Data Splitting ###
        # Split the dataset into 70% training and 30% testing sets.
        # Use stratified splitting to maintain class distribution.
        # Ensure input data is valid and non-empty.
        try:
            self.train_x, self.test_x, self.train_y, self.test_y = train_test_split(
                self.data_x, self.data_y, test_size=0.3, stratify=self.data_y, random_state=12345
            )
            if len(self.train_x) == 0 or len(self.test_x) == 0:
                raise ValueError("Splitting resulted in empty training or testing sets")
        except Exception as e:
            print(f"🚨 Split Error: Failed to split data. Ensure data_x and data_y are valid and non-empty: {e}")
            raise

        # Normalize features
        ### Feature Normalization ###
        # Scale feature values to the range [0,1] using MinMaxScaler.
        # This ensures all features contribute equally to model training.
        try:
            scaler = MinMaxScaler()
            self.train_x = scaler.fit_transform(self.train_x)
            self.test_x = scaler.transform(self.test_x)
        except Exception as e:
            print(f"🚨 Normalization Error: Failed to normalize features. Ensure features are numeric and valid: {e}")
            raise

        # Check if more than 2 classes for one-hot encoding
        ### One-Hot Encoding for MLP ###
        # If there are more than two classes, create one-hot encoded labels
        # for the MLP classifier to handle multi-class problems.
        try:
            unique_labels = np.unique(self.data_y)
            if len(unique_labels) > 2:
                # Create one-hot for MLP
                self.train_y_mlp = np.zeros((len(self.train_y), len(unique_labels)))
                self.test_y_mlp = np.zeros((len(self.test_y), len(unique_labels)))
                for i in range(len(self.train_y)):
                    self.train_y_mlp[i][int(self.train_y[i])] = 1
                for i in range(len(self.test_y)):
                    self.test_y_mlp[i][int(self.test_y[i])] = 1
            else:
                self.train_y_mlp = self.train_y
                self.test_y_mlp = self.test_y
        except Exception as e:
            print(f"🚨 Encoding Error: Failed to create one-hot labels. Ensure labels are valid integers: {e}")
            raise
        # <==== insert your code above here

    def run_comparison(self):
        """ Method to perform a fair comparison of three supervised machine learning algorithms.
        Should be extendable to include more algorithms later.

        For each of the algorithms KNearest Neighbour, DecisionTreeClassifer and MultiLayerPerceptron
        - Applies hyper-parameter tuning to find the best combination of relevant values for the algorithm
         -- creating and fitting model for each combination,
            then storing it in the relevant list in a dictionary called self.stored_models
            which has the algorithm names as the keys and  lists of stored models as the values
         -- measuring the accuracy of each model on the test set
         -- keeping track of the best performing model for each algorithm, and its index in the relevant list so it can be retrieved.

        """
        # ====> insert your code below here
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.neural_network import MLPClassifier

        # KNN: Test k values {1,3,5,7,9} - no random_state needed
        ### KNN Model Training ###
        # Train K-Nearest Neighbors models with different numbers of neighbors.
        # Store each model and track the best-performing one based on test accuracy.
        try:
            for k in [1, 3, 5, 7, 9]:
                knn = KNeighborsClassifier(n_neighbors=k)  # Removed random_state
                knn.fit(self.train_x, self.train_y)
                accuracy = 100 * knn.score(self.test_x, self.test_y)
                self.stored_models["KNN"].append(knn)
                idx = len(self.stored_models["KNN"]) - 1
                if accuracy > self.best_accuracy["KNN"]:
                    self.best_accuracy["KNN"] = accuracy
                    self.best_model_index["KNN"] = idx
        except Exception as e:
            print(f"🚨 KNN Error: Failed to train or evaluate KNN models. Check data shapes and values: {e}")
            raise

        # Decision Tree: Test combinations of max_depth, min_split, min_samples_leaf
        ### Decision Tree Training ###
        # Train Decision Tree models with various combinations of depth,
        # minimum samples for splits, and minimum samples per leaf.
        try:
            depths = [1, 3, 5]
            min_splits = [2, 5, 10]
            min_leafs = [1, 5, 10]
            for depth in depths:
                for split in min_splits:
                    for leaf in min_leafs:
                        dt = DecisionTreeClassifier(max_depth=depth, min_samples_split=split,
                                                   min_samples_leaf=leaf, random_state=12345)
                        dt.fit(self.train_x, self.train_y)
                        accuracy = 100 * dt.score(self.test_x, self.test_y)
                        self.stored_models["DecisionTree"].append(dt)
                        idx = len(self.stored_models["DecisionTree"]) - 1
                        if accuracy > self.best_accuracy["DecisionTree"]:
                            self.best_accuracy["DecisionTree"] = accuracy
                            self.best_model_index["DecisionTree"] = idx
        except Exception as e:
            print(f"🚨 Decision Tree Error: Failed to train or evaluate Decision Tree models. Check data and parameters: {e}")
            raise

        # MLP: Test combinations of hidden layer sizes and activations
        ### MLP Training ###
        # Train Multi-Layer Perceptron models with different hidden layer
        # configurations and activation functions for neural networks.
        try:
            hidden1 = [2, 5, 10]
            hidden2 = [0, 2, 5]  # 0 means no second layer
            activations = ["logistic", "relu"]
            for h1 in hidden1:
                for h2 in hidden2:
                    for act in activations:
                        if h2 == 0:
                            layers = (h1,)
                        else:
                            layers = (h1, h2)
                        mlp = MLPClassifier(hidden_layer_sizes=layers, activation=act,
                                            max_iter=1000, random_state=12345)
                        mlp.fit(self.train_x, self.train_y_mlp if len(np.unique(self.data_y)) > 2 else self.train_y)
                        accuracy = 100 * mlp.score(self.test_x, self.test_y_mlp if len(np.unique(self.data_y)) > 2 else self.test_y)
                        self.stored_models["MLP"].append(mlp)
                        idx = len(self.stored_models["MLP"]) - 1
                        if accuracy > self.best_accuracy["MLP"]:
                            self.best_accuracy["MLP"] = accuracy
                            self.best_model_index["MLP"] = idx
        except Exception as e:
            print(f"🚨 MLP Error: Failed to train or evaluate MLP models. Check data shapes and MLP parameters: {e}")
            raise
        # <==== insert your code above here

    def report_best(self) :
        """Method to analyse results.

        Returns
        -------
        accuracy: float
            the accuracy of the best performing model

        algorithm: str
            one of "KNN","DecisionTree" or "MLP"

        model: fitted model of relevant type
            the actual fitted model to be interrogated by marking code.
        """
        # ====> insert your code below here
        ### Best Model Selection ###
        # Identify the best-performing model across all algorithms
        # by comparing their test accuracies and retrieving the corresponding model.
        try:
            algorithms = ["KNN", "DecisionTree", "MLP"]
            best_alg = max(algorithms, key=lambda x: self.best_accuracy[x])
            best_acc = self.best_accuracy[best_alg]
            best_idx = self.best_model_index[best_alg]
            best_model = self.stored_models[best_alg][best_idx]
            return best_acc, best_alg, best_model
        except Exception as e:
            print(f"🚨 Selection Error: Failed to select best model. Ensure models were trained and stored correctly: {e}")
            raise
        # <==== insert your code above here
