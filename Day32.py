# Creating Command line utility in python
import argparse
import requests



def download_file(url,local_filename):
    # Note the stream= true parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size = 8195):
                # if you have chunk encoded response uncomment if
                # set chunk_size parameter to none.
                #if chunk
                f.write(chunk)
            return local_filename

parser = argparse.ArgumentParser()

# Add command line Arguments
parser.add_argument('url', help="Url of the file to download")
# parser.add_argument('output', help="By which name do You want to save file")
parser.add_argument('-o','--output',help="Name of the file",default=None)

args = parser.parse_args()
print(args.url)
print(args.output)
download_file(args.url,args.output)