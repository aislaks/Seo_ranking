from googlesearch import search
 

def search_ranking(keyword, extension, website):
    query = "seo kochi" # search string
    tld = "com" # google extension
    
    i=1
    for j in search(query, tld=tld, num=200, start =0, stop=200, pause=2): 
        if "seowolves.in" in j:
            return i
        i+=1