import scrapy
import json
from . import custom_settings
from spiders.items import PicItem

class DoubanPicSpider(scrapy.Spider):
  name='douban_pics'

  custom_settings= {
    **custom_settings.douban_settings,
    **custom_settings.image_settings
   }

  start_index = 0

  # 王祖賢圖片
  base_url = 'https://www.douban.com/j/search_photo?q=%E7%8E%8B%E7%A5%96%E8%B3%A2&limit=20&start=' 


  start_urls = [
    base_url + str(start_index)
  ]

  def parse(self, response):
    j = json.loads(response.body_as_unicode())
    srcs = [image['src'] for image in j['images']]

    yield PicItem(image_urls=srcs)

    if j['more'] is not None: 
      self.start_index = self.start_index + 20
      next_url = self.base_url + str(self.start_index)
      yield scrapy.Request(next_url, callback=self.parse)
  