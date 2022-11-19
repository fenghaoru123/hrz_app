#coding=utf8
'''
该模块读取Excel文件中的内容
'''
from public.utils.ReadExcel import ReadExcel
excelname="product_data.xlsx"
# excelname="test_data.xlsx"

class Login_Date():
    @staticmethod
    def get_Url():
        #获取测试的URL地址
        url=ReadExcel(excelname,'Sheet1').read_excel(1,0)
        return url

    @staticmethod
    def get_Username():
        #获取用户名
        username=ReadExcel(excelname,'Sheet1').read_excel(1,1)
        return (username)

    @staticmethod
    def get_Pwd():
        #获取密码
        pwd=ReadExcel(excelname,'Sheet1').read_excel(1,2)
        return pwd

    @staticmethod
    def get_Code():
        # 获取验证码
        code = ReadExcel(excelname, 'Sheet1').read_excel(1, 3)
        return code

if __name__ == '__main__':
    print (Login_Date.get_Url())
    print (Login_Date.get_Username())
    print (Login_Date.get_Pwd())
    print (Login_Date.get_Code())

