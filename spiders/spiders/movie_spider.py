import scrapy
class MovieSpider(scrapy.Spider):
  name='movie'

  header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
  }

  def start_requests(self):
    url = 'https://movie.douban.com/subject/3878007/comments?status=P'
    yield scrapy.Request(url=url, callback=self.parse, headers=self.header)

  def parse(self, response):
    result = response.css('div.comment-item')
    for r in result:
      yield {
        'author': r.css('a::text').extract()[3],
        'watched': r.css('span.comment-info span::text').extract()[0],
        'rating': r.css('span.comment-info span:nth-child(3)::attr(title)').extract()[0],
        'commentTime': r.css('span.comment-time::text').extract()[0].replace(' ', '').replace('\n',''),
        'comment': r.css('span.short::text').extract()[0].replace('\n', '') 
      }

    for a in response.css('div#paginator a.next'):
      yield response.follow(a, callback=self.parse, headers=self.header)
    
  
