# IMPORT PANDAS
import pandas as pd

# FUNCTION TO LOAD CSV DATA
def load_data(path):

    # READ CSV FILE
    df = pd.read_csv(path)

    # RETURN DATAFRAME
    return df