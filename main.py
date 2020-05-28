import requests
from bs4 import BeautifulSoup

def get_page(url):
    return requests.get(url)

if __name__ == '__main__':
    for text_id in range(5513135, 5515514):
        for date in range(20, 29):
            url = 'http://www.gov.cn/xinwen/2020-05/' + str(date) + '/content_' + str(text_id) + '.htm'
            print(url)
            try:
                page = get_page(url)
                if page.status_code == 404:
                    break
                html = page.content
                soup = BeautifulSoup(html, 'html.parser')
                content = soup.currentTag.text.split()
                if content[0] == '中国政府网':
                    break
                filename = 'data/' + str(text_id) +'.txt'
                with open(filename, 'w') as f:
                    for i in content:
                        f.write(i)
                        f.write('\n')
                print(content)
            except:
                pass