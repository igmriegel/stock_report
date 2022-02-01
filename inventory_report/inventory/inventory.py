import csv
import json
import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        file_extension = path.split(".")[-1]
        file_parsed_data = []
        if file_extension == "csv":
            with open(path) as report_file:
                file_parsed_data = [*csv.DictReader(report_file)]
        elif file_extension == "json":
            with open(path) as report_file:
                file_parsed_data = json.load(report_file)
        else:
            with open(path, "rb") as report_file:
                d = xmltodict.parse(report_file, dict_constructor=dict)
                file_parsed_data = d["dataset"]["record"]

        if type == "simples":
            return SimpleReport.generate(file_parsed_data)
        else:
            return CompleteReport.generate(file_parsed_data)
