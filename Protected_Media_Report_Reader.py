import csv
import os

class ProtectedMedia(object):

    def __init__(self):
        super().__init__()

    def read_report(self, file):
        with open(os.getcwd()+"/Protected_Media_Reports/1000437-"+file+".csv", 'r') as report:
            reader = csv.DictReader(report)
            data = [x for x in reader if x['l2']]
            return data
