import streamlit as st
from annotated_text import annotated_text
import pandas as pd
import numpy as np
import plotly.express as px
import boto3
import gspread
import json
import tempfile
from oauth2client.service_account import ServiceAccountCredentials


##################################
#           FUNCTIONS            #
##################################
def read_gshseets_dataset(file_name):
    sheet = client.open(file_name).sheet1   
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    df['zpid'] = df.apply(lambda x: str(x['zpid']).split('.')[0], axis=1)
    df['num_users_label'] = df.apply(lambda x: get_total_user_labels(x), axis=1)
    df['label_category'] = df.apply(lambda x: get_label_category(x), axis=1)
    df['final_label'] = df.apply(lambda x: get_final_label(x), axis=1)
    return df, sheet


def get_total_user_labels(x):
    i = 0
    for c in ['ariel', 'liam', 'maddy']:
        if x[c] != None:
            if x[c] != '':
                i += 1
    return i

def get_label_category(x):
    labels = []
    for c in ['ariel', 'liam', 'maddy']:
        if x[c] != None:
            if x[c] != '':
                labels.append(x[c])
    if len(labels) == 0:
        return 'not labeled'
    if len(labels) == 1:
        return 'single label'
    if len(labels) == 2:
        if len(list(set(labels))) == 1:
            return 'confirmed label'
        else:
            return 'discrepancy'
    if len(labels) == 3:
        if len(list(set(labels))) == 2:
            return 'confirmed label'
        elif len(list(set(labels))) == 3:
            return 'discrepancy'
        
def get_final_label(x):
    labels = []
    for c in ['ariel', 'liam', 'maddy']:
        if x[c] != None:
            if x[c] != '':
                labels.append(x[c])

    if x['label_category'] == 'confirmed label':
        return max(labels,key=labels.count)
    else:
        return None

def read_json_file(bucket, key):
    """
    Reads json file from s3

    Args:
        bucket [string]: Bucket path
        key [string]: File path

    Returns:
        json object
    """
    
    # Initialize boto3 to use the S3 client.
    s3_client = boto3.client('s3', 
        aws_access_key_id=st.secrets["AWS_ACCESS_KEY"],
          aws_secret_access_key=st.secrets["AWS_SECRET_KEY"])

    # Get the file inside the S3 Bucket
    s3_response = s3_client.get_object(
        Bucket=bucket,
        Key=key
    )

    # Get the Body object in the S3 get_object() response
    s3_object_body = s3_response.get('Body')

    # Read the data in bytes format
    content = s3_object_body.read()

    return json.loads(content)


##################################
#             SET UP             #
##################################
st.set_page_config(layout="wide")
st.title("ML Labeling Tool: Property Condition")
st.markdown("###### Label property description to determine condition")


config = read_json_file(bucket='residentialpropertydata', key='api/gdrive_creds.json')
tfile = tempfile.NamedTemporaryFile(mode="w+")
json.dump(config, tfile)
tfile.flush()


# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name(tfile.name, scope)#'gdrive_creds.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

labeled_data_fn = "ml_training_prop_cond_dscr_20231228"


##################################
#              APP               #
##################################
tab1, tab2, tab3 = st.tabs(["Login", "Label", "Analytics"])


##################################
#             TAB 1              #
##################################

df, sheetState = read_gshseets_dataset(file_name=labeled_data_fn)
tab1.write(df.head())




