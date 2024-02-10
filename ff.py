import random
from sklearn.preprocessing import LabelEncoder
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

label_encoder = LabelEncoder()
data_encoded = data.apply(label_encoder.fit_transform)
data_encoded.head()