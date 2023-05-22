"""
Purpose: Illustrate the math module and how to write
defensive functions by trying them, 
and if things don't work provide a custom message.

Use try / except / finally whenever a valid function could cause an error
e.g.,
- a number is not valid such as a negative radius or age
- a string is empty or missing
- the requested resouce could not be found

The math module includes:
- pi
- sin/cos/tan
- factorial
- sqrt for square root
- cbrt (in 3.11) for cube root
- comb(n,k) for combinations i.e.,
    number of ways to choose k items from n items
    w/out repetition and w/out order
- perm(n,k) for permuations i.e.,
    number of ways to choose k items from n items
    w/out repetition and With order

@ uses math module - for some advanced math

"""

import math

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)



def get_circle_area_given_radius(radius):
    """
    Return area of a circle given the radius.

    @param radius: the radius of the circle
    @return: the area of the circle
    @raise Exception: if radius is not a number

    """

    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"CALLING get_circle_area({radius})")

    try: 
        area = 2 * math.pi * radius
        logger.info(f"The circle area is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None


def get_circle_areas_given_list(radius_list):
    """
    This function should return a list with the areas of each circle

    Keyword arguments:
    radius_list -- a list of radius values (items may be invalid)
    """
    logger.info(f"CALLING get_circle_area({radius_list})")

    if len(radius_list) == 0:
        logger.error("Please add some items to the list. Nothing to do.")
        quit() # quit the program

    area_list = [] # empty list to hold the areas

    # for every element in the list passed in 
    for r in radius_list:

        try:
            area = get_circle_area_given_radius(r)
            logger.info(f"r = {r}, area={area}")
            area_list.append(area)

        except Exception as ex:
            logger.error(f"radius = {r}, Error: {ex}")


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# Literally: "if this module name == the name of the main running module"
# (as opposed to being imported by another module like we do the logger),
# then, follow these instructions.
if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")

    logger.info("TRY: Call get_circle_area_given_radius() function with a different values.")
    get_circle_area_given_radius(5)
    get_circle_area_given_radius(-16)
    get_circle_area_given_radius(math.inf)
    get_circle_area_given_radius('five')
    logger.info("")

    logger.info("TRY: Call get_circle_areas_given_list() function with a list of GOOD values")
    good_list = [5, 10, 25, 30, 45, 50]
    get_circle_areas_given_list(good_list)
    logger.info("")


    logger.info("TRY: Call get_circle_areas_given_list() function with a list that may include BAD values")
    bad_list = [-5, 0, math.inf, '30']
    get_circle_areas_given_list(bad_list)
  
    print("Done. Please check the log file for more details.")


