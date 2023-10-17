from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '''<h2>主页</h2>  
<a href="/login">登录</a>'''


@app.route('/login', methods=['GET'])
def signin_form():
    return render_template_string('''  
    <form action="/loginstatus" method="post">  
        <p>用户名: <input name="username"></p>  
        <p>密码  : <input name="password" type="password"></p>  
        <p><button type="submit">登录</button></p>  
    </form>  
    ''')


@app.route('/loginstatus', methods=['POST'])
def signin():
    # 这里只是一个简单的示例，实际上应该使用加密和密码数据库
    if request.form['username'] == 'username1' and request.form['password'] == 'password1':
        return render_template_string('''  
        <h4>Hello, <a id="user" href="/dashboard">username1</a>!</h4>  
        <a href="/logout">登出</a>  
        ''')
    return '<h4>用户名或密码错误！</h4>'


@app.route('/logout', methods=['GET'])
def logout():
    # 这里可以添加注销的逻辑，比如清除session等
    return '<h4>已登出！</h4>'


if __name__ == '__main__':
    app.run(port=5003, debug=True)