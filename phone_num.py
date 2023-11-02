import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

num=input("Enter phone number:")
c_num=phonenumbers.parse(num,"CH") #CH stands for country history
print(geocoder.country_name_for_number(c_num,"en")) #en stands for english language
service_num=phonenumbers.parse(num,"RO")
print(carrier.name_for_number(service_num,"en"))
