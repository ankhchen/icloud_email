from selenium import webdriver
import time

# cookie
c = 'X_APPLE_WEB_KB-IPNFN3A66RFT6IBPUBL7LRVXPL0="v=1:t=IAAAAAAABLwIAAAAAF1BQ9oRDmdzLmljbG91ZC5hdXRovQCPrJ80TfnLHyHpxoWjjmKZ6GIrwA9yVErOwIy4Kc2XkNF78vDRdsOBI52ntUG6mV4xgc-l5USLKXthzOwo3X8_1z-U4KjAh9-IrgElvRAgEq-ZWF-QpiJRcXcVjlA6It3GzvCo5_0wKgC1q8ANm1tspWQgDg~~"; X-APPLE-WEBAUTH-HSA-TRUST=d6d4b4d71efaf7148cdd34f3669fe051fb9cc22d2c517f1ddef7d3b6e1a3a0dc_HSARMTKNSRVXWFlaeoGEDM0nb9CBQwGoIlY09kqugKCK9ZZwGwe9a80frz7R+dBiF3H5xqX5vc1yOmC2KBZpnTrWr7qxvYMmyBqQAup+EQGWfRkznEhAN7MOU8SAqKbHSa+Rj22KS2WrSRVX; wmsid=85; X-APPLE-WEBAUTH-PCS-Documents="TGlzdEFwcGw6MTpBcHBsOjE6AcpQzVgQfmOHhWEzepszIk0Ed/IldR/XzuyScjNthoOTXIp47krMaJ/CQaKzpnjnXn1CbIX3TYEtkuARoGsREGLdTd1T+0XEwKT/h85dKjoOhGypwgAQsuNYt3h7xvbQ/LSZAvV0cGOgE92x5tU4xAmoddrUW75dxST92AKxShGo7bXx05aheQ=="; X-APPLE-WEBAUTH-PCS-Photos="TGlzdEFwcGw6MTpBcHBsOjE6AUIBPxFda0ZHgc2cc4wrmALT8HhVtpGFdxoE6BuEqt6QjOBOxchj7la6Rzbv8X6V//Hyp8xLy6gYPQyJFaxlJLifOw+P8Ln2Zrw65xmXqioCNS1aNXwdYMpCAa7MrhUVXTgWu01Vu6/29R+j09YiRrA2kEwRhNiLe75wpQfPSl4w14o7+tJRmQ=="; X-APPLE-WEBAUTH-PCS-Cloudkit="TGlzdEFwcGw6MTpBcHBsOjE6AfKeaAKELvFXCzJq2rGJ51cnz8e3SM4IgVFvi5ZKDWeSV1RRNKanz1KmBR0I2SkEaKG3C3bjs8heoAbSbFON/UFeTKaG/hed3Cn6k7TM8AW4wgE3d9HC1xRlLLhPaZryDdBlF4GCqcmULPkYGiGkvwstmxpy1FX+JjnKDLDENHzHuF38sUzYdg=="; X-APPLE-WEBAUTH-PCS-Safari="TGlzdEFwcGw6MTpBcHBsOjE6AcgiRM67kZ7Zq7S047jtQCnfFCL+E4nX9bvx6cVHFK8FT+C3FsZeh9vNlkpX6YEBVp+FTqAFHo6/eoCU4ZWk50BRN/hOHcrQA4nRk+pvQ1B5KkXw+t3pDzX+xIwo2NV844BR9IJM/P+zUndyv7fAijXDmmVn1HR5yXlHOd6E1yeXlPq8NaPASg=="; X-APPLE-WEBAUTH-PCS-Mail="TGlzdEFwcGw6MTpBcHBsOjE6AVf76LMcqru5+9d9Q7fyWjCFyNGB88wO30+xaPHLrKV1pgA9BhijR9YzyZkyrJxLla5XIlQ2IIMruirXdMpGwBJ5Q0viI9u7byvU7jDLpozNmSUV787tkMnyhzH33I+GTkDmCV2BsI+WsrbzoSmcDhBEsxOtw2M8g3ESCAFPCxo5VUUbqah7vQ=="; X-APPLE-WEBAUTH-PCS-Notes="TGlzdEFwcGw6MTpBcHBsOjE6AdkpK/NapcGtP2vcSVWB6I5oZGUA+spdS37RkozWkdHmixbCDAlM3uaLf5ZyIh6pKLd8Kn8qPFK+kBmGwcKd18bfFzkvOMUKkXwHrUGaPCNk5UZmWrSl04oL/fotQx1VCey+/0jrRwEQVDOhZbcJnpeHkX844+zeWRU8SvZg64eXAjDaVn4VmA=="; X-APPLE-WEBAUTH-PCS-News="TGlzdEFwcGw6MTpBcHBsOjE6AR9mLP7hvMvXEXy8JSSRIfiqBTWuilBye4bdlaKo6hElzruAdLxX9zdL3ovv4X7Qc9FBzlvhrWz1OSQPqvI71MSnn2rzHA3QndNTa+hLCYtHBLIb7eCwaZS4vIEkTyqgcVDlNYegkeO6sg1USPhq+3H/bys8YsIaEsY5zrASz9Cqet6nbs6/tQ=="; X-APPLE-WEBAUTH-PCS-Sharing="TGlzdEFwcGw6MTpBcHBsOjE6AWn1nb6JgxKo5SDRHmyMJmrgm3jrYmGD50qI7Tk9ISnxSnIsBtlQ63MXB1QnVn01PUQGu6xO7k8rr97rru/0mL8+aHMjh0b48avl6/CmKn79Zb8DO5r19du0PbhLTzc/IjAplLfNe5Ke8vG0qufLj2G3aa8UL+x2RuFEy0HDbxraLFMeI5fWQg=="; X-APPLE-WEBAUTH-LOGIN="v=1:t=IAAAAAAABLwIAAAAAF1eT3ERDmdzLmljbG91ZC5hdXRovQBGMeTdlpY_ODL5C0QaVkDoBgiZo48iHFCCJxEeWbSsk9a4F7jkfwMKNfd_xeOLv4zbhlMsjFrXmXJ66RDAI5s1c5H1XBkV306OPK6QyeTzXM8SLjMagbIuI-maKXFHZ1L5HJA7SVlJDL5jC9qi5n5pkNCbZQ~~"; X-APPLE-WEBAUTH-VALIDATE="v=1:t=IAAAAAAABLwIAAAAAF1eT3ERDmdzLmljbG91ZC5hdXRovQBGMeTdlpY_ODL5C0QaVkDoBgiZo48iHFCCJxEeWbSsk9a4F7jkfwMKNfd_xeOLv4zbhlMsjFrXmXJ66RDAI5s1c5H1XBkV306OPK6QyeTzXIJutbpDUvvNILvUHFDQNenLjDYApRbRQ_9zXlvdc3REzz7AlQ~~"; X-APPLE-WEBAUTH-USER="v=1:s=0:d=16763304089"; X-Apple-GCBD-Cookie=1; X-APPLE-WEB-ID=F8D2B6E59738B4BD8560BC726695E7F1985407B1; X-APPLE-WEBAUTH-TOKEN="v=2:t=IAAAAAAABLwIAAAAAF1eT3URDmdzLmljbG91ZC5hdXRovQBAO16gYrOqKWswXEryE8T41zDhMlYuET9z7RJYb4BRMkJhgsLLAiiuOJFu0AaKpSfwLJBaGfip3njg-oNmFATXWRJkhmDSrc2uylNMpGCDZzQ7HHzaQvX-qVFgG3jY38bFrPhBGha9try_8o6DWw1JkhqL8Q~~"'

def upload():
    url = 'https://www.icloud.com/#mail'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.delete_all_cookies()
    for cookie in c.split('; '):
        key, value = cookie.split('=', 1)
        driver.add_cookie(dict(
            name=key,
            value=value.strip('"'),
            domain="icloud.com",
            expires="",
            path="/",
            httpOnly=False,
            HostOnly=False,
            Secure=False
        ))
    time.sleep(10)
    driver.get(url)
    print(driver.title)
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    time.sleep(10)
    driver.find_element_by_class_name('add-button').click()
    time.sleep(10)
    # 新建文件夹
    driver.find_element_by_id('toolbar-actions-menu').click()
    time.sleep(10)
    # driver.find_element_by_class_name('me-sourcelist-row-title').send_keys('重要的文件')
    # time.sleep(2)
    # driver.find_element_by_class_name('value ellipsis').click()
    # 设置规则
    driver.find_element_by_xpath('//*[@id="actions-rules"]').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@class="sc-button-label sc-regular-size"]').click()
    time.sleep(6)
    driver.find_element_by_class_name('dropdown atv4 sc-view sc-button-view criteria-button button sc-large-size').click()

    # driver.find_element_by_xpath('//*[@class="field"]').send_keys('742517254@qq.com')
    print('===')
    time.sleep(10)


if __name__ == '__main__':
    upload()

