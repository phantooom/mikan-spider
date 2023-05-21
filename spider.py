import requests
import xmltodict
import json
import argparse


base_url = 'https://mikanani.me/RSS/Bangumi?bangumiId='

def get_bangumi_rss(bangumi_id):
    url = base_url + str(bangumi_id)
    try:
        response = requests.get(url)
    except Exception as e:
        print("{} Error:{} ".format(bangumi_id, str(e)))
        return
    if response.status_code == 200:
        content = xmltodict.parse(response.text)
        if content['rss']['channel'].get('item'):
            with open("./mikan_data/" + str(bangumi_id) + ".json", 'w', encoding='utf-8') as f:
                f.write(json.dumps(content, ensure_ascii=False))
    else:
        print("{} Error:{} ".format(bangumi_id, str(response.text)))
    


def get_all_bangumi_rss(start,end):
    for i in range(start, end):
        print("get bangumi id:{}".format(i))
        get_bangumi_rss(i)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='spider for mikanani.me')
    parser.add_argument('--start', '-s', help='start',default=1)
    parser.add_argument('--end', '-e', help='end',default=4000)
    args = parser.parse_args()
    get_all_bangumi_rss(int(args.start),int(args.end))