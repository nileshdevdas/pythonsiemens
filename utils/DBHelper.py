from utils.loghelper import getLogger;
import configparser;
import mysql.connector;
import os;
class DBHelper:
    def __init__(self):
        getLogger().info("Initialized DBHelper ")
        config = configparser.ConfigParser()
        config.read("c:/application.properties")
        print(os.path);
        self.dbconfig = config["dbconfig"]

    def getConnection(self):
        getLogger().info("GetConnection in DBHelper");
        getLogger().debug("Username " + self.dbconfig['dbusername']);
        getLogger().debug("Password " + self.dbconfig['dbpassword']);
        mydb = mysql.connector.connect(
            user=self.dbconfig['dbusername'],
            password=self.dbconfig['dbpassword']
        )
        return mydb;
