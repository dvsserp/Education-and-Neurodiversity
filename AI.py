from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder="front_end")
    app.config['SECRET_KEY'] = 'alvin'
    @app.route('/')
##- HTML integration here
    def hello_world():
        return render_template('web.html')
    
    ##-@app.route('./chat.html') for later
    ##-def chatbot():
        ##-return render_template('chat.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

