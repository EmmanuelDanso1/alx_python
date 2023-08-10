import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        return
    
    url = sys.argv[1]
    
    response = requests.get(url)
    
    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id not found in response headers.")
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    main()