from faker import Faker
fake = Faker()
import random
from random import randrange
import datetime
from dateutil.relativedelta import *


CustomerNumber=100
OperatorNumber = 3
max_call_number = 5

class Operator:
    def __init__(self,name,marketshare):
        self.name = name
        self.marketshare = marketshare
        self.customers = []

    def info(self):
        print(self.name)

def CreateOperator(OperatorNumber = OperatorNumber):
    operators = []
    last_marketshare = 0

    for i in range(OperatorNumber):
        if i==0:
            ms = random.randint(0,100)
            last_marketshare += ms
            o = Operator(fake.company(),(ms/100))
            operators.append(o)
        elif i==OperatorNumber-1:
            o = Operator(fake.company(),((100-last_marketshare)/100))
            operators.append(o)

        else:
            ms = random.randint(0,(100-last_marketshare))
            o = Operator(fake.company(),(ms/100))
            operators.append(o)
            last_marketshare += ms
    return operators

class Customer:
    def __init__(self,customerid,msisdn,country_code,msisdn_nonCC,custumerid_nonCC):
        self.customerid = customerid
        self.msisdn = msisdn
        self.operator = ""
        self.contacts = []
        self.call_records = []
        self.country_code=country_code
        self.msisdn_nonCC=msisdn_nonCC
        self.customerid_nonCC=custumerid_nonCC

    def info(self):
        print(self.customerid+"\n"+self.msisdn)


def CreatCustomer(CustomerNumber = CustomerNumber):
    if CustomerNumber % 100 != 0:
        print("""Customer numbers in multiples of 100""")
    else:
        customers = []
        for i in range(CustomerNumber):
            while True:
                msisdn = fake.msisdn()
                customerid = fake.isbn13(separator="")
                country_code=msisdn[0:3]
                msisdn_nonCC=msisdn[3:]
                custumerid_nonCC=customerid[3:]

                if int(msisdn[0])!=0 and int(customerid[0])!=0:
                    break
                #elif int(msisdn_nonCC ==custumerid_nonCC):

            #print(msisdn,customerid)
            c = Customer(customerid,msisdn,country_code,msisdn_nonCC,custumerid_nonCC)
            customers.append(c)
        return customers

operators = CreateOperator()
created_customers = CreatCustomer()
customers_4_operators = created_customers.copy()
for i in range(len(operators)):
    for j in range(int(operators[i].marketshare*100)):
        c = customers_4_operators.pop()
        c.operator = operators[i]
        operators[i].customers.append(c)


for c in created_customers:
    for i in range(random.randint(0,CustomerNumber)):
        possible_contact = random.choice(created_customers)
        if possible_contact not in c.contacts:
            c.contacts.append(possible_contact)

class CallRecord():
    def __init__(self,caller,called,timestamp,duration):
        self.CDRNo = "".join(fake.itin().split("-"))
        self.caller = caller
        self.called = called
        self.timestamp = timestamp
        self.duration = duration #Second


    def info(self):
        print(self.CDRNo)


def random_date():
    start = datetime.datetime(2013, 9, 20,13,0)
    start += datetime.timedelta(minutes=randrange(1000))
    start += datetime.timedelta(days=randrange(0,30))
    start += relativedelta(months=randrange(2,12))
    return start

CDR = []
print("CountryCode  MSISDN \t MSISDN_NONCC \t Reciever Number \t Date   Time  Duration \t  " )
for c in created_customers:
    for contact in c.contacts:
        for i in range(1,random.randint(1,max_call_number)):
            cdr = CallRecord(caller=c,called=contact,timestamp=random_date().strftime("%d-%m-%y %H:%M"),duration=random.randint(0,120*60))
            c.call_records.append(cdr)
            CDR.append(cdr)

            #print(CDR)
            print(c.country_code, "\t",c.msisdn,"\t",c.msisdn_nonCC,"\t",contact.msisdn ,"\t",random_date().strftime("%d-%m-%y %H:%M"),random.randint(0,120*60))

callback=None
for c in created_customers:
    for contact in c.contacts:
        for i in range(1,random.randint(1,max_call_number)):
            cdr = CallRecord(caller=c,called=contact,timestamp=random_date().strftime("%d-%m-%y %H:%M"),duration=random.randint(0,120*60))
            c.call_records.append(cdr)
            CDR.append(cdr)


            #print(CDR)
            if(cdr.caller==cdr.called):
                callback=True
                if(cdr.duration<500):
                    print(" FAKE RECORDS ARE ")
                    print("CountryCode  MSISDN \t MSISDN_NONCC \t Reciever Number \t Date   Time  Duration \t  " )
                    print(c.country_code, "\t",cdr.caller.msisdn,"\t",c.msisdn_nonCC,"\t",cdr.called.msisdn ,"\t",cdr.timestamp,cdr.duration)
