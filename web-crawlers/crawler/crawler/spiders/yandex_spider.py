import scrapy
import scrapy_splash


class YandexSpider(scrapy.Spider):
    name = 'yandex'
    lua_script = """
    function main(splash)
        splash.private_mode_enabled = false
        splash:go(splash.args.url)
        assert(splash:wait(10))
        local click_button = splash:jsfunc([[
        function clickButton() {
            try {
    	        var button = document.getElementsByClassName('show-more')
    			            .item(0).getElementsByTagName('button').item(0);
                button.click();
                setTimeout(() => { clickButton(); }, 300);
            }
            catch (e) {
                if (e instanceof TypeError) {
                    console.log('TYPEERROR');
                    return;
                }
            }
        }
        ]])
        click_button()
        splash:wait(10)
        return splash:html()
    end
    """

    def start_requests(self):
        urls = [
            'https://research.yandex.com/publications'
        ]
        for url in urls:
            yield scrapy_splash.SplashRequest(url=url,
                                              callback=self.parse,
                                              endpoint='/execute',
                                              args={'html': 1,
                                                    'lua_source': self.lua_script,
                                                    'wait': 30,})

    def parse(self, response):
        for article in response.css('div.publication-item.publication-item_type_horizontal'):
            article_url = 'https://research.yandex.com' + article.css('a.publication-item__title').xpath('@href').get()
            yield response.follow(article_url,
                                  callback=self.parse_article,
                                  cb_kwargs=dict(
                                      base_info={
                                          'authors': article.css('a.publication-item__researcher::text').getall(),
                                          'name': article.css('a.publication-item__title::text').get(),
                                          'meta': article.css('div.publication-item__meta::text').get(),
                                          'imageUrl': article.css('img.publication-item__image').xpath('@src').get(),
                                          'articleUrl': article_url,
                                          'source': 'yandex',
                                          'date': None,
                                      }
                                  )
                                  )

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #    yield response.follow(next_page, self.parse)

    def parse_article(self, response, *, base_info):
        if base_info is None:
            base_info = {}
        return {
            **base_info,
            'description': response.css('div.publication-page__content::text').get(),
            # 'date': response.css('div.publication-page__param-list a::text').get(),
            # 'researchAreas': response.css('div.publication-page__param-list a::text').getall(),
            # 'publishedIn': response.css('div.publication-page__param-list a::text').getall(),
        }
