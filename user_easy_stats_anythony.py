import statistics 
import turtle  
import sys  

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Ticket sales from bands during a North America Tour
tickets_sold = [
   40,
   45,
   50,
   40,
   65,
   85,
   50,
   100,
   45,
   50,
   65,
   60,
   110,
   50,
   50,
   60,
   70,
   45,
   80,
   70,
   40,
   50,
   30,
   45,
   70,
   75,
   65,
   90,
   90
]
logger.info("tickets_during_tour= " + str(tickets_sold))

# Calculating Averages and measures of central tendency

mean = statistics.mean(tickets_sold)
median = statistics.median(tickets_sold)
mode = statistics.mode(tickets_sold)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")  
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

#Calculating Measures of spread

var = statistics.variance(tickets_sold)
stdev = statistics.stdev(tickets_sold)
lowest = min(tickets_sold)
highest = max(tickets_sold)

# Change to f-strings and use 2 decimal places
logger.info(f"var    = {var:.2f}")
logger.info(f"stdev  = {stdev:.2f}")
logger.info(f"lowest = {lowest:.2f}")
logger.info(f"highest= {highest:.2f}")


# Descriptive: Univariant Timeseries Data.........................

# Creating a dataset that compares the days passed and total number of free throws made at practice
# X values - Days from start date
# Y values - Total Free Throws Made
xtimes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yvalues = [0, 15, 22, 34, 45, 46, 50, 59, 69, 71, 90]

# if the lists are not the same size,
# log an error and quit the program
if len(xtimes) != len(yvalues):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xtimes)}!={len(yvalues)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the correlation function from the statistics module
xx_corr = statistics.correlation(xtimes, xtimes)
xy_corr = statistics.correlation(xtimes, yvalues)

# log the information 
logger.info("Here's some time series data:")
logger.info(f"xtimes:{xtimes}")
logger.info(f"yvalues:{yvalues}")
logger.info(f"correlation between xtimes and xtimes = {xx_corr:.2f}")
logger.info(f"correlation between xtimes and yvalues = {xy_corr:.2f}")

# Calculate slope and intercept of a line

# Here's some bivariant data (two series of data)
# X Values - 3-Pointers Made in a Game
# Y Values - Points Scored in a Game
arrayX = [4, 0, 6, 2, 10, 8, 5, 1]
arrayY = [40, 28, 54, 36, 72, 61, 48, 30]

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(arrayX, arrayY)

# Choose an x value off in the future (future x)
future_x = 200

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{arrayX}")
logger.info(f"y:{arrayY}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_x:d},")
logger.info(f"   we predict the value of y will be { future_y:d}.")
logger.info("How'd we do? Does this make sense given the data?")
logger.info("Remember to close the app. Control c (or d or z maybe) to close it.")

# is the user ready to see a chart?
ready_for_chart = True

logger.info(f"ready_for_chart = {ready_for_chart}")

# if ready for the chart, show the data, the best fit line, and the future prediction

if ready_for_chart:

    screen = turtle.Screen()
    screen.title("Linear Regression and Prediction")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(3)  # range 1-10  (slow-fast)

    w, h = screen.window_width(), screen.window_height()
    # e.g. 512, 480

    # Draw Axes
    t.penup()
    t.goto(w / 2, 0)
    t.pendown()
    t.goto(-w / 2, 0)
    t.penup()
    t.goto(0, h / 2)
    t.pendown()
    t.goto(0, -h / 2)

    # draw points
    for index, year in enumerate(arrayX):
        t.penup()
        t.goto(arrayX[index], arrayY[index])
        t.pendown()
        t.pencolor("blue")
        t.dot(20)

    # draw best-fit line
    h = int(slope * w + intercept)
    t.penup()
    t.goto(w, h)
    w = -w
    h = int(slope * w + intercept)
    t.pencolor("green")
    t.pensize(2)
    t.pendown()
    t.goto(w, h)

    # draw prediction dot
    t.penup()
    t.goto(future_x, future_y)
    t.pendown()
    t.pencolor("red")
    t.dot(20)

    turtle.done()
    screen.mainloop()
    logger.info("Done with the chart.")

else:
    logger.info("Ready for a chart? Edit this program to see an illustration.\n")

# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())