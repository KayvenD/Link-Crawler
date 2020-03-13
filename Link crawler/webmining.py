#!/usr/bin/env python

import os
import requests
from parsel import Selector
import sys
import time
from _datetime import datetime

from webtools import webinspector
from fstool import selfrepository
from mptool import multithread

##getlist --> (out:list)
##getfile --> (out:file)

class webscrapper:

# images extraction
    def getimagelist_href(link:str):
        __image_list = []
        try:
            print("Collecting images in the link: " + link)
            __response = requests.get(link, timeout = 10)
            __selector = Selector(__response.text)
            if __response.status_code == 200:
                __image_list = __selector.xpath('//img/@src').getall()
                print("Images collected!")
        except Exception as exp:
            print("Error in the link")
        __new_list = []
        for i in __image_list:
            if not (i[0:1] == "/"):
                __new_list.append(link + "/" + i)
            else:
                __new_list.append(link + i)
        print("Done!")
        print(__new_list)
        return __new_list

    def downloadfile_image(link:str):
        __file_path = webscrapper.__url2filepath(link)
        ##convert url to dir
        ##create new dir
        cwd = os.getcwd()
        fullname = os.path.join(cwd, __file_path)
        path, basename = os.path.split(fullname)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(fullname, 'w') as f:
            f.write('test\n')
        download_entries = 0
        ##images download method
        while True:
           try:

               ## downloading method
               r = requests.get(link, stream = True, timeout = 20)
               with open(fullname, 'wb') as f:
                   f.write(r.content)
                   break

           except:
               ## re-downloading method
               print("Max retries exceeded with url: " + link)
               time.sleep(1)
               download_entries = download_entries + 1
               if (download_entries == 3):
                   break
               else:
                   continue
        print("Download successful!")

    def downloadfiles_images(links:str):
        __count = 0
        __total = len(links)
        print(str(__total) + " files to be download.")
        for i in links:
            __count = __count + 1
            print("(" + str(__count) + "/" + str(__total) + ")" + " Downloading link: " + i)
            webscrapper.downloadfile_image(i)
        print("-----------------------------------------------------------------------------------")
        print("Download finished!")

# webpage extraction
    def __url2filepath(link:str):
        if(link[0:7] == "http://"):
            __new = link.replace("http://", "")
            return __new
        else:
            print("Error in the url")

    def downloadfile_href(link:str):
        __file_path = webscrapper.__url2filepath(link)
        ##convert url to dir
        ##create new dir
        cwd = os.getcwd()
        fullname = os.path.join(cwd, __file_path)
        path, basename = os.path.split(fullname)
        if "." in basename:
            if "www." in basename:
                print(link + "is a domain!")
            else:
                if not os.path.exists(path):
                    os.makedirs(path)

                __domain = link.split("//")[-1].split("/")[0]

                download_entries = 0
                #images download method
                while True:
                    try:
                        ## downloading method
                        resp = requests.get(link)
                        __encoding = resp.encoding
                        __ncontent = str(resp.content, '<UTF-8>')
                        __text = webinspector.inspect_html(__ncontent, __domain)
                        wt = open(fullname, 'w', encoding =__encoding)
                        wt.write(__text)
                        wt.close()
                        print(link + " download successful!")
                        break
                    except:
                        ## re-downloading method
                        print("Max retries exceeded with url: " + link)
                        time.sleep(1)
                        download_entries = download_entries + 1
                        if (download_entries == 3):
                            print(link + " download skipped!")
                            break
                        else:
                            continue

            # if (os.path.getsize(fullname) == 0):
            #     #os.close(os.open(fullname,os.O_WRONLY)
            #     time.sleep(1)
            #     os.remove(fullname)
            #     print("hello")

        else:
            print("Warning! No file extension detected on the " + link)

    def downloadfiles_hrefs(links:str):
        for i in links:
            webscrapper.downloadfile_href(i)
        print("-----------------------------------------------------------------------------------")
        print("Download finished!")

# javascript extraction
    def __manage_js(link:str):
        link = link.replace("http://","")
        link = link.replace("//", "")
        link = link.replace("../","/")
        link = link.replace("..",".")
        return link

    def getjslist_href(link:str):
        __script_list = []
        try:
            print("Collecting javascript in the link: " + link)
            __response = requests.get(link, timeout = 10)
            __selector = Selector(__response.text)
            if __response.status_code == 200:
                __script_list = __selector.xpath('//script/@src').getall()

        except Exception as exp:
            print("Error in the link")

        __domain = link.split("//")[-1].split("/")[0]

        __new_script_list = []
        __count = 0
        for i in __script_list:
            __count = __count + 1
            if not __domain in i:
                __new_script_list.append("http://" + __domain + webscrapper.__manage_js(i))
            else:
                __new_script_list.append("http://" + webscrapper.__manage_js(i))

        print(str(__count) + " JavaScripts collected!")
        print(__new_script_list)
        return __new_script_list

    def downloadfile_js(link:str):
        __file_path = webscrapper.__url2filepath(link)
        ##convert url to dir
        ##create new dir
        cwd = os.getcwd()
        fullname = os.path.join(cwd, __file_path)
        path, basename = os.path.split(fullname)
        print(fullname)
        print(path)
        print(basename)
        if not os.path.exists(path):
            os.makedirs(path)
        # except:
        #     print("FileNotFoundError: [WinError 3] The system cannot find the path specified: '" + path + "'")
        with open(fullname, 'wb') as f:
            f.close()

        ##javascript download method
        download_entries = 0
        while True:
            try:
                ## downloading method
                r = requests.get(link, stream=True, timeout = 10)
                with open(fullname, 'wb') as f:
                    f.write(r.content)
                    print("Download successful!")
                    break

            except:
                ## re-downloading method
                print("Max retries exceeded with url: " + link)
                time.sleep(1)
                download_entries = download_entries + 1
                if (download_entries == 3):
                    print(link + " download skipped!")
                    break
                else:
                    continue


    def downloadfiles_jss(links:str):
        for i in links:
            webscrapper.downloadfile_js(i)
        print("-----------------------------------------------------------------------------------")
        print("Download finished!")

# html live stream video extraction

    def getnm3u8list_href(link:str):
        __response = requests.get(link)
        __selector = Selector(__response.text)
        __links = __selector.xpath('//input/@value').getall()
        print(__links)
        return __links

    def __filterlist_m3u8s(links:str):
        __list = []
        for i in links:
            if ".m3u8" in i and "http://" in i:
                __list.append(i)
        return __list

    def getm3u8list_href(link:str):
        __m3u8s = webscrapper.getnm3u8list_href(link)
        __list = webscrapper.__filterlist_m3u8s(__m3u8s)
        return __list

# web-style/Cascading Style Sheet Extraction

    def getcsslist_href(link:str):
        try:
            print("Collecting web-styles in the link: " + link)
            __response = requests.get(link)
            __selector = Selector(__response.text)
            if __response.status_code == 200:
                __links = __selector.xpath('//link/@href').getall()
        except Exception as exp:
            print("Error in the web-styles link")

        __domain = link.split("//")[-1].split("/")[0]
        __css_list = []
        __count  = 0
        for __i in __links:
            if ".css" in __i:
                __count = __count + 1
                if not __domain in __i:
                    __css_list.append("http://" + __domain + __i)
                else:
                    __css_list.append(__i)
        ##print(__css_list)
        print(str(__count) + " Web-styles collected!")
        return __css_list

    def downloadfile_css(link:str):
       __file_path = webscrapper.__url2filepath(link)
       ##convert url to dir
       ##create new dir
       cwd = os.getcwd()
       fullname = os.path.join(cwd, __file_path)
       path, basename = os.path.split(fullname)
       if not os.path.exists(path):
           os.makedirs(path)
       download_entries = 0
       while True:
           try:
               ## downloading method
               r = requests.get(link)
               ##print(r.text)
               __encoding = r.encoding
               __ncontent = str(r.content, '<UTF-8>', errors = 'replace')
               wt = open(fullname, 'w', encoding = __encoding)
               wt.write(__ncontent)
               wt.close()
               print("Download successful!")
               break
           except:
               ## re-downloading method
               print("Max retries exceeded with url: " + link)
               time.sleep(1)
               download_entries = download_entries + 1
               if (download_entries == 3):
                   print(link + " download skipped!")
                   break
               else:
                   continue

    def downloadfiles_csss(links:str):
        for __i in links:
            webscrapper.downloadfile_css(__i)
        print("-----------------------------------------------------------------------------------")
        print("Download finished!")

class webcrawler:
    #
    # action(output-type)_input(list:dict(w/ s) : string(w/o s))

    def uniquelist_hrefs(__links:str): ## remove duplicate values
        __links = list(dict.fromkeys(__links))
        return __links

    def rmanagelist_hrefs(__tlist):
        __list = webcrawler.rfilterlist_hrefs(__tlist)
        ##print(__list)
        __domain = __list[ - 1]
        ##__list.remove(__domain)
        __domain = __domain.split("//")[-1].split("/")[0]
        __url = "http://" + __domain
        ## stage1
        __newlink = []
        for i in __list:
            if (i[0:1] == "/"):
                __newlink.append(__url + i)
            else:
                __newlink.append(i)
        __newlink = list(filter(None, __newlink))
        ## stage2

        __newlist = webcrawler.uniquelist_hrefs(__newlink)
        __fflist = webcrawler.rfilterlist_hrefs(__newlist)

        ##stage3
        __plist = []
        for __i in __fflist:
            if "http://" in __i:
                __plist.append(__i)
        ##print(__plist)
        ##stage4 - remove url duplicate
        try:
            __plist.remove(__url)
            pass
        except:
            pass
        try:
            __plist.remove(__url + "/")
            pass
        except:
            pass

        return __plist

    def rfilterlist_hrefs(__list):
        __newlink = []
        for i in __list:
            i = i.replace(" rel=”nofollow", "")
            i = i.replace("http://#", "http://")
            __newlink.append(i)
        return __newlink

    def rgetlist_href(__link):
        if(__link == ""):
            sys.exit(1)
        try:
            __response = requests.get(__link)
            __selector = Selector(__response.text)
            __href_link = __selector.xpath('//a/@href').getall()
            __num = len(__href_link)
            if(__num):
                print(str(__num) + " Links collected on " + __link)
                __href_link.append(__link)
                __unique_list = webcrawler.uniquelist_hrefs(__href_link)
                __managed_list = webcrawler.rmanagelist_hrefs(__unique_list)
                return __managed_list
            else:
                print(" No link found on " + __link)
                __list = []
                return __list
            __response.close()
        except requests.exceptions.ConnectionError as err:
            print("Unable to connect :/ " + __link )
            print("Please check the URL!")
            __list = []
            return __list
            ##sys.exit(1)
        except requests.exceptions.MissingSchema as err:
            print("Invalid URL! " + __link)
            __list = []
            return __list
            ##sys.exit(1)
        except:
            print("an error occured!")
            __list = []
            return __list
            ##sys.exit(1)


    def get_content_type(__link:str):
        __contenttype = ""
        try:
            r = requests.head(__link, allow_redirects=True)
            __content = r.headers
            __contenttype = __content.get('Content-Type')
        except:
            print(__link + " Unable to read content-type!")
            pass
        ##print("content-type: " + __contenttype)
        return __contenttype

    def seed_href(__link:str):
        __stat = {}
        __domain = ""
        __time = ""
        __start_time = 0
        if "http://" in __link:
            __domain = __link.split("//")[-1].split("/")[0]
            __now = datetime.now()
            __time = __now.strftime("%m/%d/%Y/%H:%M:%S")
            if(__link == ""):
                return ""
            download_entries = 0
            while True:
                try:
                    __start_time = time.time()
                    __response = requests.get(__link)
                    if __response.status_code == 200:
                        __stat['http_response'] = 1
                        break
                except:
                    download_entries += 1
                    if(download_entries >= 3):
                        __stat['http_response'] = 0
                        break
                    else:
                        continue
        else:
            pass

        __endtime = time.time()
        __stat['starting_time'] = __time
        __stat['response_time'] = str(__endtime - __start_time) + "s"
        __stat['domain'] = __domain
        return __stat

#################################################
    def getlist_href(link:str):
        try:
            __response = requests.get(link)
            __selector = Selector(__response.text)
            __href_link = __selector.xpath('//a/@href').getall()
            ##print(__href_link)

            # __response = requests.get(link)
            # __selector = Selector(__response.text)
            # __href2_links = __selector.xpath('//link/@href').getall()

            # __all_href_links = []
            # __all_href_links.append(__href_links)
            # __all_href_links.append(__href2_links)

            __num = len(__href_link)
            if(__num):
                print(str(__num) + " Links collected on " + link)
            else:
                print(" No link found on " + link)
            __href_link.append(link)

            __response.close()

        except requests.exceptions.ConnectionError as err:
            print("Unable to connect :/")
            print("Please the URL!")
            sys.exit(1)
        except requests.exceptions.MissingSchema as err:
            print("Invalid URL!")
            sys.exit(1)
        return __href_link

    def responselist_hrefs(links:str):
        print("Getting response to all links........please wait")
        __response_list = {}
        __response = []
        for __i in links:
            __response.append(webcrawler.test_href(__i))

        __response_list['http_links'] = links
        __response_list['http_responses'] = __response
        ##print(__response_list)
        print("Seed operation done!")
        return __response_list

    def test_href(link:str):
        try:
            __response = requests.get(link, timeout = 10)
            ## http_ok = 200
            if __response.status_code == 200:
                return 1
            else:
                return 0
        except:
            print("error in the link: " + link)
            return -1

    def filterlist_hrefs(links:str):
        __newlink = []
        for i in links:
            i = i.replace(" rel=”nofollow", "")
            __newlink.append(i)
        return __newlink

    def urlchecklist_hrefs(links):
        __a = []
        __count = 0
        for i in links:
            __count = __count + 1
            if "http://" in i:
                __a.append(i)
        print(str(__count) + " Clean links collected!")
        return __a

    def getlist_from_link(link:str):
        if(isinstance(link,str)):
            __a = webcrawler.getlist_href(link)
            __b = webcrawler.uniquelist_hrefs(__a)
            __c = webcrawler.managelist_hrefs(__b)
            __d = webcrawler.urlchecklist_hrefs(__c)
            return __d
        else:
            print(" webcrawler.getlist_from_link(..) --> Not a string!")
            sys.exit()

    def getrootlist__from_link(link:str):
        if(isinstance(link,str)):
            __a = webcrawler.getlist_href(link)
            __b = webcrawler.uniquelist_hrefs(__a)
            __c = webcrawler.managelist_hrefs(__b)
            __d = webcrawler.urlchecklist_hrefs(__c)
            __dlink = []
            for i in __d:
                if link in i:
                    __dlink.append(i)
            return __dlink
        else:
            print(" webcrawler.getrootlist_from_link(..) --> Not a string!")
            sys.exit()

    def managelist_hrefs(links:str):
        __newlinks = webcrawler.filterlist_hrefs(links)
        __lastnum = len(__newlinks)
        __domain = __newlinks[__lastnum - 1]
        __newlinks.remove(__domain)
        __domain = __domain.split("//")[-1].split("/")[0]
        __domain = "http://" + __domain
        __newlink = []
        for i in __newlinks:
            if(i[0:1] == "/"):
                __newlink.append(__domain + i)
            else:
                __newlink.append(i)
        return __newlink



