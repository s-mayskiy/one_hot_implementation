import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
one_hot_columns_names = data['whoAmI'].unique()
for column_name in one_hot_columns_names:
    data[column_name] = ( data['whoAmI'] == column_name) 
#data = data.drop(['whoAmI'], axis=1)
print(data)
