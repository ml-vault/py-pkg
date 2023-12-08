import os
import re
from mlvault.config import get_r_token
from mlvault.datapack.main import DataTray, export_data_from_dataset
from mlvault.util import find_args, is_image
from PIL import Image
from datasets.dataset_dict import IterableDatasetDict
from datasets import load_dataset

def print_help():
    print("Usage: mlvcli data extract <options>")
    print("Options:")
    print("  -f <class filter> : quotes are required, comma separated")
    print("  -r <repo name>")
    print("  -d <dest dir>")

def run_extract(args:list[str]):
    tokens_raw = find_args(args, "-f")
    repo_name = find_args(args, "-r")
    dest_dir = find_args(args, "-d")
    filters = list(map(lambda token: token.strip(), tokens_raw.split(","))) if tokens_raw else []
    exclude_filters = find_args(args, "-e")
    exclude_filters = list(map(lambda token: token.strip(), exclude_filters.split(","))) if exclude_filters else []
    print(exclude_filters)
    if dest_dir:
        dest_dir = dest_dir if dest_dir.startswith("/") else os.path.join(os.getcwd(), dest_dir)
    else :
        dest_dir = os.getcwd()
    os.makedirs(dest_dir, exist_ok=True)
    if not repo_name:
        print("Please provide a repo name")
        print_help()
        exit(1)
    else:
        dataset: IterableDatasetDict = load_dataset(repo_name, split="train", token=get_r_token()) # type: ignore
        export_data_from_dataset(dataset, dest_dir, filters=filters, exclude_filters=exclude_filters)