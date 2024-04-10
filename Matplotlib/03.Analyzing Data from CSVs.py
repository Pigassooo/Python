import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# with open('data/data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

data = pd.read_csv('data/data.csv')
ids = data['Responder_id']
lang_Responses = data['LanguagesWorkedWith']
language_counter = Counter()
for response in lang_Responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of Peole who use")

plt.tight_layout()

plt.savefig('Pics/03.Most Popular Languages.png')

plt.show()