import pandas as pd
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.client import GoogleCredentials
from urllib.parse import urlparse
from urllib.parse import parse_qs

app = Flask(__name__)

CORS(app)

@app.route("/", methods=['GET'])
def home():
  gauth = GoogleAuth()
  gauth.LocalWebserverAuth()
  page = request.args.get('cols', default = 'date,campaign,clicks,spend,medium,source', type = int)
  columns = page.split(",")

  drive = GoogleDrive(gauth)
  fileDownloaded = drive.CreateFile({"id":"1zLdEcpzCp357s3Rse112Lch9EMUWzMLE"})
  fileDownloaded.GetContentFile("test_task_data.csv")
  df = pd.read_csv("test_task_data.csv",usecols=columns)
  df.to_json('data.json')
  df.head()

  f = open('data.json')
  data = json.load(f)
  return jsonify({
    "status": "success",
    "message": "Retrieving data from Google drive test_task_data.csv",
    "data": data,
    "list":list
  })


if __name__ == '__main__':
	# app.run(debug=True)
  app.run(host = '0.0.0.0', port = 8080)