import scrapy
from . import custom_settings
class MovieSpider(scrapy.Spider):
  name='movie'

  custom_settings=custom_settings.douban_settings

  start_urls = [
    'https://movie.douban.com/subject/3878007/comments?status=P'
  ]

  def parse(self, response):
    result = response.css('div.comment-item')
    for r in result:
      yield {
        'author': r.css('a::text').extract()[3],
        'watched': r.css('span.comment-info span::text').extract_first(),
        'rating': r.css('span.comment-info span.rating::attr(title)').extract_first(),
        'commentTime': r.css('span.comment-time::text').extract_first().replace(' ', '').replace('\n',''),
        'comment': r.css('span.short::text').extract_first().replace('\n', '') 
      }

    for a in response.css('div#paginator a.next'):
      yield response.follow(a, callback=self.parse)
    
  
