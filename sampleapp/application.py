from utils.loghelper import logger as logging;

from utils.DBHelper import DBHelper;
from parsers.DataParser import AirportParser;
from utils.sendmails import sendMail;

class AirportApp:

    def __init__(self):
        logging.info("Initialized ");

    def __del__(self):
        logging.info("Destructed ")

    def readFile(self):
        logging.info("reading File ")
        pass;

    def parseFile(self, fileName):
        logging.info("parsing File")
        airportParser = AirportParser();
        airportParser.parseFile(fileName);
        logging.info("Parsed Successfully")
        self.storeInDb(airportParser.records)
        pass;

    def storeInDb(self, records):
        logging.info("Storing in DB ")
        try:
            mydb = DBHelper.getConnection();
            for record in records:
                cursor = mydb.cursor()
                cursor.execute("insert into table values(%s,%s,%s,%s)", ());
                cursor.close();
                logging.info("Updated Airport Record To Database ")
            sendMail("Successfull");
        except:
            logging.error("Error In Store in DB ")
            sendMail("Error Processing the Records ")
        finally:
            if (mydb is not None & mydb.is_connected()):
                mydb.close();

    def updateStatus(self):
        logging.info("Updating Status")
        pass;

def main():
    logging.info('Staring application')
    AirportApp().parseFile("d:/inputData/airports.csv");

if __name__ == '__main__':
    main();
