from aip import AipOcr
import requests


#百度OCR配置
APP_ID = '15540586'
API_KEY = '61sMWh3Pd3FUOZaxvWpkwYdf'
SECRET_KEY = 'r0F9jvP1pet8rbuyxMDhIRGs8f8rwv4j'
client = AipOcr(APP_ID,API_KEY,SECRET_KEY)



# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()  #文件读取的内容


def get_content():
    # 测试文件也可以写路径
    image = get_file_content(r'C:\Users\Administrator\Pictures\Pictures.jpg')

    #  调用通用文字识别, 图片参数为本地图片
    result = client.basicGeneral(image)


    # 定义参数变量
    options = {
             # 识别语言类型，默认为'CHN_ENG'中英文混合
            'language_type' : 'CHN_ENG',
    }

    # 调用通用文字识别接口
    result = client.basicAccurate(image);

    words_result = result['words_result']

    #运用正则对返回结果进行提取
    text = ""

    for i in range(len(words_result)):
        text += (words_result[i]['words'] + "\n")

    return text




