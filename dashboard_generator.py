import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

#functions
def file_name_translator(file_name):
    month_table = {'01':'Janurary', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
    month = ''
    try:
        year = str(file_name[6:10])
        month_num = file_name[-6:-4]
        month = month_table[month_num]
    except KeyError:
        pass
    return f"{month}, {year}"

def month_name_to_numb(monthname):
    month_table_reversed = {'Janurary':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
    return month_table_reversed[monthname]

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

def num_to_name(num):
    month_table = {'01':'Janurary', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
    return month_table[num]
#when the user runs the program, they should select one of the CSV files

#use the os module to detect the names of all CSV files which exist in the "data" directory, then display this list to the user and prompt the user to input their selection

print("Hello, welcome to the executive dashboard generator.")
active = "yes"
year_sel = ""
month_sel = ""

def choose_year():
    while active == "yes":
        prompt = "Please begin by typing in the year you want to analyze(ex. 2018).\nIf you want to see what years/months of sales are available, type 'show me'\n Type here: "
        year_sel = input(prompt)
        available_years = ['2017', '2018', '2019']
        if year_sel in available_years:
            break
        elif year_sel == 'show me':
            path = "data/"
            file_list = os.listdir(path)
            for item in file_list:
                print(file_name_translator(item))
        else:
            print("          \nUnfortunately we don't have sales history for that year, please try another year.\n       ")
    return year_sel

def choose_month():
    while active == "yes":
        global month_sel
        prompt_2 = f"Great, please type in the month in {year_sel} you want to analyze here (ex.'March'): "
        month_sel = input(prompt_2)
        available_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        if month_sel in available_months:
            break
        else:
            print("Sorry, month not available, please try another month.")    
    return month_sel

year_sel = choose_year()
month_sel = choose_month()

print("-----------------------")
print(f"Preparing sales analysis for {month_sel}, {year_sel}...")
print("-----------------------")
print("                       ")

month_number = month_name_to_numb(month_sel)
csv_name = f"data/sales-{year_sel}{month_number}.csv"

sales_by_month = {}

def total_sales_by_month():
    path = "data/"
    file_list = os.listdir(path)
    all_csvs_for_year = [f"data/{fil}" for fil in file_list if fil[6:10] == year_sel]
    for csvs in all_csvs_for_year:
        csvs_read = pd.read_csv(csvs)
        total_mon_sales = round(csvs_read["sales price"].sum(), 2)
        month_name = num_to_name(csvs[-6:-4])
        sales_by_month[month_name] = total_mon_sales

total_sales_by_month()
# https://www.freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/ 
# I used the above website for help on combining multiple CSVs into one
csv_year_name = ''
def combine_sales_for_year(csv_year_name):
    path = "data/"
    file_list = os.listdir(path)
    all_csvs_for_year = [f"data/{fil}" for fil in file_list if fil[6:10] == year_sel]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_csvs_for_year])
    csv_year_name += f"data/combined_csv_for_{year_sel}.csv"
    combined_csv.to_csv(csv_year_name, index=False, encoding='utf-8-sig')
    return csv_year_name


while True:
    try:
        csv_read = pd.read_csv(csv_name)
        break
    except FileNotFoundError:
        print("Hello, unfortunately I couldn't find that file. Please make sure sales data for that year and month exists and resubmit.")
        year_sel = choose_year()
        month_sel = choose_month()
        month_number = month_name_to_numb(month_sel)
        csv_name = f"data/sales-{year_sel}{month_number}.csv"
        csv_read = pd.read_csv(csv_name)
        break

daily_sales = csv_read


combine_sales_for_year(csv_year_name)

combined_csv_read = pd.read_csv(combine_sales_for_year(csv_year_name))

#if file selection fails, produce an error message that says "Hello, unfortunately I couldn't find that file. Please check to make sure the file and filepath is correct and resubmit."
print("Crunching the data...")

#Output Requirements:
#Total Monthly Sales: sum of total monthly sales for each product, formatted as USD(from function) to two decimal places

total_sales = to_usd(daily_sales["sales price"].sum())

print("-----------------------")
print(f"Total {month_sel} Sales: {total_sales}")

#Below is the code to list of Top Selling Products: top sellers list with sum of total monthly sales formatted with USD function and two decimal places
sales_by_prod = daily_sales.groupby(["product"]).sum()
top_3 = sales_by_prod.nlargest(3, 'sales price')
top_3_dict = top_3.to_dict()['sales price']
top_3_list = [f"{prod}: {to_usd(sales)} " for prod, sales in top_3_dict.items()]

#Below is the cose to list of Top Selling Products for the year

yr_sales_by_prod = combined_csv_read.groupby(["product"]).sum()
top_5 = yr_sales_by_prod.nlargest(5, 'sales price')
top_5_dict = top_5.to_dict()['sales price']
top_5_list = [f"{prod}: {to_usd(sales)} " for prod, sales in top_5_dict.items()]


print("-----------------------")
print(f"Top 3 Selling Products for {month_sel}, {year_sel}:")
print("                       ")

for i, prd in enumerate(top_3_list, 1):
    print(f"{i}) {prd}")
print("-----------------------")
print(f"Compred to top 5 Selling Products for all of {year_sel}:")
print("                       ")
for i, prd in enumerate(top_5_list, 1):
    print(f"{i}) {prd}")

print("-----------------------")
print("Visualizing the data...")

#2 Graphs depicting the information above - graphs should include details on month selected
#Additional enhancements: Compare sales across months - total annual graph as the third graph?

#Graph for Total Sales for the year
x = [li for li in sales_by_month]
y = [l for l in sales_by_month.values()]

plt.rcParams["figure.figsize"] = (14, 8)
plt.plot(x,y, color='green')
plt.xticks(weight='bold')
plt.yticks(weight='bold')
plt.title(f'{year_sel} Total Sales by Month ($USD)', color='grey', fontsize=15, weight='bold', pad=30)
plt.xlabel('Month', color='grey', weight='bold', position=(.5, 0), labelpad=20, fontsize=12)
plt.ylabel('Sales in USD', color='grey', weight='bold', position=(.5, .5), labelpad=20, fontsize=12)
plt.show()


#Graph for top 3 Products within the selected year and month
y_n = [top_item for top_item in top_3_dict]
x_n = [top_sale for top_sale in top_3_dict.values()]
ax = plt.subplots(1, 1, figsize=(14, 8))
plt.xticks(weight='bold')
plt.yticks(weight='bold')
plt.barh(y_n, x_n, align='center')
plt.xlabel('Sales in USD', color='grey', weight='bold', position=(.5, 0), labelpad=20, fontsize=12)
plt.ylabel('Product Name', color='grey', weight='bold', position=(.5, .5), labelpad=20, fontsize=12)
plt.title(f"Top Selling Products for {month_sel} {year_sel}", color='grey', fontsize=15, weight='bold', pad=30)
plt.show()

#Graph for top 5 Products for the selected year
y_n_year = [top_item for top_item in top_5_dict]
x_n_year = [top_sale for top_sale in top_5_dict.values()]
ax = plt.subplots(1, 1, figsize=(14, 8))
plt.xticks(weight='bold')
plt.yticks(weight='bold')
plt.barh(y_n_year, x_n_year, align='center')
plt.xlabel('Sales in USD', color='grey', weight='bold', position=(.5, 0), labelpad=20, fontsize=12)
plt.ylabel('Product Name', color='grey', weight='bold', position=(.5, .5), labelpad=20, fontsize=12)
plt.title(f"Top Selling Products for {year_sel}", color='grey', fontsize=15, weight='bold', pad=30)
plt.show()