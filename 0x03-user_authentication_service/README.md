# README 

This document provides a brief overview of how to declare API routes, manage cookies, retrieve form data, and return various HTTP status codes in a Flask application.

## API Routes

In Flask, routes are used to map URLs to functions. You can declare routes using the `@app.route` decorator.

### Example
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

if __name__ == '__main__':
    app.run(debug=True)
```

## Cookies

Cookies are small pieces of data stored on the client side. You can get and set cookies using the `request` and `make_response` objects in Flask.

### Setting a Cookie
```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie Set")
    resp.set_cookie('username', 'John Doe')
    return resp
```

### Getting a Cookie
```python
@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Username is {username}'
```

## Form Data

To retrieve form data submitted via POST requests, you can use the `request.form` object.

### Example
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'Logged in as {username}'
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''
```

## HTTP Status Codes

Flask allows you to return various HTTP status codes using the `make_response` function or by returning a tuple.

### Example
```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/success')
def success():
    return "Success", 200

@app.route('/not_found')
def not_found():
    return "Not Found", 404

@app.route('/custom_response')
def custom_response():
    resp = make_response("Custom Response")
    resp.status_code = 202
    return resp
```

## Conclusion

This guide provides a basic overview of how to handle API routes, cookies, form data, and HTTP status codes in a Flask application. For more detailed information, refer to the [Flask documentation](https://flask.palletsprojects.com/).
