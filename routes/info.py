from flask import Blueprint, render_template, jsonify

# Create the blueprint for the information pages
info = Blueprint('info', __name__, template_folder='templates')

# Data for the information pages
pages = [
    "Page 1",
    "Page 2",
    "Page 3"
]

about_content = "About This Project\n\n"

@info.route('/')
def index():
    return render_template('information.html', 
                          pages=pages, 
                          about_content=about_content, 
                          current_page=0,
                          total_pages=len(pages))

@info.route('/get_page/<int:page_num>')
def get_page(page_num):
    if 0 <= page_num < len(pages):
        return jsonify({
            'content': pages[page_num],
            'page_num': page_num + 1,
            'total_pages': len(pages)
        })
    return jsonify({'error': 'Page not found'}), 404

@info.route('/get_about')
def get_about():
    return jsonify({
        'content': about_content
    })
