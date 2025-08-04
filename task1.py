import pandas as pd

df = pd.read_csv('database.csv')
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['age'] = df['age'].fillna(df['age'].median())
df['name'] = df['name'].fillna('Unknown')
df['gender'] = df['gender'].str.lower().map({
    'm': 'male',
    'male': 'male',
    'f': 'female',
    'female': 'female'
})
df['country'] = df['country'].str.strip().str.lower()
df['country'] = df['country'].replace({
    'us': 'usa',
    'united states': 'usa',
    'uk': 'united kingdom'
})

df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce', dayfirst=False)
df['signup_date'] = df['signup_date'].dt.strftime('%d-%m-%Y')
df.drop_duplicates(inplace=True)
df.to_csv('cleaned_database.csv', index=False)

print("Data cleaning complete!")
print(df.head())
