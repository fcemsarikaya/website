from flask import Flask, redirect, render_template

app = Flask(__name__)

repos = ["run-length-encoder", "feedback-arc-set-finder", "closest-pair", "http-client-server",
         "cosmic-system-simulator"]


@app.route("/")
def home():
    return render_template("index.html", person="FCS", list=repos)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/<rep_url>")
def git_redirect(rep_url):
    return redirect("https://github.com/fcemsarikaya/{}".format(rep_url))


def repo_management(name, action):
    if action == 'a':
        if name in repos:
            print("Repository exists")
        else:
            repos.append(name)
    elif action == 'r':
        repos.remove(name)
    else:
        print("Invalid argument")


if __name__ == "__main__":
    app.run(debug=True)