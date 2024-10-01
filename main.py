from flask import Flask, render_template, request
from news import get_news_from_rbc

app = Flask(__name__)

@app.route('/')
def index():
    count = request.args.get('count', default=3, type=int)
    count = min(max(count, 1), 10)  # Ограничиваем количество новостей от 1 до 10

    news = {
        'rbc': get_news_from_rbc(limit=count),
    }
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run()
