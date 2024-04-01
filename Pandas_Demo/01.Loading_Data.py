import pandas as pd

df = pd.read_csv('data1/survey_results_public.csv')

#print(df.shape)
#print(df.head())
#print(df.tail())
#print(df.info())

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
schema_df = pd.read_csv('data1/survey_results_schema.csv')
print(schema_df)