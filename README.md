# Retrieving data from google drive csv using python 3  
  
## usage  
Step1: python3 index.py  
Step2: Authenticate Google  
Step3: Open http://127.0.0.1:8080/cols=date,campaign,clicks,spend,medium,source  
  
## explanation  
1. we need to setup client_secret.json in google drive  
2. after open the API, it will generate `test_task_data.csv`, this is complete columns  
3. it will also generate `data.json` with specific column  
4. it will also return a json containing the csv data  
