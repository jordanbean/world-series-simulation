The goal of this project is to simulate the 2018 World Series winner using publicly available team data. We'll define a series 
of functions that compute simularity between teams using the Nearest Neighbors sklearn model, then simulate games using performance
against an opponents similar batting neighbors (for pitchers) and pitching neighbors (for batters).

We'll then randomly select scores from the distribution, assign a winner, simulate the series, then repeat the process
over the course of 20,000 simulations and calculated the odds of a team winning the series.
