import  random

Numbers = ["1",   "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9",  "0"]
Names = ["Jack", "Andrew", "Mike", "Terry", "Torvald", "Gatsby",    "Alice", "Hana", "Clare", "Janet", "Daisy"]

def get_random_email_name():
    return  random.choice(Names)+random.choice(Numbers)+\
                random.choice(Numbers)+random.choice(Numbers)\
                +random.choice(Numbers)+random.choice(Numbers)\
                +"@gmail.com"

def get_random_Credit_Card_Name():
        return  "Credit Card " + random.choice(Numbers)+ random.choice(Numbers)+ random.choice(Numbers)

def get_random_Address_Name():
        return  random.choice(Names)+ random.choice(Numbers)

def get_company_name():
        return "Company" + random.choice(Numbers)
