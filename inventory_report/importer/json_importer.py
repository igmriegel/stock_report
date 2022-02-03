import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(file_name):
        file_extension = file_name.split(".")[-1]
        if file_extension != "json":
            raise ValueError("Arquivo inválido")

        with open(file_name) as report_file:
            file_parsed_data = json.load(report_file)
            return file_parsed_data
