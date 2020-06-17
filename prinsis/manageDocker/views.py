from django.shortcuts import render
import os
import json
import subprocess
def hello_world(request):
    response = render(request, 'hello_world.html',{})
    return response
# Create your views here.

def manage(request) :
    ctx ={}
    if request.POST:
        # 拿到計算所需的參數
        image = request.POST['image']
        command = request.POST['command']
        name = request.POST['name']
       

        check_images = False

        images_json = subprocess.Popen('curl --unix-socket /var/run/docker.sock http:/v1.24/images/json').stdout
        images_list = json.loads(images_json.strip())
        for each_image_dict in images_list:
            if image in each_image_dict.['RepoTags']:
                check_images = True
        if check_images:
            os.system('docker pull '+image)

        build_cmd = "curl --unix-socket /var/run/docker.sock -H"+' "Content-Type: application/json"'+" -d '{"+'"Image"'+':"'+image+'",'+' "Cmd":"'+ command+'"'+"}' -X POST http:/v1.24/containers/create"
        
        tmp = os.popen(build_cmd).readlines()[0]
        tmp_deal = eval(tmp.strip())
        tmp_dict = {}
        tmp_dict = tmp_deal
        print(tmp_dict)
        
        id_cmd = tmp_dict['Id'][0:12]
        search = 'docker ps -a | grep "'+ id_cmd +'"'

        search_name = search.split()[-1]

        ctx['image'] = image
        ctx['command'] = command
        ctx['name'] = name

        ctx['id'] = tmp_dict['Id'][0:12]
        ctx['status'] = search_name


        # ctx['lowerLimit'] = lowerLimit

        # ctx['goodStep'] = min(stepList)
        # ctx['goodQuality'] = max(qualityList)
        # stepList = map(str, stepList)
        # ctx['qualityList'] = str(','.join(qualityList))

    # Repeat a few rounds
    return render(request, "manage.html", ctx)
