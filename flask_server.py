from flask import Flask, render_template, request, jsonify
import io
import PyPDF2
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
    
    @app.route('/chatbot', methods=['POST'])
    def test_my_ai():
        data = request.get_json()
        prompt = data.get("prompt", "")
        history = data.get("blank_list", []) 
        result, updated_history = chat_with_together_api(prompt, history)
        return jsonify({
            "message": result,
            "updated_list": updated_history
        }), 200



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
