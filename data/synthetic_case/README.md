# Structure of a folder containing your own data

To work on your real data, create a similar folder containing:

* a `.pkl` file with the observation data. This file should be a `pandas.DataFrame` with `X, Y` coordinates as index.
* a `.pkl` file with the standard deviation of the additive noise on the observations. It should contain the same `X, Y` values in the index.
* a `params_for_gaussian_only.csv` file (with your lines in the index).

and critically:

* an `input.yaml` file, that sets up your inference process.
