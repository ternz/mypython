import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'authors'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_css_text(css):
            return response.css(css).extract_first().strip()
        
        yield {
            'author': extract_css_text('.author-title::text'),
            'borndate': extract_css_text('.author-born-date::text'),
            'bornlocation': extract_css_text('.author-born-location::text'),
            'description': extract_css_text('.author-description::text')
        }
		