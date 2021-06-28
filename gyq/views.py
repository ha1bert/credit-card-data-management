from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import pandas as pd
def totojson(pdData,name,flag): #1=data.json,2=login.json
    if flag==2:
        with open(name, 'w',encoding='utf-8') as f:
            f.write("[\n")
            for i in range(len(pdData)):
                if i!= (len(pdData)-1):
                    tmp="{"+"\"username\":\""+pdData.loc[i]["username"]+"\",\"password\": \""+pdData.loc[i]["password"]+"\",\"authority\": \""+pdData.loc[i]["authority"]+"\",\"name\": \""+pdData.loc[i]["name"]+"\",\"address\": \""+pdData.loc[i]["address"]+"\",\"charger\" : \""+pdData.loc[i]["charger"]+"\",\"phone\": \""+pdData.loc[i]["phone"]+"\",\"email\": \""+pdData.loc[i]["email"]+"\"},\n"
                else:
                    tmp="{"+"\"username\":\""+pdData.loc[i]["username"]+"\",\"password\": \""+pdData.loc[i]["password"]+"\",\"authority\": \""+pdData.loc[i]["authority"]+"\",\"name\": \""+pdData.loc[i]["name"]+"\",\"address\": \""+pdData.loc[i]["address"]+"\",\"charger\" : \""+pdData.loc[i]["charger"]+"\",\"phone\": \""+pdData.loc[i]["phone"]+"\",\"email\": \""+pdData.loc[i]["email"]+"\"}"
                f.write(tmp)
            f.write("\n]")
    else:
        with open(name, 'w',encoding='utf-8') as f:
            f.write("[\n")
            for i in range(len(pdData)):
                if i!= (len(pdData)-1):
                    tmp="{"+"\"client_num\":\""+pdData.loc[i]["client_num"]+"\",\"education_level\": \""+pdData.loc[i]["education_level"]+"\",\"marital_status\": \""+pdData.loc[i]["marital_status"]+"\",\"income_category\": \""+pdData.loc[i]["income_category"]+"\",\"gender\": \""+pdData.loc[i]["gender"]+"\",\"age\" : \""+pdData.loc[i]["age"]+"\",\"credit_limit\": \""+pdData.loc[i]["credit_limit"]+"\",\"total_trans_amt\" : \""+pdData.loc[i]["total_trans_amt"]+"\",\"avg_utilization_ratio\": \""+pdData.loc[i]["avg_utilization_ratio"]+"\",\"flag\": \""+pdData.loc[i]["flag"]+"\"},\n"
                else:
                    tmp="{"+"\"client_num\":\""+pdData.loc[i]["client_num"]+"\",\"education_level\": \""+pdData.loc[i]["education_level"]+"\",\"marital_status\": \""+pdData.loc[i]["marital_status"]+"\",\"income_category\": \""+pdData.loc[i]["income_category"]+"\",\"gender\": \""+pdData.loc[i]["gender"]+"\",\"age\" : \""+pdData.loc[i]["age"]+"\",\"credit_limit\": \""+pdData.loc[i]["credit_limit"]+"\",\"total_trans_amt\" : \""+pdData.loc[i]["total_trans_amt"]+"\",\"avg_utilization_ratio\": \""+pdData.loc[i]["avg_utilization_ratio"]+"\",\"flag\": \""+pdData.loc[i]["flag"]+"\"}"
                f.write(tmp)
            f.write("\n]")
def index(request):
    return render(request, 'index.html')
def main_1(request):
    username_input=request.GET.get('username')
    return render(request, 'main_1.html', {"username_input":username_input})
def main_2(request):
    username_input=request.GET.get('username')
    return render(request, 'main_2.html', {"username_input":username_input})
def data_add(request):
    return render(request, 'data_add.html')
def login_add(request):
    return render(request, 'login_add.html')
def data_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'data_manage.html', {"username_input":username_input})
def login_manage(request):
    username_input=request.GET.get('username')
    return render(request, 'login_manage.html', {"username_input":username_input})
def persional(request):
    user=request.GET.get('username')
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    user=str(user)
    a=list(pdData[pdData["username"]==user]["username"])[0]
    return_param={
        "username": list(pdData[pdData["username"]==user]["username"])[0],
        "password": list(pdData[pdData["username"]==user]["password"])[0],
        "authority": list(pdData[pdData["username"]==user]["authority"])[0],
        "name": list(pdData[pdData["username"]==user]["name"])[0],
        "address": list(pdData[pdData["username"]==user]["address"])[0],
        "charger" : list(pdData[pdData["username"]==user]["charger"])[0],
        "phone":list(pdData[pdData["username"]==user]["phone"])[0],
        "email": list(pdData[pdData["username"]==user]["email"])[0]
    }
    return render(request, 'grzl.html', return_param)
def xgmm(request):
    user=request.GET.get('username')
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    user=str(user)
    a=list(pdData[pdData["username"]==user]["username"])[0]
    return_param={
        "username": list(pdData[pdData["username"]==user]["username"])[0],
        "password": list(pdData[pdData["username"]==user]["password"])[0],
        "authority": list(pdData[pdData["username"]==user]["authority"])[0],
        "name": list(pdData[pdData["username"]==user]["name"])[0],
        "address": list(pdData[pdData["username"]==user]["address"])[0],
        "charger" : list(pdData[pdData["username"]==user]["charger"])[0],
        "phone":list(pdData[pdData["username"]==user]["phone"])[0],
        "email": list(pdData[pdData["username"]==user]["email"])[0]
    }
    return render(request, 'xgmm.html', return_param)
def data_updata(request):
    client_num=str(request.GET.get('client_num'))
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\data.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    return_param={
        "client_num": list(pdData[pdData["client_num"]==client_num]["client_num"])[0],
        "education_level": list(pdData[pdData["client_num"]==client_num]["education_level"])[0],
        "marital_status": list(pdData[pdData["client_num"]==client_num]["marital_status"])[0],
        "income_category": list(pdData[pdData["client_num"]==client_num]["income_category"])[0],
        "gender": list(pdData[pdData["client_num"]==client_num]["gender"])[0],
        "age" : list(pdData[pdData["client_num"]==client_num]["age"])[0],
        "credit_limit":list(pdData[pdData["client_num"]==client_num]["credit_limit"])[0],
        "total_trans_amt": list(pdData[pdData["client_num"]==client_num]["total_trans_amt"])[0],
        "avg_utilization_ratio":list(pdData[pdData["client_num"]==client_num]["avg_utilization_ratio"])[0],
        "flag": list(pdData[pdData["client_num"]==client_num]["flag"])[0]
    }
    return render(request, 'data_updata.html', return_param)
def login_updata(request):
    username=str(request.GET.get('username'))
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    return_param={
        "username": list(pdData[pdData["username"]==username]["username"])[0],
        "password": list(pdData[pdData["username"]==username]["password"])[0],
        "authority": list(pdData[pdData["username"]==username]["authority"])[0],
        "name": list(pdData[pdData["username"]==username]["name"])[0],
        "address": list(pdData[pdData["username"]==username]["address"])[0],
        "charger" : list(pdData[pdData["username"]==username]["charger"])[0],
        "phone":list(pdData[pdData["username"]==username]["phone"])[0],
        "email": list(pdData[pdData["username"]==username]["email"])[0]
    }
    return render(request, 'login_updata.html', return_param)
def data_json(request):
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\data.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    #return_param={'status':["500"]}
    return HttpResponse(json.dumps(jsonData))
def login_json(request):
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    #return_param={'status':["500"]}
    return HttpResponse(json.dumps(jsonData))
def axis_data(request): #"1"=新增 "2"="修改" "3"="删除"
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\data.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    tag = str(request.POST.get('tag', 0))
    
    if(tag=="1"):
        client_num = str(request.POST.get('client_num', 0))
        education_level = str(request.POST.get('education_level', 0))
        marital_status = str(request.POST.get('marital_status', 0))
        income_category = str(request.POST.get('income_category', 0))
        gender = str(request.POST.get('gender', 0))
        age = str(request.POST.get('age', 0))
        credit_limit = str(request.POST.get('credit_limit', 0))
        total_trans_amt = str(request.POST.get('total_trans_amt', 0))
        avg_utilization_ratio = str(request.POST.get('avg_utilization_ratio', 0))
        flag = str(request.POST.get('flag', 0))
        new=pd.DataFrame({'client_num':client_num,
                  'education_level':education_level,
                  'marital_status':marital_status,
                  'income_category':income_category,
                  'gender':gender,
                 'age':age,
                  'credit_limit':credit_limit,
                  'total_trans_amt':total_trans_amt,
                  'avg_utilization_ratio':avg_utilization_ratio,
                  'flag':flag}, index=[1])
        pdData=pdData.append(new,ignore_index=True)
    elif(tag=="2"):
        client_num = str(request.POST.get('client_num', 0))
        education_level = str(request.POST.get('education_level', 0))
        marital_status = str(request.POST.get('marital_status', 0))
        income_category = str(request.POST.get('income_category', 0))
        gender = str(request.POST.get('gender', 0))
        age = str(request.POST.get('age', 0))
        credit_limit = str(request.POST.get('credit_limit', 0))
        total_trans_amt = str(request.POST.get('total_trans_amt', 0))
        avg_utilization_ratio = str(request.POST.get('avg_utilization_ratio', 0))
        flag = str(request.POST.get('flag', 0))
        
        pdData.loc[pdData["client_num"]==client_num,"education_level"]=education_level
        pdData.loc[pdData["client_num"]==client_num,"marital_status"]=marital_status
        pdData.loc[pdData["client_num"]==client_num,"income_category"]=income_category
        pdData.loc[pdData["client_num"]==client_num,"gender"]=gender
        pdData.loc[pdData["client_num"]==client_num,"age"]=age
        pdData.loc[pdData["client_num"]==client_num,"credit_limit"]=credit_limit
        pdData.loc[pdData["client_num"]==client_num,"total_trans_amt"]=total_trans_amt
        pdData.loc[pdData["client_num"]==client_num,"avg_utilization_ratio"]=avg_utilization_ratio
        pdData.loc[pdData["client_num"]==client_num,"flag"]=flag
    else:
        client_num = str(request.POST.get('client_num', 0))
        client_num=json.loads(client_num)
        for i in range(len(client_num)):
            index_num=pdData.loc[pdData['client_num']==client_num[i]].index[0]
            pdData=pdData.drop(labels=index_num,axis=0)
        pdData=pdData.reset_index(drop=True)

    totojson(pdData,file_name,1)
    return_param={"result": "1"}
    return HttpResponse(json.dumps(return_param))
def axis_manage_login(request): #"1"=新增 "2"="修改" "3"="删除"
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    tag = str(request.POST.get('tag', 0))
    
    if(tag=="1"):
        username = str(request.POST.get('username', 0))
        password = str(request.POST.get('password', 0))
        authority = str(request.POST.get('authority', 0))
        name = str(request.POST.get('name', 0))
        address = str(request.POST.get('address', 0))
        charger = str(request.POST.get('charger', 0))
        phone = str(request.POST.get('phone', 0))
        email = str(request.POST.get('email', 0))
        new=pd.DataFrame({'username':username,
                  'password':password,
                  'authority':authority,
                  'name':name,
                  'address':address,
                 'charger':charger,
                  'phone':phone,
                  'email':email}, index=[1])
        pdData=pdData.append(new,ignore_index=True)
    elif(tag=="2"):
        username = str(request.POST.get('username', 0))
        password = str(request.POST.get('password', 0))
        authority = str(request.POST.get('authority', 0))
        name = str(request.POST.get('name', 0))
        address = str(request.POST.get('address', 0))
        charger = str(request.POST.get('charger', 0))
        phone = str(request.POST.get('phone', 0))
        email = str(request.POST.get('email', 0))

        pdData.loc[pdData["username"]==username,"password"]=password
        pdData.loc[pdData["username"]==username,"authority"]=authority
        pdData.loc[pdData["username"]==username,"name"]=name
        pdData.loc[pdData["username"]==username,"address"]=address
        pdData.loc[pdData["username"]==username,"charger"]=charger
        pdData.loc[pdData["username"]==username,"phone"]=phone
        pdData.loc[pdData["username"]==username,"email"]=email
    else:
        username = str(request.POST.get('username', 0))
        username=json.loads(username)
        for i in range(len(username)):
            index_num=pdData.loc[pdData['username']==username[i]].index[0]
            pdData=pdData.drop(labels=index_num,axis=0)
        pdData=pdData.reset_index(drop=True)

    totojson(pdData,file_name,2)
    return_param={"result": "1"}
    return HttpResponse(json.dumps(return_param))
def axis_login(request):
    return_param={'result':0,'authority':0}
    user = request.POST.get('username', 0)
    psd = request.POST.get('password', 0)
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    try:
        if list(pdData[pdData["username"]==user]["password"]==psd)[0] :
            return_param={'result':1,'authority':list(pdData[pdData["username"]==user]['authority'])[0]}
        else:
            return_param={'result':0,'authority':0}
    except:
        return_param={'result':0,'authority':0}
    return HttpResponse(json.dumps(return_param))
def axis_persional(request):
    a = str(request.POST.get('username', 0))
    b = str(request.POST.get('password', 0))
    c = str(request.POST.get('authority', 0))
    d = str(request.POST.get('name', 0))
    e = str(request.POST.get('address', 0))
    f = str(request.POST.get('charger', 0))
    g = str(request.POST.get('phone', 0))
    h = str(request.POST.get('email', 0))
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    pdData.loc[pdData["username"]==a,"password"]=b
    pdData.loc[pdData["username"]==a,"authority"]=c
    pdData.loc[pdData["username"]==a,"name"]=d
    pdData.loc[pdData["username"]==a,"address"]=e
    pdData.loc[pdData["username"]==a,"charger"]=f
    pdData.loc[pdData["username"]==a,"phone"]=g
    pdData.loc[pdData["username"]==a,"email"]=h
    totojson(pdData,file_name,2)
    return_param={"result": "1"}
    return HttpResponse(json.dumps(return_param))
def axis_xgmm(request):
    a = str(request.POST.get('username', 0))
    b = str(request.POST.get('password', 0))
    c = str(request.POST.get('authority', 0))
    d = str(request.POST.get('name', 0))
    e = str(request.POST.get('address', 0))
    f = str(request.POST.get('charger', 0))
    g = str(request.POST.get('phone', 0))
    h = str(request.POST.get('email', 0))
    file_name=os.path.dirname(os.path.abspath('__file__'))+"\\statics\\html\\data\\login.json"
    data = open(file_name,'r',encoding='utf-8')
    jsonData = json.load(data)
    pdData=pd.DataFrame(jsonData)
    pdData.loc[pdData["username"]==a,"password"]=b
    pdData.loc[pdData["username"]==a,"authority"]=c
    pdData.loc[pdData["username"]==a,"name"]=d
    pdData.loc[pdData["username"]==a,"address"]=e
    pdData.loc[pdData["username"]==a,"charger"]=f
    pdData.loc[pdData["username"]==a,"phone"]=g
    pdData.loc[pdData["username"]==a,"email"]=h
    totojson(pdData,file_name,2)
    return_param={"result": "1"}
    return HttpResponse(json.dumps(return_param))