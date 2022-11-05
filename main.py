import requests as r
from bs4 import BeautifulSoup as bs
import csv

URL_BASE = 'https://www.rajagrafindo.co.id/store/'

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
        
        base_html = r.get(URL_BASE).content
        base_soup = bs(base_html,'html.parser')
        last_page_url = base_soup.find('a',class_='pager_last')['href']
        last_page_num = int(last_page_url.split('/')[-2])    
        page_url_list = []
        page_url_list.append('https://www.rajagrafindo.co.id/store/')
        for i in range(2,last_page_num+1):
            page_url_list.append(f'https://www.rajagrafindo.co.id/store/page/{i}/')
            
        for page_url in page_url_list:
            html = r.get(page_url).content
            soup = bs(html,'html.parser')
            products = soup.find_all('a', class_ = 'woocommerce-LoopProduct-link woocommerce-loop-product__link')
            for product in products:
                product_url = product['href']
                product_html = r.get(product_url).content
                product_soup = bs(product_html,'html.parser')
                
                product_name = product_soup.find('h1', class_='product_title entry-title').text
                price = float(product_soup.find('p', class_='price').text.replace('Rp','').replace(',',''))
                print('',product_url,product_name,price)
                
                description = product_soup.find('div', class_='woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab').text
                print(description)
                
                penulis = product_soup.find('li', class_='pa_penulis').text.split(':')[1].strip()
                print(penulis)
                
                isbn = product_soup.find('li', class_='pa_isbn').text.split(':')[1].strip()
                print(isbn)

                halaman = product_soup.find('li', class_='pa_halaman').text.split(':')[1].strip()
                print(halaman)

                ukuran = product_soup.find('li', class_='pa_ukuran').text.split(':')[1].strip()
                print(ukuran)

                tahun = product_soup.find('li', class_='pa_tahun-terbit').text.split(':')[1].strip()
                print(tahun)
                                
                input()
                price = product.find('strike').text
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
