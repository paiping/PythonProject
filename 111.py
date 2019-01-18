#python图像对比
#人工智能  站在巨人的肩膀上
#json模块
#requests模块
#老师 空山`
import requests
#token值 为的是拼接接口
def get_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lVfov6E1oaWZR9f4qIhd9Hjy&client_secret=Gubrc6RnMTdA3Eb8WumHIGrz4vHgCTdy"
    content = requests.get(url).text
    print(content)
    print(eval(content[:-1]) ['access_token'])

#get_token()
#图片读出来 转换为bcscna64编码
def imadata(img1,img2):
    import base64
    with open(img1,"rb") as r:
       pic1=base64.b64encode(r.read())
        
    with open(img2,"rb") as r:
       pic2=base64.b64encode(r.read())

    
#进行对比获得结果


