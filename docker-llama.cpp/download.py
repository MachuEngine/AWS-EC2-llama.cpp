import os
from huggingface_hub import snapshot_download

token = os.getenv("HF_TOKEN")

snapshot_download(
    repo_id="google/gemma-2-2b-it",
    # repo_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
    local_dir="models/gemma-2-2b-it",
    # local_dir="models/Meta-Llama-3.1-8B-Instruct",
    token=token,
    ignore_patterns=["original/*"],
    # local_dir_use_symlinks 파라미터 제거
)
