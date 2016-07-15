import urllib2, os
from datetime import datetime
from bs4 import BeautifulSoup

NON_CONTRIBUTION_COLOR = "#eeeeee"

response = urllib2.urlopen("https://github.com/users/{0}/contributions".format(os.environ["GITHUB_USER_NAME"])).read()
soup = BeautifulSoup(response, 'html.parser')

def did_contribute(date):
    for day_elem in soup.svg.g.find_all('g'):
        day_data = day_elem.find_all('rect')[-1]
        day_date = datetime.strptime(day_data['data-date'], '%Y-%m-%d').date()
        if (date == day_date):
            # If today
            if day_data['fill'] == NON_CONTRIBUTION_COLOR:
                return False
            else:
                return True

if __name__ == "__main__":
    today_date = datetime.today().date()
    did_contribute(today_date)
