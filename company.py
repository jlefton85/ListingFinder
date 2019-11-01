import pandas as pd

class Company:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.jobs = pd.DataFrame(columns=["Job", "Location", "Listing Date"])
    
    def parse_json(self):
        pass
