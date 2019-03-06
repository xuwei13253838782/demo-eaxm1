# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json
from home_application.utils.ESB import ESBApi



#
#
# def dev_guide(request):
#     """
#     开发指引
#     """
#     return render_mako_context(request, '/home_application/dev_guide.html')
#
#
# def contactus(request):
#     """
#     联系我们
#     """
#     return render_mako_context(request, '/home_application/contact.html')


def test_exam(request):
    '''
    测试
    :param request:
    :return:
    '''
    return render_json(
        {
            'name': request.user.username,
            'test': 'demo-eaxm',
            'message': 'success'
        }
    )

def home(request):
    """
    首页
    """

    return render_mako_context(request, '/home_application/index.html')




def get_ip(request):
    bk_biz_id = request.GET.get('get_app_id')
    res = {
        'data': [],
        'result': False
    }
    get_ip = []
    get_ip_list = ESBApi(request).search_host(bk_biz_id)
    get_ip_list1 = get_ip_list['data']['info']
    for ip in get_ip_list1:
        re = {}
        re['id'] = ip['host']['bk_host_id']
        re['ip'] = ip['host']['bk_host_innerip']
        re['system'] = ip['host']['bk_os_name']
        re['cloudID'] = ip['host']['bk_cloud_id'][0]['id']
        get_ip.append(re)
    res['data'] = get_ip
    res['result'] = True
    print res
    return render_json(res)

def get_job(request):
    bk_biz_id = request.GET.get('get_app_id')
    res = {
        'data': [],
        'result': False
    }
    get_job = []
    get_job_list = ESBApi(request).get_job_list(bk_biz_id)
    get_job_list1 = get_job_list['data']
    for job in get_job_list1:
        re = {}
        re['id'] = job['bk_job_id']
        re['name'] = job['name']
        get_job.append(re)
    res['data'] = get_job
    res['result'] = True
    return render_json(res)
#
def task(request):
    """
    执行任务
    """
    res = {}
    get_app = []
    app_list = ESBApi(request).get_app_by_user()
    app_list1 = app_list['data']
    for app in app_list1:
        re = {}
        re['id'] = app['ApplicationID']
        re['name'] = app['ApplicationName']
        get_app.append(re)
    return render_mako_context(request, '/home_application/task.html', {'get_app': get_app})


def task_record(request):
    """
    任务记录
    """
    get_app = []
    app_list = ESBApi(request).get_app_by_user()
    app_list1 = app_list['data']
    for re_name in app_list1:
        re = {}
        re['id'] = re_name['ApplicationID']
        re['name'] = re_name['ApplicationName']
        get_app.append(re)
    get_user = []
    get_user_list = ESBApi(request).get_all_users()
    get_user_list1 = get_user_list['data']
    for user in get_user_list1:
        re = {}
        print user['bk_username']
        re['name'] = user['bk_username']
        get_user.append(re)
    return render_mako_context(request, '/home_application/record.html',{'get_app': get_app, 'get_user': get_user})
