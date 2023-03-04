'''
首先，我们导入了Flask类。
其次我们创建了Flask的实例，第一个参数是应用模块或者包的名称。 如果你使用单一的模块（如本例），你应该使用 __name__ ，因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同（ 也即是 ‘__main__’ 或实际的导入名）。这是必须的，这样 Flask 才知道到哪去找模板、静态文件等等。
route()是一个路由，其实是一个装饰器，在其中输入URL，会帮我们在这个URL下执行对应的方法。
接着是函数主体，可以写方法也可以调用其他方法的返回值，最后返回到浏览器上显示的信息
最后我们用 run() 函数来让应用运行在本地服务器上。 其中 if __name__ ==’__main__’: 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。debug=True开启了调试模式，相当于在发生错误时提供一个相当有用的调试器。host=’0.0.0.0‘可以允许同一个局域网内别的用户访问，这个方法让操作系统监听所有公网 IP。port自定义端口。
'''

from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='', static_folder='templates', template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def home():
    #return '<h1>Home</h1>'
    return render_template('/index.html')

"""
@app.route('/signin/', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin/', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)