import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import cloudscraper  # type: ignore
from requests_html import HTMLSession  # type: ignore


def linkToSoup_scrapingAnt(
      url_to_Scrape, pCountry=None, apiKey=None, loadCss=None,
      parser='html.parser', isv=True, returnErr=False):
    '''
    This function uses the ScrapingAnt API to fetch and parse a webpage,
    optionally using a proxy country and CSS selector.
    It handles API key management, URL construction, and error reporting,
    returning a BeautifulSoup object or an error message.
    '''

    defaultKey = 'YOUR_API_TOKEN'  # paste here
    sa_api = 'https://api.scrapingant.com/v2/general'
    sa_key = str(apiKey) if apiKey else defaultKey

    qParams = {'url': url_to_Scrape, 'x-api-key': sa_key}
    if pCountry:
        qParams['proxy_country'] = pCountry
    if loadCss:
        qParams['wait_for_selector'] = loadCss

    reqUrl = f'{sa_api}?{urlencode(qParams)}'
    if isv:
        print('fetching with ScrapingAnt:', url_to_Scrape, '\nwith ', reqUrl)
    r = requests.get(reqUrl)
    if r.status_code == 200:
        return BeautifulSoup(r.text, parser)

    if isv:
        print('failed to fetch page', r.status_code, r.reason)
    errorMsg = f'{r.status_code} {r.reason} from {reqUrl}'
    errorMsg += f'\nfailed to fetch {url_to_Scrape}'
    return {'errMsg': errorMsg, 'resp': r} if returnErr else None


# def rqSoup(targetUrl, conf={}, isv=True, returnErr=False):
def linkToSoup(targetUrl, conf={}, isv=True,
               returnErr=False, returnResp=False):
    '''
    This function fetches and parses a webpage using the requests library,
    with optional configuration for headers, cookies, etc.
    It supports detailed logging and error handling, and
    can return the response object along with the parsed BeautifulSoup object.
    '''

    bsParser = conf.get('parser', 'html.parser')
    reqArgs = {k: v for k, v in conf.items() if k != 'parser'}
    try:
        # can pass headers/cookies/etc via conf
        r = requests.get(targetUrl, **reqArgs)
        # r = cloudscraper.create_scraper().get(targetUrl)
        # r = HTMLSession().get(targetUrl)

        if r.status_code == 200:
            # ######## CAN ADD OTHER CHECKS ######## #
            if isv:
                print(repr(r), '[ parser:', bsParser, '] from', r.url)
            soup = BeautifulSoup(r.content, bsParser)
            return (soup, r) if returnResp else soup

        errMsg = f'<{r.status_code} {r.reason}> - '
        errMsg = f'{errMsg}Failed to scrape {targetUrl}'
    except Exception as e:
        errMsg = f'Failed to scrape {targetUrl} \n - errorMsg: "{str(e)}"'
    if isv:
        print(errMsg)

    ret1 = errMsg if returnErr else None
    return (ret1, r) if returnResp else ret1


def linkToSoup_h(targetUrl, conf={}, isv=True, returnErr=False):
    '''
    This function fetches and parses a webpage
    using the requests_html library, with optional configuration.
    It handles errors and logging,
    returning a BeautifulSoup object or an error message.
    '''

    parser = conf["parser"] if "parser" in conf else None
    try:
        # r = requests.get(targetUrl)
        # r = cloudscraper.create_scraper().get(targetUrl)
        r = HTMLSession().get(targetUrl)

        if r.status_code == 200:
            # ######## CAN ADD OTHER CHECKS ######## #
            return BeautifulSoup(r.content, parser)
        errMsg = f'<{r.status_code} {r.reason}> - '
        errMsg = f'{errMsg}Failed to scrape {targetUrl}'
    except Exception as e:
        errMsg = f'Failed to scrape {targetUrl} \n - errorMsg: "{str(e)}"'
    if isv:
        print(errMsg)
    return errMsg if returnErr else None


def linkToSoup_c(targetUrl, conf={}, isv=True, returnErr=False):
    '''
    This function fetches and parses a webpage
    using the cloudscraper library to bypass anti-bot measures.
    It includes error handling and logging,
    returning a BeautifulSoup object or an error message.
    '''

    parser = conf["parser"] if "parser" in conf else None
    try:
        # r = requests.get(targetUrl)
        r = cloudscraper.create_scraper().get(targetUrl)
        # r = HTMLSession().get(targetUrl)

        if r.status_code == 200:
            # ######## CAN ADD OTHER CHECKS ######## #
            return BeautifulSoup(r.content, parser)
        errMsg = f'<{r.status_code} {r.reason}> - '
        errMsg = f'{errMsg}Failed to scrape {targetUrl}'
    except Exception as e:
        errMsg = f'Failed to scrape {targetUrl} \n - errorMsg: "{str(e)}"'
    if isv:
        print(errMsg)
    return errMsg if returnErr else None
