from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, prod_list):
        fab_dates = [
            cls.parse_date(item["data_de_fabricacao"]) for item in prod_list
        ]
        exp_dates = [
            cls.parse_date(item["data_de_validade"]) for item in prod_list
        ]
        companies = [item["nome_da_empresa"] for item in prod_list]
        oldest_prod = cls.get_oldest_date(fab_dates)
        nearest_expired = cls.get_nearest_expiration_date(exp_dates)
        stock = max(cls.get_largest_stock(companies))
        r_1 = f"Data de fabricação mais antiga: {oldest_prod}\n"
        r_2 = f"Data de validade mais próxima: {nearest_expired}\n"
        r_3 = f"Empresa com maior quantidade de produtos estocados: {stock}\n"
        report_all_rows = r_1 + r_2 + r_3

        return report_all_rows

    @classmethod
    def parse_date(cls, date_string):
        return date.fromisoformat(date_string)

    @classmethod
    def get_oldest_date(cls, date_list):
        oldest_date = date.today()
        for date_loop in date_list:
            if date_loop < oldest_date:
                oldest_date = date_loop
        return oldest_date

    @classmethod
    def get_nearest_expiration_date(cls, date_list):
        today = date.today()
        closest_exp_date = date(
            year=(today.year + 100), month=today.month, day=today.day
        )
        for date_loop in date_list:
            if date_loop > today and date_loop < closest_exp_date:
                closest_exp_date = date_loop

        return closest_exp_date

    @classmethod
    def get_largest_stock(cls, company_list):
        stock_counter = {}
        for company in company_list:
            try:
                stock_counter[str(company)] += 1
            except KeyError:
                stock_counter[str(company)] = 1

        return stock_counter
