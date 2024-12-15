import requests
from bs4 import BeautifulSoup

def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        content = soup.get_text(separator=' ', strip=True)
        return purifier(content)
    else:
        return f"Failed to retrieve content. Status code: {response.status_code}"

def purifier(content:str):
    """
    Function used to purify the content with non allowed characters.
    """
    ALLOWED_CHRACTERS=[
        "A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '0','1','2','3','4','5','6','7','8','9',' ','-',"[",']','{','}','!','@','#', '$','%','^','&','\\','*','(',
        ")",':',',','.','?','_'
    ]
    filtered=content.upper()
    for i in filtered:
        if i not in ALLOWED_CHRACTERS:
            filtered=filtered.replace(i,'',-1)   
    return filtered



if __name__=="__main__":
    url = """https://www.ndtv.com/india-news/explained-why-delhis-aqi-was-494-today-but-international-monitor-said-1600-7054945"""
    content = get_content(url)
    print(content)