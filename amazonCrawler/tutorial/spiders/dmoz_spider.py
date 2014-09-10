from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import DmozItem

class DmozSpider(CrawlSpider):
	name = "dmoz"
	#allowed_domains = ["dmoz.org"]
	start_urls = [

"http://www.amazon.com/Kodak-C1530-Digital-Camera-White/product-reviews/B004MB8302/ref=cm_cr_pr_top_link_2?ie=UTF8&filterBy=addFourStar&pageNumber=1&showViewpoints=0&sortBy=bySubmissionDateDescending", 
"http://www.amazon.com/Kodak-C1530-Digital-Camera-White/product-reviews/B004MB8302/ref=cm_cr_pr_top_link_2?ie=UTF8&filterBy=addFourStar&pageNumber=2&showViewpoints=0&sortBy=bySubmissionDateDescending", 
"http://www.amazon.com/Kodak-C1530-Digital-Camera-White/product-reviews/B004MB8302/ref=cm_cr_pr_top_link_2?ie=UTF8&filterBy=addFourStar&pageNumber=3&showViewpoints=0&sortBy=bySubmissionDateDescending", 
"http://www.amazon.com/Kodak-C1530-Digital-Camera-White/product-reviews/B004MB8302/ref=cm_cr_pr_top_link_2?ie=UTF8&filterBy=addFourStar&pageNumber=4&showViewpoints=0&sortBy=bySubmissionDateDescending", 
"http://www.amazon.com/Kodak-C1530-Digital-Camera-White/product-reviews/B004MB8302/ref=cm_cr_pr_top_link_2?ie=UTF8&filterBy=addFourStar&pageNumber=5&showViewpoints=0&sortBy=bySubmissionDateDescending", 
"http://www.amazon.com/Kodak-C1530-Digital-Camera-White/product-reviews/B004MB8302/ref=cm_cr_pr_top_link_2?ie=UTF8&filterBy=addFourStar&pageNumber=6&showViewpoints=0&sortBy=bySubmissionDateDescending", 
"http://www.amazon.com/Kodak-C1530-Digital-Camera-White/product-reviews/B004MB8302/ref=cm_cr_pr_top_link_2?ie=UTF8&filterBy=addFourStar&pageNumber=7&showViewpoints=0&sortBy=bySubmissionDateDescending", 
"http://www.amazon.com/Kodak-C1530-Digital-Camera-White/product-reviews/B004MB8302/ref=cm_cr_pr_top_link_2?ie=UTF8&filterBy=addFourStar&pageNumber=8&showViewpoints=0&sortBy=bySubmissionDateDescending", 

	]
	

	rules = [Rule(SgmlLinkExtractor(allow=["http://www.amazon.com/Canon-PowerShot-A2500-Stabilized-2-7-Inch/product-reviews/B00B5HE2UG/ref=cm_cr_pr_top_link_3?ie=UTF8&filterBy=addFiveStar&pageNumber=\d+&showViewpoints=0&sortBy=bySubmissionDateDescending"]), callback="parse_item")]

	

	def parse(self, response):
		self.log("Hi, this is an item page! %s" % response.url)
		sel = HtmlXPathSelector(response)
		sites = sel.select('//div[@class="reviewText"]')
		items = []
		
		for site in sites:
			item = DmozItem()
			item['productid'] = "13"
			item['star'] = "4"
			item['bodytext'] = site.select('text()').extract()
			
			text=""
			for elem in item['bodytext']:
				text += elem.rstrip()
				
			item['bodytext'] = text
			
			items.append(item)
		return items