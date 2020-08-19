import os
import json
import base64
import requests
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
test_cat = os.path.join(dir_path, 'test_images')
def file2base64(path):
    with open(path, mode='rb') as fl:
        encoded = base64.b64encode(fl.read()).decode('ascii')
        return encoded


def extract_vecs(ims,max_size=640):
    time_now1 = datetime.datetime.now()
    target = [file2base64("test_images/" + im) for im in ims]
    time_now2 = datetime.datetime.now()
    print(time_now2-time_now1)
    req = {"images": {"data": target},"max_size":max_size}
    resp = requests.post('http://10.60.2.199:18080/extract', json=req)
    time_now3 = datetime.datetime.now()
    print(time_now3-time_now2)
    
    data = resp.json()
    return data
def test_verfication():
        source = os.path.join(test_cat , 'TH.png')
        target = os.path.join(test_cat, 'TH1.jpg')
        target2 = os.path.join(test_cat, 'TH.png')
        list=[]
        list.append(file2base64(target))
        list.append(file2base64(target2))
        req = {"source": {"data":file2base64(source)}, "target":{"data":list}}
        resp = requests.post('http://10.60.2.199:18080/ver', json=req)
        data = resp.json()
        return data
def test_getEmb1():
        source = os.path.join(test_cat , 'Stallone.jpg')
        req = {"source": {"url":source}}
        resp = requests.post('http://10.60.2.199:18080/getEmb', json=req)
        data = resp.json()
        return data
def test_getEmb2():
        source = os.path.join(test_cat , 'Stallone.jpg')
        req = {"source": {"data":file2base64(source)}}
        resp = requests.post('http://10.60.2.199:18080/getEmb', json=req)
        data = resp.json()
        return data
def test_getEmb3():
        source = os.path.join(test_cat , 'Stallone.jpg')
        source2 = os.path.join(test_cat , 'TH1.jpg')
        source3 = os.path.join(test_cat , 'TH.png')
        list = [] 
        list.append(file2base64(source))
        list.append(file2base64(source2))
        list.append(file2base64(source3))

        req = {"source": {"data":list}}
        resp = requests.post('http://10.60.2.199:18080/getEmbList', json=req)
        data = resp.json()
        return data
#data =test_verfication()
#data =test_getEmb2()
data =test_getEmb3()
print(data)
#data = extract_vecs(images, 640)
#print(data)
