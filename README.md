Sales Data Dashboard

A web-based data visualization dashboard that displays key sales metrics using data from a structured SQL database. Built using Python, Flask, Matplotlib, and HTML/CSS, this project is designed for portfolio showcasing and can be deployed or hosted independently.

Features

-Units Sold by Region: Bar chart of total units sold across different regions.
-Monthly Revenue Overview: Line chart showing revenue trends over months.
-Top Spending Customers: Visual of the highest-paying customers.
-Revenue by Product: Bar chart of revenue distribution across products.

Tech Stack

Backend: Python (Flask)
Data Access: SQL (via helper Python modules)
Visualization: Matplotlib
Frontend: HTML, CSS

Directory Structure

sales-data-dashboard/
├── app.py
├── db.py
├── config.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── images/
│   │   └── dashboard.png
│   └── styles/
│       └── style.css
├── units_by_region.py
├── monthly_revenue.py
├── top_customers.py
└── revenue_by_product.py

Setup Instructions

1. Clone the Repository

bash
git clone https://github.com/your-username/sales-data-dashboard.git
cd sales-data-dashboard

2. Set Up Virtual Environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

bash
pip install -r requirements.txt

4. Configure the Database

Edit `dashboard.py` or `config.py` to match your database credentials and setup.

5. Run the App

bash
python app.py


Navigate to `http://127.0.0.1:5000` in your browser.

Screenshots
![Dashboard-ss](<Screenshot 2025-05-10 183549.png>)

Author

[Ishan Jha](https://www.linkedin.com/in/ishan-jha-244770207/)
