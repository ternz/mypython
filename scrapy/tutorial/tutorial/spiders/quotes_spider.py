import scrapy


class QuotesSipder(scrapy.Spider):
	name = 'quotes' 

	def start_requests(self):
		urls = [
			'http://quotes.toscrape.com'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
	
	def parse(self, response):
		for quote in response.css('div.quote'):
			text = quote.css('span.text::text').extract_first()
			author = quote.css('small.author::text').extract_first()
			tags = quote.css('div.tags a.tag::text').extract()
			yield {'text':text, 'author':author, 'tags':tags}

		next_page = response.css('li.next a::attr(href)').extract_first() 
		if next_page is not None:
			yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

