from django.shortcuts import render
import os
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
        
        build_cmd = "curl --unix-socket /var/run/docker.sock -H"+' "Content-Type: application/json"'+" -d '{"+'"Image"'+':"'+image+'",'+' "Cmd":"'+ command+'"'+"}' -X POST http:/v1.24/containers/create"

        tmp = os.popen(build_cmd).readlines()[0]
        tmp_deal = eval(tmp.strip())
        tmp_dict = {}
        tmp_dict = tmp_deal
        print(tmp_dict)

        # modelsStr  = request.POST['路徑模式'].split(',')
        # n = int(request.POST['初代數量'])
        # goodDNA, stepList, qualityList, spendTime = ga.myGA(unitsStr, modelsStr, n, growthCap, iterationsNum, lowerLimit, mutCap)

        ctx['image'] = image
        ctx['command'] = command
        ctx['name'] = name

        ctx['id'] = tmp_dict['Id']
        ctx['status'] = tmp_dict['Warnings']


        # ctx['lowerLimit'] = lowerLimit

        # ctx['goodStep'] = min(stepList)
        # ctx['goodQuality'] = max(qualityList)
        # stepList = map(str, stepList)
        # ctx['qualityList'] = str(','.join(qualityList))

    # Repeat a few rounds
    return render(request, "manage.html", ctx)
