#main.py
import requests
from lxml import html
import time
import random
cookie ="sb=axmCXVCo9FnGIwA0fdDuQIJ3; datr=axmCXcd3mCIy4PGEtfbcwePA; dpr=1.25; _fbp=fb.1.1595616984788.267001686; locale=vi_VN; _fbc=fb.1.1599501257695.IwAR1ZgZ6IwX7lZiH6iuZ35ihLatxDiDQcnc5STQvzxjvn_3p5H25E9ii_FiM; c_user=100010046823648; xs=41%3A_KLCaxwKMC950A%3A2%3A1599762950%3A3261%3A6319; fr=0vrRiuHxMhxl9hYlH.AWVnSuBKquqFIYS7ZG5k5Xv4weQ.BdgfJi.MQ.F9Y.0.0.BfWnIG.AWUrz6ql; spin=r.1002644134_b.trunk_t.1599762951_s.1_v.2_; presence=EDvF3EtimeF1599762954EuserFA21B10046823648A2EstateFDutF1599762954577CEchF_7bCC; wd=884x748"
def auto_like(link):
    try:
    	#headers để giả lập là người dùng
        headers = {
            'authority': 'mbasic.facebook.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookie
        }
        #truy cập đến newsfeed của bạn
        page = requests.get(
            'https://mbasic.facebook.com' + link,
            headers=headers
        )

        tree = html.fromstring(page.content)
        # lấy nút like ra
        like_posts = tree.xpath("//span[contains(@id,'like_')]/a[contains(@href,'a/like.php')]/@href")
        see_more = tree.xpath("//a[contains(@href,'stories.php?aftercursorr')]/@href")
        print(see_more[0])
        # Sau đó thực hiện bấm nút like
        for link in like_posts:
            res = requests.get('https://mbasic.facebook.com' + link, headers=headers)
            print('Đã like bài viêt')
            time.sleep(random.choice(range(15)))
        # Chuyển đến trang tiếp theo
        auto_like(see_more[0])

    except Exception:
        auto_like('/')
auto_like('/')
