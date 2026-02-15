import fastf1
import pandas as pd
import os
from tqdm import tqdm

#ensure cache directory exists
if not os.path.exists('f1_cache'):
    os.makedirs('f1_cache')
    
fastf1.Cache.enable_cache('f1_cache')

seasons = [2022, 2023]  #seasons to fetch
sessions_to_fetch = ['Q', 'R']  #qualifying and race
limit_races = None  #set to an integer for testing

all_data = []

for year in seasons:
    schedule = fastf1.get_event_schedule(year)
    races = schedule[schedule['EventFormat'].notna()]

    if limit_races:
        races = races.head(limit_races)

    for _, race in races.iterrows():
        event_name = race['EventName']
        print(f"\nProcessing {event_name} {year}...")

        for sess_type in sessions_to_fetch:
            print(f"Loading session: {sess_type}")
            try:
                session = fastf1.get_session(year, event_name, sess_type)
                session.load()
            except Exception as e:
                print(f"  (X) Could not load session {sess_type} for {event_name}: {e}")
                continue

            weather = session.weather_data

            for drv in tqdm(session.drivers, desc=f"    Drivers in {sess_type}"):
                drv_laps = session.laps.pick_drivers(drv)
                drv_laps = drv_laps[~drv_laps['LapTime'].isna()]

                for _, lap in drv_laps.iterlaps():
                    try:
                        telemetry = lap.get_telemetry()

                        #telemetry aggregates
                        avg_speed = telemetry['Speed'].mean()
                        max_speed = telemetry['Speed'].max()
                        min_speed = telemetry['Speed'].min()
                        avg_throttle = telemetry['Throttle'].mean()
                        full_throttle_percentage = (telemetry['Throttle'] >= 95).sum() / len(telemetry)
                        avg_brake = telemetry['Brake'].mean()
                        brake_events = (telemetry['Brake'] > 0).sum()
                        avg_gear = telemetry['nGear'].mean()
                        drs_usage = (telemetry['DRS'] > 0).sum() / len(telemetry)

                        #lap metadata
                        lap_number = lap['LapNumber']
                        stint = lap['Stint']
                        compound = lap['Compound']
                        tyre_life = lap['TyreLife']
                        sector1 = lap['Sector1Time'].total_seconds() if pd.notnull(lap['Sector1Time']) else None
                        sector2 = lap['Sector2Time'].total_seconds() if pd.notnull(lap['Sector2Time']) else None
                        sector3 = lap['Sector3Time'].total_seconds() if pd.notnull(lap['Sector3Time']) else None

                        #weather h
                        weather_row = weather.iloc[(weather['Time'] - lap['LapStartTime']).abs().argsort()[:1]]
                        air_temp = weather_row['AirTemp'].values[0]
                        track_temp = weather_row['TrackTemp'].values[0]
                        humidity = weather_row['Humidity'].values[0]
                        wind_speed = weather_row['WindSpeed'].values[0]
                        wind_dir = weather_row['WindDirection'].values[0]

                        #append
                        all_data.append({
                            'Year': year,
                            'Event': event_name,
                            'Session': sess_type,
                            'Driver': drv,
                            'LapNumber': lap_number,
                            'Stint': stint,
                            'Compound': compound,
                            'TyreLife': tyre_life,
                            'Sector1': sector1,
                            'Sector2': sector2,
                            'Sector3': sector3,
                            'AverageSpeed': avg_speed,
                            'MaxSpeed': max_speed,
                            'MinSpeed': min_speed,
                            'AvgThrottle': avg_throttle,
                            'FullThrottlePercentage': full_throttle_percentage,
                            'AvgBrake': avg_brake,
                            'BrakeEvents': brake_events,
                            'AvgGear': avg_gear,
                            'DRSUsage': drs_usage,
                            'AirTemp': air_temp,
                            'TrackTemp': track_temp,
                            'Humidity': humidity,
                            'WindSpeed': wind_speed,
                            'WindDirection': wind_dir,
                            'LapTime': lap['LapTime'].total_seconds()
                        })

                    except Exception:
                        continue  #skip broken telemetry

#save data
df = pd.DataFrame(all_data)
df.to_csv('laps_dataset.csv', index=False)
print(f"\nData collection complete! {len(df)} laps saved to laps_dataset.csv")