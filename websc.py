import requests
import bs4

#サイトURL
url = "https://xxxxxxx"

#webサイトの情報をGETする
res = requests.get(url)

#全てのHTML情報を表示
#print(res.text)

#名前をつけてhtmlファイルに出力
#with open('citportal.html', 'w') as file:
    #file.write(res.text)


#エラー処理

#HTTPコードの出力
#print(res.status_code)

#もしステータスコードが200番台以外の時はエラーとして停止してエラーメッセージを出す
#res.raise_for_status()
#print(res.text)

#HTML文字列を解析
soup = bs4.BeautifulSoup(res.text, "html.parser")
link = soup.select("#list a")

#aタグのURlを全て出力
for link in link:
    print("{}".format(link.get("href")))
