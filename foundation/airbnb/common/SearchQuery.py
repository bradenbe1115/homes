from typing import Tuple

#TODO: abstract search query class

PROPERTY_TYPE_MAP = {
    'House':1,
    'Apartment':3,
    'Guesthouse':2,
    'Hotel':4
}

class SearchQuery:

    URL_ROOT = "https://www.airbnb.com/s/{city}--{state}--{country}/homes"
    CHECK_IN_CHECK_OUT_URL_ROOT = "checkin={check_in}&checkout={check_out}"
    URL_EXCLUDE_ATTRIBUTES = ['_city','_state','_country','check_in','check_out']
    
    def __init__(
            self, 
            city: str, 
            state: str, 
            country: str, 
            check_in: str,
            check_out: str,
            adults: int = None,
            children: int = None,
            infants: int = None,
            min_bedrooms: int = None,
            min_beds: int = None,
            property_types: list = None):
        
        self.city = city
        self.state = state
        self.country = country
        self.check_in = check_in
        self.check_out = check_out
        self.adults = adults
        self.children = children
        self.infants = infants
        self.min_bedrooms = min_bedrooms
        self.min_beds = min_beds
        self.l2_property_type_ids = property_types

        return
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        self._city = str(value).replace(" ","-")

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):

        if len(str(value)) <= 2:
            raise Exception("State Abbreviated - Search Query class only accepts full state names")
        
        else:
            self._state = str(value).replace(" ","-")

    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, value):
        self._country = str(value).replace(" ","-")

    @property
    def l2_property_type_ids(self):
        return self._l2_property_type_ids
    
    @l2_property_type_ids.setter
    def l2_property_type_ids(self, value):
        
        if value == None:
            self._l2_property_type_ids = None
            return

        mapped_property_types = []
        for property_type in value:
            
            if property_type not in list(PROPERTY_TYPE_MAP.keys()):
                raise Exception(f"Property type only takes the values {*list(PROPERTY_TYPE_MAP.keys()),}")
            
            else:
                mapped_property_types.append(PROPERTY_TYPE_MAP[property_type])
        
        self._l2_property_type_ids = mapped_property_types
    
    @property
    def query(self):

        query = self.URL_ROOT.format(city=self.city, state=self.state, country=self.country)
        query += ('?' + self.CHECK_IN_CHECK_OUT_URL_ROOT.format(check_in = self.check_in, check_out = self.check_out))
        
        params = [x for x in self.__dict__.keys() if x not in self.URL_EXCLUDE_ATTRIBUTES and self.__dict__[x] != None]
        
        for param in params:

            param_url_name = param if param[0] != "_" else param[1:]

            if type(self.__dict__[param]) == list:
                for value in self.__dict__[param]:
                    
                    query += f'&{param_url_name}={value}'
            else:
                query += f'&{param_url_name}={self.__dict__[param]}'
        

        return query
                


    
