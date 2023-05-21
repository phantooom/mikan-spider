import os
import argparse
import json

def walk_dir(dir,topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            yield os.path.join(root, name)
        for name in dirs:
            yield os.path.join(root, name)
# {
#     "guid": {
#         "@isPermaLink": "false",
#         "#text": "【豌豆字幕组&风之圣殿字幕组】★10月新番[偶像活动/Aikatsu!][101][繁体][720P][MP4](内详)"
#     },
#     "link": "https://mikanani.me/Home/Episode/3004740dc496f17b5269196e7eb133bd7d1b0afc",
#     "title": "【豌豆字幕组&风之圣殿字幕组】★10月新番[偶像活动/Aikatsu!][101][繁体][720P][MP4](内详)",
#     "description": "【豌豆字幕组&风之圣殿字幕组】★10月新番[偶像活动/Aikatsu!][101][繁体][720P][MP4](内详)[218.5MB]",
#     "torrent": {
#         "@xmlns": "https://mikanani.me/0.1/",
#         "link": "https://mikanani.me/Home/Episode/3004740dc496f17b5269196e7eb133bd7d1b0afc",
#         "contentLength": "229113856",
#         "pubDate": "2014-09-28T17:39:00"
#     },
#     "enclosure": {
#         "@type": "application/x-bittorrent",
#         "@length": "229113856",
#         "@url": "https://mikanani.me/Download/20140928/3004740dc496f17b5269196e7eb133bd7d1b0afc.torrent"
#     }
# }



def pase_json(json_file):
    titles = []
    with open(json_file, 'r', encoding='utf-8') as f:
        content = f.read()
        json_content = json.loads(content)
        items = json_content['rss']['channel']['item']
        # movie
        if isinstance(items, dict):
            titles.append(items['title'])
        else:
            for item in items:
                titles.append(item['title'])
    return titles
def pase_all_json(dir):
    all_titles = []
    for file in walk_dir(dir):
        if file.endswith('.json'):
            titles = pase_json(file)
            all_titles.extend(titles)
    with open('all_titles.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_titles))
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parser for mikanani.me rss json')
    parser.add_argument('--dir', '-d', help='dir',default='./mikan_data')
    args = parser.parse_args()
    pase_all_json(args.dir)