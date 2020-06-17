from django.shortcuts import render
def hello_world(request):
    response = render(request, 'hello_world.html',{})
    return response
# Create your views here.

def manage(request) :
    ctx ={}
    if request.POST:
        # 拿到計算所需的參數
        test = request.POST['test']
        # modelsStr  = request.POST['路徑模式'].split(',')

        # n = int(request.POST['初代數量'])
        # growthCap = int(request.POST['族群最大數量'])
        # lowerLimit = int(request.POST['族群最小數量'])
        # iterationsNum = int(request.POST['演化次數'])
        # mutCap = int(request.POST['突變最多次數'])

        # goodDNA, stepList, qualityList, spendTime = ga.myGA(unitsStr, modelsStr, n, growthCap, iterationsNum, lowerLimit, mutCap)

        ctx['test'] = test
        # ctx['lowerLimit'] = lowerLimit
        # ctx['iterationsNum'] = iterationsNum
        # ctx['mutCap'] = mutCap


        # ctx['goodDNA'] = goodDNA
        # ctx['goodStep'] = min(stepList)
        # ctx['goodQuality'] = max(qualityList)
        # ctx['spendTime'] = spendTime
        # stepList = map(str, stepList)
        # qualityList = map(str, qualityList)
        # ctx['stepList'] = str(','.join(stepList))
        # ctx['qualityList'] = str(','.join(qualityList))

    # Repeat a few rounds
    return render(request, "manage.html", ctx)
