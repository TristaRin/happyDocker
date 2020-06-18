# happyDocker
`I'm Docker, and I'm happy!`
## Table of Content

* [About the Project](#project)
* [Built With](#Package-Used)
* [Getting Started](#getting-start-with-your-own-server)
* [Prerequisites](#how-to-build-your0own-project)
  	* [Installation](#django)
	* [Installation](#docker)
	* [Installation](#後端處理-views.py)
	* [Installation](#deploy)
* [Installation](#)
* [Installation](#特別感謝)
* [Installation](#future)
* [Usage](#reference)

## Project
- 主頁面: 針對需求輸入 `image` 和 `command`
![](https://i.imgur.com/riCVT8U.png)

- 建立成功顯示 Container 資訊
![](https://i.imgur.com/3jmV60w.png)

- 點選 `Runnnn it !` 跳轉頁面並輸入欲執行的指令
	- 點選 `Add another Container!` 可跳轉回建立頁面 
![](https://i.imgur.com/nkQb9gp.png)


## Package  Used
1. python3 3.6.9
2. pipenv
3. django 3.0.3
4. Docker
5. curl

## Getting start with your own server
1. Enter remote server
```
ssh 帳號＠遠端ip
```

2. prepare all packages
```
sudo apt install python3-pip
pip3 install pipenv
```

3. clone project
```
git clone https://github.com/TristaRin/happyDocker.git
```

4. in your project folder, and enter the virtual environment. install django

```
cd happyDocker/
python3 -m pipenv shell
pip3 install django==3.0.3
```

5. runserver
```
cd prinsis/
python manage.py migrate
python manage.py runserver 163.22.17.137:8000
```
6. use it
http://163.22.17.137:8000/manageDocker/manage


## How to build your own project
### Django

1. localhost 佈署

    請先確認 python3 版本3.6.9
    然後安裝一些管理套件
    ```
    sudo apt install python3-pip
    pip3 install pipenv
    ```

2. 在本地端建好專案~
    先建一個資料夾叫 
    對此資料夾創建（或進入）虛擬環境
    再裝個 django
    ```
    mkdir happyDocker
    cd happyDocker/
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
    ALLOWED_HOSTS = ['163.22.17.137', 'localhost', '127.0.0.1']
    ```
    
3. localhost 可以看小火箭了 
    ```
    cd ..
    python manage.py runserver
    ```
    （注意）請確認你是在虛擬環境中，若不再虛擬環境中runserver會錯誤
   
    
4. 終於可以來新增一個 app 了～
    在 /happyDocker/prinsis 底下建一個 app 叫 manageDocker
    ```
    python manage.py startapp manageDocker
    ```
    修改 /happyDocker/prinsis/prinsis 底下的 setting.py
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
     在 /happyDocker/prinsis 底下建一個資料夾叫 templates
    ```
    cd ..
    mkdir templates
    
    ```
    修改 /happyDocker/prinsis/prinsis 底下的 setting.py

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
    修改 /happyDocker/prinsis/prinsis 底下的 urls.py
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
    1. 在 /happyDocker/prinsis/manageDocker 底下建一個 urls.py
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
    
    2. 在 /happyDocker/prinsis/templates 底下創一個 hello_world.html 和 manage.html
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
    
### Docker
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

### 後端處理 views.py
1. 將前端資料 POST 到後端
```python=
if request.POST:
        # 拿到計算所需的參數
		# POST 的 key 為 tag 中的 name
        image = request.POST['image']
        command = request.POST['command']
    
```
2. 確認 image 是否已存在

Docker 相關指令：
- （CMD 指令）使用 `curl` 以及 `docker.sock` socket檔抓取 image 的 json 資料
```shell
curl --unix-socket /var/run/docker.sock http:/v1.24/images/json
```
- pull image 
	- 須為存在在 [dockerhub](https://hub.docker.com/search/?type=image) 上的 image
```shell
docker pull <image_name>
```
- 快速刪除存在 `<none>` 的特定 image
```shell
docker images -f "dangling=true" -q
```
使用 python 執行 command line 指令：
```python=
os.system(<command>) # 執行指令
os.popen(<command>).readlines() # 每行讀取 CMD 的 stdout
```
處理 `json` 檔：

```python=
import json
<list> = json.loads(<data>)
```

實際實做範例：
```python=
check_images = False

        images_json = os.popen('curl --unix-socket /var/run/docker.sock http:/v1.24/images/json').readlines()[0]

        images_list = json.loads(images_json.strip())
        try:
			# list 中為 dictionary
            for each_image_dict in images_list:
				# RepoTags 為紀錄 image 的 key
                if image in each_image_dict['RepoTags']:
                    check_images = True
                    break
        except TypeError:
            # 處理 <none> 問題
            os.system('docker images -f "dangling=true" -q')
            for each_image_dict in images_list:
                if image in each_image_dict['RepoTags']:
                    check_images = True
                    break
        
        if check_images == False:
            os.system('docker pull '+image)

```
3. 依據 POST 回來的資訊 build Container
此專案將建立的 Container 放背景執行
**不建議使用 `-idt`**
(CMD) 建立 Container
```shell
docker run -idt <image> <command> 
```
實際範例並抓取回傳的 `Container id`：
```python=
build_cmd = "docker run -idt "+ image+ " "+ command
        tmp = os.popen(build_cmd).readlines()[0]
        tmp_deal = tmp.strip()
        
```

4. 抓取 Container name
(CMD)抓取 Container name 使用：
```shell
docker ps -a | grep "<Container_id>"
```
實際範例程式：
```python=
# 抓取 11 位 id
id_cmd = tmp_deal[0:12]
# 讀取回傳資料後最後一項為 Container name
search = os.popen('docker ps -a | grep "'+ id_cmd +'"').readlines()[0]
search_name = search.split()[-1]
```
5. 將 Container 資料使用 render 渲染回網頁
```python=
try:        
	ctx['image'] = image
	ctx['command'] = command
	ctx['name'] = search_name

	ctx['id'] = id_cmd
	ctx['status'] = 'Success'
    
except:
            
    ctx['image'] = image
    ctx['command'] = command
    ctx['name'] = ''

    ctx['id'] = ''
    ctx['status'] = 'Fail'

return render(request, "manage.html", ctx)

```
### Deploy 

1. 將以上專案 push 到 github 上 
2. 在遵循 Getting start with your own server 的步驟即可

## 工作分工

小公主：Django 架設，manage.html 前端，Server 申請
姊姊：Docker 建立，views.py (後端)， reaction.html 前後端

## 特別感謝
:smile: BlueT, 守恩, 果子維, 王威, 逸于, 丁丁, 許家瑋

## future
- 增加 停止/執行 特定 Container 的功能
- Container 建立時的參數增加
- 能夠定時清理使用不到的 Container
- 可以更改 Container 名字
