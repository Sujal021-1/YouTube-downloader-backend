# YouTube-downloader-backend

from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    url = request.json['url']
    video_url = None
    audio_url = None

    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        for f in info['formats']:
            if f.get('ext') == 'mp4' and f.get('acodec') != 'none':
                video_url = f.get('url')
            if f.get('ext') == 'm4a' and not f.get('vcodec'):
                audio_url = f.get('url')
    return jsonify({'video': video_url, 'audio': audio_url})

if __name__ == '__main__':
    app.run(debug=True)
    
