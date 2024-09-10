import pandas as pd
import random

# Load the CSV file
file_path = 'Data1.csv'
df = pd.read_csv(file_path)

# Remove extra spaces from the column names
df.columns = df.columns.str.strip()

# Function to convert date to the format 'yyyy-mm-dd'
def convert_date(date_str):
    return pd.to_datetime(date_str).strftime('%Y-%m-%d')

# Base number for v_uni_no
base_uni_no = 4482536649151954

# Open the file to write the SQL queries with utf-8 encoding
output_path = 'SQL_Insert_Queries1.txt'
with open(output_path, 'w', encoding='utf-8') as file:
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

        query = f"""INSERT INTO videos (
        v_url, 
        v_date, 
        v_uni_no, 
        status, 
        filter, 
        title, 
        v_desc, 
        length, 
        cntlike, 
        cntdislike, 
        views, 
        cntcomment, 
        v_descr, 
        language
        ) VALUES (
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
        );\n\n"""

        # Write each query on a new line
        file.write(query)

print(f"SQL queries saved to {output_path}")
