import requests

cet_url='https://www.chsi.com.cn/cet/query'



def query_score(id,xm):
    params={'zkzh':id,'xm':xm}
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Referer': 'https://www.chsi.com.cn/cet/',
        'X-Forwarded-For':'127.0.0.'
    }
    
    r=requests.get(url=cet_url,params=params,headers=headers)
    
    text=r.text
    search_text = ['<span class="colorRed">', '</span>']
    total_score_start = text.find(search_text[0])
    total_score_start += len(search_text[0])
    total_score_end = text.find(search_text[1], total_score_start)
    try:
        total_score = str(int(text[total_score_start:total_score_end]))
        return total_score
    except:
        return -1

