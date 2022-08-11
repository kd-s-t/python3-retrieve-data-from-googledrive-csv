from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


app.run(host = '0.0.0.0', port = 8080)