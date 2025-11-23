#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    nianling=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    mima=VARCHAR
    shoujihaoma=VARCHAR
    xingbie=VARCHAR
    nianling=Integer
    touxiang=Text
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class medicaldata(BaseModel):
    __doc__ = u'''medicaldata'''
    __tablename__ = 'medicaldata'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    huanzhe=models.CharField ( max_length=255, null=True, unique=False, verbose_name='患者ID' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    nianling=models.CharField ( max_length=255, null=True, unique=False, verbose_name='年龄' )
    shengao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='身高' )
    tizhong=models.FloatField   (  null=True, unique=False, verbose_name='体重' )
    tizhizhishu=models.FloatField   (  null=True, unique=False, verbose_name='体质指数(BMI)' )
    smokingstatus=models.CharField ( max_length=255, null=True, unique=False, verbose_name='吸烟状况' )
    drinkingfrequency=models.CharField ( max_length=255, null=True, unique=False, verbose_name='饮酒频率' )
    yundongpinlv=models.CharField ( max_length=255, null=True, unique=False, verbose_name='运动频率' )
    rijunyundongliang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='日均运动量' )
    eatinghabits=models.CharField ( max_length=255, null=True, unique=False, verbose_name='饮食习惯' )
    shuimianshizhang=models.IntegerField  (  null=True, unique=False, verbose_name='睡眠时长' )
    xueya=models.CharField ( max_length=255, null=True, unique=False, verbose_name='血压' )
    xinlv=models.IntegerField  (  null=True, unique=False, verbose_name='心率' )
    bloodsugarlevel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='血糖水平' )
    danguchunshuiping=models.FloatField   (  null=True, unique=False, verbose_name='胆固醇水平' )
    diagnosticresults=models.CharField ( max_length=255, null=True, unique=False, verbose_name='诊断结果' )
    zhiliaofangan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='治疗方案' )
    suozaidiqu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='所在地区' )
    environmentalpollutionindex=models.FloatField   (  null=True, unique=False, verbose_name='环境污染指数' )
    yiliaoziyuan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='医疗资源分布' )
    jiuzhencishu=models.IntegerField  (  null=True, unique=False, verbose_name='就诊次数' )
    zhuyuanshizhang=models.IntegerField  (  null=True, unique=False, verbose_name='住院时长' )
    yichuanyinsu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='遗传因素' )
    xinlijiankang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='心理健康状况' )
    shehuijingji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='社会经济状态' )
    zhiyeleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职业类型' )
    jiaoyushuiping=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教育水平' )
    jibingjinzhan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='疾病进展状态' )
    shenghuofangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='生活方式改变' )
    yimiaojiezhongshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='疫苗接种史' )
    jiazubingshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='家族病史' )
    '''
    huanzhe=VARCHAR
    xingbie=VARCHAR
    nianling=VARCHAR
    shengao=VARCHAR
    tizhong=Float
    tizhizhishu=Float
    smokingstatus=VARCHAR
    drinkingfrequency=VARCHAR
    yundongpinlv=VARCHAR
    rijunyundongliang=VARCHAR
    eatinghabits=VARCHAR
    shuimianshizhang=Integer
    xueya=VARCHAR
    xinlv=Integer
    bloodsugarlevel=VARCHAR
    danguchunshuiping=Float
    diagnosticresults=VARCHAR
    zhiliaofangan=VARCHAR
    suozaidiqu=VARCHAR
    environmentalpollutionindex=Float
    yiliaoziyuan=VARCHAR
    jiuzhencishu=Integer
    zhuyuanshizhang=Integer
    yichuanyinsu=VARCHAR
    xinlijiankang=VARCHAR
    shehuijingji=VARCHAR
    zhiyeleixing=VARCHAR
    jiaoyushuiping=VARCHAR
    jibingjinzhan=VARCHAR
    shenghuofangshi=VARCHAR
    yimiaojiezhongshi=VARCHAR
    jiazubingshi=VARCHAR
    '''
    class Meta:
        db_table = 'medicaldata'
        verbose_name = verbose_name_plural = '医疗数据'
class medicaldataforecast(BaseModel):
    __doc__ = u'''medicaldataforecast'''
    __tablename__ = 'medicaldataforecast'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    smokingstatus=models.CharField ( max_length=255, null=True, unique=False, verbose_name='吸烟状况' )
    drinkingfrequency=models.CharField ( max_length=255, null=True, unique=False, verbose_name='饮酒频率' )
    eatinghabits=models.CharField ( max_length=255, null=True, unique=False, verbose_name='饮食习惯' )
    bloodsugarlevel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='血糖水平' )
    environmentalpollutionindex=models.CharField ( max_length=255, null=True, unique=False, verbose_name='环境污染指数' )
    diagnosticresults=models.CharField ( max_length=255, null=True, unique=False, verbose_name='诊断结果' )
    '''
    smokingstatus=VARCHAR
    drinkingfrequency=VARCHAR
    eatinghabits=VARCHAR
    bloodsugarlevel=VARCHAR
    environmentalpollutionindex=VARCHAR
    diagnosticresults=VARCHAR
    '''
    class Meta:
        db_table = 'medicaldataforecast'
        verbose_name = verbose_name_plural = '预测数据'
