import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    file_path = sys.argv[1]
    type_of_report = sys.argv[2]
    file_extension = file_path.split(".")[-1]

    if file_extension == "csv":
        report_writer = InventoryRefactor(CsvImporter)
        print(report_writer.import_data(file_path, type_of_report), end="")
    elif file_extension == "json":
        report_writer = InventoryRefactor(JsonImporter)
        print(report_writer.import_data(file_path, type_of_report), end="")

    else:
        report_writer = InventoryRefactor(XmlImporter)
        print(report_writer.import_data(file_path, type_of_report), end="")


if __name__ == "__main__":
    main()
