from flask import Flask,Response , render_template
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/updateTime')
def events():
    def generate():
        while True:
            # Send the current time as an SSE event
            yield f"data: {time.ctime()}\n\n"
            time.sleep(1)  # Wait 1 second before sending the next event

    # Return a streaming response with the correct SSE headers
    return Response(generate(), content_type='text/event-stream', status=200)

if __name__ == '__main__':
    app.run(debug=True)