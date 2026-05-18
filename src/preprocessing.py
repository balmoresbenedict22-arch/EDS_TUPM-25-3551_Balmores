# CLEAN DATA FUNCTION
def clean_data(df):

    # REMOVE NULL VALUES
    df = df.dropna()

    return df


# SELECT FEATURES AND TARGET
def select_features(df):

    # INPUT FEATURES
    X = df[[
        'CO AQI Value',
        'Ozone AQI Value',
        'NO2 AQI Value',
        'PM2.5 AQI Value'
    ]]

    # TARGET OUTPUT
    y = df['AQI Category']

    return X, y