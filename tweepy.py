from tld import get_tld 
import csv 
from urllib.parse import urlparse

domains_names = {}
count = 0

# opening the CSV file 
with open('final-URLs.csv', mode ='r')as file: 
    
  # reading the CSV file 
  csvFile = csv.reader(file) 
  
  # displaying the contents of the CSV file 
  for lines in csvFile:  
    res = get_tld(lines[0], as_object=True) #Get the root as an object 
    print (res.fld) #res.fld to extract the domain 
    domains_names.setdefault(res.fld, 0)

    domains_names[res.fld] += 1