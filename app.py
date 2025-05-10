from flask import Flask, render_template
import matplotlib.pyplot as plt
import os

# Custom modules to retrieve processed data from the database
from units_by_region import get_units_by_region
from monthly_revenue import get_monthly_revenue
from top_customers import get_top_customers
from revenue_by_product import get_revenue_by_product

# Flask app initialized
app = Flask(__name__)

@app.route("/")
def dashboard():
    '''
    Main route for rendering the sales dashboard.

    This function:
    - Retrieves sales-related data using the custom modules.
    - Generates a 2x2 grid of matplotlib plots showing key metrics.
    - Saves the image to the static/images folder.
    - Renders an HTML template to display the image.

    Returns:
        str: Rendered HTML template with embedded image path.
    '''

    # Fetch processed data
    df_region = get_units_by_region()
    df_monthly = get_monthly_revenue()
    df_customers = get_top_customers()
    df_products = get_revenue_by_product()

    # Create matplotlib figure with subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    #fig.suptitle('Sales Data Dashboard', fontsize=18) #commented out to avoid duplication of title 

    # Plot 1: Units Sold by Region
    if not df_region.empty:
        axs[0, 0].bar(df_region['region'], df_region['total_units'], color='cyan', zorder=2, alpha=0.9, edgecolor='black', linewidth=2)
        axs[0, 0].set_title('Units Sold by Region')
        axs[0, 0].tick_params(axis='x', rotation=45)

    # Plot 2: Monthly Revenue Overview
    if not df_monthly.empty:
        axs[0, 1].plot(df_monthly['month'], df_monthly['monthly_revenue'], marker='o', color='hotpink', zorder=2, linewidth=2)
        axs[0, 1].set_title('Monthly Revenue')
        axs[0, 1].tick_params(axis='x', rotation=45)

    # Plot 3: Top Spending Customers
    if not df_customers.empty:
        axs[1, 0].bar(df_customers['customer_name'], df_customers['total_spent'], color='limegreen', zorder=2, alpha=0.9, edgecolor='black', linewidth=2)
        axs[1, 0].set_title('Top Spending Customers')
        axs[1, 0].tick_params(axis='x', rotation=45)

    # Plot 4: Revenue by Product
    if not df_products.empty:
        axs[1, 1].bar(df_products['product_name'], df_products['total_revenue'], color='orange', zorder=2, alpha=0.9, edgecolor='black', linewidth=2)
        axs[1, 1].set_title('Revenue by Product')
        axs[1, 1].tick_params(axis='x', rotation=45)

    # Layout Spacing Adjusted
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Path of the image savefile
    image_folder = os.path.join('static', 'images')
    os.makedirs(image_folder, exist_ok=True)

    # Save the dashboard image
    image_path = os.path.join(image_folder, 'dashboard.png')
    plt.savefig(image_path)
    plt.close()

    # Completion message
    print(f"Dashboard saved to: {os.path.abspath(image_path)}")

    return render_template("index.html", image_file='images/dashboard.png')

if __name__ == "__main__":
    app.run(debug=True)
