# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    def __init__(self):
        print('pipeline init....')
        self.json_file=open('gg.json','wb+')
        self.json_file.write('\n'.encode('UTF-8'))
        
    def process_item(self, item, spider):
        print('pipeline process_item....')
        textgg=json.dumps(dict(item),ensure_ascii=False)+ '\n'
        print('pipeline process item:', textgg)
        self.json_file.write(textgg.encode('UTF-8'))
        #return item

    def close_spider(self,spider):
        print('-------关闭文件-------')
        # self.json_file.seek(-2,1)
        self.json_file.write('\n'.encode('UTF-8'))
        self.json_file.close()
