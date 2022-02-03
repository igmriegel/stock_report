from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer, data=[]):
        self.importer = importer
        self.data = data

    def import_data(self, path, type):
        imported_data = self.importer.import_data(path)
        self.data = [*self.data, *imported_data]

    def __iter__(self):
        return InventoryIterator(self.data)
