import huggingface_hub

def upload_file(repo_id:str, local_file:str, repo_path:str, w_token:str):
    huggingface_hub.upload_file(repo_id=repo_id, path_in_repo=repo_path, path_or_fileobj=local_file, token=w_token)
