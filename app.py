from flask import Flask, render_template, request
import os

# Flask 앱 설정
app = Flask(__name__,
            template_folder=os.path.join(os.getcwd(), 'app/templates'),
            static_folder=os.path.join(os.getcwd(), 'app/static'),
            static_url_path='/static')

# 메인 페이지
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pass
    return render_template('index.html')

# 게시판 페이지
@app.route('/forum', methods=['GET', 'POST'])
def forum():
    if request.method == 'POST':
        item = item
        # POST 요청 처리
        pass
    return render_template('forum.html')

# 채팅 페이지
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        # POST 요청 처리
        pass
    return render_template('chat.html')

# 도서 페이지
@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        # POST 요청 처리
        pass
    return render_template('books.html')

# 굿즈 페이지
@app.route('/goods', methods=['GET', 'POST'])
def goods():
    if request.method == 'POST':
        # POST 요청 처리
        pass
    return render_template('goods.html')

# 중고 판매 페이지
@app.route('/resale', methods=['GET', 'POST'])
def resale():
    if request.method == 'POST':
        # POST 요청 처리
        pass
    return render_template('resale.html')

if __name__ == '__main__':
    app.run(debug=True)
