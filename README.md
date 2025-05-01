# project1_customer_orders-
 Loads order and customer, data Cleans duplicates ,Loads clean data into PostgreSQL, runs a SQL query to get Top N customers by order count
 # Customer Orders Insight Pipeline

## 🔍 Overview
Simple pipeline to clean, load, and analyze customer orders using Python and SQL.

## 📂 Folder Structure
- `python/`: Scripts to load and clean data
- `sql/`: Query for insights
- `data/`: Sample CSV files

## 🛠️ Technologies
- Python (pandas, psycopg2)
- PostgreSQL
- GitHub

## 📈 Output
Top 3 customers by number of orders
| customer_name | total_orders |
|---------------|--------------|
| Alice         | 3            |
| Bob           | 1            |
| Charlie       | 1            |

