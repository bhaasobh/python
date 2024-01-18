import csv ,os,json

class DataSummary:
    def __init__(self,datafile: str,metafile: str):
            self.data_summary = list()
            if not datafile or not metafile:
                raise ValueError("need to pass both params")
            try:
                with open(datafile, 'r') as json_file:
                    self.json_data = json.load(json_file)
            except FileNotFoundError:
                raise ValueError(f"JSON file '{datafile}' not found.")

            try:
                with open(metafile, 'r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    self.csv_fields = csv_reader.fieldnames
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