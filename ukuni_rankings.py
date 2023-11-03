from bs4 import BeautifulSoup
from requests import get


def rankings(subject):
    rks = {}
    url = "https://www.ukuni.net/uk-ranking/subject/" + subject
    soup = BeautifulSoup(get(url).text, "lxml")
    for tr in soup.find_all("tr"):
        uni = tr.find("td", {"class": "views-field views-field-title-1"}).string
        rk = tr.find("td", {"class": "views-field views-field-field-times"}).string
        rks[uni] = rk
    return rks


def overall_rankings():
    rks = []
    url = "https://www.ukuni.net/uk-ranking/overall"
    soup = BeautifulSoup(get(url).text, "lxml")
    for tr in soup.find_all("tr"):
        try:
            uni = tr.find("td", {"class": "views-field views-field-title"}).string
            rk = tr.find("span", {"class": "timesred"}).string.strip()
        except (AttributeError):
            continue
        rks.append([uni, rk])
    return rks


if __name__ == "__main__":
    # math_rks=rankings('mathematics')
    # cs_rks=rankings('computer-science')
    ovrl_rks = overall_rankings()
