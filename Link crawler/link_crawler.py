
from webmining import webscrapper
from webmining import webcrawler
from fstool import fileoperation
from fstool import list_transfer
from webtools import download_media
from fstool import collection_management
from mptool import multithread

from mongotools import create_mongodb_connection
from mongotools import userlist
from fstool import selfrepository
import time
import os

import sys

#---------------------------------------------------------------------------------------------------

target_url = 'http://www.ahzixun.cn/'
# target_url = ""
wc = create_mongodb_connection("mongodb://localhost:27017/", "kay's_database", "web_data")

db_domain = ""
db_url = ""
db_st = ""
db_rt = ""
db_mt = ""
db_hsc = ""

#
wc.delete_collection()
__wlist = webcrawler.getlist_from_link(target_url)
for i in __wlist:
    db_mt = webcrawler.get_content_type(i)
    _stat = webcrawler.seed_href(target_url)
    db_st = _stat.get('starting_time')
    db_rt = _stat.get('response_time')
    db_hsc = _stat.get('http_response')
    db_domain = _stat.get('domain')
    db_url = i

    __udata = userlist.create_list(db_domain, db_url, db_st, db_rt, db_mt, db_hsc)
    wc.add_one_dictlist(__udata)
wc.show_content()

# start = time.time()
#
# __wlist = webcrawler.getlist_from_link(target_url)
# selfrepository.addlist2file(target_url,__wlist)
#
#
# __execution_times = 2
# __execution_counter = 0
#
# def main():
#     global __execution_counter
#
#     print("start")
#     __execution_counter = __execution_counter + 1
#     print(__execution_counter)
#
#     global biglist
#     global __target_file
#
#     __target_file = selfrepository.get_available_file()
#     biglist = selfrepository.getlist_from_a_file(__target_file)
#     print("crawling.... " + __target_file)
#
#     multithread.run(task, 10)
#     setup()
#
# def task():
#     while True:
#
#         if(biglist):
#             __popitem = selfrepository.poplist(biglist)
#             __hreflist = webcrawler.rgetlist_href(__popitem)
#             selfrepository.depositlist(__popitem,__hreflist)
#         else:
#
#
#             break
#
# def setup():
#
#     if (__execution_counter >= __execution_times):
#         exit()
#
#     __status = selfrepository.disposefile(__target_file)
#     if __status == 1:
#         if (selfrepository.countfile_in_the_workingdir() == 0):
#             selfrepository.prepare_temp_file()
#             main()
#         else:
#             main()
#
# def exit():
#     end = time.time()
#     print("Time taken in seconds : ", (end - start))
#     sys.exit()
#
# main()

#===============================================================


###save collected links
# ##fileoperation.create_file('link.txt')
# __domain = fileoperation.url2filepath(target_url)
# list_transfer.addlist2file(__domain,__list)
#
# # ## ping links
# # __response_list = webcrawler.responselist_hrefs(__list)
# # print(__response_list['http_links'])
# # print(__response_list['http_responses'])
#
# ## download links
# webscrapper.downloadfiles_hrefs(__list)
#




# ## download images
# __imagelinks = webscrapper.getimagelist_href(target_url)
# #webscrapper.downloadfiles_images(__imagelinks)


#
# ## download javascript
# __jslinks = webscrapper.getjslist_href(target_url)
# webscrapper.downloadfiles_jss(__jslinks)
#
# ## download web-styles/CSS
# __csslinks = webscrapper.getcsslist_href(target_url)
# webscrapper.downloadfiles_csss(__csslinks)
