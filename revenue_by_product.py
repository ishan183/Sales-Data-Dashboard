# revenue_by_products.py
import pandas as pd
from db import get_connection

def get_revenue_by_product():
    query = """
        SELECT 
            p.product_name AS product_name,
            ROUND(SUM(s.quantity * p.price), 2) AS total_revenue
        FROM 
            products p
        JOIN 
            sales s ON p.product_id = s.product_id
        GROUP BY 
            p.product_id
        ORDER BY 
            total_revenue DESC;
    """
    conn = get_connection()

    df_products = pd.read_sql(query, conn)
                              
    conn.close()

    # Return the result for plotting
    return df_products
