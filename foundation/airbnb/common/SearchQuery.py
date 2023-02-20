from typing import Tuple

URL_ROOT = "https://www.airbnb.com/s/{city}--{state}--{country}/homes"
CHECKIN_CHECKOUT_ROOT = "checkin={check_in}&checkout={check_out}"
VALID_KWARGS = ['adults','children','infants']


class SearchQuery:
    def __init__(self, city: str, state: str, country: str, **kwargs):
        self.city = city
        self.state = state
        self.country = country
        self.kwargs = kwargs

        self._validate_inputs()
        self._validate_kw_inputs()
        self._inputs_formatter()
        self._set_base_url()
        self._set_kw_params()
        return

    def get_query(self,check_in: str, check_out: str) -> str:
        """
        Function returns formatted url query to use for AirBnB listings based on class properties

        Returns:
            full_url (str): query url for listings in specified area and with specified parameters
        """
        
        base_url_dates = self.base_url + '?' + CHECKIN_CHECKOUT_ROOT.format(check_in=check_in,check_out=check_out)
        full_url = base_url_dates + self.kw_params

        return full_url
    
    def _set_base_url(self) -> None:
        """
            Class method to set base url for search query. Inputs formatted address keys to root url.    
        """

        self.base_url = URL_ROOT.format(city=self.city, state=self.state, country=self.country)

        return
    
    def _set_kw_params(self) -> None:
        """
            Class method to set keyword params for search url
        """

        kw_params = ""
        for arg, value in self.kwargs.items():
            kw_params += f"{arg.lower()}={value}"

        self.kw_params = kw_params
    
    def _validate_inputs(self) -> Tuple[int, str]:
        """
            Internal class method to do some quick validation on inputs

            Returns:
                result_code (int): code to indicate if validation was successful (0 if successful)
                result_msg (str): Message to indicate result of validation process or errors if applicable
        """

        if self._state_format_check() != 0:
            raise Exception("State Abbreviated")

        return 0, "Success"
    
    def _state_format_check(self) -> int:
        """
            Internal method to check if state name in right format i.e. not abbreviated

            Returns:
                result_code (int): 0 if success, 1 if failed
        """

        if len(self.state) <= 2:
            return 1
        
        else:
            return 0
        
    def _clean_spaces(self) -> None:
        """
            Replaces spaces with hypens for necessary fields
        """
        self.city = self.city.replace(" ","-")
        self.state = self.state.replace(" ","-")
        self.country = self.country.replace(" ","-")

        return


    def _inputs_formatter(self) -> None:
        """
            Formats city, state, and country strings correctly for use in query string         
        """

        self._clean_spaces()

        return
    
    def _validate_kw_inputs(self) -> None:

        for arg in self.kwargs:
            if arg.lower() not in VALID_KWARGS:
                raise Exception(f"{arg} is not a valid argument")
