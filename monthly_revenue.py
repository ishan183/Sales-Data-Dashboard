import pandas as pd
from db import get_connection

def get_monthly_revenue():
    query = """
    SELECT 
        MONTH(s.sale_date) AS month,
        SUM(s.quantity * p.price) AS monthly_revenue
    FROM 
        sales s
    JOIN 
        products p ON s.product_id = p.product_id
    GROUP BY 
        month
    ORDER BY 
        month;
    """

    conn = get_connection()

    df_monthly_revenue = pd.read_sql(query, conn)

    # Close the connection
    conn.close()

    # List of month names
    month_names = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]

    # Replace month numbers with month names
    df_monthly_revenue['month'] = df_monthly_revenue['month'].apply(
        lambda x: month_names[x - 1]  # Subtract 1 because the list index is zero-based
    )

    return df_monthly_revenue
