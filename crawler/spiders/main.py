import scrapy
import re
from urllib.parse import urlparse
from urllib.parse import parse_qs
from crawler.items import CrawlerItem
import itertools

class MainSpider(scrapy.Spider):
    name = 'main'
    url = "https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"

    headers = {
        'scheme':' https',
        'accept':' */*',
        'accept-encoding':' gzip, deflate, br',
        'accept-language':' undefined',
        'content-type':' application/json',
        'cookie':' mangoShopCookie_Version=v4; BolsaCookie=01; ak_bmsc=E60C3FCDE5A08908711B1831EC84F270~000000000000000000000000000000~YAAQZS0UAhf34ciCAQAATOvSzhDxjPjt+rv2+cPC7wxYjLglMK//x3fg8cElNUSa9aPTC1s4VpIkBVEheV9EIHtiwC6d8r7BFwu4wXLeaoxFMYDY+svk0RNVFrJWlDxjFQLvpDUqmgyPelCSc8uhf/GiGxkalYWMow/KgcHZjUpzB+JID2eszgisHzMgtvlkmRLJztSYOPl/s/4Xs8YFSInAwEAy2KigjCA1hIZj1+6h46U65Jfy+VxW9MA1PHqTW5sU6ne8X3DrqjlQXjPzvp2vpsBOXGqqIhLnf4OEHYOm3PspLTVmzDn/JqPRIu20qtxTdTsr4Nso+REUdV/c4hsZm75PVuGIMZWein/Y1chHig8aliGazdrKfyEthCNhFHNVotqqknUDxA==; bm_sz=6985956318A8BFE0BD95996F3897CE17~YAAQZS0UAhn34ciCAQAATevSzhDPt7aam9IFSH4cYXsM71gUTwtCOLjpv+sciUoV/0nWdyL6EXaVoN/A2yynSV+txTsDSVAzjKPO3o6vE2xTalSwuz/HEbvTjqDmwfK+KGlvj1dx00fvv6UqUarsmI/ePwZknIi40bBArK+CLA+WXjgbcTr6VMsn7qXIoTZr5FjwNzmAoVt5hAU+uIoAvo0NzXhPN9NuNF7uAOoVtPa/F5zOq4BXcnO2eOWp2F+lE72j4wFY6f5VoC4wIN5TgRRBmaFtje9PRAZ/0ZWoLhLczw==~4605494~4536633; anonymousId=8ccd9744-5739-46bd-8eb6-f60a5ef66960; _abck=B0477F5062B126E02EB7CE43A73E3E20~0~YAAQZS0UAjP34ciCAQAAfvPSzgivPjgqEE+MMpMsa/P6RwyZBIAQGSRdeKoPrGDscO4Zozt9kbqj8OVRPlvFLZL8uGyKgMz74hHsGFQXVcvPa7wMe6EOTUXzfdZ4trYJkdTX3M3Iyo1TMjsNRdt28QGdeu+/rCt59dYDbrMNEmwpr/gmWQES+6vKP1O4UCtszIk5BCy6CXgPOUkvQbFiY5Qj+eHOH25pG4VtDGZ7JHUF4uns0JG2K7ocPH0cEWCzaVANHGDl9IybhwiRq0CHR5+oxNZrgpyo7DwkorvLwPk1aGfkpxbVCH9Qn/AfnyrT9+G22OgLnbfNjmTUK28txRJIr9XecsaF7S1f9gEGx97nNH+zGNSAu6oMOerevJ5NiP3ZL1WjWZHssJyGyL+Er3VcAIRsM/8=~-1~-1~-1; OptanonAlertBoxClosed=2022-08-24T07:48:37.272Z; _gaexp=GAX1.2.E8xcJvm1R3C3pboy70QlYQ.19299.1; _gcl_au=1.1.721005473.1661327317; googleexperiments=t8C28DR0Sb2tRepMbNXt4A:1,KgtNo3S3SWCTsPzuWFIT-Q:1,b7AXQ_k3OolrT4dy9Jo-mT:2,; AKA_A2=A; mangoShopCookie=IN_006____006_001_she___UY46T3MJ84X1POCL3ZNP1FY5; MNGSESSIONID=7B72224EC4391DA4898B5B5CAFDEA109; AWSELB=BFC5C7171EE3DEE8EF093B004B4B9C189E4132CE52F2F942ECF2CEA9CF986FE90AFC7D65D2A81D1120ACCD07E792A09A41B820B925DE5A9441478424AF0CFC20F248DD295D2509C84F0A6D697757898EF01CE61583; oam.Flash.RENDERMAP.TOKEN=1a1zlj3apm; bm_mi=ACB3B8668E939ACD1E16B8D03BA80F40~YAAQYy0UAu01FseCAQAAp8brzhBCiEQnjRYqTr/4OWearswIwnj6plKoisELrNS/yyLtzRw1BG8M+7LcK2gIP8sPHTze/k6tVH+pt6gLE7v4Ub+uN4ry2YrpoR3+mtqZyGFmXMvoNSxFwHpxUEjMghRIgFLJql3JckDU/7JJq7FgtVBrVNEKAPOymSksYqEodVFIAIAciV2ez8s/vymV0aWfaD07PaJMX+pIxsGpeGhwkV+5hBYo577WDjPh6FyVMLVmJc1LjN1kutY43LCAGPCkCJhYiA3W/r5tAEJtIkH7dFNEhPAJ2swnfTf9FmrDovGbNNjRFFF+zooQahWutqGi/GiFEY+2J/8uemOrlcQi/A6EZWs1euSOJzCv9VM+~1; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Aug+24+2022+11:15:35+GMT+0300+(Eastern+European+Summer+Time)&version=6.20.0&isIABGlobal=false&hosts=&consentId=f79c0f60-95df-45a8-a38c-19f117722b1e&interactionCount=1&landingPath=NotLandingPage&groups=C0001:1,C0003:1,C0002:1,C0004:1,C0005:1&geolocation=BG;22&AwaitingReconsent=false; bm_sv=33B89302035942A49C405EA4582062FC~YAAQYy0UAvU1FseCAQAAasnrzhAJvBCbxyRKE7M2jk/1LET+u4CjNbh4mOIeMtpFNgBxKO7XNB6l9mvWSx6r5LaKcb+F5oVEa3Q1fvC6dpbn66WXowxqQvUEDmifANE1s8p/64vg3n5AhatnBXz7QXhPqf5mORRdL49NRB9gqnwrPP1j5Csxwyu78P8ENU0+nOeE8Yf7Shm0wv7htcxhaeNtfXkxAdk6Rnx+MHhR2p2IhTBqhz7lebICt8DJkRYv~1',
        'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'stock-id':'006.IN.0.true.false.v1'
    }

    def start_requests(self):
        # generating the api url using parameters from our starting url and regex
        parsed_url = urlparse(self.url)
        stock_id = re.findall(r'\d+\b', parsed_url.path)[0]
        color_id = parse_qs(parsed_url.query)['c'][0]

        api_url = f'https://shop.mango.com/services/garments/{stock_id}{color_id}'
        yield scrapy.Request(api_url, headers=self.headers, cb_kwargs={'color_id':color_id})

    def parse(self, response, color_id):
        jsonresponse = response.json()
        item = CrawlerItem()
        item['price'] = jsonresponse['price']['price']

        # Matching the id of the color we need to extract the label
        item['color'] = [data['label'] for data in jsonresponse['colors']['colors'] if data['id'] == color_id][0]

        # Using itertools to flatten this double list into a single one and removing the first element
        # Then getting the label value from all the dicts in the list
        sizes_list = list(itertools.chain(*[data['sizes'] for data in jsonresponse['colors']['colors'] if data['id'] == color_id]))[1:]
        item['sizes'] = [size['label'] for size in sizes_list]

        item['name'] = jsonresponse['name']
        yield item