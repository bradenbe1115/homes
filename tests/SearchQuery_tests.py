from homes.foundation.search_query import AIRBNBSearchQuery

assert AIRBNBSearchQuery(city='Detroit',state='Michigan',country='United States',check_in='2023-03-25',check_out='2023-04-01').query == 'https://www.airbnb.com/s/Detroit--Michigan--United-States/homes?checkin=2023-03-25&checkout=2023-04-01'

assert AIRBNBSearchQuery(city='Detroit',state='Michigan',country='United States',check_in='2023-03-25',check_out='2023-04-01',adults=2).query == 'https://www.airbnb.com/s/Detroit--Michigan--United-States/homes?checkin=2023-03-25&checkout=2023-04-01&adults=2'

print(AIRBNBSearchQuery(city='Detroit',state='Michigan',country='United States',check_in='2023-03-25',check_out='2023-04-01',adults=2,property_types=['House','Apartment']).query)