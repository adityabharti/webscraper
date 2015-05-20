import scrapy

from job.items import StarbucksItem

class StarbucksSpider(scrapy.Spider):
    name = "starbucks"
    allowed_domains = ["starbucks.in"]
    start_urls = ["http://www.starbucks.in/coffeehouse/store-locations/"]

    def parse(self, response):
	for sel in response.xpath('//div[contains(@class, "region size2of3")]/*[self::strong]'):
		item = StarbucksItem()
    		item['title'] = " ".join(item.strip() for item in sel.xpath('following-sibling::div[position() < 4 and not(starts-with(., "Timings"))]/text()').extract())
		yield item
