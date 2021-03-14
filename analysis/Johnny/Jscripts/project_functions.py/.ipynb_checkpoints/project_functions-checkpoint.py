{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "    # Method Chain 1 (Load data and rename the column)\n",
    "\n",
    "    df1 = (\n",
    "           pd.read_csv('Medical_Cost.csv')\n",
    "          .rename(columns={\"charges\": \"Medical Costs per region\"})\n",
    "          .rename(columns={\"sex\": \"Gender\"})\n",
    "          .rename(columns={\"smoker\": \"Tobacco User\"})\n",
    "          .rename(columns={\"age\": \"Age\"})\n",
    "          .rename(columns={\"region\": \"Region\"})\n",
    "          .rename(columns={\"children\": \"Children\"})\n",
    "          .rename(columns={\"bmi\": \"BMI\"}))\n",
    "    \n",
    "    # Method Chain 2 ( Cleaning the costs and BMI by riunding them into 2 decimal places)\n",
    "    \n",
    "    def format(x):\n",
    "        return \"${:0.2f}\".format(x)\n",
    "    \n",
    "    df1['Medical Costs per region'] = (df1['Medical Costs per region'].apply(format))\n",
    "\n",
    "    df1['BMI'] = ( round(df1['BMI'])) \n",
    "    # Method Chain  3(Sorting the data )\n",
    "    df4 = ( df1.sort_values(by=['Age'], ascending = True))\n",
    "     # Method Chain  3(Organizing the order of the columns )\n",
    "    df5 = ( df4[['Age','Gender','Children','BMI','Tobacco User','Medical Costs per region','Region']])    \n",
    "    return df5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
