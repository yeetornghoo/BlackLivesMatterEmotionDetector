from Controller import LogController



def run(df):
    LogController.log_h1("START DATA ASSESS")

    LogController.log_h2("Show Dataframe head")
    print(df.head())
    LogController.log_h2("Show Dataframe info")
    print(df.info)
    LogController.log_h2("Show Dataframe describe")
    print(df.describe())
    LogController.log_h2("Show Dataframe number of null")
    print(df.isna().sum())

