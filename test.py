import streamlit as st
# from annotated_text import annotated_text
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import boto3
# import gspread
# import json
# import tempfile
# from oauth2client.service_account import ServiceAccountCredentials

st.write('00000' + st.secrets["aws_access_key"])

# ##################################
# #           FUNCTIONS            #
# ##################################
# def read_gshseets_dataset(file_name):
#     sheet = client.open(file_name).sheet1   
#     data = sheet.get_all_records()
#     df = pd.DataFrame(data)
#     df['zpid'] = df.apply(lambda x: str(x['zpid']).split('.')[0], axis=1)
#     df['num_users_label'] = df.apply(lambda x: get_total_user_labels(x), axis=1)
#     df['label_category'] = df.apply(lambda x: get_label_category(x), axis=1)
#     df['final_label'] = df.apply(lambda x: get_final_label(x), axis=1)
#     return df, sheet


# def get_total_user_labels(x):
#     i = 0
#     for c in ['ariel', 'liam', 'maddy']:
#         if x[c] != None:
#             if x[c] != '':
#                 i += 1
#     return i

# def get_label_category(x):
#     labels = []
#     for c in ['ariel', 'liam', 'maddy']:
#         if x[c] != None:
#             if x[c] != '':
#                 labels.append(x[c])
#     if len(labels) == 0:
#         return 'not labeled'
#     if len(labels) == 1:
#         return 'single label'
#     if len(labels) == 2:
#         if len(list(set(labels))) == 1:
#             return 'confirmed label'
#         else:
#             return 'discrepancy'
#     if len(labels) == 3:
#         if len(list(set(labels))) == 2:
#             return 'confirmed label'
#         elif len(list(set(labels))) == 3:
#             return 'discrepancy'
        
# def get_final_label(x):
#     labels = []
#     for c in ['ariel', 'liam', 'maddy']:
#         if x[c] != None:
#             if x[c] != '':
#                 labels.append(x[c])

#     if x['label_category'] == 'confirmed label':
#         return max(labels,key=labels.count)
#     else:
#         return None

# def read_json_file(bucket, key):
#     """
#     Reads json file from s3

#     Args:
#         bucket [string]: Bucket path
#         key [string]: File path

#     Returns:
#         json object
#     """
    
#     # Initialize boto3 to use the S3 client.
#     s3_client = boto3.client('s3', 
#         aws_access_key_id=st.secrets["aws_access_key"],
#           aws_secret_access_key=st.secrets["aws_secret_key"])

#     # Get the file inside the S3 Bucket
#     s3_response = s3_client.get_object(
#         Bucket=bucket,
#         Key=key
#     )

#     # Get the Body object in the S3 get_object() response
#     s3_object_body = s3_response.get('Body')

#     # Read the data in bytes format
#     content = s3_object_body.read()

#     return json.loads(content)


# ##################################
# #             SET UP             #
# ##################################
# st.set_page_config(layout="wide")
# st.title("ML Labeling Tool: Property Condition")
# st.markdown("###### Label property description to determine condition")


# config = read_json_file(bucket='residentialpropertydata', key='api/gdrive_creds.json')
# tfile = tempfile.NamedTemporaryFile(mode="w+")
# json.dump(config, tfile)
# tfile.flush()


# # define the scope
# scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# # add credentials to the account
# creds = ServiceAccountCredentials.from_json_keyfile_name(tfile.name, scope)#'gdrive_creds.json', scope)

# # authorize the clientsheet 
# client = gspread.authorize(creds)

# labeled_data_fn = "ml_training_prop_cond_dscr_20231228"


# ##################################
# #              APP               #
# ##################################
# tab1, tab2, tab3 = st.tabs(["Login", "Label", "Analytics"])


# ##################################
# #             TAB 1              #
# ##################################

# df, sheetState = read_gshseets_dataset(file_name=labeled_data_fn)
# tab1.write(df.head())











# import streamlit as st
# from streamlit_gsheets import GSheetsConnection

# # Create a connection object.
# conn = st.connection("gsheets", type=GSheetsConnection)
# st.write(dir(conn))
# df = conn.read().iloc[:,:13]
# st.write(df.head())

# st.write('client1', conn.client)
# st.write(dir(conn.client))

# st.write(conn.client.open('ml_training_prop_cond_dscr_20231228').sheet1)


# [connections.gsheets]
# spreadsheet = "https://docs.google.com/spreadsheets/d/1TJlQI2tS_NxV-OR8uUCDWsdUehaG8bjznl6EIEkQQic/edit#gid=0"

# # From your JSON key file
# type = "service_account"
# project_id = "ml-training-data-409613"
# private_key_id = "44175a94a89772fb140e391e16f20c88ab81ee03"
# private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDPHJTFUQIcyd5l\neznQ3XjtCwv8LKS8Mzzk7NEunWAYT4KUrHRVgp/lkeh1Y1ABBjqgXwRv+spV79MN\npm6aRkCJ+aA3wmiwaCrB3XvW0nu9Sds9ik7y0iXBgPyCBiM2YgCajHNY/0vfkKLf\naC+3uo1R8PcraSoIgXjE6UDx/cUTCrDtfMnlwdWY9JqkNVUGgXk7HqDxZUw3DUru\nurvBz4KFLoljDfrcfWLsuiyxWjwAXUuVpC9hnqLD1sTswyT10/a9VdLuNKd2KEyW\nPXc37Vde2UcC8m0xcZtukt887M2FA3Kltqh4EthNxNFcZLrOPKFfPobM33PZOiw7\ni7vt5UOfAgMBAAECggEAXjJim4enjU5m/wLXnd5M9IrUraHkXtBy/q+SyD+9h/EJ\ns/Lniki5zqDY+CLuLTkXCv+MNh37TrCf7hJnNXWEPvyw2Qtrr+gAomHIxEDBFKt1\nsnyoQZpAn8y5i62c8EwMeD4u7ChY6tqOqUtqgIaxZbZRxIW1H187fVuVNTq1Gl4t\n+6947hHqa3jgyBueh2acuqk37hbmCJ8KhS5ep1T1VdcZpaLE8hBMfn5/nayu3ygU\nXsmYr/vIFG7D1pwlSF5o2d44zvMqCF7bBQOfOxJASfzV6fXNg7DS5uEgHkzc70W9\nDcfX035BXpDjOHSVQsyHykRoRmKr8BXoSQbbYlLY+QKBgQDmTD6+bg1krkPuTg7G\nNYHb4uKeh4O6rfNZuM7pWzNskpAU4HhIgzfTosPUqRZv77/tC6lrmO41pZ+CvUdt\nrjM03v8r4KuszDkRYqlTWp0MCixCtr6rlU11zB/+xF9zdLdWLinLB9glKlq++P4S\ngrFS+S8NnMNAES7MVhpmoeJt5QKBgQDmOeRZUYen7pHSIF2NwFF4qRRIOkJGYYZE\n08Ne/W26Nvr5zHOctysruSQ/uaAK3bO2V1vUM0ljb9WjaeT2HjmbQqtzUFH1+EfR\ntYBVLJlue1cxH41zj6rsMCSb6/c62gDJV5oCR9G9ZQdocWbvRsd/o4b6mj+Vn+t9\nlmr7kgXzMwKBgHcxGPw4O0hThScOUUk2okoqyD1iR8RTiXJzWuud3ySfSmDzuG1X\nNIqdYBttlAZFIKFP+tSMZyVu3fqteg2DLk975rdP5apeXF7qIFbavBNiJHw21sI5\nWMjR5/FUs04vJ0A8TjcdjTnXDPZwKhdsethFzZuO+eLrwbvSCIH74RQdAoGAC4Pt\nxgHr9RxbstTnmQV7jbt3Rj2Tvw11t8+XwBKRAHVrjD8LsVUAFcnG5GEWfjSknoQ0\nFaMTEqQvXWMYjq7oVrm49aWY0+K9ROH9L0VxzzLgI5bebl9LP1ERI7NjxE/PJkL5\ncw/Aj+aTvkedzG4P4HR/dd1tPMCo+LkjVL3zCj0CgYBKXpPUQwXLaPV3iDjMSLXn\nqV/TGrwZkqm5G8FFzn2aRCEKdnLjJs+Gjvkp93/iAD6us2bjfKECmyWS3V7bVdiC\n2Mmqdrg6UUfI5lj6GZu760/QYJelTUfdXUhxt2qRnWykrzq0gQs87MbbIMCHjfkf\nXyDTsBqhBYSiS6wBblk0ZQ==\n-----END PRIVATE KEY-----\n"
# client_email = "gdrive-service-account@ml-training-data-409613.iam.gserviceaccount.com"
# client_id = "102901218807592202019"
# auth_uri = "https://accounts.google.com/o/oauth2/auth"
# token_uri = "https://oauth2.googleapis.com/token"
# auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
# client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/gdrive-service-account%40ml-training-data-409613.iam.gserviceaccount.com"
