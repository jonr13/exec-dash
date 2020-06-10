import os
import pandas as pd

#functions
def file_name_translator(file_name):
    month_table = {'01':'Janurary', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
    year = str(file_name[6:10])
    month_num = file_name[-6:-4]
    month = month_table[month_num]
    return f"{month}, {year}"

def month_name_to_numb(monthname):
    month_table_reversed = {'Janurary':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
    return month_table_reversed[monthname]

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


while True:
    try:
        csv_read = pd.read_csv(csv_name)
        break
    except FileNotFoundError:
        print("Hello, unfortunately I couldn't find that file. Please make sure sales data for that year and month exists and resubmit.")
        year_sel = choose_year()
        month_sel = choose_month()
        csv_read = pd.read_csv(csv_name)
        break

print(csv_read)

#if file selection fails, produce an error message that says "Hello, unfortunately I couldn't find that file. Please check to make sure the file and filepath is correct and resubmit."

print("-----------------------")
print("Crunching the data...")

#Output Requirements:
#Total Monthly Sales: sum of total monthly sales for each product, formatted as USD(from function) to two decimal places

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

#jordan_stats = pd.read_csv("jordan_stats.csv")
#print(jordan_stats.head(3))
# displays the first three rows of the dataset
#print(jordan_stats.count())
#counts the rows of the dataset

#print(jordan_stats[stats["BLK"] > 4])


#List of Top Selling Products: top sellers list with sum of total monthly sales formatted with USD function and two decimal places
#2 Graphs depicting the information above - graphs should include details on month selected
#Additional enhancements: Compare sales across months - total annual graph as the third graph?

