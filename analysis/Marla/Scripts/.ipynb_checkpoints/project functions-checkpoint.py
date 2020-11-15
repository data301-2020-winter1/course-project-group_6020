{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "    # Method Chain 1 (Load data and deal with missing data)\n",
    "\n",
    "    df1 = (\n",
    "          pd.read_csv(url_or_path_to_csv_file)\n",
    "          .rename(columns= {\"instant\":\"Index\", \"dteday\":\"Date\",\"season\":\"Season\",\"yr\":\"Year\",\"mnth\":\"Month\",\"hr\":\"Hour\",\"holiday\":\"Holiday\",\"weekday\":\"Week_day\",\"workingday\":\"Working_day\",\n",
    "                            \"weathersit\":\"Weather\",\"temp\":\"Temperature\",\"atemp\":\"FeelTemp\",\"hum\":\"Humidity\",\"windspeed\":\"Wind_speed\",\"casual\":\"Casual_users\",\"registered\":\"Registered_users\",\n",
    "                            \"cnt\": \"Total_users\" }, errors= 'ignore')\n",
    "          .dropna(axis = 0, how= 'any')\n",
    "          .dropna(columns = 'Index', errors='ignore')\n",
    "          \n",
    "      )\n",
    "\n",
    "    # Method Chain 2 (Create new columns, drop others, and do processing)\n",
    "\n",
    "    df2 = (\n",
    "          df1\n",
    "          .assign(...)\n",
    "      )\n",
    "\n",
    "    # Make sure to return the latest dataframe\n",
    "\n",
    "    return df2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
