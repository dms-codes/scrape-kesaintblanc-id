import requests as r
from bs4 import BeautifulSoup as bs
import csv

def get_status_stock(status_stock):
    status_stock = status_stock.lstrip('\n')
    status_stock = status_stock.rstrip('\n')
    #print(status_stock)
    #print(status_stock.split('\n'))
    status = status_stock.split('\n')[1].replace('\t','')
    stock = int(status_stock.split('\n')[3].replace('\t',''))
    return status,stock

if __name__ == '__main__':
    with open('data.csv','a+',encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        col_names = ['Product Name',
                    'Product URL',
                    'Price',
                    'Product Img URL',
                    'Status',
                    'Stock',
                    'Img URL 1',
                    'Img URL 2',
                    'Img URL 3',]
        writer.writerow(col_names)
        url_base = 'https://kesaintblanc.id/?halaman='
        page_list = list(range(1,31))
        for page in page_list:
            urlpage = url_base+str(page)
            print(page, urlpage)
            html = r.get(urlpage).content
            soup = bs(html,'html.parser')
            products = soup.find_all('div', class_ = 'product product-single')
            for product in products:
                product_url = 'https://kesaintblanc.id/'+product.find('a')['href']
                print('\t'+product_url)
                price = product.find('strike').text
                product_name = product.find('h2').text
                product_img_url = 'https://kesaintblanc.id/'+product.find('img')['src']
                #print(product_name,product_url,price,product_img_url)
                
                product_html = r.get(product_url).content
                product_soup = bs(product_html,'html.parser')
                product_soup.find('div', class_='tab-content')
                description = product_soup.find_all('p')[5].text
                status_stock = product_soup.find_all('p')[3].text
                status,stock = get_status_stock(status_stock)
                img_track = product_soup.find('div', class_='col-md-6')
                #print(img_track)
                #input()
                slick_track = img_track.find_all('img')
                img_list = []
                for slide in slick_track:
                    if 'gambar/produk/' in slide['src']:
                        url = 'https://kesaintblanc.id/'+slide['src']
                        if url not in img_list:
                            img_list.append(url)
                img_1, img_2, img_3 = '', '', ''
                if len(img_list)==1:
                    img_1 = img_list[0]
                elif len(img_list)==2:
                    img_1, img_2 = img_list[0], img_list[1]
                elif len(img_list)==3:
                    img_1, img_2, img_3 = img_list[0], img_list[1], img_list[2]            
                writer.writerow([product_name,product_url,price,product_img_url,
                                 status,stock,img_1, img_2, img_3])#,img_list)
                
                #input()
                
            #break
