
# coding: utf-8

# In[1]:

import tensorflow as tf
import pandas as pd

def read_csv(file_name):
    Data = pd.read_csv('./CSV_Data_Folder/%s' %file_name, header=None)
    return Data

def csv_transpose(Data):
    Buffer = pd.DataFrame.transpose(Data)
    return Buffer

def csv_transpose_save_to_file(Data):
    Buffer = pd.DataFrame.transpose(Data)
    Buffer.to_csv('Data_transpose.csv', header=None)

def get_csv_frame(column, row):
    return pd.DataFrame(columns=range(0, column), index=range(0, row))


# In[ ]:



