# IMPORT LIBRARIES
import matplotlib.pyplot as plt

# PLOT HISTOGRAM
def plot_histogram(df):

    # CREATE HISTOGRAM
    df.hist(figsize=(10, 8))

    # SAVE GRAPH
    plt.savefig("outputs/graphs/histogram.png")

    # SHOW GRAPH
    plt.show()