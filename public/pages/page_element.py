#coding=utf8

class Page_Elment:
    #登录模块
    userName=('xpath','//*[//*[@id="txtUserName"]]')    #用户名
    passWord=('xpath','//*[@id="txtPassword"]')    #密码
    loginBtn=('xpath','//*[@id="user-login"]')     #进入登录界面按钮
    comeBtn=('xpath','//*[@id="btnLogin"]')        #点击登录按钮
    home=('xpath','/html/body/div[1]/div/a/h1')          #返回首页
    loginOut=('xpath','/html/body/div[2]/div[2]/p[1]/span/a')

    #点击模块
    shumaguan=('xpath','/html/body/div[2]/div[2]/div/ul[1]/li[1]/a')
    shouji=('xpath','/html/body/div[3]/div/ul/li[1]/a')