from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer, data=[]):
        self.importer = importer
        self.data = data

    def import_data(self, path, type):
        imported_data = self.importer.import_data(path)
        self.data = [*self.data, *imported_data]
        if type == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
