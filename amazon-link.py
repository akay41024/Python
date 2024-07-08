import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/Allen-Solly-Regular-AMKP317G04249_Jet-Black_XX-Large/dp/B06Y1X1HTM/?_encoding=UTF8&pd_rd_w=zk6jL&content-id=amzn1.sym.6a567e3d-fd9a-4932-aa05-d0107e1bcce7&pf_rd_p=6a567e3d-fd9a-4932-aa05-d0107e1bcce7&pf_rd_r=HCM63EVACQZ9AS2FFN4R&pd_rd_wg=LAJjD&pd_rd_r=bde2085b-d5fc-43f2-bf2e-b92f4d6fc325&ref_=pd_hp_d_btf_a2i_gw_cml'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
links = [a['href'] for a in soup.find_all('a', href=True)]
for link in links:
    print(link)
