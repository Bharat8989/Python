import io
from flask import Flask, request, send_file, jsonify,Response
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# pip install dicttoxml  download the 
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
  
    data = request.get_json(silent=True)
    
    
        
    if not data:
        return jsonify({"error": "No JSON data provided or invalid JSON"}), 400

    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    story = []
    
    
    styles = getSampleStyleSheet()

    
    story.append(Paragraph("<b>JSON to PDF Generated Report</b>", styles['Title']))
    story.append(Spacer(1, 25))

    
    for key, value in data.items():
        
        if key in styles:
            current_style = styles[key]
            text = f"{value}"
        else:
            
            current_style = styles['BodyText']
            text = f"<b>{key.capitalize()}:</b> {value}"
        
        story.append(Paragraph(text, current_style))
        story.append(Spacer(1, 15))
    
    doc.build(story)
    
    
    buffer.seek(0)

    
    return send_file(
        buffer,
        as_attachment=False,
        download_name='report.pdf',
        mimetype='application/pdf'
    )
    
@app.route('/json-to-xml', methods=['POST'])
def json_to_xml():
    json_data = request.get_json()
    
    book_title = json_data.get('title')
    book_author = json_data.get('author')
    
    root = ET.Element("book")
    
    title_element = ET.SubElement(root, "title")
    title_element.text = str(book_title)
    
    author_element = ET.SubElement(root, "author")
    author_element.text = str(book_author)
    
    xml_string = ET.tostring(root, encoding='utf-8', method='xml')
    
    return Response(xml_string, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True)
