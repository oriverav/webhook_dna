from flask import Flask, request, Response

app = Flask(__name__)

# '/webhook' URL where the webhook will be running in the server
# POST means that the webhook will only hear to POST requests
@app.route('/webhook', methods=['POST'])
def respond():
	print(request.json)
	print(request.json['ciscoDnaEventLink'])
	return Response(status=200)

# The app will run in all the IPs of your computer in port 5000 by default.
# App will be running with HTTPS
if __name__ == '__main__':
	app.run(host='0.0.0.0', ssl_context='adhoc')
