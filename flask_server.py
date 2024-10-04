from flask import Flask, render_template, request
import io
import pypdf
from AI_Stuff.AI_MAIN import chat_with_together_api

def create_app():
    app = Flask(__name__, template_folder="front_end")
    configure_app(app)         
    register_routes(app)       
    return app

def configure_app(app):
    app.config['SECRET_KEY'] = 'alvin'

def register_routes(app):
    @app.route('/')
    def hello_world():
        return render_template('web.html')
    
    @app.route('/chat')
    def chatbot():
        return render_template('chat.html')
    
    @app.route('/geometry')
    def geolink():
        return render_template('geometry.html')
    
    @app.route('/compsci')
    def compsci():
        return render_template('compsci.html')
    
    @app.route('/astro')
    def astro():
        return render_template('astro.html')
    
    @app.route('/test_my_ai')
    def test_my_ai():
       query = "Write a one sentence quote"
       history = []
       history.append({"role": "user", "content": query})
       result, x = chat_with_together_api(history)
       history.append({"role":"assistant","content":result})
       return result, history


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
