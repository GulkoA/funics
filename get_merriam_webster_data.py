import requests
import json
import os

    
def get_merriam_webster_data(word, api_key):
    """
    Retrieves pronunciation and definition data from the Merriam-Webster Elementary Dictionary API.

    Args:
        word: The word to look up.
        api_key: Your Merriam-Webster API key.

    Returns:
        A dictionary containing pronunciation and definition data, or None if the API request fails 
        or the word is not found.
    """

    url = f"https://www.dictionaryapi.com/api/v3/references/sd2/json/{word}?key={api_key}"  # URL for the API request (Elementary dictionary api)

    try:
        response = requests.get(url)
        #print(f"response.content: {response.content}") # Debug
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        data = response.json()


        if not data or not isinstance(data[0], dict) or 'hwi' not in data[0]: # Error handling for invalid responses
            print(f"Word '{word}' not found in Merriam-Webster or API response is invalid.")
            return None
        
        # Extract relevant information (pronunciation and definitions). Handle multiple pronunciations
        pronunciations = []
        if 'prs' in data[0]['hwi']:  # Check if pronunciations exist
            for pr in data[0]['hwi']['prs']:
                pronunciation = pr.get('mw', '') # Get Merriam-Webster pronunciation
                sound = pr.get('sound', {})  # Handle cases where 'sound' might be missing
                audio = sound.get('audio', '')

                # Create audio link (replace with your preferred audio format and region if needed)
                # The detailed logic from the documentation is implemented below
                if audio:
                    subdirectory = ""
                    if audio.startswith("bix"):
                        subdirectory = "bix"
                    elif audio.startswith("gg"):
                        subdirectory = "gg"
                    elif audio.startswith(tuple("0123456789_")): # Using a tuple for efficiency
                        subdirectory = "number"
                    else:
                        subdirectory = audio[0].lower()
                    
                    audio_link = f"https://media.merriam-webster.com/audio/prons/en/us/mp3/{subdirectory}/{audio}.mp3" # Using MP3 as default
                    # Download the MP3 file
                    downloaded_file = download_mp3(audio_link, word)
                    pronunciations.append({
                        'pronunciation': pronunciation, 
                        'audio_link': audio_link,
                        'local_audio_file': downloaded_file
                    })
                else:
                    pronunciations.append({'pronunciation': pronunciation}) # Handle entries without audio
        


        #Short definition is preferred for our usage
        definitions = data[0].get("shortdef", [])

        if not definitions: # Fall back to detailed definitions if shortdef is not available
            definitions = []  #  Use detailed definitions if shortdef is not available
            for item in data[0].get("def", [{}])[0].get("sseq", []):
                for sub_item in item:  # handle subsenses
                  if isinstance(sub_item, list) and sub_item[0] == "sense":
                    definitions.extend([text[1] for text in sub_item[1].get("dt", []) if text[0] == "text"])



        return {'pronunciations': pronunciations, 'definitions': definitions}


    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None

def download_mp3(url, word):
    """
    Downloads the MP3 file from the given URL.

    Args:
        url: The URL of the MP3 file.
        word: The word associated with the pronunciation.

    Returns:
        The path to the downloaded file, or None if download fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Create a 'pronunciations' directory if it doesn't exist
        os.makedirs('pronunciations', exist_ok=True)

        # Save the file
        filename = f"pronunciations/{word}.mp3"
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"Successfully downloaded pronunciation for '{word}'")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading MP3: {e}")
        return None




# Example usage (replace with your API key):

api_key = "413e9c1e-6813-49b5-b95a-aec07325f276"  
word = "hello"

word_data = get_merriam_webster_data(word, api_key)

if word_data:
    print(json.dumps(word_data, indent=4)) # Print formatted JSON data