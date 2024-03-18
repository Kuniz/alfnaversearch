alfnaversearch : Naver Search Workflow for Alfred ![Test](../../actions/workflows/test-naver-ac.yml/badge.svg) ![Release](../../actions/workflows/release.yml/badge.svg)
==============

Naver Search Workflow for Alfred

Alfred에서 네이버 검색, 네이버 쇼핑, 네이버 지도, 국어/영어/일본어/중국어/한자/독일어/프랑스어/이탈리아어/러시아어/스페인어/태국어/베트남어/인도네시아어 사전 검색이 자동완성 되는 워크플로우
Naver is a most famous search engine in Korea.
This workflow finds words in dictonaries of Naver dictionary and searches contents by Naver search engine. 
You can use easily to discover Korean contents with the this Alfred workflow.

Install workflow
--------------

- [releases](../../releases/latest) 페이지의 `NaverSearch.alfredworkflow`를 다운로드 받아서 실행한다.

- MacOS 12.3 이상의 경우
  - python3 설치
    - `brew install python`
    - `xcode-select --install`

- Alfred 4.0 이상 지원
- Python 2 사용 불가


Usage
--------------
* `na ...`  : Naver Search(일반 네이버 검색)
* `ns ...`  : Naver Shopping(네이버 쇼핑 검색)
* `nt ...`  : Naver Terms(네이버 지식백과 검색)
* `nmap ...` : Naver Map(네이버 지도 검색) - Configure Workflow...에서 위치정보를 입력할 수 있으며 이 정보로부터 지도 검색시 반영 (미입력시 기본값으로 '서울시청'의 위치정보 반영)  
* `nmapip ...` : Naver Map(네이버 지도 검색) - 사용자의 IP주소로부터 위치정보를 가져와 지도 검색시 반영(IP로부터 위치정보를 가져올 수 없을 땐 Configure Workflow...의 설정값 사용)
* `nak ...` : Naver Korean Dictionary (국어 사전)
* `nae ...` : Naver Korean-English Dictionary (영어 사전)
* `naee ...` : Naver English-English Dictionary (영영 사전)
* `naj ...` : Naver Korean-Japanese Dictionary (일본어 사전)
* `nac ...` : Naver Korean-Chinese Dictionary (중국어 사전)
* `nah ...` : Naver Hanja Dictionary (한자 사전)
* `nad ...` : Naver Korean-German Dictionary (독일어 사전)
* `naf ...` : Naver Korean-French Dictionary (프랑스어 사전)
* `nai ...` : Naver Korean-Italian Dictionary (이탈리아어 사전)
* `nar ...` : Naver Korean-Russian Dictionary (러시아어 사전)
* `nas ...` : Naver Korean-Spanish Dictionary (스페인어 사전)
* `nat ...` : Naver Korean-Thai Dictionary (태국어 사전)
* `nav ...` : Naver Korean-Vietnamese Dictionary (베트남어 사전)
* `nan ...` : Naver Korean-Indonesian Dictionary (인도네시아어 사전)
* `nau ...` : Naver Korean-Uzbekistan Dictionary (우즈베키스탄어 사전)
* `nane ...` : Naver Korean-Nepali Dictionary (네팔어 사전)
* `namn ...` : Naver Korean-Mongolian Dictionary (몽골어 사전)
* `namy ...` : Naver Korean-Burmese Dictionary (미안마어 사전)
* `nasw ...` : Naver Korean-Swahili Dictionary (스와힐리어 사전)
* `naar ...` : Naver Korean-Aramaic Dictionary (아랍어 사전)
* `nakm ...` : Naver Korean-Cambodian Dictionary (캄보디아어 사전)
* `nafa ...` : Naver Korean-Persian Dictionary (페르시아어 사전)
* `nahi ...` : Naver Korean-Hindi Dictionary (힌디어 사전)
* `nanl ...` : Naver Korean-Dutch Dictionary (네덜란드어 사전)
* `nasv ...` : Naver Korean-Swedish Dictionary (스웨덴어 사전)
* `nauk ...` : Naver Korean-Ukrainian Dictionary (우크라이나어 사전)
* `naka ...` : Naver Korean-Gruziya Dictionary (조지아어 사전)
* `nacs ...` : Naver Korean-Czech Dictionary (체코어 사전)
* `nahr ...` : Naver Korean-Croatian Dictionary (크로아티아어 사전)
* `natr ...` : Naver Korean-Turkish Dictionary (터키어 사전)
* `napt ...` : Naver Korean-Portuguese Dictionary (포르투갈어 사전)
* `napl ...` : Naver Korean-Polish Dictionary (폴란드어 사전)
* `nafi ...` : Naver Korean-Finnish Dictionary (핀란드어 사전)
* `nahu ...` : Naver Korean-Hungarian Dictionary (헝가리어 사전)
* `nasq ...` : Naver Korean-Albanian Dictionary (알바니아어 사전)
* `naro ...` : Naver Korean-Rumanian Dictionary (루마니아어 사전)
* `nala ...` : Naver Korean-Latin Dictionary (라틴어 사전)
* `nael ...` : Naver Korean-Greek Dictionary (그리스어 사전)


단축키 관련 기능 추가

* Cmd + C : 상세 내용이 클립보드에 복사
* Cmd + N, C 혹은 Cmd + Enter : 자동완성 텍스트가 클립보드로 복사
* Cmd + Y 혹은 Shift : 검색결과 미리 보기 웹브라우져 출력

Externel Module
--------------
 This workflow used alfred-workflow more than v0.0.2. Alfred-workflow can find there(https://github.com/deanishe/alfred-workflow).
 This workflow used alp(A Python Module for Alfred Workflows) module at v0.0.1. It created by Daniel Shannon. 
 Certifi : using ssl with default urllib

LICENSE
--------------
 - MIT
