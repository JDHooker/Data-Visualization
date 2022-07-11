import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

my_filepath = "../input/best-selling-mobile-phones/best-selling-mobile-phones.csv"

my_data = pd.read_csv(my_filepath, index_col="manufacturer")

my_data.head()

sns.scatterplot(x=my_data['year'], y=my_data['units_sold_m'], hue=my_data['form'])