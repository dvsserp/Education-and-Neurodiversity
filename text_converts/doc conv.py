from flask import Flask, render_template, request
import PyPDF2
### Review on Day of Hackathon/Asa Review Test
app = Flask(__name__)

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ''
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        text = extract_text_from_pdf(file)
        print("Text extracting in progress.")
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(text)
        print("Success")
        return 'File successfully converted to text!'

if __name__ == '__main__':
    app.run(debug=True)