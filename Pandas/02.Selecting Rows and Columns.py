import pandas as pd

people = {
    "first" : ["Corey", "Jane", "John"],
    "last" : ["Schafer", "Doe", "Doe"],
    "email" : ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
}

dfe = pd.DataFrame(people)

#print(dfe['email'])
#print(dfe.email)
#print(dfe[['last','email']])
#print(dfe.columns)
#print(dfe.iloc[[0,1], 2])
#print(dfe)
#print(dfe.loc[0])
#print(dfe.columns)

df = pd.read_csv('data1/survey_results_public.csv')
pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
schema_df = pd.read_csv('data1/survey_results_schema.csv')

#print(df['Hobbyist'])
#print(df.columns)
#print(df['Hobbyist'].value_counts())