from flask import Flask, jsonify, render_template
from flask_cors import CORS  # ← import it
import pyodbc
import pandas as pd

app = Flask(__name__)
CORS(app) 
# DB Connection
def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=gem_tenders;"
        "Trusted_Connection=yes;"
    )

@app.route('/')
def index():
    return render_template('index.html')  # Loads the base page

@app.route('/api/tenders')
def fetch_tenders():
    conn = get_connection()
    query = "SELECT organisation, tender_id, address, item_description FROM tender_data ORDER BY updated_at DESC"
    df = pd.read_sql(query, conn)
    conn.close()
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    
    app.run(debug=True)
