import urllib, urllib2, cookielib

data_login={
    'username':'imsuperm@3g.sina.cn',
    'password':'Alex0801',
    'savestate':'1',
    'ec':'0',
    'pagerefer':'http://passport.sina.cn/sso/logout?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn',
    'entry':'mweibo',
    'wentry':'',
    'loginfrom':'',
    'client_id':'',
    'code':'',
    'qq':'',
    'hff':'',
    'hfp':'',
    }

headers_login={
    'Connection':'keep-alive',
    'Referer':'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

cj=cookielib.CookieJar()
opener_login=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener_login)
requrl_login='https://passport.weibo.cn/sso/login'
postdata=urllib.urlencode(data_login)
req_login=urllib2.Request(requrl_login,postdata,headers_login)
res_login=urllib2.urlopen(req_login)
print res_login.read()
print '\n\nDon\'t know if it is finished\n\n'
requrl_visit='http://weibo.cn/'
headers_visit={
    'Connection':'keep-alive',
    'Host':'weibo.cn',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
req_visit=urllib2.Request(requrl_visit,urllib.urlencode(''),headers_visit)
res_visit=urllib2.urlopen(req_visit)
print res_visit.read()
