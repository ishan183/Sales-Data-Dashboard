import pandas as pd
from db import get_connection

def get_units_by_region():
    query = """
        SELECT 
            c.region AS region,
            SUM(s.quantity) AS total_units
        FROM 
            sales s
        JOIN 
            customers c ON s.customer_id = c.customer_id
        GROUP BY 
            c.region
        ORDER BY 
            total_units DESC;
    """
    conn = get_connection()
    df_units_by_region = pd.read_sql(query, conn)
    conn.close()
    return df_units_by_region