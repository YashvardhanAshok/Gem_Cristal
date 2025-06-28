import pyodbc
import pandas as pd

# Set up your DB connection
conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )



# SQL query to get live status
query = """
SELECT *,
       CASE 
           WHEN end_date < CAST(GETDATE() AS DATE) 
              THEN 'No' ELSE 'Yes'
       END AS Live
FROM dbo.tender_data;
"""

# Read query result into a DataFrame
df = pd.read_sql(query, conn)

# Optional: Close connection
conn.close()

# Show result
print(df.head())