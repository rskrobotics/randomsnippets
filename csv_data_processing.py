import csv
from datetime import datetime
from matplotlib import pyplot as plt


class GrainError(Exception):
    pass


class GrainEntry:
    def __init__(self, index, grain, year, month, price):
        self.grain = grain
        self.price = round(float(price), 5)
        self.date = datetime.strptime((year + " " + month), "%Y %b")
        self.index = index


class GrainLedger:
    def __init__(self):
        self.grain_type = {}

    def add(self, grain_entry):
        if grain_entry.grain not in self.grain_type.keys():
            self.grain_type[grain_entry.grain] = []
        self.grain_type[grain_entry.grain].append(grain_entry)

    def sort_by_date(self):
        for key in self.grain_type:
            self.grain_type[key].sort(key=lambda x: x.date)


def show_plot(graintype):
    if graintype in grain_ledger.grain_type.keys():
        plt.plot([i.date for i in grain_ledger.grain_type[graintype]],
                 [i.price for i in grain_ledger.grain_type[graintype]])
        plt.xlabel('Date')
        plt.ylabel('Price in dollars *10^3/bushel')
        plt.grid()
        plt.title(graintype)
        plt.show()
    else:
        raise GrainError("No data for such grain!")


if __name__ == '__main__':
    grain_ledger = GrainLedger()
    with open('FeedGrains/FeedGrains.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for inx, row in enumerate(csv_reader):
            if row[0] != "1":
                continue
            if inx > 1 and row[-4] == "Monthly" \
                    and row[12] == "Dollars per bushel" \
                    and row[6] == "United States" \
                    and row[3] == row[8]:
                grain_ledger.add(
                    GrainEntry(inx, row[3], row[13], row[-2], row[-1]))
    try:
        grain_ledger.sort_by_date()
        show_plot("Oats")
    except GrainError as grn:
        print(grn)


