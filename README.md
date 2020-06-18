# happyDocker
I'm Docker, and I'm happy!

## Django

1. 遠端佈署+本地端佈署(遠端本地都要做一遍)

    請先確認 python3 版本3.6.9
    然後安裝一些管理套件
    ```
    sudo apt install python3-pip
    pip3 install pipenv
    ```

2. 在本地端建好專案~
    先建一個資料夾叫 myPrj
    對此資料夾創建（或進入）虛擬環境
    再裝個 django
    ```
    mkdir myPrj 
    cd myPrj/
    python3 -m pipenv shell
    pip3 install django==3.0.3
    ```
    建一個 django 專案叫 prinsis
    ```
    django-admin startproject prinsis
    ```
    進入專案、匯入 django sql 、(建管理員)
    ```
    cd prinsis/
    python manage.py migrate
    (python manage.py createsuperuser)
    ```

    若要讓專案可以跑在遠端伺服器上要改一下這個檔案

    ```
    cd prinsis/
    vim settings.py
    ```
    ```python=
    DEBUG = False
    ALLOWED_HOSTS = ['163.22.17.137', 'localhost', '127.0.0.1']
    ```

3. 把本地專案移到遠端伺服器上
    （要先 cd 到放 myPrj 的目錄底下）
    ```
    scp -r myPrj/ s018@163.22.17.137:/home/s018/
    ```


>  FIXME:
sudo ufw allow 8000
sudo ufw deny 8000

4. 可以看小火箭了 
    先進到遠端
    ```
    ssh s018＠163.22.17.137
    cd myPrj/prinsis/
    ```
    在遠端跑的指令長這樣～
    ```
    python manage.py runserver 163.22.17.137:8000
    ```

    請確認你是在虛擬環境中，若不再環境中runserver會以下錯誤
    ![](https://i.imgur.com/pZZGGcq.png)
    正常情況
    ![](https://i.imgur.com/m5AvyHR.png)
    
    ![](https://i.imgur.com/bFqtIYa.png)
    （補充）
    在本地跑的指令長這樣～
    ```
    cd ..
    python manage.py runserver
    ```
5. 終於可以來新增一個 app 了～（咱們先在本地端做）
    在 /myPrj/prinsis 底下建一個 app 叫 manageDocker
    ```
    python manage.py startapp manageDocker
    ```
    修改 /myPrj/prinsis/prinsis 底下的 setting.py
    ```
    cd prinsis/
    vim setting.py
    ```
    
    ```python=
     INSTALLED_APPS = [
         ...
         'manageDocker',                                                         
     ]
     
     ```
     在 /myPrj/prinsis 底下建一個資料夾叫 templates
    ```
    cd ..
    mkdir templates
    
    ```
    修改 /myPrj/prinsis/prinsis 底下的 setting.py

    ```
    cd prinsis/
    vim setting.py 
    ```
    ```python=
    TEMPLATES = [
        {
            ...,
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            ],
            ...
        }
    ]
    ```
    
    ```python=
    LANGUAGE_CODE = 'zh-hant'

    TIME_ZONE = 'Asia/Taipei'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = False
    ```
    修改 /myPrj/prinsis/prinsis 底下的 urls.py
    ```
    vim urls.py
    ```
    ```python=
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('manageDocker/',include('manageDocker.urls')),
    ]
                    
    ```
6. 在這 app 裡面寫些 api
    1. 在 /myPrj/prinsis/manageDocker 底下建一個 urls.py
    ```
    cd ..
    cd manageDocker/
    vim urls.py
    ```
    ```python=
    from django.urls import path, include
    from . import views
    from django.conf.urls import url
    
    urlpatterns = [
        path('hello_world',views.hello_world), 
        url('manage', views.manage),
    ]
    ```
    
    2. 在 /myPrj/prinsis/templates 底下創一個 hello_world.html 和 manage.html
    ```
    cd ..
    cd templates/
    vim hello_world.html
    ```
    ```htmlmixed=
    <!DOCTYPE html>
    <html>
    <head>
        <title></title>
    </head>
    <body>
    Hello World
    </body>
    </html>
    ```
    ```
    vim manage.html
    ```
    （補充）我是用 bootstrap 的 [範例頁面](https://getbootstrap.com/docs/4.5/examples/checkout/) 怎麼用 bootstrap [請參考這](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
    
    ```htmlmixed=
    <!doctype html>
    <html lang="en">
      <head>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
        <meta name="generator" content="Jekyll v4.0.1">
        <title>Checkout example · Bootstrap</title>


        <style>
          .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
          }

          @media (min-width: 768px) {
            .bd-placeholder-img-lg {
              font-size: 3.5rem;
            }
          }
        </style>
        <!-- Custom styles for this template -->
        <link href="form-validation.css" rel="stylesheet">
      </head>
      <body class="bg-light">
        <div class="container">
      <div class="py-5 text-center">
        <img class="d-block mx-auto mb-4" src="/docs/4.5/assets/brand/bootstrap-solid.svg" alt="" width="72" height="72">
        <h2>Build your  docker</h2>
        <p class="lead">This is a happyDocker! Which makes you happy?</p>
      </div>

      <div class="row">
        <div class="col-md-4 order-md-2 mb-4">
          <h4 class="d-flex justify-content-between align-items-center mb-3">
            <span class="text-muted">container info</span>
            <span class="badge badge-secondary badge-pill">{{status}}</span>
          </h4>
          <ul class="list-group mb-3">
            <li class="list-group-item d-flex justify-content-between lh-condensed">
              <div>
                <h6 class="my-0"> id</h6>
              </div>
              <span class="text-muted">{{id}}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between lh-condensed">
              <div>
                <h6 class="my-0">image file</h6>
              </div>
              <span class="text-muted">{{image}}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between lh-condensed">
              <div>
                <h6 class="my-0">command</h6>
              </div>
              <span class="text-muted">{{command}}</span>
            </li>

            <li class="list-group-item d-flex justify-content-between lh-condensed">
              <div>
                <h6 class="my-0">name</h6>
              </div>
              <span class="text-muted">{{name}}</span>
            </li>

          </ul>


        </div>
        <div class="col-md-8 order-md-1">
          <h4 class="mb-3">Input</h4>

          <form class="needs-validation" novalidate action="manage" method="post">{% csrf_token %}

              <div class="col-md-6 mb-3">
                <label for="firstName">image</label>
                <input type="text" class="form-control" id="image"  name="image" placeholder="" value="" required>
                <div class="invalid-feedback">
                  Valid first name is required.
                </div>
              </div>

              <div class="col-md-6 mb-3">
                <label for="firstName">command</label>
                <input type="text" class="form-control" id="command"  name="command" placeholder="" value="" required>
                <div class="invalid-feedback">
                  Valid first name is required.
                </div>
              </div>

            <hr class="mb-4">
            <button class="btn btn-primary btn-lg btn-block" type="submit">Build it!</button>
          </form>
        </div>
      </div>

      <footer class="my-5 pt-5 text-muted text-center text-small">
        <p class="mb-1">&copy; 2020-06-18 prinsis</p>

      </footer>
    </div>

    </body>
    </html>


    
    ```
    (補充)
    django 規定在 form 後面加要 token
    ```
    {% csrf_token %}
    ```
    
    3. 修改/myPrj/prinsis/manageDocker/ 底下的 views.py
    ```
    cd ..
    cd manageDocker/
    vim views.py
    ```
```python=
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
        # name = request.POST['name']
       

        check_images = False

        images_json = os.popen('curl --unix-socket /var/run/docker.sock http:/v1.24/images/json').readlines()[0]

        images_list = json.loads(images_json.strip())
        for each_image_dict in images_list:
            if image in each_image_dict['RepoTags']:
                check_images = True
        if check_images == False:
            os.system('docker pull '+image)

        build_cmd = "curl --unix-socket /var/run/docker.sock -H"+' "Content-Type: application/json"'+" -d '{"+'"Image"'+':"'+image+'",'+' "Cmd":"'+ command+'"'+"}' -X POST http:/v1.24/containers/create"
        
        tmp = os.popen(build_cmd).readlines()[0]
        tmp_deal = eval(tmp.strip())
        tmp_dict = {}
        tmp_dict = tmp_deal
        print(tmp_dict)
        
        try:
            id_cmd = tmp_dict['Id'][0:12]
            search = os.popen('docker ps -a | grep "'+ id_cmd +'"').readlines()[0]

            search_name = search.split()[-1]
        
            ctx['image'] = image
            ctx['command'] = command
            ctx['name'] = search_name

            ctx['id'] = tmp_dict['Id'][0:12]
            ctx['status'] = 'Success'
        except:
            ctx['image'] = image
            ctx['command'] = command
            ctx['name'] = ''

            ctx['id'] = ''
            ctx['status'] = 'Fail'
 



        # ctx['lowerLimit'] = lowerLimit

        # ctx['goodStep'] = min(stepList)
        # ctx['goodQuality'] = max(qualityList)
        # stepList = map(str, stepList)
        # ctx['qualityList'] = str(','.join(qualityList))

    # Repeat a few rounds
    return render(request, "manage.html", ctx)

```

看成果(在 runserver的前提下)
http://127.0.0.1:8000/manageDocker/hello_world
    
http://<server_wan_ip>:8000/manageDocker/hello_world 

    
    
    


## Docker
- 在 server 上架 Docker engine
[docker 安裝參考](https://docs.docker.com/engine/install/ubuntu/)
1. Update the apt package index and install packages to allow apt to use a repository over HTTPS:
```shell
$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```
2. Add Docker’s official GPG key:
```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88
```
![](https://i.imgur.com/Ik6K4uZ.png)

3. Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below. Learn about nightly and test channels.
```shell
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

```

![](https://i.imgur.com/TmSrtJh.png)

- install Docker egine 
1. Update the apt package index, and install the latest version of Docker Engine and containerd, or go to the next step to install a specific version:
```shell
 $ sudo apt-get update
 $ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
2. To install a specific version of Docker Engine, list the available versions in the repo, then select and install:

	a. List the versions available in your repo:
	` apt-cache madison docker-ce`
	
	b. Verify that Docker Engine is installed correctly by running the hello-world image.
	
	`$ sudo docker run hello-world`
	![](https://i.imgur.com/SFlsRNy.png)
	
:::danger
權限問題
使每次執行 docker 時不用加 sudo
```text=
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post http://%2Fvar%2Frun%2Fdocker.sock/v1.40/images/create?fromImage=ubuntu&tag=latest: dial unix /var/run/docker.sock: connect: permission denied
```
- Create the docker group.
`sudo groupadd docker`

- Add your user to the docker group.
`sudo usermod -aG docker ${USER}`
- logout
:::

