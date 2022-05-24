import requests
import json
#code by 影子team 王宇晨
#查询的方式，修改此处即可改变获取信息的方法
titletype = "site"
main_data = "##"
zone_key_id = "##"

def post_request(data , titletype):
    burp0_url = "https://0.zone:443/api/data/"
    burp0_cookies = {"csrftoken": "3a7edM7p75eUjMDf7hYj9pmyFIsBjTeSTstZErZPEhMhATcyz8tki9K01f2GA03s", "sessionid": "z2f2o9p63wq6zu68op6ud5y3zcg7qr04"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Dnt": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Content-Type": "application/json", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}
    burp0_json={"page": data, "pagesize": 10, "title": main_data, "title_type": titletype, "zone_key_id": zone_key_id}
    response_data = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    result_data = response_data.text
    #转换成json格式
    json_result_data = json.loads(result_data)
    #获取数据
    data_json_result  = json_result_data['data']
    return data_json_result

if __name__ == "__main__":
    #设置初始data值
    data = 1
    while (1):
        data_json_result = post_request(data,titletype)
        data = data + 1
        for url in data_json_result:
            print(url['url'])
        if(data_json_result == []):
            break








