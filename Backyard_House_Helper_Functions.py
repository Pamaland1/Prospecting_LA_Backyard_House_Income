#helper functions for Backyard House Project

import pandas as pd

def create_psql_schema(dataframe, schema_name)
    """ (dataframe, string) --> None
    
    Create an empty schema called schema_name in psql and populate schema from a dataframe.  
    """
    # Create dictionary to use to connect to pSQL databases
	params = {
    	'host': 'localhost',  # We are connecting to our _local_ version of psql
    	'user': 'agar',
    	'port': 5432          # port 
	}
	
	#connect to pSQL database
    connection_string = f'postgres://agar:{params["host"]}@{params["host"]}:{params["port"]}/properties'
    engine = create_engine(connection_string, pool_pre_ping=True)
    
    # Create Empty Schema in pSQL
    df.iloc[:0].to_sql(schema_name, engine, index=False)
    
    # Populate Empty Schema in pSQL
	df.iloc[:].to_sql(schema_name, engine, index=False, if_exists = 'append', chunksize = 1000)


#Define function that takes in the building area, lot area, and outputs the backyard house bedroom capacity

def bedroom_count(sfmain, site):
    """ (float, float) -> int

    Return 3, 2, or 1 indicating the number of bedrooms a backyard house could have
    based on the size of the lot (site), and the size of the main house (sfmain).
    The area of the main structure plus the backyard house should be less than
    the size of the site.  The typical backyard house area for a 3 br
    is 1200 sf, 2 br is 700 sf, 1 br is 400 sf.

    >>> bedroom_count(2400,7200)
    3
    >>> bedroom_count(700, 5000)
    0
    """
    if sfmain >= 2400 and (sfmain + 1200)*2 <= site:
        br = 3
        return br
    elif sfmain >= 1400 and (sfmain + 700)*2 <= site:
        br = 2
        return br
    elif sfmain >= 800 and (sfmain + 400)*2 <= site:
        br = 1
        return br
    else:
        br = 0
    return br

def geo_data_dist_func(df, new_col_name, target_df, target)
    """
    Create a new column for a datafraframe that adds information from comparative
    dataset based on closest proximity to example in main dataset, df.
    """

    new_data_list = []

    for i in range(len(df)):
        min_d = np.inf
        min_d_ix = 0

        max_lat = df['latitude'][i] + (10/69)
        max_lon = df['longitude'][i] + (10/69)
        min_lat = df['latitude'][i] - (10/69)
        min_lon = df['longitude'][i] - (10/69)

        for j in range(len(target_df)):
            #search within a 10 mile radius
            if target_df[lat][j]<max_lat and target_df[lat][j]>min_lat\
               and target_df[lon][j]<max_lon and target_df[lon][j]>min_lon:
                distance = geodesic(df['lat_lon'][i], target_df['lat_lon'][j]).miles
                if distance < min_d:
                    min_d = distance
                    min_d_ix = j
        new_data =  target_df[target][min_d_ix]
        new_data_list.append(new_data)

    airbnb_df[new_col_name] =  new_data_list

def geo_data_amenity_count_func(df, dist, lat, lon, new_col_name):
    """
    Create a new column for a dataframe that adds information from comparative
    dataset based on a count of amenities that are within a specified distance
     to example in main dataset, df.
    """
    new_data_list = []

    for i in range(len(airbnb_df)):
        min_d = np.inf
        min_d_ix = 0

        #approx 5 mile radius around airbnb
        max_lat = airbnb_df['latitude'][i] + (dist/69)
        max_lon = airbnb_df['longitude'][i] + (dist/69)
        min_lat = airbnb_df['latitude'][i] - (dist/69)
        min_lon = airbnb_df['longitude'][i] - (dist/69)

        new_data_count=0
        for j in range(len(df)):
            #search within a dist mile radius for min_dist
            if df['latitude'][j]<max_lat and df['latitude'][j]>min_lat and\
               df['longitude'][j]<max_lon and df['longitude'][j]>min_lon:
                new_data_count+=1
        new_data_list.append(new_data_count)

    airbnb_df[new_col_name] =  new_data_list

def model_and_scores(dataframe, model, modelname):
    """
    Build a crossvalidated model for a dataset and ouput its average scores.
    """
    X = dataframe.iloc[:, 1:]

    y = dataframe.iloc[:, 0]

    # perform train/test split
    X_train, X_test, y_train, y_test = \
        train_test_split(pd.get_dummies(X), y, test_size=0.2, random_state=42)

    kf = KFold(n_splits=5, random_state=42, shuffle=True)
    kf.get_n_splits(X_train)

    rmse_list = []
    mae_list = []
    r2_list = []

    for train_ind, val_ind in kf.split(X_train):

        #assign train and validate sets
        X_tr, y_tr = X_train.iloc[train_ind], y_train.iloc[train_ind]
        X_val, y_val = X_train.iloc[val_ind], y_train.iloc[val_ind]

        #fit model
        lr_model = LinearRegression()
        dtr_model = DecisionTreeRegressor(max_features="sqrt", max_leaf_nodes = 100)
        gbr_model = GradientBoostingRegressor()
        xgb_model = xgb.XGBRegressor()
        model.fit(X_tr, y_tr)

        # score fit model on validation data
        preds = model.predict(X_val)

        val_score = model.score(X_val, y_val)
        rmse = np.sqrt(metrics.mean_squared_error(y_val,preds))
        mae = metrics.mean_absolute_error(y_val, preds)

        r2_list.append(val_score)
        rmse_list.append(rmse)
        mae_list.append(mae)

    print(modelname, " results")
    print("rmse cv avg: ", mean(rmse_list))
    print("mae cv avg: ", mean(mae_list))
    print("val cv avg: ", mean(r2_list))
