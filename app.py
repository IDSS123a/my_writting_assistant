from flask import Flask, render_template, request
import random

# Create Flask app instance
app = Flask(__name__)

class MyWritingAssistant:
    def __init__(self):
        self.author_name = ""
        self.theme_description = ""
        self.num_chapters = 0
        self.about_author = ""
        self.book_title = ""
        self.chapter_titles = []
        self.min_chars = {
            "preface": 0,
            "chapter": 0,
            "epilogue": 0,
            "about_author": 0
        }
    
    def generate_book_title(self):
        themes = self.theme_description.split()
        title = f"Putovanje u svijet: {' '.join(themes[:3])}..."
        return title.capitalize()
    
    def generate_chapter_content(self, chapter):
        return f"U {chapter}, tema se razvija kroz prizmu ličnih iskustava, suočavanje s poteškoćama, ali i prihvatanje neizbežnog. Tu ne postoji 'dobre i loše strane', već samo duboki momenti introspekcije."
    
    def generate_preface(self):
        return f"U svakom knjigama postoji ona početna tačka, trenutak kada postajemo svestan nečega više. Ova knjiga istražuje upravo to – ne samo temu {self.theme_description}, već i nas same kroz očigledne i skriveno mudre detalje."
    
    def generate_about_author(self):
        return f"{self.author_name} je osoba koja razmišlja dublje od običnog posmatrača. Njegovo razumevanje sveta nije površno, već podloženo introspekciji i detaljnoj analizi složenih tema."
    
    def generate_epilogue(self):
        return "Na kraju, knjiga postaje više od sledeće stranice. To je iskustvo koje ostaje u vama, dugo nakon što ste je završili."

@app.route('/', methods=['GET', 'POST'])
def home():
    assistant = MyWritingAssistant()
    if request.method == 'POST':
        assistant.author_name = request.form['author_name']
        assistant.theme_description = request.form['theme_description']
        assistant.num_chapters = int(request.form['num_chapters'])
        assistant.about_author = request.form['about_author']
        
        # Generating book details
        assistant.book_title = assistant.generate_book_title()
        assistant.chapter_titles = [f"Poglavlje {i+1}" for i in range(assistant.num_chapters)]
        
        # Generating sections of the book
        preface = assistant.generate_preface()
        about_author = assistant.generate_about_author()
        epilogue = assistant.generate_epilogue()
        chapter_contents = [assistant.generate_chapter_content(chapter) for chapter in assistant.chapter_titles]
        
        return render_template('book_details.html',
                            book_title=assistant.book_title,
                            chapter_titles=assistant.chapter_titles,
                            preface=preface,
                            about_author=about_author,
                            epilogue=epilogue,
                            chapter_contents=chapter_contents)
    
    return render_template('index.html')

# This is important for gunicorn to find the app
application = app

if __name__ == "__main__":
    app.run(debug=True)