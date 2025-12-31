
HOW THE CODE WORKS:

1. In the model's program, I imported pandas and two sublibraries from Scikit-Learn: ensemble and metrics. I then imported the class RandomForestRegressor from the ensemble sublibrary and mean_absolute_error from the metrics sublibrary.
2. I assign the lap_dataset.csv to a data frequency variable using pandas.
3. I then had to encode the event column of the data as it's not quite possible (at least in my knowledge) to train any kind of random forest model on raw string data directly. How does the encoding pipeline work you might be asking? First you initialize a list for the event dictionary. You then get all the unique event names from the data. And then in order, for each event, you run a loop that iterates through the data on condition that the even it unique, then you assign it a respective value in the list by adding a value to the list which would be the length of the list (eg. Pre-Season Track Session would be index 0 in the list because it is the first unique event in the data and the length of the list at that time would be 0). Then in the dataframe add a new column for Event_ID to represent the each event numerically.
4. Then I'm looking to set what I want to predict with vs. what I'm actually predicting. I set a features list with the input parameters "Driver", "AirTemp", "TrackTemp", and "EventID". Then I set a variable name target to the parameter "LapTime"
5. 
