import hashlib
from datetime import date
import datetime
from http.client import HTTPResponse
# from turtle import pd
import uuid
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from bson import ObjectId
import requests
import os
import json
import json
import random
import string
import random
from Rkdfuniversity.settings import userdb
from  easebuzz_lib.easebuzz_payment_gateway import Easebuzz
# Create your views here.



MERCHANT_KEY = "FB3LFRTFVW" 
SALT ="EWU97KQ2RA"
ENV = "prod"


def Student_data(request):
    try:
        if request.method == "POST":

            Data = {
                'enrollmentNo': request.POST.get('enrollmentNo'),
                'firstname': request.POST.get('firstname').replace("(", "").replace(")", "").replace("'", ""),
                'FatherName': request.POST.get('FatherName').replace("'", ""),
                'Course': request.POST.get('Course').replace("(", "").replace(")", "").replace("'", ""),
                'feeType': request.POST.get('feeType'),
                'phone': request.POST.get('phone'),
                'productinfo':"yes",
                'email': 'info@gmail.com',
                'surl': "https://rkdf.payjix.com/" ,
                'furl': "https://rkdf.payjix.com/",
                'udf3': "yes",
                'udf4': "yes",
                'udf5': "yes",
                'address1': "Feeszone Bhopal",
                'address2': "Feeszone Bhopal",
                'city': "Indore",
                'state':"MP",
                'country': "India",
                'zipcode': "452006",
                'amount':  request.POST.get('amount'),
            }
            createdOn = datetime.datetime.now()
            txnid = Data['firstname'].strip().replace(' ', '_')+"_"+str(Data['phone']
                                                      ).replace('/', '_')+"_"+str(random.randint(1000, 9999))
            MercUnqRef = Data['firstname'].replace(' ', '_')+"_"+"_" + \
                str(Data['phone']).replace('/', '_') + \
                "_"+str(random.randint(1000, 9999))
            orderId = Data['firstname'].strip()+"_" + str(
                Data['phone']).replace('/', '_')+"_"+str(random.randint(1000, 9999))
            amount = Data['amount']
            print("amount", amount)
            payment_page = {
                
                'enrollmentNo': request.POST.get('enrollmentNo'),
                'firstname': request.POST.get('firstname').replace("(", "").replace(")", "").replace("'", ""),
                'FatherName': request.POST.get('FatherName').replace("'", ""),
                'Course': request.POST.get('Course').replace("(", "").replace(")", "").replace("'", ""),
                'feeType': request.POST.get('feeType'),
                'createdOn': createdOn,
                "amount": amount,
                'phone': request.POST.get('phone'),
                'txnid': txnid,
                'MercUnqRef': MercUnqRef,
                'orderId': orderId,
                'productinfo':"yes",
                'email': 'info@gmail.com',
                'surl': "https://rkdf.payjix.com/response/" ,
                'furl': "https://rkdf.payjix.com/response/",
                'udf3': "yes",
                'udf4': "yes",
                'udf5': "yes",
                'address1': "Feeszone Bhopal",
                'address2': "Feeszone Bhopal",
                'city': "Indore",
                'state':"MP",
                'country': "India",
                'zipcode': "452006",
                
            }
            print("-------payment_page-------",payment_page)
            userdb.Student.insert(payment_page)

                    
            return render(request, 'existingindex.html',payment_page)                
        return render(request,'existingform.html')
    
    except Exception as e:
        return render(request,'existingform.html')
def firstpage(request):
    return render(request,'first.html')  

easebuzzObj = Easebuzz(MERCHANT_KEY, SALT, ENV)

def studentregistration(request):
    
    try:
        if request.method == 'POST': 
            print("-------------request.POST--studentregistration----",request.POST)
            Data = {
                
                'firstname': request.POST.get('firstname'),
                'FatherName': request.POST.get('FatherName'),
                'Course': request.POST.get('Course'),
                'feeType': request.POST.get('feeType'),
                'phone': request.POST.get('phone'),
                'productinfo':"yes",
                'email': 'info@gmail.com',
                'surl': "https://rkdf.payjix.com/" ,
                'furl': "https://rkdf.payjix.com/",
                'udf3': "yes",
                'udf4': "yes",
                'udf5': "yes",
                'address1': "Feeszone Bhopal",
                'address2': "Feeszone Bhopal",
                'city': "Indore",
                'state':"MP",
                'country': "India",
                'zipcode': "452006",
                'amount':  request.POST.get('amount'),
            }
            createdOn = datetime.datetime.now()
            txnid = Data['firstname'].strip().replace(' ', '_')+"_"+str(Data['phone']
                                                      ).replace('/', '_')+"_"+str(random.randint(1000, 9999))
            MercUnqRef = Data['firstname'].replace(' ', '_')+"_"+"_" + \
                str(Data['phone']).replace('/', '_') + \
                "_"+str(random.randint(1000, 9999))
            orderId = Data['firstname'].strip()+"_" + str(
                Data['phone']).replace('/', '_')+"_"+str(random.randint(1000, 9999))
            amount = Data['amount']
            print("amount", amount)
            payment_page = {
                
                'firstname': request.POST.get('firstname'),
                'FatherName': request.POST.get('FatherName'),
                'Course': request.POST.get('Course'),
                'feeType': request.POST.get('feeType'),
                'createdOn': createdOn,
                "amount": amount,
                'phone': request.POST.get('phone'),
                'txnid': txnid,
                'MercUnqRef': MercUnqRef,
                'orderId': orderId,
                'productinfo':"yes",
                'email': 'info@gmail.com',
                'surl': "https://rkdf.payjix.com/response/" ,
                'furl': "https://rkdf.payjix.com/response/",
                'udf3': "yes",
                'udf4': "yes",
                'udf5': "yes",
                'address1': "Feeszone Bhopal",
                'address2': "Feeszone Bhopal",
                'city': "Indore",
                'state':"MP",
                'country': "India",
                'zipcode': "452006",
                
            }
            print("-------payment_page-------",payment_page)
            userdb.Student.insert(payment_page)
            return render(request, 'index.html', payment_page)
        else:
            return render(request, "studentregistration.html")

    except Exception as e:
        print('----311----', e)
        return render(request, "studentregistration.html")
    
@csrf_exempt
def response(request):
    final_response = easebuzzObj.easebuzzResponse(request.POST)
    data = json.loads(final_response)
    print("----response -failled---",data)
    # if data['status'] == 0:
    #     print("----response -failled---",data)
    #     return render(request, 'paymentfail.html')
    # User cancelled the UPI transaction  Transaction Not Permitted to CardHolder  
    
    # userdb.erroreventpayment.insert_one(data)  
    data['data'] = {'name_on_card': 'NA', 'bank_ref_num': '415086126830', 'udf3': 'Tuition fee', 'hash': '865510738347a8548acf87cc57049b7135e4c3efe83c551acf9329b711e3ed6062804b30b6c46b893531aea1da0795517e5b3deb350faee40c73e930781f7165', 'firstname': 'ASHMIT CHOUBEY', 'net_amount_debit': '12500.0', 'payment_source': 'Easebuzz', 'surl': 'https://srg.payjix.com/response/', 'error_Message': 'APPROVED OR COMPLETED SUCCESSFULLY', 'issuing_bank': 'NA', 'cardCategory': 'NA', 'phone': '0000000000', 'easepayid': 'E240529UDW85R3', 'cardnum': 'NA', 'key': '6G06V4OQ6O', 'udf8': '', 'unmappedstatus': 'NA', 'PG_TYPE': 'NA', 'addedon': '2024-05-29 07:00:30', 'cash_back_percentage': '50.0', 'status': 'success', 'card_type': 'UPI', 'merchant_logo': 'https://s3.ap-southeast-1.amazonaws.com/easebuzz/pay.easebuzz.in/logo/131993/iZtpKldP.jpeg', 'udf6': '', 'udf10': '', 'upi_va': 'ashmitchoubey-1@okhdfcbank', 'txnid': 'ASHMIT_CHOUBEY_460073_7059', 'productinfo': 'Apple', 'bank_name': 'NA', 'furl': 'https://srg.payjix.com/response/', 'udf1': 'BALLB', 'amount': '12500.0', 'udf2': 'AJAY CHOUBEY', 'udf5': 'R2301633460073', 'mode': 'UPI', 'udf7': '', 'error': 'APPROVED OR COMPLETED SUCCESSFULLY', 'udf9': '', 'bankcode': 'NA', 'deduction_percentage': '0.0', 'email': 'initiate.payment@easebuzz.in', 'udf4': 'S132452B2JQ'}
    print("-----    --data---",data)
    if data['data']['status'] == "success" or data['data']['error'] == "Successful Transaction" :
        print("----response -success---",data)
        userdb.Student.update(
            {"txnid": data['data']['txnid']}, {"$set": data['data']})
        get_data = userdb.Student.find(
            {"txnid": data['data']['txnid']})
        studentdata = {}
        for i in get_data:
            del i['_id']
            # userdb.successtrans.insert_one(i)
            studentdata.update(i)

        # ProTest.Essobuze.insert_one(data)
        return render(request, 'PDF.html', {'response_data': studentdata})
    else:
        return render(request, 'paymentfail.html')  
    
def initiate_payment(request):

    if request.method == 'POST':
        print("*********",request.POST)
        final_response = easebuzzObj.initiatePaymentAPI(request.POST)
        print("=================", type(final_response))
        result = json.loads(final_response)
        # dat=json.dumps(result)
        print("result-------=-==", type(result))

        if result['status'] == 1:
            print(
                "result['data']result['data'] ----------result['data'] ", result['data'])
            return redirect(result['data'])
        else:
            # ProTest.Essubuze.insert(final_response)
            print("--------+++++++=========", final_response)

            # return HttpResponse(final_response)
            return render(request, 'serverfail.html', {'response_data': final_response})
    else:
        print("yesssssssssssssssssssssss")
        return render(request, 'studentregistration.html')          