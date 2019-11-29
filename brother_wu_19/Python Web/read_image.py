#coding=utf-8
import pytesseract #识别图片的包
from PIL import Image    #截取图的模块
from ShowapiRequest import ShowapiRequest   #通过介入其他公司的API来识别验证码

# image =Image.open("D:/chrom/b.png")
# text=pytesseract.image_to_string(image)#识别图片
# print(text)

#珍惜使用，收费！
# r = ShowapiRequest("http://route.showapi.com/1274-2","120758","442339340d024aa9bc80faf62b53629d" )
# #r.addBodyPara("imgUrl", "http://sitold.uhuasuan.com/securitycode")
# #r.addBodyPara("base64", "")
# r.addFilePara("imgFile", "D:/chrom/b.png")
# res = r.post()
# text=res.json()["showapi_res_body"]["texts"]
# print(res.text) # 返回信息
# print(text)




# r = ShowapiRequest("http://route.showapi.com/184-4","120758","442339340d024aa9bc80faf62b53629d" )
# r.addBodyPara("typeId", "34")
# r.addBodyPara("convert_to_jpg", "0")
# r.addFilePara("image",r"D:/chrom/b.png")#文件上传时设置
# res = r.post()
# print(res.text) # 返回信息
