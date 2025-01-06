import streamlit as st

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "mysqldb"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    print("================")
    print(secret)
    print("================")
    return secret

st.set_page_config(
    page_title="AWS",
    page_icon="👋",
    layout="wide"
)

st.header("Hi, welcome!")
st.subheader(get_secret())
