import streamlit as st

import boto3
from botocore.exceptions import ClientError

#Get Secrets
region_name = 'us-east-1'
db_secrets = 'mysqldb'
openapikey_secret = 'openaikey2'

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

try:
    db_secrets_value_response = client.get_secret_value(
        SecretId=db_secrets
    )

    openapikey_secret_value_response = client.get_secret_value(
        SecretId=db_secrets
    )


except ClientError as e:
    print("Error is-")
    # For a list of exceptions thrown, see
    # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    raise e

db_secrets_value = db_secrets_value_response['SecretString']
openapikey_secret_value = openapikey_secret_value_response['SecretString']




st.set_page_config(
    page_title="AWS",
    page_icon="👋",
    layout="wide"
)

st.header("Hi, welcome!")
st.subheader(db_secrets_value)
st.subheader(openapikey_secret_value)
