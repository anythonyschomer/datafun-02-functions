"""
Purpose: Use the Math Module to create some Functions regarding ticket sales for Live Music
Author: Anythony Schomer
Function 1 - Calculate the ticket sale differential between two bands.
Function 2 - Calculate the total amount of band lineup combinations for a show. 
Function 3 - Find the total amount of tickets sold. 
"""

#Import the Math module
import math

#Setting up the logger
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

#Function 1 - Find the difference of ticket sales for one band vs another band
#Defining the function
def find_ticket_difference_amount(band1_tickets, band2_tickets):

    #Creating a variable that calculates the differance between two teams scores.
    ticket_differential = band1_tickets - band2_tickets
    logger.info(f"The ticket differential for the show is {ticket_differential}")
    return ticket_differential

#Running Function 1
#Showing that it works for positive values (Tickets for a show)
find_ticket_difference_amount(50, 10)
#Showing that it works for negative values (Less tickets sold, less interest in the band)
find_ticket_difference_amount(5, 15)
#Showing that it works when people want to see the same band equally
find_ticket_difference_amount(20, 20)

#Function 2 - Calculate the total amount of band lineup combinations for a show.
#Defining the function
def total_lineup_combinations(diff_bands):

    #Creating a variable that calculates the total starting lineup combinations for a basketball team (From the total, choose 5 starters)
    total_combos = math.comb(diff_bands,5)
    logger.info(f"The total number of combinations for the band lineup is {total_combos}")
    return total_combos

#Test Running Function 2
total_lineup_combinations(10)
total_lineup_combinations(15)
total_lineup_combinations(5)

#Function 3 - Find the total amount of tickets sold. 
#Defining the function
def total_points_scored(band1_show, band2_show, band3__show):

    #Creating a variable that calculates the total points scored for a team
    total_tickets_sold = band1_show + band2_show + band3__show
    logger.info(f"The total number of tickets sold was {total_tickets_sold}")
    return total_tickets_sold

#Test Running Function 3
total_tickets_sold_3bands: (10, 15, 5)
total_tickets_sold_3bands: (25, 35, 20)

#Logging info as required in task 3.1
logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

# Print the logged information
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())