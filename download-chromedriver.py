import json
import requests
import os
from fnmatch import fnmatch
import argparse

Parser = argparse.ArgumentParser()
Parser.add_argument('--version', default='120', type=str)
args = Parser.parse_args()

def make_request(furl):
    # Make a GET request
    response = requests.get(furl)
    data = json.loads(response.text)
    return(data)
    
def transform_data(fdata):
    version = fdata['version']
    revision = fdata['revision']
    downloads = fdata['downloads']
    url = downloads.get('chromedriver', [{}])[0].get('url', False)
    
    return {
        'version': version,
        'revision': revision,
        'url': url
    }

def download_latest(fdata,ffile,fversion):
    full_path = os.path.join((os.getcwd()),ffile)
    versions = [d['url'] for d in fdata if fnmatch(d['version'], f'*{fversion}*')]
    if versions:
        print(f"downloading {versions[-1]}")
        response = requests.get(versions[-1])
        data = response.content
        with open(full_path,'wb') as f:
            f.write(data)
        
    else:
        print("No matching versions found.")

url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
version = args.version if float(args.version) > 115 else exit("Version must be greaer than 116")
file = f'chrome-driver-{version}.zip'

# script starts!
data = make_request(url)
data = [transform_data(d) for d in data['versions']]
download_latest(data,file,version)
