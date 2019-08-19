from selenium import webdriver
import time

# cookie
c = 'X_APPLE_WEB_KB-IPNFN3A66RFT6IBPUBL7LRVXPL0="v=1:t=IAAAAAAABLwIAAAAAF1BQ9oRDmdzLmljbG91ZC5hdXRovQCPrJ80TfnLHyHpxoWjjmKZ6GIrwA9yVErOwIy4Kc2XkNF78vDRdsOBI52ntUG6mV4xgc-l5USLKXthzOwo3X8_1z-U4KjAh9-IrgElvRAgEq-ZWF-QpiJRcXcVjlA6It3GzvCo5_0wKgC1q8ANm1tspWQgDg~~"; X-APPLE-WEBAUTH-HSA-TRUST=d6d4b4d71efaf7148cdd34f3669fe051fb9cc22d2c517f1ddef7d3b6e1a3a0dc_HSARMTKNSRVXWFlaeoGEDM0nb9CBQwGoIlY09kqugKCK9ZZwGwe9a80frz7R+dBiF3H5xqX5vc1yOmC2KBZpnTrWr7qxvYMmyBqQAup+EQGWfRkznEhAN7MOU8SAqKbHSa+Rj22KS2WrSRVX; wmsid=85; X-APPLE-WEBAUTH-PCS-Documents="TGlzdEFwcGw6MTpBcHBsOjE6AX/yKqZ9xCAbMdAlunB8n/1+ziRJFi0UlxZXJQXAbi0DlhWkeTz3mgK6yAYDhHGjOYvTobEuv7wsegxyf/Jt2QUtRZdZDp8kTPwMi03L3hi8zIdkCI81WsZXo/IH2+5FY+W+RC+uUIOJpcBOncb3uxF8eGv6At13FvhPpaRMlZWd9ewIZQ8P9w=="; X-APPLE-WEBAUTH-PCS-Photos="TGlzdEFwcGw6MTpBcHBsOjE6ATNsGbcijJ+vRZkiZfX92VwInoug2RBf9oIQHmWQvqDBlChAg8dXNSdFeGxM1lw7CawHNwR0l64HQYnvUZtcbDzEGju33CXYuLQqkndIMKKt6olVVsCmW9swT4V0LZjns3W5NW/V3ZC1heAX1SqlFNsbiArch09JE/geIJi5XzVrQEbweW9log=="; X-APPLE-WEBAUTH-PCS-Cloudkit="TGlzdEFwcGw6MTpBcHBsOjE6AXMfolQXYYecaG2Dfcaf/+oOX2ydcFa0cbcL2xre6NcPsBC5bsXKP7PChYM5oNpUK7k+U7V4P1IgI61X/wgbsyww3xzsmmL9c3jzOAncr3QjkFA6tOp1YERKeFKR6wj0+XuwBnwrPjUZTIQHcdsGKuki3bSmDHGt3LtimJ4C8qa31YS0ZojQ2w=="; X-APPLE-WEBAUTH-PCS-Safari="TGlzdEFwcGw6MTpBcHBsOjE6AQRo82MMVG8/GS/UHbpUFuQvwrn9oZEevB1mzNXeDIpuKhTKbd8McMcWJzTH7lSbXMNRly+JM4ngJo4oySk10KAAal+icAd4Kwgd9spQXtab5o6nmA6RTSajsec8j2AZHdzgA5K5yw7HeieGEJOfF7OCVOTNOgRQ3IcIDMJLTPS9w5dK30vuRg=="; X-APPLE-WEBAUTH-PCS-Mail="TGlzdEFwcGw6MTpBcHBsOjE6AV6RYPQh46ZSRf8BV+Y1hJAb2wf7GXLtYLlLD35gg0T49YqzyrVeAenn5bhRfChfzcuiPt7ycvn0MZhPkywYlWDKpiXe580Az9i5UoKbhKLAueWzgqphR2qhQoLfwOy07+pVlf1uaWHEfalni0qtYofY21zHXg16qj8sqj7VcxBHlZ/o3+bzEw=="; X-APPLE-WEBAUTH-PCS-Notes="TGlzdEFwcGw6MTpBcHBsOjE6Aenb7AI3yQ8C8aYl/v4quKYU7Xt8QKdvspoMNUObMdT2SkczDRBaN41vqN9oxj9/4UJKHhUMXcx2vBDiqosevsjtt8kbtpM2e5S6vGIOTwaYwWiDxSVg6rtKe04RQf7Exe5Jxcfm5EkBaXymp/kwD9vaGavbKd4zC+aETn0kdlwwQSNMR7RAjQ=="; X-APPLE-WEBAUTH-PCS-News="TGlzdEFwcGw6MTpBcHBsOjE6AcfEtIwjUDoI9LLUpWBBN32oiEo/O1jsPDS6DKwAt4TMrrreF7EzMiV7jQ3zFaZxmzNOF2Z8iuywe14KSTFzH3xXdOxrZlvr8RcVPQf0MhwVv3bqA/IPvrjDPL2jLAkeyiE5VgxXofr4pwhzT+OWQaAlCq96Llbw3eC+g987xoTZHr2gXypbNQ=="; X-APPLE-WEBAUTH-PCS-Sharing="TGlzdEFwcGw6MTpBcHBsOjE6AUzC3zL4ZLHPa9vCWn86TcENjKm0AKvivKcc0L2yV3oF75lLRrE0wo7p96Elw+VmEHpo9De0lMBIZiVcbovk/nGqW8iJyDSIcnEXVsUQt5EMzWVUbX5oOKj/+V8mrDBhtKZbxXYN1qYLeiWq7EGOr0iNKgFBPQUJx8Sjz3TD3RL5rtOKRCsmQg=="; X-APPLE-WEBAUTH-LOGIN="v=1:t=IAAAAAAABLwIAAAAAF1WTmMRDmdzLmljbG91ZC5hdXRovQDP8leI2Y9wqqLp2H588qHcYugxfXHwOtyIhVTA8PmepxPUocLbmakuCti9KXKjc--IfgFZmCxK-_Z6rFtcaDCz7N1PM6IpuWgkIgTQvCgtwnLGPdXK1dpRu71w2LCEfzyrHcqOrpFDR5aqoJHRXf_a8lKelA~~"; X-APPLE-WEBAUTH-USER="v=1:s=0:d=16763304089"; X-Apple-GCBD-Cookie=1; X-APPLE-WEB-ID=F8D2B6E59738B4BD8560BC726695E7F1985407B1; X-APPLE-WEBAUTH-VALIDATE="v=1:t=IAAAAAAABLwIAAAAAF1WX8QRDmdzLmljbG91ZC5hdXRovQBo-qoVXcq-uUou4H6pOW4YDSAgZ0F5FxWpfqK6-duBcDWKspyPXpMkqus1Iad6PyshlLcAvBd8qo5sEXjsa3Fgt94wEvcVMZ7BbYcxkXKfcBfEF91SG3XPyEIAY0CWPPT8DacnZAtWVJFRcEKvI9Co7Rqt-A~~"; X-APPLE-WEBAUTH-TOKEN="v=2:t=IAAAAAAABLwIAAAAAF1WX8gRDmdzLmljbG91ZC5hdXRovQAB-PQdaceEpo7oL9TvBSTHAupUshppDaces7dM6VDEDZHMftroRtAYPEZe_06VjrTLnnco2X1trlVe8tIMz-wVuFgbGRz7_oUrX_EmdRWbXGReEN8LqdGbWPdZUX5iP4JSCbWQ_PuBT2ce-JaDCoedIH6mHA~~"'


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
    time.sleep(6)
    driver.get(url)
    print(driver.title)
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    time.sleep(4)
    driver.find_element_by_class_name('add-button').click()
    time.sleep(5)
    driver.find_element_by_id('toolbar-actions-menu').click()
    time.sleep(2)
    # driver.find_element_by_class_name('value ellipsis').click()
    driver.find_element_by_link_text('规则')
    print('===')
    time.sleep(10)


if __name__ == '__main__':
    upload()
