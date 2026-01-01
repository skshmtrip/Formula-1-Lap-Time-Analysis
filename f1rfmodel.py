#imports (make sure the library is installed on your machine)
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


#assigning the dataset to an variable
df = pd.read_csv("laps_dataset.csv")


#event encoding
event_to_id = {}
for event in df["Event"].unique():
    event_to_id[event] = len(event_to_id)

df["EventID"] = df["Event"].map(event_to_id)

#enumerate session type
df["SessionType"] = df["Session"].map({"Q":0, "R":1}).astype(float)

#input and outputs
features = ["Driver", "AirTemp", "TrackTemp", "EventID", "SessionType"]
target = "LapTime"

df = df[features + [target]].dropna()

split_index = int(0.8 * len(df))


#train-test split
train_df = df.iloc[:split_index]
test_df = df.iloc[split_index:]

X_train = train_df[features]
y_train = train_df[target]

X_test = test_df[features]
y_test = test_df[target]

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print(f"training complete | mean absolute error = {mae}.")


#user input
print("LAP TIME PREDICTOR")
print("known event (copy and paste special characters):")
for e in event_to_id:
    print("-", e)

sesh_type_mapping = {"Q":0, "R":1}

try:
    driver = int(input("driver number (name respective to season): "))
    air_temp = float(input("air temperature: "))
    track_temp = float(input("track temperature: "))
    event_name = input("event name (case sensitive): ")
    sesh_type = input("session type (Q for qualifying and R for race | case sensitive): ")

    if event_name not in event_to_id:
        print("event not in training data")
    elif sesh_type not in sesh_type_mapping:
        print("invalid session type")
    else:
        sesh_num = sesh_type_mapping[sesh_type]
        event_id = event_to_id[event_name]
        sample = [[driver, air_temp, track_temp, event_id, sesh_num]]
        prediction = model.predict(sample)
        print("lap time:", round(prediction[0], 3), "seconds")

except ValueError:
    print("incorrect input type.")
