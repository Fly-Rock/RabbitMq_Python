#coding=UTF-8
from flask import Flask,jsonify
from flask import request


"""
trade/v1.1/groupbuy
POST
"""

app = Flask(__name__)

"""
B端：单个拼团活动的所有参团人数列表
"""

user_list = {
    "status": 0,
    "message": "success",
    "time": "",
    "data": {
        "items": [
            {
                "userId": 23051038,
                "userName": "ejni",
                "nickName": "nickname",
                "userAvatar": "http://f1.ct.hjfile.cn/image/group/201708/051320578626738.png",
                "joinTime": ""
            }
        ],
        "total": 2123
    }
}

"""
B端：单个拼团活动的单个子团参团人数列表
"""

child_user_list = {
    "status": 0,
    "message": "success",
    "time": "",
    "data": {
        "items": [
            {
                "userId": 23051038,
                "userName": "ejni",
                "nickName": "nickname",
                "userAvatar": "http://f1.ct.hjfile.cn/image/group/201708/051320578626738.png"

            }
        ],
        "total": 2123
    }
}

order_info = {
    "status": 0,
    "message": "success",
    "time": "",
    "data": {
        "groupId": 82139653,
        "isOffShelve": false,
        "isOrg": false,
        "orderId": 12996382,
        "orderImg": "http://f1.ct.hjfile.cn/image/group/201709/271456499144ef2.png",
        "orderTime": "2017-09-27T16:13:41+0800",
        "orderTitle": "测试-Python基础学习",
        "orgId": 50000024,
        "payStatus": 2,
        "payTime": "2017-09-27T16:13:58+0800",
        "price": "",
        "orgName": "",
        "teachUserId": 1222,
        "showId": 82139653,
        "childGroupLeaderId": 1222,
        "startTime": "",
        "endTime": "",
        "groupMemberCount": 12222,
        "minMemberCount": 122,
        "groupTime": ""
    }
}




@app.route("trade/v1.1/groupbuy/add",methods=["GET"])
def teacher_group_add():

    group_buy_req = {
        "groupId":12223,
        "activityImage":"",
        "activityPrice":"99.99",
        "minMemberCount":10,
        "startTime":"",
        "endTime":""
    }

    response_buy = {
        "status":0,
        "message":"success",
        "time":"",
        "data":{
            "activityId":"1223"
        }
    }

print(group_buy_req)

"""
trade/v1.1/groupbuy/list?type={type}&pageNo={pageNo}&pageSize={pageSize}
GET
"""
@app.route("trade/v1.1/groupbuy/list",methods=["GET"])
def teacher_group_list():

    teacher_group_list = {
        "status": 0,
        "message": "",
        "time": "",
        "data": {
            "items":[
                {
                    "activityId": "5000000",
                    "activityName": "拼团活动名称",
                    "groupId": 12222,
                    "memberCount": 122,
                    "activityPrice": "2.90",
                    "productPrice": "5.00",
                    "minMemberCount": 1,
                    "startTime": "",
                    "endTime": "",
                    "activityImage": "https://cc.hjfile.cn/cc/g/2017/8/8/2017080808355895665486.jpg"
                }
            ],
            "total":233
        }
    }
    return jsonify(teacher_group_list)


"""
拼团详细页面调用接口：
/trade/v1.1/groupbuy/{id}?childId={childId}&childMemberLimit={limit}&intro={intro}
该接口用在三个页面上面：
拼团主活动页面需要调用接口：/trade/v1.1/groupbuy/{id}?childMemberLimit=1&intro=1
单个小团分享页面:/trade/v1.1/groupbuy/{id}?childId={childId}&childMemberLimit=3&intro=1
单个小团状态页面不要群简介信息：/trade/v1.1/groupbuy/{id}?childId={childId}&childMemberLimit=0&intro=0
###成员数量和 单团信息 不一样

"""
@app.route("/trade/v1.1/groupbuy/5000000",methods=["GET"])
def getActivity():
    activityRespone = {
        "status": 0,
        "message": "",
        "time": "",
        "data": {
            "activityId": "5000000",
            "activityName": "活动名称",
            "activityImage": "https://cc.hjfile.cn/cc/g/2017/8/8/2017080808355895665486.jpg",
            "activityPrice": "99.99",
            "productPrice": "999.99",
            "minMemberCount": 10,
            "memberCount": 3,
            "buyMemberCount": 2,
            "groupId": 81956935,
            "startTime": "2017-10-08T20:36:01+0800",
            "endTime": "2017-11-08T20:36:01+0800",
            "intro": {
                "contentId": "81956935",
                "section": [
                    {
                        "contentStruct": {
                            "img": [
                                {
                                    "height": 343,
                                    "ref": "[!--IMG#0--]",
                                    "src": "https://cc.hjfile.cn/cc/g/2017/8/8/2017080808355895665486.jpg",
                                    "width": 800
                                }
                            ],
                            "txt": [
                                {
                                    "ref": "[!--TXT#0--]",
                                    "text": "大家好，我是一名语文老·师兼国学爱好者。希望传承国学之美，希望帮助大家找到高中语文学习的正确途径"
                                }
                            ]
                        },
                        "contents": [
                            {
                                "ref": [
                                    "[!--TXT#0--]"
                                ],
                                "type": "txt"
                            },
                            {
                                "ref": [
                                    "[!--IMG#0--]"
                                ],
                                "type": "img"
                            }
                        ]
                    }
                ]
            },
            "userOrderStatus": 0,
            "joinChildGroupId": "F0001",
            "productUserInfo": {
                "userId": 75904638,
                "userName": "jerry",
                "nickName": "jerry_nick",
                "userAvatar": "http://f1.ct.hjfile.cn/image/group/201708/051320578626738.png"
            },
            "childGroupItems": [
                {
                    "memberCount": 1,
                    "minMemberCount": 10,
                    "isLeader": True,
                    "userId": 23051038,
                    "userName": "ejni",
                    "nickName":"nick",
                    "userAvatar": "http://f1.ct.hjfile.cn/image/group/201708/051320578626738.png"
                }
            ]
        }
    }
    data = {

        "name":"ddd"
    }
    return jsonify(activityRespone)

#/im/v1.1/group/{groupId}/activity_list


@app.route("/im/v1.1/group/81956935/activity_list",methods=["GET"])
def activity_list():

    """
    /im/v1.1/group/{groupId}/activity_list
    非鉴权
    """
    activity_list = {
        "data": [
            {
                "activityId": "5000000",
                "type": 1
            }
        ],
        "message": "",
        "time": "",
        "status": 0
    }
    return jsonify(activity_list)

if __name__ == "__main__":
    app.run('172.16.12.165',8090)


