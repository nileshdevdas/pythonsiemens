from models import  Airport;

class AirportParser:
    records = list();
    def parseRecord(self, row):
        airport = Airport.Airport();
        airport.id=row[0];
        airport.ident= row[1]
        airport.type=row[2]
        airport.name= row[3]
        return airport;

    def parseFile(self, filename, encoding="UTF-8"):
        data =open(file=filename, mode='r', encoding=encoding);
        lines = data.readlines()
        for line in lines:
            record = self.parseRecord(line.split(","));
            self.records.append(record);
