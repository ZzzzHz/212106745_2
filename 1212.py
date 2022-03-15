import json
from time import strftime, sleep

import requests
def one():
    url='https://j1.pupuapi.com/client/product/storeproduct/detail/4dcdeca2-f5a3-4be8-9e2f-e099889a23a0/ccac09fa-5171-4f1e-9263-e731be3400d7'
    head={
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    req=requests.get(url,headers=head)
    str1=json.loads(req.text)
    # 解析
    print('------------------商品：'+str1['data']['name']+'------------------')
    print('规格：' +str1['data']['spec'])
    print('价格：' +str(str1['data']['price']/100))
    print('原价/折扣价：'+str(str1['data']['market_price'])+'/'+str(str1['data']['price']))
    print('详情内容：'+str(str1['data']['sub_title']))
    print('-------------------"'+str1['data']['name']+'"的价格波动------------------')
    # 实时监控商品价格
    while (True):
        # 自定义时间格式
        nowTimeAndPrint = strftime('%Y'+'-'+'%m'+'-'+'%d'+' '+'%H:%M')
        print(nowTimeAndPrint+",价格为:"+str(str1['data']['price']/100))
        sleep(3)
if __name__ == '__main__':
    one()