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
    for text_id in range(9183059, 9197224):
        for date in range(13, 29):
            url = 'http://www.chinanews.com/gn/2020/05-' + str(date) + '/' + str(text_id) + '.shtml'
            print(url)
            try:
                page = get_page(url)
                page.encoding = 'utf-8'
                if page.status_code != 404:
                    html = page.text
                    soup = BeautifulSoup(html, 'html.parser')
                    content = soup.find('div', attrs={'class':'content'}).find_all('p')
                    for i in range(len(content)):
                        content[i] = content[i].text
                    filename = 'data/' + str(text_id) +'.txt'
                    with open(filename, 'w') as f:
                        for i in content:
                            f.write(i)
                            f.write('\n')
                    print(text_id)
            except:
                pass