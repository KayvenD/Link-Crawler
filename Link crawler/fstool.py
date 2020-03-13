#!/usr/bin/env python

from os import path
import os
import sys

import shutil

class fileoperation:
    def create_file(filename:str):
        if not path.exists(filename):
            __fhndl = open(filename,"x")
            __fhndl.close()
            print(filename + " is created!")
        else:
            print("File is present!")

    def save_data(filename, data:str):
        if(data):
            data = data + "\n"
            __fhndl = open(filename,"a+")
            __fhndl.write(data)
            __fhndl.close()

    def url2filepath(link:str):
        if(link[0:7] == "http://"):
            __new = link.replace("http://", "")
            __new = __new.replace(".", "_")
            __new = __new + ".txt"
            return __new
        else:
            print("Error in the url")


class list_transfer:
    def addlist2file(filename:str,list):
        for i in list:
            fileoperation.save_data(filename,i)
            print(i + " successfully added!")


class collection_management:

    def getlist_from_a_file(__fpath):
        with open(__fpath, "r+") as __f:
            __list = list(__f)
        return __list
    def poplist(__list):
        __item = __list.pop()
        return __item

class selfrepository:

    def get_available_file():
        __entries = os.listdir('.crawler-cache/')
        __cwd = os.getcwd()
        __txt_list = []
        for __file in __entries:
            if __file.endswith('.txt'):
                __txt_list.append(__file)
        return __txt_list[-1]


    def countfile_in_the_workingdir():
        __entries = os.listdir('.crawler-cache/')
        __filecount = 0
        for __file in __entries:
            if __file.endswith('.txt'):
                __filecount += 1
        return __filecount


    def prepare_temp_file():
        print("Moving cache files to working directory................please wait!")
        __entries = os.listdir('.crawler-cache/temp/')
        __cwd = os.getcwd()
        __txt_list = []

        for __file in __entries:
            if __file.endswith('.txt'):
                __txt_list.append(__file)

        __destination_path = __cwd + '/.crawler-cache/'
        for __txtfile in __txt_list:
            __source_path = __cwd + '/.crawler-cache/temp/' + __txtfile
            if (shutil.copy(__source_path, __destination_path)):
                os.remove(__source_path)


    def depositlist(__filename, __list):
        __nfilename = selfrepository.__url2filepath(__filename)
        cwd = os.getcwd()
        __full_path = cwd + "/.crawler-cache/temp/" + __nfilename
        fullname = os.path.join(cwd, __full_path)
        path, basename = os.path.split(fullname)

        if not os.path.exists(path):
            os.makedirs(path)
        for __i in __list:
            selfrepository.__save_data(__full_path, __i)
            ##print(__i + " successfully added to temp dir!")

    def disposefile(__filename):
        __nfilename = selfrepository.__url2filepath(__filename)
        cwd = os.getcwd()
        __source_path = cwd + "/.crawler-cache/" + __nfilename
        __grave_path = cwd + "/.crawler-cache/grave/"
        if not os.path.exists(__grave_path):
            os.makedirs(__grave_path)
        __destination_path = __grave_path + __nfilename
        try:
            if(shutil.copy(__source_path,__destination_path)):
                os.remove(__source_path)
                return 1
            else:
                return 0
        except:
            print("file not found!")
            sys.exit()
            ##pass

    def poplist(__list):
        __item = __list.pop()
        return __item

    def getlist_from_a_file(__filename):
        __nfilename = selfrepository.__url2filepath(__filename)
        cwd = os.getcwd()
        __full_path = cwd + "/.crawler-cache/" + __nfilename
        fullname = os.path.join(cwd, __full_path)
        path, basename = os.path.split(fullname)
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            with open(__full_path, "r+") as __f:
                __list = list(__f)
                __f.close()
                __converted_list = []
                for __i in __list:
                    __converted_list.append(__i.strip())
                return __converted_list
        except:
            print("No such file or directory: '" + __full_path + "'")
            print("process terminated!")
            sys.exit(1)

    def test(filename):
        cwd = os.getcwd()
        full_path = cwd + "/.crawler-cache/" + filename
        fullname = os.path.join(cwd, full_path)
        path, basename = os.path.split(fullname)
        if not os.path.exists(path):
            os.makedirs(path)

        with open(full_path, 'w') as f:
            f.write('test\n')
        f.close()

    def addlist2file(filename, data:str):
        __nfilename = selfrepository.__url2filepath(filename)
        cwd = os.getcwd()
        full_path = cwd + "/.crawler-cache/" + __nfilename
        fullname = os.path.join(cwd, full_path)
        path, basename = os.path.split(fullname)

        if not os.path.exists(path):
            os.makedirs(path)
        for __i in data:
            selfrepository.__save_data(full_path, __i)
            print(__i + " successfully added!")

    def __save_data(__fpath, __data:str):
        if(__data):
            __data = __data + "\n"
            try:
                with open(__fpath,"a+") as __fhndl:
                    __fhndl.write(__data)
                    __fhndl.close()
            except:
                pass

    def __url2filepath(__link:str):
        __new = __link.split("//")[-1].split("/")[0]
        __new = __new.replace(".","_")
        __new = __new.replace("_txt",".txt")
        if ".txt" in __new:
            return __new
        else:
            __new = __new + ".txt"
            return __new

    # def addlist2file(filename:str, list):
    #     if (data):
    #         data = data + "\n"
    #         __fhndl = open(filename, "a+")
    #         __fhndl.write(data)
    #         __fhndl.close()
    #
    #         __file_path = webscrapper.__url2filepath(link)
    #         ##convert url to dir
    #         ##create new dir
    #         cwd = os.getcwd()
    #         fullname = os.path.join(cwd, __file_path)
    #         path, basename = os.path.split(fullname)
    #         if not os.path.exists(path):
    #             os.makedirs(path)
    #         with open(fullname, 'w') as f:
    #             f.write('test\n')
    #         download_entries = 0






