import os
import json

TunnelPort=4040

def get_ngrok_url(startswith: str = 'https://') -> str:
    ngrok_tunnels = 'http://localhost:{}/api/tunnels'.format(TunnelPort)
    r = os.system(f'curl {ngrok_tunnels} > tunnels.json 2> /dev/null')

    if r != 0:
        os.system('rm -f tunnels.json')
        raise OSError('Either ngrok is not running or curl is not installed.')

    with open('tunnels.json', 'r') as f:
        tunnels = json.loads(f.read())
        os.system('rm -f tunnels.json')

        for tunnel in tunnels['tunnels']:
            if tunnel['public_url'].startswith(startswith):
                return tunnel['public_url']

if __name__ == "__main__":
    url = get_ngrok_url()

import chardet

# 檢測文件編碼
with open('index.html', 'rb') as file:
    result = chardet.detect(file.read())

# 使用檢測到的編碼打開文件
with open('index.html', 'r', encoding=result['encoding']) as file:
    html_content = file.read()

# 將HTML内容拆分成行
lines = html_content.split('\n')

# 要替换的新文本
new_text = '<meta http-equiv="refresh" content="1;url={}">'.format(url)

# 替换第六行
lines[5] = new_text 

# 重建HTML内容
html_content = '\n'.join(lines)

with open('index.html', 'w',encoding=result['encoding']) as file:
    file.write(html_content)
