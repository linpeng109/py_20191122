import openpyxl


def parser(filename, sheetname):
    workbook = openpyxl.load_workbook(filename=filename)

    worksheet = workbook[sheetname]
    for row in worksheet.rows:
        for cell in row:
            print(cell.value, "\t", end="")


if __name__ == '__main__':
    parser('AFS-8510.xlsx', '断续流动程序')
