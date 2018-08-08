import itchat,time
from matplotlib import pyplot as plt 

Wchat = itchat.auto_login(hotReload=True)

def WechatFriends():
    friends = itchat.get_friends()[1:]
    boy=0
    girl=0
    friend_count=0
    for i in friends:
#         print("NickName对应的内容是别人的名字:", i["NickName"])
#         print("RemarkName对应的内容是你给别人的备注:", i["RemarkName"])
#         print("Signature对应的内容是别人的个性签名:", i["Signature"])
#         print("City对应的是别人的城市:", i["City"])
#         print("Sex对应的是好友的性别:", i["Sex"])
        if i["Sex"]==2:
            girl+=1
        else:
            boy+=1
        friend_count+=1
#     print(friend_count)
    return friend_count,boy,girl
# print("总：",friend_count)
# print("男：",boy)
# print("女：",girl)

# 好友数量统计
friend_count,boy,girl=WechatFriends()
print(friend_count)
print(boy)
print(girl)

def showsex():
    plt.figure(figsize=(6,9))
    labels = [u'男',u'女']
    friend_count,boy,girl=WechatFriends()
    sizes = [boy,girl]
    colors=['lightskyblue','red']
    patches,l_text,p_text = plt.pie(sizes,labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
    for t in l_text:
        t.set_size=(30)
    for t in p_text:
        t.set_size=(20)
# 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()


# showsex()

def ChatroomsAbout(IsDict=False,):
    chatrooms=itchat.get_chatrooms()
    count=len(chatrooms)
    chatrooms_NickName=[]
    chatrooms_dict={}
    for i in range(count):
        chatrooms_NickName.append(chatrooms[i]["NickName"])
        chatrooms_dict.setdefault(chatrooms[i]["NickName"],chatrooms[i]["UserName"])
    #存到通讯录群的数量
    #print(count)
    #存到通讯录群的名称列表
    #print(chatrooms_NickName)
    if IsDict == True:
        return chatrooms_dict
    return count,chatrooms_NickName   

# chatrooms=itchat.get_chatrooms()
# print(chatrooms[1])

#查询对应群名称的username
# list(ChatroomsAbout(True).keys())[1]

def FriendsInformation():
    friends_list=[]
    friends_single={}
    friends = itchat.get_friends()[1:]
    for i in range(len(friends)):
#         friends_single["UserName"]=i["UserName"]
#         friends_single["RemarkName"]=i["RemarkName"]
#         print(friends_single)
#         friends_list.append({"UserName":friends[i]["UserName"],"RemarkName":friends[i]["RemarkName"]})
        friends_single.setdefault(friends[i]["UserName"],friends[i]["RemarkName"])
#     print(friends_list)
    return friends_single

# # FriendsInformation()
# # 查询好友username对应的自己昵称

# print(FriendsInformation()["@ca423b595ef76eb4077e5b3d61cfffae222f47f3a80bb066008c48aa0cccef3f"])

# FriendsInformation_dict=FriendsInformation()
# print(FriendsInformation_dict)

def RoomMemberList(name):
    memberList = itchat.update_chatroom(name, detailedMember=True)
    return memberList["MemberList"]

def MembersInformation(memberlist):
    friends_single={}
    for i in range(len(memberlist)):
#         friends_single["UserName"]=i["UserName"]
#         friends_single["RemarkName"]=i["RemarkName"]
#         print(friends_single)
#         friends_list.append({"UserName":friends[i]["UserName"],"RemarkName":friends[i]["RemarkName"]})
        friends_single.setdefault(memberlist[i]["UserName"],memberlist[i]["NickName"])
#     print(friends_list)
    return friends_single
# # 返回群某个群所有用户信息
# Room_Members=RoomMemberList("@@54b8c51bd4f9a098edd7b40e6f8664fe04c8b261de338de09bd1a90b1de994f5")
# Room_Members_dict=MembersInformation(Room_Members)
# print(Room_Members_dict)

def RoomMembersInformation(RoomUserName):
    Room_Members=RoomMemberList(RoomUserName)
    Room_Members_dict=MembersInformation(Room_Members)
    return Room_Members_dict

def IsRoomMemberInFriend(RoomMembersInformation_dict,FriendsInformation_dict):
    Friends_count=0
    Friends_member=[]
    NoFriends_count=-1
    NoFriends_member=[]
    for d,x in RoomMembersInformation_dict.items():
#         print("key:"+d+",value:"+x)
        if d in FriendsInformation_dict.keys():
#             print("yes")
            Friends_count+=1
            Friends_member.append(FriendsInformation_dict[d])
        else:
            NoFriends_count+=1
            NoFriends_member.append(x)
    return Friends_count,NoFriends_count,Friends_member,NoFriends_member
# IsRoomMemberInFriend(RoomMembersInformation_dict,FriendsInformation_dict)

def test(Room_username):
#     Room_usernameList=ChatroomsAbout(True)
#     print(Room_username)
    RoomMembers_dict=RoomMembersInformation(Room_username)
#     print(RoomMembers_dict)
    Friend_dict=FriendsInformation()
    Friends,NoFriends,Member_friends,Member_Nofriends=IsRoomMemberInFriend(RoomMembers_dict,Friend_dict)
    print("共有："+str(len(RoomMembers_dict))+"人")
    
    print("好友："+str(Friends))
    print("非好友："+str(NoFriends))
    print("好友为："+str(Member_friends))
    print("非好友为："+str(Member_Nofriends))

def RoomShow():
    chatrooms=ChatroomsAbout(True)
    count=len(chatrooms)
    chatrooms_NickName=[]
    chatrooms_dict={}
    for i in range(count):
        chatrooms_NickName.append(list(chatrooms.keys())[i])
        chatrooms_dict.setdefault(i,list(chatrooms.values())[i])
        print(str(i)+':'+list(chatrooms.keys())[i])
    #存到通讯录群的数量
    #print(count)
    #存到通讯录群的名称列表
#     print(chatrooms_NickName)
    while True:
        k=input("群聊编号:\n")
        try:
            print(chatrooms_NickName[int(k)])
            test(chatrooms_dict[int(k)])
        except:
            break
#     return chatrooms_dict 
RoomShow()

