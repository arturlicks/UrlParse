from flask import Flask, render_template, request

app = Flask(__name__)


class UrlSplit:
    def __init__(self, wdparameter, value):
        self.wdparameter = wdparameter
        self.value = value


@app.route('/')
def home():
    return render_template('main.html', pagetitle='URL Parser')


@app.route('/result', methods=['POST', ])
def splitanddisplay():
    # Split the application URL from the parameters
    urlafter = request.form['urlin'].split('?')
    # After the split, the first index of the array is the hostname + application
    objecturl = UrlSplit('Application', urlafter[0])
    list = [objecturl]
    # Create the array of keypairs from the URL parameters: Parameter Value
    parameterssplit = urlafter[1].split('&')
    # Loop on the parameter array to Split the parameter and value by = character
    for parameter in parameterssplit:
        # For each entry the parameter must be split from the property and the value
        last = parameter.split('=')
        objecturl = UrlSplit(last[0], last[1])
        list.append(objecturl)

    return render_template('result.html', pagetitle='Result Table', completelist=list)


app.run()
