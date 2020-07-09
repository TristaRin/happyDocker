from django.shortcuts import render
from shellescape import quote
import os
import json
import docker

tmp_ctx = {}
def hello_world(request):
    response = render(request, 'hello_world.html',{})
    return response
# Create your views here.

def manage(request) :
    global tmp_ctx
    ctx ={}
    if request.POST:
        # 拿到計算所需的參數
        image = request.POST['image']
        command = request.POST['command']
        # name = request.POST['name']
        if '&' in command:
            ctx['status'] = 'Invalid input'
            return render(request, "manage.html", ctx)
        check_images = False

        images_json = os.popen('curl --unix-socket /var/run/docker.sock http:/v1.24/images/json').readlines()[0]

        images_list = json.loads(images_json.strip())
        try:
            for each_image_dict in images_list:
                if image in each_image_dict['RepoTags']:
                    check_images = True
                    break
        except TypeError:
            # 處理 none 字串問題
            os.system('docker images -f "dangling=true" -q')
            for each_image_dict in images_list:
                if image in each_image_dict['RepoTags']:
                    check_images = True
                    break
        print(check_images)
        if check_images == False:
            # quote : shellescape
            os.system('docker pull '+quote(image))
        try:

            build_cmd = "docker run -idt "+ quote(image) + " "+ quote(command)
            tmp = os.popen(build_cmd).readlines()[0]
            tmp_deal = tmp.strip()
        except:
            ctx['image'] = image
            ctx['command'] = command
            ctx['name'] = ''

            ctx['id'] = ''
            ctx['status'] = 'Fail'
            return render(request, "manage.html", ctx)
        try:
            id_cmd = tmp_deal[0:12]
            search = os.popen('docker ps -a | grep "'+ id_cmd +'"').readlines()[0]

            search_name = search.split()[-1]
        
            ctx['image'] = image
            ctx['command'] = command
            ctx['name'] = search_name

            ctx['id'] = id_cmd
            ctx['status'] = 'Success'
            tmp_ctx = ctx
        except:
            
            ctx['image'] = image
            ctx['command'] = command
            ctx['name'] = ''

            ctx['id'] = ''
            ctx['status'] = 'Fail'

    return render(request, "manage.html", ctx)

def react(request) :
    ctx = {}
    if request.POST:
        # 拿到計算所需的參數
        command = request.POST['command']
        tmp_for_all = os.popen('docker ps -a').readlines()
        # name = request.POST['name']
        # 抓最新的執行
        name = ((os.popen('docker ps -l').readlines()[1].strip()).split())[-1]
        idNow = ((os.popen('docker ps -l').readlines()[1].strip()).split())[0]
        # os.system('docker start -i '+ tmp_ctx['name'])
        cmd = 'docker exec -i '+ name +' '+ quote(command)
        try:
            tmp = os.popen(cmd).readlines()
            ctx['id'] = idNow
            ctx['name'] = name
            ctx['statusCMD'] = 'Success'
            ctx['output'] = ''.join(tmp)
            ctx['allContainer'] = ''.join(tmp_for_all)
        except:
            ctx['status'] = 'Fail'
            ctx['output'] = 'No output'
            ctx['allContainer'] = '\n'+''.join(tmp_for_all)
        print(ctx)
    else:
        print('No Request')
    return render(request, "reaction.html",ctx)
def reactionStop(request) :
    ctx = {}
    if request.POST:
        # 拿到計算所需的參數
        stop = request.POST['stop']
        
        tmp = os.popen('docker stop '+ quote(stop)).readlines()   
        tmp_for_all = os.popen('docker ps -a').readlines()
        try:
            if stop == tmp[0].strip():
            # 成功停止
                ctx['statusStop'] = 'Success'
                ctx['id'] = ''
                ctx['name'] = ''
                ctx['statusCMD'] = ''
                ctx['output'] = ''
                ctx['allContainer'] = ''.join(tmp_for_all)
            else:
                ctx['statusStop'] = 'Fail'
                ctx['status'] = ''
                ctx['output'] = 'No output'
                ctx['allContainer'] = '\n'+''.join(tmp_for_all)
        except:
            ctx['statusStop'] = 'Fail'
            ctx['status'] = ''
            ctx['output'] = 'No output'
            ctx['allContainer'] = '\n'+''.join(tmp_for_all)

    return render(request, "reaction.html",ctx)

def prune(request):
    ctx = {}
    os.system('docker container prune')
    os.system('y')
    tmp_for_all = os.popen('docker ps -a').readlines()
    ctx['allContainer'] = '\n'+''.join(tmp_for_all)
    return render(request, "reaction.html",ctx)