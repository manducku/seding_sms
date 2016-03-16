#kth sms API를 활용한 파이썬 모듈 
import requests
def enrollNumber(sendnumber, comment, api_version, client_id, header_code): #발신 번호 등록
    url = "http://api.openapi.io/ppurio/{api_version}/sendnumber/save/{client_id}".format(
    api_version = api_version,
    client_id = client_id, 
    )

    header = {
        'x-waple-authorization': header_code,
    }

    data = {
            'sendnumber': sendnumber,
            'comment': comment,
            }
    r = requests.post(
            url,
            data = data, 
            headers = header,
            )
    
    print(r.status_code, r.content)

    if(r.status_code == 200):
       print(r.json())

def sendingSMS(send_phone, dest_phone, msg_body, api_version, client_id, header_code):  #메시지 보내기
    url = "http://api.openapi.io/ppurio/{api_version}/message/sms/{client_id}".format(
            api_version = api_version,
            client_id = client_id,
            )
    header = {
            'x-waple-authorization':header_code,
            }

    data = {
            'send_phone': send_phone,
            'dest_phone': dest_phone,
            'msg_body': msg_body,
            }

    r = requests.post(
            url,
            headers = header,
            data = data, 
            )

    print (r.status_code)


    if(r.status_code == 200):
        print(r.json())

