import xlrd

class read_data():
    def read_sheet(n):
        # 打开当前目录下文件
        print('主人，您要读取第', n,'行数据')
        workbook = xlrd.open_workbook('../testdata/testdata.xlsx')
        print('总表数=', workbook.nsheets)
        print('表名称=', workbook.sheet_names())
        table1 = workbook.sheet_by_name('Sheet1')
        print('数据类型为', table1.row(0))
        print('一共有:', len(table1.col_values(0)), '列')
        #判断传值如果正确，则进行打印，否则输出没有此行数据
        if n in range(0, len(table1.col_values(0))):
            row_list = table1.row_values(n)
            print('主人，你读取的数据为', row_list)
            return row_list
        else:
            print('没有此行数据,你是智障嘛')

if __name__ == '__main__':
    self = read_data().read_sheet(1)
    #self.read_sheet(2)