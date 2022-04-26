def scrape():
    from bs4 import BeautifulSoup
    from bs4.dammit import EncodingDetector
    import requests

    parser = "html.parser"  # or 'lxml' (preferred) or 'html5lib', if installed
    url = 'https://www.clpdomeo.com/en/shopping/product-categories?c_eco_points=10-1500&product_list_limit=96'
    resp = requests.get(url)
    http_encoding = (
        resp.encoding if "charset" in resp.headers.get("content-type", "").lower() else None
    )
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, parser, from_encoding=encoding)

    print(soup)
    # for link in soup.find_all('product-item-link'):
    #     print(link)

    # print(data)

    # dates = soup.find_all('td', class_='list-txt-date')  # iterable
    # for date in dates:
    #     results = soup.find_all('td', class_='list-headline')   # iterable
    #     date1 = date.text.strip()
    # for result in results:  #make results into object 'result'
    #     rowdata = [date1, result.text.replace('\n',''), result.find('a')['href']]
    #     # rowdata = [date1, result.text.replace('\n', ''), result.find('a')['href'].replace('\n', '')]
    #     # links_writer.writerow(rowdata)
    #     print(rowdata)

if __name__ == "__main__":
    scrape()

