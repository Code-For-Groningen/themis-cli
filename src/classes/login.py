# Login to Themis
import requests
from requests.exceptions import HTTPError
from re import search
from datetime import datetime

class Themis:
    # Set environment
    def __init__(self, course, assignment, username, password) -> None:
        self.url = 'https://themis.housing.rug.nl/course/' + f'{self.getCurrentAcademicYear()}/' + course + '/' + assignment
        self.username = username
        self.password = password
        self.req = requests.Session()

        self.__login(username, password)
    
    # Login
    def __login(self, username, password):
      self.username = username
      self.password = password

      url = 'https://themis.housing.rug.nl/log/in'
      r = self.req.get(url)

      csrf = search(r'_csrf" value="(.*)"', r.text).group(1)
      
      payload = {'username': username, 'password': password, '_csrf': csrf}
      
      # TODO: WHY DOES LOGGING IN NOT WORK
      headers = {
          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
          "Accept-Language": "en-US,en;q=0.5",
          "Accept-Encoding": "gzip, deflate, br",
          "Content-Type": "application/x-www-form-urlencoded",
          "Origin": "https://themis.housing.rug.nl",
          "DNT": "1",
          "Connection": "keep-alive",
          "Referer": "https://themis.housing.rug.nl/log/in",
          "Cookie": f"session={self.req.cookies['session']}",
          "Upgrade-Insecure-Requests": "1",
          "Sec-Fetch-Dest": "document",
          "Sec-Fetch-Mode": "navigate",
          "Sec-Fetch-Site": "same-origin",
          "Sec-Fetch-User": "?1",
          "Pragma": "no-cache",
          "Cache-Control": "no-cache",
      }

      r = self.req.post(url, data=payload, headers=headers, allow_redirects=True)
      print(r.text)
      if (r.status_code == 200) or (r.status_code == 302):
        return True
      else:
        return False
    
    # Get exercises
    def __getExercises(self):
      if self.loginPersist():
        print(self.req.cookies["session"])
        r = self.req.get(self.url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0', 'Cookie':f'session={self.req.cookies["session"]}'})
        print(r.text)
        return search(r'class="iconize ass-submitable" title="(.+?)"', r.text).group(1)

    # Checks if logged in
    def loginPersist(self):
        try:
          self.req.get(self.url).raise_for_status()
          return True
        except HTTPError:
          if not self.username and not self.password:
             return False
          
          return self.login(self.username, self.password)
            
       
    # Get year
    def getCurrentAcademicYear(self):
        now = datetime.now()
        if now.month >= 8:
            return str(now.year) + "/" + str(now.year + 1)
        else:
            return str(now.year - 1) + "/" + str(now.year)
        

    # Does nothing for now
    # TODO: Get urls for exerciss and download inputs and outputs
    def formatExercises(self):
      if self.loginPersist():
        exercises = self.__getExercises()
        for ex in exercises:
           print(ex)

if __name__ == "__main__":
    t = Themis('progfun', 'tutorial4', 's5230837', 'Bobit0Drog@231')
    t.formatExercises()