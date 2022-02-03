import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file_name):
        file_extension = file_name.split(".")[-1]
        if file_extension != "xml":
            raise ValueError("Arquivo inválido")

        with open(file_name, "rb") as report_file:
            d = xmltodict.parse(report_file, dict_constructor=dict)
            file_parsed_data = d["dataset"]["record"]
            return file_parsed_data
