# exec-dash
The following is a README file for the instructions on how to use the executive dashboard generator

Setup: The user should run "dashboard_generator.py" to run the program

Steps:
1. The user is first pomprted to input the year he/she would like to pull sales history for.
He or she should type in a year like '2018' or '2017', for example
* The user also has the option of typing 'show me' to see all available sales history files by year and month

2. Next, the user is then prompted to type in the month within the selected year, that he/she wants to analyze sales for.
He/she should type in month like 'March' or 'May', for example.

* The user also has the option of typing 'show me' to see all available sales history files by year and month

* Error Checking: If the user types in a month that is not available, he/she will receive an error stating
"unforuntately I could not find that file. Please make sure sales data exists for the year/month combination" and is 
asked to retype in a year and a month.

3. The users recieves the following information after successfully loading sales data:
    * Total Month Sales
    * Top 3 Selling Products for that month, year
    * Top 5 Selling Products for the entire year for comparison

4. The user receives 3 graphs for visualization of the data provided above.
    * A line graph of month by month sales for the year selected
    * A bar graph for the top 3 selling products for that month, year
    * A bar graph for the top 5 selling products for the selected year
