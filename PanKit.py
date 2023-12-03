import requests
from typing import *
from colorama import Fore

base_url: Final[str] = 'https://pan.baidu.com/share/wxlist?channel=weixin&version=2.2.2&clienttype=25&web=1'
headers: Final[Dict[str, any]] = {'User-Agent': 'netdisk',
                                  'Cookie': 'BDUSS=U5kYzlubnc1cnRldjc3cU4xeDE5Slpjb25rSWFVZG9CYzd5dmFDOVUxZzI1VEJpRVFBQUFBJCQAAAAAAAAAAAEAAACDdi-fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADZYCWI2WAlid',
                                  'Referer': 'https://pan.baidu.com/disk/home'
                                  }

def to_surl(original_pan_url: str) -> str:
    """
    Return the file identifier of a shared link
    """
    sections = original_pan_url.split('/')
    for i in range(len(sections)):
        if sections[i] == 's':
            return sections[i + 1]

def get_list(shorten_url: str, password: str) -> Dict[str, str]:
    """
    Get file list from shared url
    return: {'filename': filename, 'md5', md5, 'size', size}
    """
    data = {'shorturl': shorten_url,
            'dir': '',
            'root': 1,
            'pwd': password,
            'page': 1,
            'num': 1000,
            'order': 'time'
            }
    while True:
        # The resposne should not exceed more than three seconds
        try:
            response = requests.post(base_url, headers=headers, data=data, timeout=3)
            break
        except:
            pass

    response_data = response.json()
    # Lots of information of shared file contained in the response
    # print(response_data)
    # There are more than just filename, md5, and size
    filename = response_data['data']['list'][0]['server_filename']
    md5 = response_data['data']['list'][0]['md5']
    size = response_data['data']['list'][0]['size']
    return {'filename': filename, 'md5': md5, 'size': size}

# The link below is only for demonstration purpose
pan_url = 'https://pan.baidu.com/s/1eSEf69c?_at_=1701623455129'
pwd = ''
print(get_list(shorten_url=to_surl(pan_url), password=pwd)['filename'])
print(get_list(shorten_url=to_surl(pan_url), password=pwd)['md5'])
print(get_list(shorten_url=to_surl(pan_url), password=pwd)['size'])
