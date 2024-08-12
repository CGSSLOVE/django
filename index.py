#!/usr/bin/env python
print("Content-Type: text/html")   # 헤더
print()
print("""<!DOCTYPE html>
<html>
<head>
    <title>이세계 아이돌</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="li1.css?after">
    <script type="text/javascript" src="DN.js" defer></script>
    <style>
        #backcolor{
            width: 100%;
               height: 100%;
                padding: 0px;
                border-width: 0px;
        }
    </style>
</head>
<body
    <div id="main">
        <div id="main_up" >
            <div style="width:100%;">
                <h1>
                    <a style="color:white" href="index.html">이세계아이돌</a>
                </h1>
            </div>
            <div id="main_upright_box">
                    <input type="button" class="up" id="backcolor" value="night" onclick="daynight(this)"/>
            </div>
        </div>
        <div id="main_down">
        <div id="main_down_text">
            <p>
            <img src="https://upload.wikimedia.org/wikipedia/ko/thumb/b/b3/%EC%9D%B4%EC%84%B8%EA%B3%84%EC%95%84%EC%9D%B4%EB%8F%8C_LockDown_%EC%9D%B8%ED%84%B0%EB%B7%B0.png/250px-%EC%9D%B4%EC%84%B8%EA%B3%84%EC%95%84%EC%9D%B4%EB%8F%8C_LockDown_%EC%9D%B8%ED%84%B0%EB%B7%B0.png">
            </p>
            <p>
            <strong>이세계아이돌</strong>은 2021년 12월 17일에 데뷔한 왁 엔터테인먼트 소속의 6인조 버츄얼 걸그룹이다.<br>
            前 트위치 스트리머이자 現 아프리카TV BJ인 우왁굳이 기획한 프로젝트를 통해서 결성되었으며 디지털 싱글 앨범 <u>RE : WIND</u>를 발매하며 정식으로 데뷔하였다.
            </p>
        </div>
            <div id="main_down_ul">
                <ul>
                    <li><a class="li1" href="index.py?id=outline">개요</a></li>
                    <li><a class="li1" href="ndex.py?id=member">멤버</a></li>
                    <li><a class="li1" href="ndex.py?id=song">노래</a></li>
                </ul>
            </div>
        </div>
    </div>
    <p>
        댓글을 써보세요!<br>
        <a href="practice.html">연습용 넘어가기</a>
        <a href="print.html">프린트용 넘어가기</a>
        <a href="majhong.html">마작용 넘어가기</a>
    </p>
</body>
</html>
""")