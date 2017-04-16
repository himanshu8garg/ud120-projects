#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len(enron_data)
i =0
j=0
minimum=0
maximum=0
for key,value in enron_data.items():
    print (key, [value for item in value])
    #print enron_data[key]["poi"]
    #print enron_data[key]["email_address"]
    minimum=enron_data[key]["exercised_stock_options"]
    if (minimum>enron_data[key]["exercised_stock_options"]):
        minimum=enron_data[key]["exercised_stock_options"]
    if (enron_data[key]["total_payments"]== "26704229"):
        j+=1
	print key 
#print len(enron_data)-i
print i
print j

#print enron_data["PRENTICE JAMES"]["total_stock_value"]
#for key,value in enron_data.items():
#    if (enron_data[key]=='COLWELL WESLEY'):
#        print len(enron_data[key]["email_address"])
#print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
#print enron_data["SKILLING JEFFREY K"]["total_payments"]
#print enron_data["LAY KENNETH L"]["total_payments"]
#print enron_data["FASTOW ANDREW S"]["total_payments"]

stocks=[]
for key, value in enron_data.items():
    if (value["exercised_stock_options"]!="NaN"):
        stocks.append(value["exercised_stock_options"])
print stocks
print min(stocks)
print max(stocks)
stocks=sorted(stocks)
print stocks[0]
print stocks[(len(stocks)-1)]

salary=[]
for key, value in enron_data.items():
    if (value["salary"]!="NaN"):
        salary.append(value["salary"])
print salary
print min(salary)
print max(salary)
salary=sorted(salary)
print salary[0]
print salary[(len(salary)-1)]





