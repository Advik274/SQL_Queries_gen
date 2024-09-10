import pandas as pd
import random

# Load the CSV file
file_path = 'Data.csv'
df = pd.read_csv(file_path)

# Remove extra spaces from the column names
df.columns = df.columns.str.strip()

# Function to convert date to the format 'yyyy-mm-dd'
def convert_date(date_str):
    return pd.to_datetime(date_str).strftime('%Y-%m-%d')

# Base number for v_uni_no
base_uni_no = 4482536649151951

# List to store SQL queries
sql_queries = []

for index, row in df.iterrows():
    v_url = row['URL'].split('=')[-1]
    v_date = convert_date(row['Date'])
    v_uni_no = base_uni_no + index
    status = row['Content']
    filter_value = row['Filter']
    title = row['Title']
    v_desc = row['Description'] if row['Description'] != '-' else title
    length = row['Length']
    cntlike = random.randint(50, 300)
    cntdislike = random.randint(10, 50)
    views = random.randint(350, 800)
    cntcomment = 0
    language = row['Language']

    query = f"""(
    '{v_url}', 
    '{v_date}', 
    '{v_uni_no}', 
    '{status}', 
    '{filter_value}', 
    '{title}', 
    '{v_desc}', 
    '{length}', 
    {cntlike}, 
    {cntdislike}, 
    {views}, 
    {cntcomment}, 
    '{v_desc}', 
    '{language}'
    )"""
    
    
    sql_queries.append(query)

# Combine all queries into one SQL statement
sql_output = "INSERT INTO videos (\n    v_url, \n    v_date, \n    v_uni_no, \n    status, \n    filter, \n    title, \n    v_desc, \n    length, \n    cntlike, \n    cntdislike, \n    views, \n    cntcomment, \n    v_descr, \n    language\n) VALUES \n" + ",\n".join(sql_queries) + ";"

# Save the output to a .txt file
output_path = 'SQL_Insert_Queries1.txt'
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(sql_output)

print(f"SQL queries saved to {output_path}")
