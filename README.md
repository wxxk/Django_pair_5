# Django Pair Project 3

### 20221014 KDT - 실무 맞춤형 풀스택 1기 1회차 이상욱 @wxxk

>- 회원가입, 로그인, 회원 목록 조회, 회원 정보 조회, 회원 정보 수정, 로그아웃

### 목차

| 내용                            |
| ------------------------------- |
| [프로젝트소개](#프로젝트소개) |
| [코드구현](#코드구현)           |
| [코드실행](#코드실행)           |
| [배운점](#배운점)             |



### 프로젝트소개

---

- #### 목적

  >페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스 개발
  >
  >- CRUD 구현
  >- Staticfiles 활용 정적 파일(이미지, CSS, JS) 다루기
  >- Django Auth 활용 회원 관리(회원가입 / 회원조회 / 로그인 / 로그아웃)



- #### 개발 환경

  > 언어 : HTML, CSS, Python, JavaScript
  >
  > 프레임워크 : Django



### 코드구현

---

> ### 1. 회원가입
>
> >앱 App
> >
> >앱 이름 : accounts
> >
> >모델 Model
> >
> >모델 이름 : User
>
> - Django **AbstractUser** 모델 상속
>
> **폼 Form**
>
> - Django 내장 회원가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 작성
> - 해당 폼은 아래 필드만 출력합니다.
>   - username
>   - first_name
>   - last_name
>   - password1
>   - password2
>   - email
>
> **기능 View**
>
> - 회원가입	
>
>   - `POST` http://127.0.0.1:8000/accounts/signup/
>
>   - CustomUserCreationForm을 활용해서 회원가입 구현
>
> **화면 Template**
>
> - 회원가입 페이지
>
>   - `GET` http://127.0.0.1:8000/accounts/signup/
>
>   - 회원가입 폼
>
> 
>
> ------
>
> ### 2. 로그인
>
> **폼 Form**
>
> - 로그인
>   - Django 내장 로그인 폼 **AuthenticationForm 활용**
>
> **기능 View**
>
> - 로그인
>
>   - `POST` http://127.0.0.1:8000/accounts/login/
>
>   - **AuthenticationForm**를 활용해서 로그인 구현
>
> **화면 Template**
>
> - 로그인 페이지
>
>   - `GET` http://127.0.0.1:8000/accounts/login/
>
>   - 로그인 폼
>
>   - 회원가입 페이지 이동 버튼
>
> 
>
> ------
>
> ### 3. 회원 목록 조회
>
> **기능 View**
>
> - 회원 목록 조회
>   - `GET` http://127.0.0.1:8000/accounts/
>   - is_superuser를 활용해서 관리자만 볼 수 있도록 구현
>
> **화면 Template**
>
> - 회원 목록 페이지
>
>   - `GET` http://127.0.0.1:8000/accounts/
>
>   - 회원 목록 출력
>
>   - 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동
>
> 
>
> 
>
> ---
>
> ### 4. 회원 정보 조회(사용자)
>
> **기능 View**
>
> - 회원 정보 조회
>   - `GET` http://127.0.0.1:8000/accounts/<int:pk>/
>
> **화면 Template**
>
> - 회원 조회 페이지(프로필 페이지)
>   - `GET` http://127.0.0.1:8000/accounts/<int:pk>/
>
> 
>
> 
>
> ------
>
> ### 5. 회원 정보 수정
>
> **폼 Form**
>
> - 회원 정보 수정
>   - Django 내장 회원 수정 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성
>   - 해당 폼은 아래 필드만 출력합니다.
>     - last_name
>     - first_name
>     - email
>
> **기능 View**
>
> 회원 정보 수정
>
> - `POST` http://127.0.0.1:8000/accounts/update/
>
> **화면 Template**
>
> 회원 정보 수정 페이지
>
> - `GET` http://127.0.0.1:8000/accounts/update/
>
> 
>
> ------
>
> ### 6. 로그아웃
>
> **기능 View**
>
> - 로그아웃
>
>   - **AuthenticationForm**를 활용해서 로그아웃 구현
>
>   - `POST` http://127.0.0.1:8000/accounts/logout/
>
> 
>
> ------
>
> ### 7.  팔로우
>
> ##### 기능 view
>
> 팔로우
>
> - `POST` http://127.0.0.1:8000/accounts/follow/
>
> 
>
> ### 8. 네비게이션바
>
> **화면 Template**
>
> - **네비게이션바**
>
>   - 리뷰 목록 페이지 이동 버튼
>
>   - 리뷰 작성 페이지 이동 버튼
>
>   - 비로그인 유저는 작성 버튼 클릭시 로그인 화면으로 이동
>
>   - 로그인 상태에 따라 다른 화면 출력
>     1. 로그인 상태
>        - 로그인 한 사용자의 username 출력
>          - 회원정보를 클릭하면 회원 정보 조회(사용자) 페이지로 이동
>          - 로그아웃 버튼
>     2. 비 로그인 상태
>        - 로그인 페이지 이동 버튼
>        - 회원가입 페이지 이동 버튼
>
> 
>
> ------
>
> ### 9. 리뷰 생성
>
> **앱 App**
>
> 앱 이름 : reviews
>
> 모델 Model
>
> 모델 이름 : Review
>
> - 모델 필드
>
>   | 이름       | 역할          | 필드           | 속성              |
>   | ---------- | ------------- | -------------- | ----------------- |
>   | title      | 리뷰 제목     | Char           |                   |
>   | content    | 리뷰 내용     | Text           |                   |
>   | movie_name | 영화 이름     | Char           |                   |
>   | grade      | 영화 평점     | Char           |                   |
>   | created_at | 리뷰 생성시간 | DateTime       | auto_now_add=True |
>   | updated_at | 리뷰 수정시간 | DateTime       | auto_now = True   |
>   | image      | 이미지        | ProcessedImage |                   |
>   | user       | 유저          | ForeignKey     |                   |
>   | like_users | 좋아요        | ManyToMany     |                   |
>
> 
>
> **기능 View**
>
> 데이터 생성
>
> - `POST` http://127.0.0.1:8000/reviews/create/
>
> **화면 Template**
>
> **리뷰 작성 페이지**
>
> - `GET` http://127.0.0.1:8000/reviews/create/
> - 리뷰 작성 폼
>
> 
>
> ------
>
> ### 10. 리뷰 목록 조회
>
> **기능 View**
>
> - 데이터 목록 조회
>   - `POST` http://127.0.0.1:8000/reviews/
>
> **화면 Template**
>
> - 리뷰 **목록 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/
>
>   - 리뷰 목록 출력
>
>   - 더보기 버튼을 클릭하면 해당 리뷰의 정보 페이지로 이동
>
> 
>
> ------
>
> ### 11. 리뷰 정보 조회
>
> **기능 View**
>
> - 데이터 정보 조회
>   - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
>
> **화면 Template**
>
> - **리뷰 정보 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
>
>   - 해당 리뷰 정보 출력
>
>   - 수정 / 삭제 / 뒤로가기 버튼 
>
> 
>
> ------
>
> ### 12. 리뷰 정보 수정
>
> **기능 View**
>
> - 데이터 수정
>   - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
>
> **화면 Template**
>
> - **리뷰 수정 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
>
>   - 리뷰 수정 폼
>   - 뒤로가기 버튼
>
> 
>
> ------
>
> ### 13. 리뷰 삭제
>
> **기능 View**
>
> - 데이터 삭제
>   - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/
>
>  
>
> ------
>
> ### 14. 댓글 생성
>
> **기능 View**
>
> - 댓글 생성
>   - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/comments/
>
> **화면 Template**
>
> - 리뷰 **목록 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/
>   - 댓글 목록 출력
>
>  
>
> ------
>
> ### 15. 댓글 삭제
>
> **기능 View**
>
> - 댓글 생성
>   - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/comments/delete/
>
> **화면 Template**
>
> - 리뷰 **목록 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/comments/delete/
>   - 댓글 삭제
>
> 
>
> ### 16. 좋아요 생성
>
> **기능 View**
>
> - 좋아요 생성
>   - `POST` http://127.0.0.1:8000/reviews/likes
>
> **화면 Template**
>
> - 리뷰 **목록 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/likes
>   - 좋아요 생성



### 코드실행

---

![bandicam-2022-10-30-23-33-30-943](README.assets/bandicam-2022-10-30-23-33-30-943-16671418467512.gif)



### 배운점

---

### Heroku 설치 & 로그인

##### 1. Heroku CLI 설치

##### 2. [터미널] Heroku 설치 확인

```bash
heroku --version

# 아래 메세지가 출력되면 정상
# heroku/7.65.0 darwin-x64 node-v14.19.0
```

### 배포 준비

##### 1. [터미널] 패키지 설치

⚠️ 가상 환경이 실행된 상태인지 확인합니다.

```bash
pip install gunicorn 
pip install dj-database-url # PostgreSQL 설정용 패키지
pip install psycopg2-binary # PostgreSQL 설정용 패키지
pip install whitenoise # 정적 파일 처리용 패키지
pip install python-dotenv # 환경 변수 관리 패키지

pip freeze > requirements.txt # 패키지 목록 저장
```



##### 2. [Procfile] Procfile

❓ Procfile 헤로쿠가 배포 과정에 실행할 명령어 모음 파일

 🧑‍💻 [manage.py](http://manage.py) 가 있는 폴더에 **`Procfile`**(대소문자 구분) 생성하고 아래 명령어 작성 프로젝트명 → django-admin startproject `[프로젝트명]`

프로젝트명 작성

```
web: gunicorn [프로젝트명].wsgi --log-file -
```

예시

```
web: gunicorn pjt.wsgi --log-file -
```



##### 3. [runtime.txt] runtime.txt 생성

❓ runtime.txt 헤로쿠가 사용해야할 파이썬 버전 명시

🧑‍💻 [manage.py](http://manage.py) 가 있는 폴더에 **`runtime.txt`** 생성 후 버전 작성

파이썬 버전 작성

```
python-3.9.15
```



##### 4. [[settings.py](http://settings.py)] 데이터베이스 PostgreSQL 설정

❓ PostgreSQL 관계형 데이터베이스 중 하나로 헤로쿠에서 기본적으로 지원하는 데이터베이스 헤로쿠에서는 SQLite를 사용할 수 없기 때문에 추가 설정이 필요합니다.

🧑‍💻 [[settings.py](http://settings.py)] DATABASES 아래에 코드를 추가합니다.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

"""
기존 DATABASES 코드 아래에 아래 세 줄을 추가합니다.
"""
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)
```



##### 5. [.env / [settings.py](http://settings.py)] SECRET_KEY 분리

❓ SECRET_KEY Django 인증(회원가입, 로그인 등등) 과정에 필요한 외부로 노출되면 안되는 비밀키입니다.

🧑‍💻 [Djecrety.ir](http://Djecrety.ir) 에서 새로운 SECRET_KEY를 생성해서 사용합니다. manage.py가 있는 폴더에`.env` 파일을 생성합니다.

[.env] 생성한 SECRET_KEY를 작성합니다.

[Djecrety](https://djecrety.ir/)

```
# .env
SECRET_KEY="생성한 SECRET_KEY"

# 예시
# SECRET_KEY="$o5(+um4@+4g#3pp_zj-+b3vx99qbecllpsr%wh-d&hk(d=he@"
```

⚠️ .env 파일을 `.gitignore`에 추가합니다.

🧑‍💻 [[settings.py](http://settings.py)] SECRET_KEY 코드를 수정합니다.

```python
"""
기존
SECRET_KEY = "..."
"""

# 수정
"""
아래 3줄은 파일 최상단에 작성합니다.
"""
from dotenv import load_dotenv
import os
load_dotenv() # .env 파일에서 환경 변수를 불러옵니다.

# 기존 SECRET_KEY 대신 사용합니다.
SECRET_KEY = os.getenv("SECRET_KEY")
```



##### 6. [[settings.py](http://settings.py)] ALLOWED_HOSTS 설정

 ❓ ALLOWED_HOSTS 서비스 접속을 허용할 도메인(주소) 목록입니다.

 🧑‍💻[[settings.py](http://settings.py)] ALLOWED_HOSTS을 수정합니다.

```python
"""
# 기존
ALLOWED_HOSTS = []
또는
ALLOWED_HOSTS = ['*']
"""

# 수정
ALLOWED_HOSTS = ["127.0.0.1", "localhost", ".herokuapp.com"]
```



##### 7. [[settings.py](http://settings.py) / .env] DEBUG 설정

❓ DEBUG 오류가 발생했을 때 오류 원인 출력(노란 화면) 여부에 대해 결정하는 옵션입니다. 사용자에게 노출되면 안 되는 정보들이 많이 포함된 화면입니다. 그러므로 *배포 환경*에서는 DEBUG 옵션을 비활성화(*False*) 시킵니다.

🧑‍💻 환경 변수를 통해 개발 환경(True)과 배포 환경(False)에서 다른 값이 할당되도록 하겠습니다. [[settings.py](http://settings.py)] DEBUG 값을 수정합니다.

```python
"""
# 기존 
DEBUG = True
"""

# 수정
# 환경 변수에서 가져온 DEBUG 값이
# (개발 환경) "True" 라면 DEBUG에 True 가 할당됩니다.
# (배포 환경) "False" 라면 DEBUG에 False 가 할당됩니다.
DEBUG = os.getenv("DEBUG") == "True"
```

🧑‍💻 [.env] DEBUG 값을 추가합니다.

```
SECRET_KEY="..."

DEBUG="True"
```



##### 8. [[settings.py](http://settings.py)] STATIC_ROOT 설정

❓ STATIC_ROOT

배포 이전에는 Django가 각 앱의 static 폴더에서 정적 파일을 처리합니다. 하지만, 배포 이후에는 정적 파일에 대한 처리가 필요합니다. 정적 파일 처리를 위해 파일을 모아야 하는데(python [manage.py](http://manage.py) collectstatic) STATIC_ROOT에 할당된 경로에 파일이 모입니다.

🧑‍💻 [[settings.py](http://settings.py)] STATIC_ROOT를 생성하고, 경로를 할당합니다.

```python
"""
STATIC_URL = '/static/'
STATIC_URL 아래에 작성합니다.
"""

STATIC_ROOT = BASE_DIR / "staticfiles"
```



##### 9. [[settings.py](http://settings.py)] whitenoise 설정

❓ whitenoise 정적(static) 파일을 사용자에게 제공해주는 패키지입니다. DEBUG = False 일 때 장고는 정적 파일을 사용자에게 제공하지 않습니다. 정적 파일 제공을 whitenoise가 대신 담당 합니다.

🧑‍💻 [[settings.py](http://settings.py)] MIDDLEWARE 리스트의 `SecurityMiddleware` 아래에 코드를 추가합니다. *SecurityMiddleware*는 기존에 작성 되어 있는 Middleware 입니다. *SecurityMiddleware*를 추가하지 않도록 합시다.

```python
MIDDLEWARE = [
		"""
		SecurityMiddleware는 추가하지 않습니다.
		SecurityMiddleware는 기존에 있는 코드입니다.
		"""
    "django.middleware.security.SecurityMiddleware",

		# SecurityMiddleware 아래에 다음 코드를 추가합니다.
    "whitenoise.middleware.WhiteNoiseMiddleware",

		# ... 이하 생략
]
```



##### 확인사항

⚠️ 생성한 파일들(Procfile, runtime.txt, .env)이 올바른 위치에 있는지 파일 이름이 정확한지 확인해주세요.

![화면 캡처 2022-10-30 235023](README.assets/화면 캡처 2022-10-30 235023.png)

⚠️ .gitignore 에 .env / db.sqlite3 가 등록된 상태인지 확인해주세요.

⚠️ 패키지 목록을 저장 했는지 확인해주세요.



### 배포

##### 1. Heroku 로그인

1. [터미널] 명령어 입력

   ```bash
   heroku login
   ```

2. [터미널] 웹 로그인

   아래 상태에서 아무 키나 입력하면 로그인 페이지가 열립니다.

   ![화면 캡처 2022-10-30 235122](README.assets/화면 캡처 2022-10-30 235122.png)

3. [브라우저] Log In 버튼 클릭

   ![화면 캡처 2022-10-30 235148](README.assets/화면 캡처 2022-10-30 235148.png)

4. [브라우저] 로그인 완료 확인, 창 닫기

   ![화면 캡처 2022-10-30 235215](README.assets/화면 캡처 2022-10-30 235215.png)

5. [터미널] 로그인 성공 메세지 확인

   ![화면 캡처 2022-10-30 235235](README.assets/화면 캡처 2022-10-30 235235.png)

### 2. [터미널] Heroku 앱 생성

```bash
# 앱 이름을 정해서 랜덤으로 정해서 생성해줍니다.
heroku create
```

### 3. [터미널] 헤로쿠 환경(배포 환경)에서의 환경 변수(env) 등록

1. [브라우저] 헤로쿠 대쉬보드 접속

   [Heroku](https://dashboard.heroku.com/apps/)

2. [브라우저] 생성한 앱 대쉬보드 접속

3. [브라우저] Settings - Reveal Config Vars 클릭

![화면 캡처 2022-10-30 235306](README.assets/화면 캡처 2022-10-30 235306.png)

d. DEBUG = False 입력 → Add 클릭 / SECRET_KEY = 생성한 SECRET_KEY 입력 → Add 클릭

![화면 캡처 2022-10-30 235342](README.assets/화면 캡처 2022-10-30 235342.png)



##### 4. [터미널] 배포

```bash
git add .

git commit -m "Commit Message"

# 로컬 master 브랜치 -> 헤로쿠 저장소 master 브랜치
git push heroku master
```

##### 5. [터미널] 데이터베이스 설정

```bash
# 데이터베이스 마이그레이트
heroku run python manage.py migrate

# 관리자 계정 생성
heroku run python manage.py createsuperuser
```

##### 6. [터미널] 웹사이트 열기

```bash
heroku open
```



### 재배포

🧑‍💻 git add - commit - push heroku master를 합니다. makemigrations를 했다면 migrate



