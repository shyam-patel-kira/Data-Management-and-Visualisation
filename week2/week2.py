import pandas as pd
import os

cols = ['age_afm', 'consumer', 'h_often_12m', 'h_often_5beer_12m', 'edu']


def read_data():
    # this function reads the wanted subset of the data and renames the coloumns
    col_wanted = ['S1Q4A', 'CONSUMER', 'S2AQ5B', 'S2AQ5G', 'S1Q6A']
    data = pd.read_csv('/home/data-sci/Desktop/analysis/course/nesarc_pds.csv',
                       low_memory=False, usecols=col_wanted, )
    data.rename(columns={'S1Q4A': 'age_afm',
                         'CONSUMER': 'consumer',
                         'S2AQ5B': 'h_often_12m',
                         'S2AQ5G': 'h_often_5beer_12m',
                         'S1Q6A': 'edu'}, inplace=True)
    return data


'''pickling data makes it easy to not having to loud the csv
file every time we run the  script so the pickle_data and
get_pickle are for that '''


def pickle_data(data):
    data.to_pickle('cleaned_data.pickle')


def get_pickle():
    return pd.read_pickle('cleaned_data.pickle')


def the_data():
    """this function will check for the pickle file if not fond
    it will read the csv file then pickle it  """
    if os.path.isfile('cleaned_data.pickle'):
        data = get_pickle()

    else:
        data = read_data()
        pickle_data(data)
    return data


def distribution(var_data):
    """this function will print out the frequency
    distribution for every variable in the data-frame   """
    var_data = pd.to_numeric(var_data, errors='ignore')
    print("the count of the values in {}".format(var_data.name))
    print(var_data.value_counts())
    print("the % of every value in the {} variable  ".format(var_data.name))
    print(var_data.value_counts(normalize=True))
    print("-----------------------------------")


def print_dist():
    # this function loops though the variables and print them out
    for i in cols:
        print(distribution(the_data()[i]))


print_dist()
