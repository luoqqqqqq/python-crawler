import scrapy
import json
from myspider.items import MyspiderItem

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    #allowed_domains = ['www.bilibili.com']
    #with open('/Users/jason/Desktop/luo/python-crawler/myspider/myspider/package_names.txt','r') as load_f:
           # for jsonstr in load_f.readlines():
              #  data=json.loads(jsonstr)
    datas=open('/Users/jason/Desktop/luo/python-crawler/myspider/myspider/package_names.txt','r').readlines()
    page=1
    w=0
    list1=[]
    print(datas)
    

    for da in datas:
        da=str(da).replace('\n','')
        
        list1.append(da)
    print(list1)
    start_urls = ['https://play.google.com/store/apps/details?id=com.android.chrome']
    def parse(self, response):
        # print('parse 开始:')
            item=MyspiderItem()
            item['title']=response.xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[1]/div/h1/span/text()').extract()
            
            item['iconurl']=response.xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[1]/img[1]/@src').extract()
            
        
            item['subtitle']=response.xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[1]/div/div/div[2]/div/span[1]/text()').extract()
                
                #print(subt)
            
            item['contentRatingTitle']=response.xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[2]/div/div/div[3]/div[2]/span/text()').extract()
            
            coni=[]
            for q in range(1,17):
                contentRatingIconUrl=response.xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[1]/div/div/div[1]/div[%s]/div/img/@src' %q).extract()
                if len(contentRatingIconUrl) > 0:
                    coni.append(contentRatingIconUrl[0])
                #print(contentRatingIconUrl)
            
            item['description']=response.xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[2]/div/section/div/div[1]/text()[1]').extract()
            
            item['averageUserRating']=response.xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[3]/section/div/div/div[1]/div/div/div[1]/div[1]/text()').extract()
           # a=['title','iconurl','subtitle','contentRatingTitle','description','averageUserRating']
            #b=[title,iconurl,subtitle,contentRatingTitle,description,averageUserRating]
           # q=zip(a,b)
           # d=dict(q)
            # con=[]
            # print(coni)
            item['images']=coni
            # for x in range(1,17):
                
                
            #     print("item['con%s']"%x   +'=%s'  %coni[x-1])
            yield item
            #dd=dict(zip(con,coni))
           # d.update(dd)
            
            
            
            #json1=json.dumps(d)
            #print('JSON content:', json1)
            #with open('/Users/jason/Desktop/luo/python-crawler/myspider/myspider/spiders/text.txt','w') as f:
                #json.dump(d,f)
            if self.page <4:  # 控制！否则无限递归了。。
                self.page += 1
                self.w  += 1
                print('爬第：%d 页' % self.page)
                new_url = 'https://play.google.com/store/apps/details?id=%s' %self.list1[self.w]
                # callback 回调函数，页面进行解析
                yield scrapy.Request(url=new_url, callback=self.parse)
        
      
#/html/body/c-wiz[4]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[1]/c-wiz/section/div/div[3]/div/div/div/div[1]
#//*[@id="yDmH0d"]/c-wiz[4]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[1]/c-wiz/section/div/div[3]/div/div    /div/div[1]/div[1]/div[1]/div/a/div[2]/div/div[1]/span
#//*[@id="yDmH0d"]/c-wiz[4]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[1]/c-wiz/section/div/div[3]/div/div    /div/div[1]/div[2]/div[1]/div/a/div[2]/div/div[1]/span
#//*[@id="yDmH0d"]/c-wiz[4]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[1]/c-wiz/section/div/div[3]/div/div    /div/div[1]/div[3]
#/html/body/c-wiz[4]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[1]/c-wiz/section/div/div[3]/div/div