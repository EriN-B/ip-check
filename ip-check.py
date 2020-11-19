import geoip2.database
import re
import geoip2.database

#Import local Database and  create reader to read from it
reader=geoip2.database.Reader('./GeoLite2-City_20200901/GeoLite2-City.mmdb')
#import data file
data = open('', 'r') #data input
output = open('','w') #first input validation, clean the Document
output_r = open('/Users/erin.2/Projects/lukb/DI/Aufträge/GeoIp/Data/output.txt','r')
end_output = open("/Users/erin.2/Projects/lukb/DI/Aufträge/GeoIp/Data/end_output.txt",'w') #last validation. This file contains only ip adresses
Lines = data.readlines() 
index=0
count=0
re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}") #ip-regex
data2 = data.read()
# Strips the newline character
for line in Lines: 
    if True:
        ip = re.findall(re_ip,line)
        output.write(("Line{}: {}".format(count, ip)))
        output.write("\n")
        count_index = line.split()
        index+=1
        count +=1

Lines_output = output_r.readlines()

for line in Lines_output: #Find the IP's
    find_start = line.find("[")
    find_end = line.find("]")
    find_comma = line.find(",")
    first = line[find_start+2:find_comma-1]
    end_output.write(first+"\n")

#Import local Database and  create reader to read from it
reader=geoip2.database.Reader('./GeoLite2-City_20200901/GeoLite2-City.mmdb')
#import data file
data = open('/Users/erin.2/Projects/lukb/DI/Aufträge/GeoIp/Data/end_output.txt', 'r')
log = open("/Users/erin.2/Projects/lukb/DI/Aufträge/GeoIp/Data/log.txt",'w')
line = data.readline()
cnt = 1
not_identified = 0 #Number of not identified Ip's
not_identified_a = [] #store not identified ip's
while line:
    try:
        ip=line.rstrip()
        response =reader.city(ip)
        log.write(ip+" --> "+response.country.name+"\n")
        line = data.readline()    
        cnt += 1    
    except:
        line = data.readline()     
        not_identified += 1j
        not_identified_a.append(ip)
        
        
log.write(str(cnt+not_identified)+" E-Mails scanned"+"\n")
log.write(str(not_identified)+" E-mails couldnt be identified, "+(str((100/cnt)*not_identified))+" %")

#Close all openened Reader
reader.close()  
data.close()
log.close()
output.close()
output_r.close()
end_output.close()
