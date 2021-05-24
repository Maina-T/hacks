from datetime import datetime
import json

class DateWork:
    # convert date 
    def convert_date(self):
        old = '25/05/2021'
        dateobj = datetime.strptime(old,'%d/%m/%Y')
        print(dateobj)

    
    def myconverter(self,value):
        if isinstance(value, datetime.datetime):
            return value.__str__()
    
    # Serialize date
    def serialize_datetime(self):
        # self.scraped_orders is list of dictionary with datetime.datetime value
        for order in self.scraped_orders:
            convert = json.dumps(order, default = self.myconverter)
            bid_order = json.loads(convert) # convert string dictionary to dictionary
            # print(type(bid_order))
            self.orders.append(bid_order)

if __name__ == "__main__":
    tit = DateWork()
    tit.convert_date()
    tit. serialize_datetime()