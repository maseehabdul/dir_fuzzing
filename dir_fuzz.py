import requests
import argparse

def fuzz():
    
        print("----------------------Dir fuzzing tool created by own -------------------------")
        # Create an ArgumentParser object
        parser = argparse.ArgumentParser(description="URL and Word Argument Parser")

            # Add the URL argument
        parser.add_argument("-url", "--url", required=True, help="The URL to fetch")

            # Add the word argument
        parser.add_argument("-w", "--word", required=True, help="The word to search for")


        args = parser.parse_args()

        url = args.url
        word = args.word
        
        with open(word,"r") as file:
            for line in file:
                    directory = line.strip()
                    url1 =f"{url}/{directory}"
                    
                                
                
                    response = requests.get(url1)

                    # Check the response status code
                    if response.status_code == 200:
                            print(f"Directory found: {url1}")
                    elif response.status_code == 404:
                            print(f"Not Found: {url1}")
                        
                            
             
    
        
if __name__ == "__main__":
    fuzz()

Whoxy API Key = "(?i)(?:whoxy)(?:.|[\\n\\r]){0,40}\\b([0-9a-z]{33})\\b"

