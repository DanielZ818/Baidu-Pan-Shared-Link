import PanKit as pan

# The link below is only for demonstration purpose
pan_url = 'https://pan.baidu.com/s/1eSEf69c?_at_=1701623455129'
pwd = ''

print(pan.get_list(shorten_url=pan.to_surl(pan_url), password=pwd)['filename'])
print(pan.get_list(shorten_url=pan.to_surl(pan_url), password=pwd)['md5'])
print(pan.get_list(shorten_url=pan.to_surl(pan_url), password=pwd)['size'])
