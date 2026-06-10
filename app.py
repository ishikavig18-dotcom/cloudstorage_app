from flask import Flask, render_template, request, redirect, session, url_for
from authlib.integrations.flask_client import OAuth
import boto3
import os
import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

BUCKET_NAME = os.getenv("BUCKET_NAME")
REGION = os.getenv("REGION")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION
)

app = Flask(__name__)

app.secret_key = "cloud_storage_secret_key"

# ==========================
# AWS S3 CONNECTION
# ==========================

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION
)

# ==========================
# GOOGLE OAUTH
# ==========================

oauth = OAuth(app)

google = oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url=
    "https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile"
    }
)

# ==========================
# HOME
# ==========================

@app.route('/')
def home():

    if 'user' not in session:
        return render_template('login.html')

    files = []

    try:

        response = s3.list_objects_v2(
            Bucket=BUCKET_NAME
        )

        if 'Contents' in response:

            for obj in response['Contents']:

                files.append(
                    {
                        "name": obj['Key'],
                        "size": round(obj['Size']/1024, 2)
                    }
                )

    except Exception as e:
        print(e)

    return render_template(
        'index.html',
        files=files,
        user=session['user']
    )

# ==========================
# GOOGLE LOGIN
# ==========================

@app.route('/login')
def login():

    return google.authorize_redirect(
        url_for(
            'authorize',
            _external=True
        )
    )

# ==========================
# GOOGLE CALLBACK
# ==========================

@app.route('/authorize')
def authorize():

    token = google.authorize_access_token()

    user = token['userinfo']

    session['user'] = user

    return redirect('/')

# ==========================
# LOGOUT
# ==========================

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')

# ==========================
# TEST S3
# ==========================

@app.route('/test-s3')
def test_s3():

    buckets = s3.list_buckets()

    result = ""

    for bucket in buckets['Buckets']:
        result += bucket['Name'] + "<br>"

    return result

# ==========================
# UPLOAD
# ==========================

@app.route('/upload', methods=['POST'])
def upload():

    if 'user' not in session:
        return redirect('/')

    if 'file' not in request.files:
        return redirect('/')

    file = request.files['file']

    if file.filename == '':
        return redirect('/')

    s3.upload_fileobj(
        file,
        BUCKET_NAME,
        file.filename
    )

    return redirect('/')

# ==========================
# DOWNLOAD
# ==========================

@app.route('/download/<path:filename>')
def download_file(filename):

    url = s3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': BUCKET_NAME,
            'Key': filename
        },
        ExpiresIn=3600
    )

    return redirect(url)

# ==========================
# SHARE
# ==========================

@app.route('/share/<path:filename>')
def share_file(filename):

    share_url = s3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': BUCKET_NAME,
            'Key': filename
        },
        ExpiresIn=86400
    )

    return f"""
    <h2>Share Link</h2>

    <textarea rows='8' cols='100'>
{share_url}
    </textarea>

    <br><br>

    <a href="/">Back</a>
    """

# ==========================
# DELETE
# ==========================

@app.route('/delete/<path:filename>')
def delete_file(filename):

    s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=filename
    )

    return redirect('/')

# ==========================
# RUN
# ==========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)