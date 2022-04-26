def scrape():
    import requests
    import csv
    from bs4 import BeautifulSoup

    with open('media_file.csv', 'w', encoding='utf-8', newline='') as media_file:
        for i in range(1, 16, 15):
            links_writer = csv.writer(media_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            URL = 'https://www.omitted.com/?start='+str(i)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            dates = soup.find_all('td', class_='list-txt-date')  # iterable
            for date in dates:
                results = soup.find_all('td', class_='list-headline')   # iterable
                date1 = date.text.strip()
            for result in results:  #make results into object 'result'
                rowdata = [date1, result.text.replace('\n',''), result.find('a')['href']]
                # rowdata = [date1, result.text.replace('\n', ''), result.find('a')['href'].replace('\n', '')]
                # links_writer.writerow(rowdata)
                print(rowdata)

if __name__ == '__main__':
    scrape()