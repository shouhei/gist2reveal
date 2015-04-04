from flask import Flask
from flask import render_template
import requests
import pypandoc

app = Flask(__name__)

@app.route("/<id>")
def md2reveal(id=None):
    if id is None:
        abort(400)
    r = requests.get('https://api.github.com/gists/'+id)
    r_dict = r.json()
    response = {}
    for data in r_dict["files"].values():
        response["body"] = pypandoc.convert(data["content"],'revealjs',format='md', extra_args=['--slide-level=2'])
        response["title"] = data['filename']
    return render_template('index.html',title=response['title'], body=response['body'])

if __name__ == "__main__":
    app.run()
