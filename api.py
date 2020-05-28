from app import napp

@napp.route('/helloword')
def downloadOneBook():
    return 'Hello World!'
