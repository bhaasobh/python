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
        res = dict()
        try:
            res = self.data_summary[item]
        except :
            raise IndexError("out of bounds index")

        return res

    __getitem__ = DataAccess