from flask import Flask, request, render_template_string

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>

<head>
    <title>Multiplication Table</title>
</head>

<body>

<h1>Multiplication Table Generator</h1>

<form method="POST">

<label>Enter a number:</label>

<input
type="number"
name="number"
required>

<br><br>

<button type="submit">
Generate
</button>

</form>

{% if number %}

<h2>Table of {{ number }}</h2>

{% for i in range(1,11) %}

<p>{{number}} × {{i}} = {{number*i}}</p>

{% endfor %}

{% endif %}

</body>

</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    number = None

    if request.method == "POST":
        number = int(request.form["number"])

    return render_template_string(
        template,
        number=number
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)