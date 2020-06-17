from django.shortcuts import render
import os
import json
import subprocess
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
       
        check_images = False

        images_json = os.popen('curl --unix-socket /var/run/docker.sock http:/v1.24/images/json').readlines()[0]

        images_list = json.loads(images_json.strip())
        for each_image_dict in images_list:
            if image in each_image_dict['RepoTags']:
                check_images = True
                break
        if check_images == False:
            os.system('docker pull '+image)

        # build_cmd = "curl --unix-socket /var/run/docker.sock -H"+' "Content-Type: application/json"'+" -d '{"+'"Image"'+':"'+image+'",'+' "Cmd":"'+ command+'"'+"}' -X POST http:/v1.24/containers/create"
        print(command)
        build_cmd = "docker run -idt "+ image+ " "+ command
        tmp = os.popen(build_cmd).readlines()[0]
        tmp_deal = tmp.strip()
        
        
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
        name = ((os.popen('docker ps -l').readlines()[1].strip()).split())[-1]
        idNow = ((os.popen('docker ps -l').readlines()[1].strip()).split())[0]
        # os.system('docker start -i '+ tmp_ctx['name'])
        cmd = 'docker exec -i '+name+' '+command
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

    return render(request, "reaction.html",ctx)
