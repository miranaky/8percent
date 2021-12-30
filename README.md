# 📍 [Assignment 4] - 8퍼센트

<p align="center">

  <h2 align="center">🍴 Team 제6볶음 🍴</h2>
  <p align="center" width="50%">
  <img width="60%" src="https://user-images.githubusercontent.com/73830753/141292063-a61a979d-4178-4e60-a472-df12c270bb80.jpg"/>
  <p align="center">
    각기 다른 재료가 모여 맛있는 제육볶음을 만들듯,<br>
    서로 다른 개성있는 개인이 모여 멋진 결과물을 만들어내는 Team 제6볶음입니다.
  </p>
  </p>

</p>

## 💁‍♀️ Members

| 이름   | github                                    | 담당 기능                                        |
| ------ | ----------------------------------------- | ------------------------------------------------ |
| 신재민 | [shinjam](https://github.com/shinjam)     | Test코드 적용, 배포                              |
| 신우주 | [shinwooju](https://github.com/shinwooju) | 개인 사정으로 불참                               |
| 최혜림 | [rimi0108](https://github.com/rimi0108)   | 거래 내역 조회 api                               |
| 강성묵 | [miranaky](https://github.com/miranaky)   | 전체 총괄, 계좌 출금 api, 거래내역 Test코드 작성 |
| 김민규 | [SkyStar-K](https://github.com/SkyStar-K) | 계좌 입금 API                                    |

## ⭐ 과제 출제 기업 정보

- 기업명 : 8퍼센트
- [8퍼센트 사이트](https://8percent.kr/)
- [wanted 채용공고 링크](https://www.wanted.co.kr/wd/64695)

## ⭐ 과제 내용

<details>
    <summary>내용 보기</summary>

### **[필수 포함 사항]**

- READ.ME 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

<aside>
📝 “계좌 거래 API”를 구현해주세요. API는 3가지가 구현되어야 합니다.

</aside>

**✔️ API 목록**

---

- 거래내역 조회 API
- 입금 API
- 출금 API

**✔️ 주요 고려 사항은 다음과 같습니다.**

---

- 계좌의 잔액을 별도로 관리해야 하며, 계좌의 잔액과 거래내역의 잔액의 무결성의 보장
- DB를 설계 할때 각 칼럼의 타입과 제약

**✔️ 구현하지 않아도 되는 부분은 다음과 같습니다.**

---

- 문제와 관련되지 않은 부가적인 정보. 예를 들어 사용자 테이블의 이메일, 주소, 성별 등
- 프론트앤드 관련 부분

**✔️ 제약사항은 다음과 같습니다.**

---

- (**8퍼센트가 직접 로컬에서 실행하여 테스트를 원하는 경우를 위해**) 테스트의 편의성을 위해 mysql, postgresql 대신 sqllite를 사용해 주세요.

**✔️ 상세설명**

---

**1)** 거래내역 조회 **API**

- 아래와 같은 조회 화면에서 사용되는 API를 고려하시면 됩니다.
  [https://lh6.googleusercontent.com/PdtI4YvVu3biJ0TyEGCHVrR0fAPOQsILYHEczQHmR3UMKEINxlIjjp\_-3gOGu5yGh3YXpxbegNYqNCEosUosq3nKRTMpte6ZiRUccX8iRlD5rxLJ1HWFy6E2HcMFMIMGZO7eVQl5](https://lh6.googleusercontent.com/PdtI4YvVu3biJ0TyEGCHVrR0fAPOQsILYHEczQHmR3UMKEINxlIjjp_-3gOGu5yGh3YXpxbegNYqNCEosUosq3nKRTMpte6ZiRUccX8iRlD5rxLJ1HWFy6E2HcMFMIMGZO7eVQl5)

거래내역 API는 다음을 만족해야 합니다.

- 계좌의 소유주만 요청 할 수 있어야 합니다.
- 거래일시에 대한 필터링이 가능해야 합니다.
- 출금, 입금만 선택해서 필터링을 할 수 있어야 합니다.
- Pagination이 필요 합니다.
- 다음 사항이 응답에 포함되어야 합니다.
  - 거래일시
  - 거래금액
  - 잔액
  - 거래종류 (출금/입금)
  - 적요

**2)** 입금 **API**

입금 API는 다음을 만족해야 합니다.

- 계좌의 소유주만 요청 할 수 있어야 합니다.

**3)** 출금 **API**

출금 API는 다음을 만족해야 합니다.

- 계좌의 소유주만 요청 할 수 있어야 합니다.
- 계좌의 잔액내에서만 출금 할 수 있어야 합니다. 잔액을 넘어선 출금 요청에 대해서는 적절한 에러처리가 되어야 합니다.

**4)** 가산점

다음의 경우 가산점이 있습니다.

- Unit test의 구현
- Functional Test 의 구현 (입금, 조회, 출금에 대한 시나리오 테스트)
- 거래내역이 1억건을 넘어갈 때에 대한 고려
  - 이를 고려하여 어떤 설계를 추가하셨는지를 README에 남겨 주세요.

</details>

## 🛠 사용 기술 및 tools

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 🏄‍♀️ 모델링

![modeling](https://user-images.githubusercontent.com/73830753/141414993-121661f4-4eda-4404-a4df-91a633270c09.png)

## 🖇 API

[Postman API Document](https://documenter.getpostman.com/view/13670333/UVC8CRde)

## 설치 및 실행 방법

```
$ git clone https://github.com/JE6BOKM/8percent.git && cd 8percent
$ pip install -r requirements.txt
$ export DJANGO_SECRET_KEY='oa&8a6swp0y)muhd0%g%f2p4u&e4r_12ar6g6*vqmc5=ty1z&)'
$ python manage.py runserver
```

## 구현 기능

### 유저 회원가입 및 로그인

### 회원 별 계좌 생성

- 로그인 된 유저만 해당 기능을 사용할 수 있습니다.
- User는 1개의 Account(계좌)를 만들 수 있습니다.
  - /eightpercent/account 에 POST Request로 계좌를 생성합니다.
  - 기존에 생성된 계좌가 있으면 이미 있다는 메세지와 함꼐 400 Bad Request return 됩니다.
- User는 자신의 Account(계좌)를 볼 수 있습니다.
  - /eightpercent/account 에 GET Request로 요청
  - 자신의 계좌번호와, 잔액, 그리고 고객 이름을 확인 할 수 있습니다.

### 입금

- User 에게 입금 금액, 적요를 입력받습니다.
- User는 이미 계좌가 생성되어 있어야 합니다.
- 계좌에 입금 요청이 되면 Transaction을 기록합니다.
  - 계좌의 balance에서 요청된 금액 만큼 더합니다.
- 성공적으로 입금이 완료되면 다음 내용이 표기됩니다.
  - transaction_type: DEPOSIT
  - transaction_amount
  - description
  - account
  - account_balance

### 출금

- User 에게 출금 금액, 적요를 입력받습니다.
- User는 이미 계좌가 생성되어 있어야 합니다.
- 계좌에 출금 요청 금액보다 잔액이 많이 남아있으면 Transaction을 기록합니다.
  - 계좌의 balance에서 요청된 금액 만큼 뺍니다.
  - Transaction을 기록합니다.
  - 요청된 금액이 계좌의 잔액보다 많으면 Transaction을 기록하지 않고 400 bad request 를 리턴합니다.
  - 음수의 값으로 요청을 하면 Transaction을 기록하지 않고 400 bad request를 리턴합니다.
- 성공적으로 출금이 완료되면 다음 내용이 표기됩니다.
  - transaction_type :withdraw
  - transaction_amount
  - description
  - account
  - remaining_balance

### 거래내역 조회

- user에 해당하는 account만 조회할 수 있도록 token을 통해 받은 user 정보를 통해 account 정보를 받아옵니다.
- user가 만들지 않은 account의 거래 내역은 조회할 수 없습니다.
- 조회 내역은 10개씩 pagination되도록 구현했습니다.
- filtering
  - query parameter로 transaction_type을 받아 입금, 출금 타입을 선택하여 filtering 할 수 있도록 구현하였습니다.
  - start_day와 end_day을 query parameter로 받아 거래 기간을 선택하여 filtering 할 수 있도록 구현하였습니다.
    - end_day는 넣을 시 0시로 계산되어 들어가기 때문에 end_day에 1을 더하여 filtering 하였습니다.
      - ex) 2021-11-12일로 end_day를 지정하였을 시 2021-11-12 00:00시로 지정되어 들어가기 때문에 12일 00:00시 이전 정보까지 출력됩니다.
  - default로 최근 거래내역이 위로 올라가게 조회되기 때문에 거래내역 역순으로 조회 가능하게 ordering=True를 query parameter로 받을 수 있게 하였습니다.

## Ploblems

> _고려 단계에 있는 내용입니다._

### ❓ 거래내역이 1억건을 넘어갈 때에 대한 고려

거래 내역이 1억건이 넘어갈 경우 데이터 조회 시간에 이슈가 있습니다.

### Solutions

- **DB Indexing**: 거래내역은 데이터의 수정삭제가 거의 없는 자료 입니다. 수정이 적고 조회가 많을 때 효과적인 Indexing을 활용 할 수 있습니다. B-Tree 등의 알고리즘을 사용하기 때문에 빠르고 현프로젝트에는 고유한 값인 트랜잭션 id에 적용을 생각 하고 있습니다.
- **Cache**: 일정 주기 혹은 특정 시점에 자주 조회되는 특정 범위의 거래내역을 케시에 저장해두어 DB 조회를 줄여 조회 속도를 높힐 수 있습니다.

## 📁 폴더 구조

```
├── README.md
├── apps
│   ├── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── local.py
│   │   ├── production.py
│   │   └── test.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── authentications.py
│   │   ├── management
│   │   │   └── commands
│   │   │       └── dummy.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   └── serializers.py
│   ├── eightpercent
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── test_transaction_view.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── urls.py
│   ├── users
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── test_viewsets.py
│   │   ├── urls.py
│   │   └── views.py
│   └── wsgi.py
├── conftest.py
├── local_db.sqlite3
├── manage.py
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── requirements.txt
├── setup.cfg
└── test
    ├── __init__.py
    ├── factories
    │   ├── __init__.py
    │   └── users.py
    └── schema
        ├── __init__.py
        └── users.py
```

# Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 [8퍼센트](https://8percent.kr/)에서 출제한 과제를 기반으로 만들었습니다.
