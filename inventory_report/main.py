import sys
from inventory.inventory_refactor import InventoryRefactor
from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter
from importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    file_path = sys.argv[1]
    type_of_report = sys.argv[2]
    file_extension = file_path.split(".")[-1]

    if file_extension == "csv":
        InventoryRefactor(CsvImporter)
    elif file_extension == "json":
        InventoryRefactor(JsonImporter)
    else:
        InventoryRefactor(XmlImporter)

    print(file_path, type_of_report)


if __name__ == "__main__":
    main()
