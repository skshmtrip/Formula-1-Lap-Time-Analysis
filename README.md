# Environmental Effects on Lap Times: Race vs Qualifying Analysis

## OVERVIEW
This project investigates how track and air temperatures can affect a Max Verstappen's lap time across qualifying sessions at the Miami GP in Formula 1 specified to the model. Using the telemetry and weather data from the 2022 and 2023 seasons, I perform hypothesis testing (t-test specifically) to compare lap time distributions in environmental conditions during qualifying.

## RESEARCH QUESTION
Do track and air temperature significantly influence simulated lap times, and does this effect differ in qualifying sessions at Miami?

### Hypotheses:
1. H₀: Simulated lap times do not differ between cool and warm conditions at Miami.
2. H₁: Simulated lap times differ significantly under varying environmental temperatures at Miami.

## DATASET (laps_dataset.csv)
The dataset contains telemetry and weather information for the 2022 and 2023 Formula 1 seasons. Key variables for observation in this analysis include:
- LapTime (s): Target variable
- SessionType: Qualifying (Q)
- TrackTemp (C) & AirTemp (C): weather variables
- Driver & Event: Max Verstappen (1) and Miami GP
Laps affected by incidents or outliers were removed to ensure clean, independent comparisons.

## HYPOTHESIS TESTING
To see how track and air temps mess with lap times, I used the Random Forest model to simulate Max Verstappen’s qualifying laps at Miami GP across different environmental conditions. Then I ran t-tests on these predicted lap times to check if the differences were significant.
### Testing Process:
1. Set up the simulations:
   - Driver Number: 1 (Max Verstappen)
   - Session: Q (Qualifying)
   - Event Name: Miami Grand Prix
   - Track Temperature: varies between 25-32 (C)
   - Air Temperature: varies between 33-40 (C)
   - Constant variables: Driver Number, Session, and Event Name
   - Varying variables: Track Temperature and Air Temperature
2. Make groups for t-test:
   - Low TrackTemp/AirTemp (below median lap time)
   - High TrackTemp/AirTemp (above median lap time)
3. Simulate data using the model
4. Low environmental temperature lap times go in one list, high environmental temerature lap times go in another
5. Run t-test
6. Record pvalue and t value, compare p value with alpha value of 0.05 (with respect to confidence being 0.95)
7. Conclude hypothesis.

### Testing:
Data:
| Air Temp | Track Temp | Lap Time |
|----------|------------|----------|
| 25       | 33         | 96.39    |
| 26       | 34         | 93.78    |
| 27       | 35         | 92.996   |
| 28       | 36         | 92.996   |
| 29       | 37         | 97.896   |
| 30       | 38         | 97.896   |
| 31       | 39         | 98.202   |
| 32       | 40         | 98.202   |

| Hot-Temp Lap Time | Cold-Temp Laptime|
|----------|------------|
| 97.896       | 96.39         |
| 97.896       | 93.78         |
| 98.202       | 92.996         |
| 98.202       | 92.996         |

#### Test Results:
t = -4.952
p = 0.015

#### Results 
0.015 < 0.05
- p < α
- Results are significant.
- Reject Null Hypothesis.

## FINAL VERDICT
Due to null hypothesis being rejectable, we can conclude that simulated lap times differ significantly under varying environmental temperatures at Miami.
