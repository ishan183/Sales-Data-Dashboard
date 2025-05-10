import pandas as pd
from db import get_connection

def get_top_customers():
    query = """
        SELECT 
            c.name AS customer_name,
            SUM(s.quantity * p.price) AS total_spent
        FROM 
            sales s
        JOIN 
            customers c ON s.customer_id = c.customer_id
        JOIN 
            products p ON s.product_id = p.product_id
        GROUP BY 
            c.customer_id
        ORDER BY 
            total_spent DESC
        LIMIT 10;
    """
    conn = get_connection()

    df_top_customers = pd.read_sql(query, conn)

    conn.close()

    return df_top_customers