import os
import boto3
from github import Github

def download_data():

    local_directory = "md/files"

    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    g = Github("api-key")

    organization_name = "aws-samples"

    org = g.get_organization(organization_name)

    limit = 1000
    c = 0

    for repo in org.get_repos():
        if c >= limit:
            break
        
        for content_file in repo.get_contents(""):
            file_name = content_file.name

            if file_name.endswith(".md") and not (
                file_name=="CODE_OF_CONDUCT.md" or 
                file_name=="CONTRIBUTING.md" or 
                file_name=="NOTICE.md" or 
                file_name=="LICENSE.md"):
            

                content = content_file.decoded_content.decode("utf-8")

                if len(content) <= 1500:
                    continue
                
                path = content_file.url.split("/")[5:]
                file_path = "-".join(path[:-1])

                local_file_path = os.path.join(local_directory, file_path+"-"+content_file.name)

                with open(local_file_path, "w", encoding="utf-8") as file:
                    file.write(content)

                c+=1
                

                #print(f"Downloaded: {file_path+'-'+content_file.name} to {local_file_path}")}


def upload_data():

    s3 = boto3.client("s3")

    directory_path = "./md/files"

    bucket = "aygo-ia-project"

    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            s3.upload_file(
                Filename="./md/files/"+filename,
                Bucket= bucket,
                Key="data/"+filename,
            )
            print(f"Uploaded: {filename} to {bucket} bucket")


def main():
    download_data()
    upload_data()

if __name__ == "__main__":
    main()