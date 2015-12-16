import os,sys
import hashlib

def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        print(hash)
    return hash
def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        print(hash)
    return hash
CalcSha1('E:/ooxx/0061Uxz8jw1epr7wjvjnvj30g10ngtdv.jpg')
CalcMD5('E:/ooxx/0061Uxz8jw1epr7wjvjnvj30g10ngtdv.jpg')