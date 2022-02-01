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
        stck = cls.get_largest_stock(companies)
        oldest = f"Data de fabricação mais antiga: {oldest_prod}\n"
        nearest = f"Data de validade mais próxima: {nearest_expired}\n"
        lrgst = f"Empresa com maior quantidade de produtos estocados: {stck}\n"
        report_string = oldest + nearest + lrgst

        return report_string

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

        return max(stock_counter)


# test_data = [
#     {
#         "id": 1,
#         "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2020-07-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#         "instrucoes_de_armazenamento": "in blandit ultrices enim",
#     },
#     {
#         "id": 2,
#         "nome_do_produto": "sodium ferric gluconate complex",
#         "nome_da_empresa": "sanofi-aventis U.S. LLC",
#         "data_de_fabricacao": "2020-05-31",
#         "data_de_validade": "2023-01-17",
#         "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
#         "instrucoes_de_armazenamento": "duis bibendum morbi",
#     },
#     {
#         "id": 3,
#         "nome_do_produto": "Dexamethasone Sodium Phosphate",
#         "nome_da_empresa": "sanofi-aventis U.S. LLC",
#         "data_de_fabricacao": "2019-09-13",
#         "data_de_validade": "2023-02-13",
#         "numero_de_serie": "BA52 2034 8595 7904 7131",
#         "instrucoes_de_armazenamento": "morbi quis tortor id",
#     },
#     {
#         "id": 4,
#         "nome_do_produto": "Uricum acidum, Benzoicum acidum",
#         "nome_da_empresa": "Newton Laboratories, Inc.",
#         "data_de_fabricacao": "2019-11-08",
#         "data_de_validade": "2019-11-25",
#         "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
#         "instrucoes_de_armazenamento": "velit eu est congue elementum",
#     },
# ]

# SimpleReport.generate(test_data)
