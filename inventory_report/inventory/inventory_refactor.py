from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer

    def import_data(self, path, type):
        print(type)
        self.importer.import_data(path)

    def __iter__(self):
        return InventoryIterator(self.import_data)
