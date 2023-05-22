from Band_tickets import Band_tickets

from util_datafun_logger import setup_logger

if __name__ == "__main__":

    logger, logname = setup_logger(__file__)

    band1 = "Blink182"
    tickets1 = "Tickets sold @ diff shows"
    data1 = [25, 20, 40, 25, 30]
    object1 = Band_tickets(band1, tickets1, data1)

  
    band2 = "Green Day"
    tickets2 = "Tickets sold @ diff shows"
    data2 = [15, 30, 20, 25, 35]
    object2 = Band_tickets(band2, tickets2, data2)

    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")

    object_list = [object1, object2]

    for object in object_list:
      logger.info(object)
      logger.info(f"Count: {object.count()}")
      logger.info(f"Total Points Scored: {object.sum()}")
      logger.info(f"Average Points Per Game: {object.average()}")
      logger.info(f"Median: {object.median()}")
      logger.info("------------------")

      with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())