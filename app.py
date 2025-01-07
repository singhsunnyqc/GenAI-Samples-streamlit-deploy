import streamlit as st

import json
import boto3
from botocore.exceptions import ClientError

#Get Secrets
region_name = 'us-east-1'
db_secrets_key = 'mysqldb'
openapikey_secret_key = 'openaikey2'

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

try:
    db_secrets_value_response = client.get_secret_value(
        SecretId=db_secrets_key
    )

    openapikey_secret_value_response = client.get_secret_value(
        SecretId=openapikey_secret_key
    )


except ClientError as e:
    print("Error is-")
    # For a list of exceptions thrown, see
    # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    raise e


db_secrets = db_secrets_value_response["SecretString"]
openapikey_secret = openapikey_secret_value_response["SecretString"]


# if "SecretString" in db_secrets_value_response:
#     db_secrets = db_secrets_value_response["SecretString"]
# else:
#     db_secrets = db_secrets_value_response["SecretBinary"].decode("utf-8")

# if "SecretString" in openapikey_secret_value_response:
#     openapikey_secret = openapikey_secret_value_response["SecretString"]
# else:
#     openapikey_secret = openapikey_secret_value_response["SecretBinary"].decode("utf-8")


# db_secrets = db_secrets_value_response
# openapikey_secret = openapikey_secret_value_response

# db_secrets = json.loads(db_secrets) if isinstance(db_secrets, str) else db_secrets
# openapikey_secret = json.loads(openapikey_secret) if isinstance(openapikey_secret, str) else openapikey_secret


db_secrets = json.loads(db_secrets)
openapikey_secret = json.loads(openapikey_secret)

st.set_page_config(
    page_title="AWS",
    page_icon="👋",
    layout="wide"
)

st.header("Hi, welcome!")
st.subheader(db_secrets)
st.subheader(openapikey_secret)
st.subheader(openapikey_secret["openaikey2"])
st.subheader(db_secrets["username"])
st.subheader(db_secrets["password"])
st.subheader(db_secrets["host"])
st.subheader(db_secrets["port"])

# st.subheader(db_secrets["username"])
# st.subheader(db_secrets["username"])
# st.subheader(db_secrets["password"])
# st.subheader(db_secrets["host"])
# st.subheader(db_secrets["port"])

st.subheader(openapikey_secret)
