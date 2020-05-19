import scrapy
import scrapy_splash


class FacebookSpider(scrapy.Spider):
    name = 'facebook'
    facebook_base_url = 'https://ai.facebook.com'

    def start_requests(self):
        urls = [
            self.facebook_base_url + f'/results/?q&content_types[0]=publication&sort_by=relevance&view=list&page={i}'
            for i in range(1, 60)
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
            article_url = self.facebook_base_url + article.css('a._8xc5._8x97._8w61').xpath('@href').get()
            yield response.follow(article_url,
                                  callback=self.parse_article,
                                  cb_kwargs={'base_info': {
                                      'researchAreas': article.css('div._8x6u h4::text').getall(),
                                      'name': article.css('div._8wpz h4::text').get(),
                                      'authors': [name.strip() for name in authors],
                                      'articleUrl': article_url,
                                  }})

    def parse_article(self, response, *, base_info):
        return {**base_info,
                "description": response.css('p._8w6f._8w61._8w6h::text').get()}
