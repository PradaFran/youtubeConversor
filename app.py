from pytube import YouTube
from flask import Flask, render_template, request

app = Flask(__name__)
#
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        Download(link)
    return render_template('index.html') 
def Download(link):
    try:
        youtube_object = YouTube(link)
        youtube_stream = youtube_object.streams.get_highest_resolution()
        youtube_stream.download(output_path='downloads')
        print("Download is completed successfully")
    except Exception as e:
        print(f"An error has occurred: {str(e)}")

if __name__ == '__main__': # 
    app.run()