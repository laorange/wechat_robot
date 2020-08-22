import pandas as pd


def csv_to_xlsx_pd(csv_path: str = '../base_on_PyWeChatSpy/data/private_space/user_list.csv',
                   excel_path: str = '../base_on_PyWeChatSpy/data/private_space/user_list.xlsx',
                   encoding: str = 'utf-8'):
    csv = pd.read_csv(csv_path, encoding=encoding)
    csv.to_excel(excel_path, sheet_name='data')


if __name__ == '__main__':
    csv_to_xlsx_pd()
