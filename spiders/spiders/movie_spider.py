import scrapy
class MovieSpider(scrapy.Spider):
  name='movie'

  custom_settings = {
    'DEFAULT_REQUEST_HEADERS': {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
  }

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
    
  
