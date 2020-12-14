import asyncio
import aiohttp
import json


async def request_data(url):
    # use aiohttp.request (as a context manager) to get data from url
    # then return data as str
    async with aiohttp.request('GET', url) as response:
        return await response.text()


async def get_reddit_top(subreddit):
    # use request_data coroutine to get reddit top
    # then unpack data to json:
    # %reddit_name%: {
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     },
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     }
    # }
    url_pattern = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'
    raw_data = await request_data(url_pattern)
    unpacked = json.loads(raw_data)
    children = [item['data'] for item in unpacked['data']['children']]
    return [subreddit, children]


async def main():
    # use asyncio.gather to get tops for reddits "python", "compsci", "microbork"
    # try to use *args instead of hardcoded function calls
    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    required_fields = {
        'score',
        'permalink'
    }
    res = await asyncio.gather(*(get_reddit_top(subreddit) for subreddit in reddits))
    resulting_dict = dict()
    for result in res:
        key = result[0]
        inner_dict = dict()
        inner_list = result[1]
        for item in inner_list:
            inner_key = item.get('title')
            inner_value = {k: v for k, v in item.items() if k in required_fields}
            inner_value["link"] = f"https://www.reddit.com/{inner_value.pop('permalink')}"
            inner_dict[inner_key] = inner_value
        resulting_dict[key] = inner_dict
    print(resulting_dict)

asyncio.run(main())
