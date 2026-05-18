# IMPORT MODEL
from sklearn.linear_model import LogisticRegression

# TRAIN MODEL FUNCTION
def train_model(X_train, y_train):

    # CREATE MODEL
    model = LogisticRegression()

    # TRAIN MODEL
    model.fit(X_train, y_train)

    return model