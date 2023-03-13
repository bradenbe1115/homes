


class BaseSearchQuery:
    """
        Base class to implement the domain object of a search query. 
        Search query objects will need to be able to take in site-specific search parameters and build an url query that will be used in downstream objects.

        Specific implementation will vary based on the site in question. Each specific abstraction should override the default query method.

        Args:

            city (str): city to search for properties in
            state (str): state to search for properties in
            country (str): country to search for properties in
            check_in (str): date for first day to search
            check_out (str): date for last day to search
    """

    LOCATION_URL_ROOT = "{city}--{state}--{country}"
    CHECK_IN_CHECK_OUT_URL_ROOT = "{check_in}--{check_out}"

    def __init__(
            self, 
            city: str, 
            state: str, 
            country: str, 
            check_in: str,
            check_out: str):
        
        self.city = city
        self.state = state
        self.country = country
        self.check_in = check_in
        self.check_out = check_out

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
    def query(self):

        query = self.LOCATION_URL_ROOT.format(city=self.city, state=self.state, country=self.country)
        query += self.CHECK_IN_CHECK_OUT_URL_ROOT.format(check_in = self.check_in, check_out = self.check_out)
        return query

            
