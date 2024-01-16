import csv ,os,json

class DataSummary:
    def __init__(self,datafile: str,metafile: str):
        self.datafile = datafile
        self.metafile = metafile
        self.features = []
        self.data = dict()
        with (open(self.metafile) as file):
            reader = csv.reader(file)
            for row in reader:
                self.features.append(row)
                break
        print(len(self.features[0]))
        for item in self.features[0]:
            self.data = item

        countries = []
        with open(metafile , 'r') as file:
            csv_dict = csv.DictReader(file)
            for row in csv_dict:
                countries.append(dict(row))
                print(dict(row))

        with open(self.datafile) as file:
            data = json.load(file)
            #print(data)
        for record in data['data']:
            print('*************')
            for key,value in record.items():
                print(key)