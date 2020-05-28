import requests
import random
from bs4 import BeautifulSoup
from UA import USER_AGENT_LIST

def get_page(url):
    # 随机选取一个user-agent
    USER_AGENT = random.choice(USER_AGENT_LIST)
    # 构造请求头
    headers = {'user-agent': USER_AGENT}
    # 返回网页
    return requests.get(url, headers=headers)

if __name__ == '__main__':
    for text_id in range(9190000, 9197224):
        for date in range(21, 29):
            # 构造URL
            url = 'http://www.chinanews.com/cj/2020/05-' + str(date) + '/' + str(text_id) + '.shtml'
            print(url)
            try:
                page = get_page(url)
                # 修改网页编码，防止乱码
                page.encoding = 'utf-8'
                # 有内容的话就解析
                if page.status_code != 404:
                    html = page.text
                    soup = BeautifulSoup(html, 'html.parser')
                    content = soup.find('div', attrs={'class':'content'}).find_all('p')
                    for i in range(len(content)):
                        content[i] = content[i].text
                    # 将爬取到的文本保存到本地
                    filename = 'data/' + str(text_id) +'.txt'
                    with open(filename, 'w') as f:
                        for i in content:
                            f.write(i)
                            f.write('\n')
                    print(text_id)
            except:
                pass