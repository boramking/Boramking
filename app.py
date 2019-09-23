from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
# '/'url로 들어왔을 때, 아래 함수를 호출 시켜줘라는 뜻!
def index():
    return render_template('index.html')
# 괄호 사이에 아무것도 없다는 건, input이 따로 필요 없다는 의미.
# flask : 웹 사이트 서버 라이브러리.
# a태그 주소 쓸 때, 내 사이트 간의 이동은 도메인 주소를 따로 쓰지 않아도 됨. 외부 사이트로 갈 때는 full 주소를 써야함.

if __name__ == '__main__':
    import os
    app.run('0.0.0.0', port=os.environ.get('PORT', 5000))
#함수의 괄호 안에서 'ctrl+p'를 누르면 인수(?)를 확인 할 수 있다.