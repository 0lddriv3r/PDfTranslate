import requests
# import re
from bs4 import BeautifulSoup


def translate(text, from_language='en', to_language='zh-CN'):
    base_url = "https://translate.google.cn/m?hl={}&sl={}&ie=UTF-8&q={}"
    url = base_url.format(to_language, from_language, text)
    # print('\n***********\n' + text + '\n***********\n')
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        html_text = response.text
        #.*? non-greedy or minimal fashion
        #(?<=...)Matches if the current position in the string is preceded
        # by a match for ... that ends at the current position
        # p = re.compile(r'(?<=TRANSLATED_TEXT=).*?;')
        # m = p.search(html_text)
        # response_text = m.group(0).strip(';')
        try:
            soup = BeautifulSoup(html_text, 'lxml')
            translate_text = soup.find('div', class_='t0').string
            print('Translate Successful!')
            return translate_text
        except Exception as dom_e:
            print('Exception:\n' + str(dom_e) + '\n')
            return 'Dom Tree Parse Failed!'
    except Exception as request_e:
        print('Exception:\n' + str(request_e) + '\n')
        return 'Get HTML Text Failed!'


if __name__ == '__main__':
    with open('libctdb.txt', 'r') as f:
        text = f.read()
        translate_text = translate(text, 'en', 'zh-CN')
        with open('translibctdb.txt', 'a') as f:
            f.write(translate_text)
