import os
import requests
from tqdm import tqdm

def download_model(url, model_name):
    """Downloads a llamafile model from a URL and
      saves it to the llamafile directory."""

    llamafile_dir = "llamafile"
    if not os.path.exists(llamafile_dir):
        os.makedirs(llamafile_dir)

    file_path = os.path.join(llamafile_dir, model_name)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))
        with open(file_path, "wb") as f, tqdm(
            desc=f"Downloading {model_name}", total=total_size,
            unit="B", unit_scale=True, unit_divisor=1024
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                bar.update(len(chunk))


        print(f"Downloaded {model_name} successfully to {file_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {model_name}: {e}")
        return False

if __name__ == "__main__":
    models = {
        "TinyLlama-1.1B-Chat-v1.0.F16.llamafile":
        "https://huggingface.co/Mozilla/TinyLlama-1.1B-Chat-v1.0-llamafile/resolve/main/TinyLlama-1.1B-Chat-v1.0.F16.llamafile?download=true",
        "rocket-3b.Q5_K_M.llamafile":
        "https://huggingface.co/Mozilla/rocket-3B-llamafile/resolve/main/rocket-3b.Q5_K_M.llamafile?download=true",
    }

    for model_name, url in models.items():
        download_model(url, model_name)