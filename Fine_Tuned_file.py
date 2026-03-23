import os
from dotenv import load_dotenv
from huggingface_hub import snapshot_download

# Load environment variables from .env file
load_dotenv()

snapshot_download(
    repo_id="TuShar2309/nokia-isam-bge-large",
    local_dir="./nokia-isam-bge-large",
    token=os.getenv("HF_TOKEN")  # your HF token
)
print("✅ Model downloaded")