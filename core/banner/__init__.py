from os import path
def banner():
    banner = open(path.join("core", "banner", "banner_1.txt")).read()
    print (banner)