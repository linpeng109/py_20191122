import openpyxl


def main(filename):
    workbook = openpyxl.load_workbook(filename=filename)

    worksheet = workbook["断续流动程序"]
    for row in worksheet.rows:
        for cell in row:
            print(cell.value, "\t", end="")
