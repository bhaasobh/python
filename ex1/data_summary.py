#name : Bahaa Sobh ID : 204657365

import csv ,os,json

class DataSummary:
    def __init__(self,datafile: str,metafile: str):
            self.data_summary = list()
            if not datafile or not metafile:
                raise ValueError("need to pass both params")
            try:
                with open(datafile, 'r') as json_file:
                    self.json_data = json.load(json_file) #reading the json file
            except FileNotFoundError:
                raise ValueError(f"JSON file '{datafile}' not found.")

            try:
                with open(metafile, 'r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    self.csv_fields = csv_reader.fieldnames #get the fields name from the excel
            except FileNotFoundError:
                raise ValueError(f"CSV file '{metafile}' not found.")

            for data in self.json_data['data']:
                summary_record = {}
                for field in self.csv_fields:
                    if field in data:
                        summary_record[field] = data[field]
                    else:
                        summary_record[field] = None

                self.data_summary.append(summary_record)

    #DataAcsses returned a single record or list
    def DataAccess(self, item):
        if(isinstance(item,int)):
            res = dict()
            try:
                res = self.data_summary[item]
            except :
                raise IndexError("out of bounds index")
            return res
        else:
            if(item in self.csv_fields):
                res = list()
                for record in self.data_summary:
                    try :
                        res.append(record[item])
                    except:
                        pass
            else:
                raise Exception("unknown feature")
            return res

    __getitem__ = DataAccess



    #sum return the sum of the objects d1
    def sum(self,item):
        try:
            res = len(self[item])
            return res
        except:
          raise  ValueError("unknown feature")

    def count(self,item):
        if (item in self.csv_fields):
            res =0
            for record in self.data_summary:
                if record[item]==None:
                    res +=1
        else:
            raise Exception("unknown feature")
        return res

    def mean(self,item):
        count =0;
        i=0;
        res=0;
        if (item in self.csv_fields):
            for record in self.data_summary:
                try:
                    if record[item]!=None:
                        i+=1
                        number=float(record[item])
                        count += number
                except:
                     raise TypeError("Feature TypeError")
        else:
            raise Exception("Unknown Feature")

        res = count/i
        return res


    def min(self,item):
        res = 0;
        all = list()
        if (item in self.csv_fields):
            for record in self.data_summary:
                try:
                    if record[item] != None:
                        all.append(float(record[item]))
                except:
                    raise TypeError("Feature TypeError")
        else:
            raise Exception("Unknown Feature")
        return min(all)

    def max(self,item):
        res = 0;
        all = list()
        if (item in self.csv_fields):
            for record in self.data_summary:
                try:
                    if record[item] != None:
                        all.append(float(record[item]))
                except:
                    raise TypeError("Feature TypeError")
        else:
            raise Exception("Unknown Feature")
        return max(all)

    def unique(self,item):
        unique_list = []
        if (item in self.csv_fields):
            list = self[item]
            for x in list:
                if x not in unique_list and x != None:
                    unique_list.append(x)
            unique_list.sort()
            return unique_list
        else :
            raise Exception("Unknown Feature")

    def mode(self,item):
        counter = 0
        res = []
        if (item in self.csv_fields):
            listt = self[item]
            uniqueList = self.unique(item)
            for record in listt:
                if record in uniqueList:
                    listt.remove(record)
            for x in listt:
                if x not in res and x != None:
                    res.append(x)
            res.sort()
            return res
        else :
            raise Exception("Unknown Feature")

    def empty(self,item):
        listt = self[item]
        count =0
        for x in listt:
            if x == None:
                count = count+1
        return count

    def to_csv(self,filename,delimiter=','):
        supported_delimiter=['.',':','|','-',';','#','*',',']
        if(delimiter not in supported_delimiter):
            delimiter = ','

        features =self.csv_fields

        with open(filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=delimiter)

            csv_writer.writerow(features)

            for record in self.data_summary:
                values = [record.get(feature, '') for feature in features]
                csv_writer.writerow(values)
            print("excel saved")
