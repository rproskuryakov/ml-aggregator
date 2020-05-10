import scrapy
import scrapy_splash


class FacebookSpider(scrapy.Spider):
    name = 'facebook'

    def start_requests(self):
        urls = [
            'https://ai.facebook.com/results/?q&content_types[0]=publication&sort_by=relevance&view=list&page=1',
        ]
        lua_script = """
        function main(splash, args)
            splash.private_mode_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(10.0))
            return {
                html = splash:html(),
                png = splash:png()
                    }
        end
        """
        for url in urls:
            yield scrapy_splash.SplashRequest(url=url,
                                              callback=self.parse,
                                              endpoint='execute',
                                              args={'lua_source': lua_script,
                                                    'html': 1,
                                                    'wait': 30})

    def parse(self, response):
        for article in response.xpath('//div[@id="fb_ai_results_grid"]/div'):
            authors = article.css('p._8w6f._8xm4._8w61._8w6h._8zob::text').get().split(',')
            yield {
                'researchArea': article.css('div._8x6u h4::text').get(),
                'name': article.css('div._8wpz h4::text').get(),
                'authors': [name.strip() for name in authors],
                'pre-text': article.css('div._8xkk p::text').get(),
            }
