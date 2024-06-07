import fastapi
import httpx
from scrapy.selector import Selector
import time
import os

api = fastapi.FastAPI()

@api.get('/api/weather/{city}')
async def weather(city: str):
    url = f'https://pogoda.mail.ru/prognoz/{city}/'

    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=None)
        response.raise_for_status()

    selector = Selector(text=response.text)
    t = selector.xpath('//div[@class="information__content__temperature"]/text()').getall()[1].strip()

    print("FASTAPI PID: ", os.getpid())
    time.sleep(6)

    return {'city':city, 'temperature':t, 'source':'pogoda.mail.ru'}
