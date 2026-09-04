# Build a log analyzer that reads, processes, and writes file data
import csv

def calculate_product_totals(sale_list):
    """Takes a list of sale records and returns (total_quantity, total_revenue)."""
    revenue = 0
    product_quantity = 0    
    for sale in sale_list:
        revenue += sale["price"] * sale["quantity"]
        product_quantity += sale["quantity"] 
    return(product_quantity, revenue)
    
# Read sales data
sales = []
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        sales.append(row)

print(f"Loaded {len(sales)} sales records.")
for sale in sales:
    print(f" Sale: qty {sale["quantity"]} price ${sale["price"]}")        

# Group by product and calculate total sales revenue
products = {}
for sale in sales:
    product = sale["product"]
    if product not in products:
        products[product] = []
    products[product].append(sale)

print("\n=== Sales Revenue ===")
total_revenue = 0
for product_name, sale_list in products.items():
    product_quantity, revenue = calculate_product_totals(sale_list)      
    total_revenue += revenue     
    print(f"\n{product_name} Total QTY sold: {product_quantity} - Product Revenue: ${revenue:.2f}")    
print(f"\ntotal revenue: ${total_revenue:.2f}")

# Group sales by date and calculate revenue per day
daily_revenue = {}
for sale in sales:
    date = sale["date"]
    revenue = sale["price"] * sale["quantity"]
    if date not in daily_revenue:
        daily_revenue[date] = 0
    daily_revenue[date] += revenue
print("\n=== Highest Revenue Day ===")
highest_sales_date = ""
highest_daily_revenue = 0
for date, total in daily_revenue.items():
    if total > highest_daily_revenue:
        highest_daily_revenue = total
        highest_sales_date = date
print(f"{highest_sales_date}: ${highest_daily_revenue:.2f}")       

# Write a formatted summary to a text file
with open("sales_report.txt", "w") as file:
    file.write("Sales Report".center(40) + "\n")
    file.write("=" * 40 + "\n\n")
    file.write(f"Total revenue: ${total_revenue:.2f}\n\n")
    file.write("Revenue per product:\n")
    file.write(f"{'Product':<15}{'Total Qty':<10}{'Total Revenue':<10}\n")
    file.write("-" * 35 + "\n")

    for product_name, sale_list in products.items():
        product_quantity, revenue = calculate_product_totals(sale_list)      
        file.write(f"{product_name:<15}{product_quantity:<10}${revenue:<10.2f}\n")
    file.write(f"\nHighest Revenue Day: {highest_sales_date} (${highest_daily_revenue:.2f})\n")
    
# Write summary data to CSV
with open("product_summary.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["product", "total_quantity", "total_revenue"])
    writer.writeheader()

    for product_name, sale_list in products.items():
        product_quantity, revenue = calculate_product_totals(sale_list)
        writer.writerow({"product": product_name, "total_quantity": product_quantity, "total_revenue": round(revenue, 2)})
