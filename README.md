# Formula-1-Lap-Time-Predictive-Model
Scraped data from the FastF1 library and used Random Forest model trained on the scraped telemetry, lap metadata, and weather data to predict lap times based on user input of personal data.

Specification on user input: the program uses python console to ask the user what data they want to input. Driver number (eg. Max Verstappen is 1), weather temp (celcius), track temp (celsius), and the racing event.

HOW THE MODEL WORKS:

1. In the model's program, I imported pandas and two sublibraries from Scikit-Learn: ensemble and metrics. I then imported the class RandomForestRegressor from the ensemble sublibrary and mean_absolute_error from the metrics sublibrary.

2. I assign the lap_dataset.csv to a data frequency variable using pandas.

3. I then had to encode the event column of the data as it's quite difficult to 
