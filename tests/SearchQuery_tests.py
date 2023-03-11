from homes.foundation.airbnb.common.SearchQuery import SearchQuery

def test_search_queries(city: str, state: str, country: str, check_in: str, check_out: str, **kwargs):
    sq = SearchQuery(city, state, country, **kwargs)
    return sq.get_query(check_in, check_out)

assert test_search_queries('Detroit','Michigan','United States','2023-03-25','2023-04-01') == 'https://www.airbnb.com/s/Detroit--Michigan--United-States/homes?checkin=2023-03-25&checkout=2023-04-01'

assert test_search_queries('Detroit','Michigan','United States','2023-03-25','2023-04-01',adults=2) == 'https://www.airbnb.com/s/Detroit--Michigan--United-States/homes?checkin=2023-03-25&checkout=2023-04-01&adults=2'

print(test_search_queries('Detroit','Michigan','United States','2023-03-25','2023-04-01',property_type='House'))