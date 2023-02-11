# 읽어주세요!
---
프로젝트 구조는 다음과 같습니다.
```text
▼ myScreen
  ▼ static
    ▼ css
      ▼ common
        reset.css
        common.css
    ▼ img
    ▼ js
      ▼ common
        common.js
  ▼ templates
    index.html
  ▼ venv
  app.py
  dbprac.py
  meta_prac.py
```
이중 static 폴더내 css, js 폴더 두개로 나뉘는데, css폴더에는 기능구현시 작성한 css파일을 정리합니다. 만일 자신이 작업 중 css 스타일을 적용하고자 한다면, 이 폴더에 css파일을 작성한 후 index.html에 불러와주시면 됩니다.  

js파일도 똑같습니다. 작업 도중 스크립트를 작성하는 경우 본인이 작업할 js파일을 static > js 폴더에 생성하여 index.html에 불러와주시면 됩니다.  
파일을 html에 import하는 방법은 다음과 같습니다.

### 1. css 파일 index.html에 포함시키기
```html
<head>
    <!-- 1. css 파일 import href 속성에 파일 위치를 지정해주시면 됩니다.-->
    <link rel="stylesheet" type="text/css" href=".././static/css/common/reset.css">
    <!-- 여기 아래에 위와 같이 css 파일을 포함시켜주세요! -->
</head>
```

### 2. js 파일 index.html에 포함시키기
```html
<body>

    <!-- js 파일의 경우 body 태그 내 맨 아래에 포함시킵니다. -->
    <script src=".././static/js/common/common.js" type="application/javascript"></script>
    <!-- js 파일의 아래에 포함시켜주세요. -->
</body>
```

### * 해당 프로젝트에서는 다음과 같이 작업을 진행하는 일이 없도록 합시다.
```html
<!-- index.html -->
<script>
    console.log('안녕!')
</script>
<style>
    .hi{
        background: red;
    }
</style>
```

작업 도중 태그의 id값이 겹치는 일을 자주 볼 수 있을것입니다. 태그에 id를 부여하는 경우 반드시 자신의 작업기능-id명 으로 통일하도록 합시다. ex) 투두리스트 작업을 진행하는 경우 div 태그내 append로 태그를 추가할 경우 div태그 id 속성은 다음과 같이 작성합시다. id="todo-list" 와 같이 id를 지정해두도록 합시다.

### 예시 즐겨찾기(favorites) 기능을 구현하는 경우 id 및 클래스 값으로 favorites_임의의 이름
```html
<section>
    <div class="favorites_menu">
            <button class="favorites_btn" onclick="showFavoritesLinks()">
                즐겨찾기 메뉴
            </button>
            <div id="favorites_list_wrap" class="favorites_list_wrap d-none">
                <ul class="favorites_add_wrap">
                    <input class="favorites_input_url" id="favorites_addUrl"/>
                    <button class="favorites_add_btn" onclick="saveLink()">
                        +
                    </button>
                </ul>
                <ul id="favorites_list" class="favorites_list">
                </ul>
            </div>
        </div>
</section>
```

venv 폴더내 파이썬 라이브러리에는 웹종강에서 사용한 서버 패키지, 크롤링 패키지, mongoDB 커넥션 패키지가 포함되어 있습니다.
```text
1. Flask
2. dnspython
3. bs4
4. requests
5. pymongo
```
앞으로 프로젝트 작업 과정에서 필요한 정보는 이곳에 정리해두도록 하겠습니다. 그럼 건승합시다.