import os
from urllib import request

bianhao = input("请输入书编号(https://book.pep.com.cn/**编号**/mobile/index.html):")
yema = input("请输入页数:")
targetdir = "D:/人教版课本电子书自动获取/"
for i in range(1,int(yema),1):
    print("正在下载-第" + str(i) + "页……")
    url = "https://book.pep.com.cn/" + bianhao + "/files/mobile/"+  str(i) + ".jpg"
    name = "课本" + str(i) + ".jpg"
    request.urlretrieve(url, name)
print("下载成功！请在“C:\users\用户名\”查看（服了我）！")
print("(附：可以使用“分组依据”将图片分开再进行“剪切”命令！)")
os.system("pause")