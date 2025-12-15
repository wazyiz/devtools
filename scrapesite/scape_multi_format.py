import requests
import os
import re
from urllib.parse import urlparse

# --- Configuration (Based on your input) ---
BASE_API_URL = 'https://4jyhe6vpvb.execute-api.af-south-1.amazonaws.com/prod/v1/documents/list' 
DOWNLOAD_DIR = 'downloaded_files_organized' # Renamed main directory for clarity
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# --- JSON Path Configuration ---
JSON_LIST_KEY = 'data'   
FILE_URL_KEY = 'doc_url' 
FILE_NAME_KEY = 'title'  
CATEGORY_KEY = 'category' # Used for subfolders
# -----------------------------------------------------------------

def clean_filename(name):
    """Sanitize the name to be safe for use as a directory or file name."""
    # Remove characters that are illegal in file paths and replace spaces with underscores
    cleaned = re.sub(r'[^\w\-_\. ]', '', name).strip()
    return cleaned.replace(' ', '_')

def get_filename_from_url(url, fallback_name):
    """
    Extracts the filename and extension from the URL. 
    If not found, it uses the fallback_name and tries to append a common extension if missing.
    """
    try:
        # 1. Try to get filename and extension from the URL path
        parsed_url = urlparse(url)
        path = parsed_url.path
        url_filename = os.path.basename(path).split('?')[0] # remove query string from filename
        
        # If the URL filename has an extension, use it
        if '.' in url_filename and len(url_filename.split('.')[-1]) <= 5: 
            return clean_filename(url_filename)

    except Exception:
        pass # Fall through to use fallback name

    # 2. Use the fallback name (the document title)
    # Check if the fallback name already has a common extension
    common_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.jpeg', '.png', '.zip', '.xlsx', '.csv']
    fallback_name_lower = fallback_name.lower()

    for ext in common_extensions:
        if fallback_name_lower.endswith(ext):
            return clean_filename(fallback_name)

    # If no extension is found (e.g., just a title), append a common generic extension (optional, but safer)
    return f"{clean_filename(fallback_name)}.file" # Using .file as a generic safety extension


def download_file(url, folder_path, file_name):
    """Downloads a single file to the specified folder without checking for specific Content-Types."""
    
    final_path = os.path.join(folder_path, file_name)

    try:
        response = requests.get(url, stream=True, headers=HEADERS, timeout=30)
        response.raise_for_status() 

        # We skip the Content-Type check here to allow all file types (doc, jpg, zip, etc.)

        with open(final_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk: 
                    f.write(chunk)
        print(f"  -> Downloaded: {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"  -> Failed to download {file_name} from {url}: {e}")

def scrape_and_download_by_category():
    """Main function to scrape the API endpoint and download files into category subfolders."""
    
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    print(f"\n--- Fetching data from API endpoint: {BASE_API_URL} ---")

    try:
        # 1. Make the API request
        response = requests.get(BASE_API_URL, headers=HEADERS, timeout=30)
        response.raise_for_status() 
        
        data = response.json()
        
        # 2. Extract the list of files
        file_list = data.get(JSON_LIST_KEY, [])
        
        if not file_list:
            print(f"No documents found under the key '{JSON_LIST_KEY}'. Check configuration.")
            return
        
        print(f"Found {len(file_list)} documents to process.")

        # 3. Loop through the files, determine category, and download
        for file_info in file_list:
            pdf_url = file_info.get(FILE_URL_KEY)
            pdf_title = file_info.get(FILE_NAME_KEY)
            category = str(file_info.get(CATEGORY_KEY, 'Uncategorized')) # Default to 'Uncategorized' if key is missing
            
            # Determine the subfolder name
            category_folder_name = clean_filename(category)
            category_folder_path = os.path.join(DOWNLOAD_DIR, category_folder_name)
            os.makedirs(category_folder_path, exist_ok=True)
            
            if pdf_url and pdf_title:
                final_filename = get_filename_from_url(pdf_url, pdf_title)
                print(f"Processing: {pdf_title} (Category: {category})")
                download_file(pdf_url, category_folder_path, final_filename)
            elif pdf_url:
                 print(f"  -> Skipped a document with URL: {pdf_url} (Missing title/name key: '{FILE_NAME_KEY}')")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}. Check URL and ensure it's accessible.")
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON response. The API might not be returning valid JSON.")
    except requests.exceptions.RequestException as e:
        print(f"A connection error occurred: {e}")

    print("\n--- Scraping process finished ---")

if __name__ == "__main__":
    scrape_and_download_by_category()
