import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(file_name):
        file_extension = file_name.split(".")[-1]
        if file_extension != "csv":
            raise ValueError("Arquivo inválido")

        with open(file_name) as report_file:
            file_parsed_data = [*csv.DictReader(report_file)]
            return file_parsed_data


# print(CsvImporter.import_data("inventory_report/data/inventory.csv"))
