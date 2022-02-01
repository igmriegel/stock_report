from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, prod_list):
        first_report = super().generate(prod_list)
        companies = [item["nome_da_empresa"] for item in prod_list]
        companies_stock = super().get_largest_stock(companies)
        quantity_report = "Produtos estocados por empresa: \n"
        for company, stock in companies_stock.items():
            quantity_report += f"- {company}: {stock}\n"
        final_report = first_report + "\n" + quantity_report
        return final_report
