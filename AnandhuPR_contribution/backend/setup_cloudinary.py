"""
Helper script to set up Cloudinary credentials.
"""
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_cloudinary_config():
    # Get Cloudinary credentials from environment variables
    cloud_name = os.environ.get("CLOUDINARY_CLOUD_NAME")
    api_key = os.environ.get("CLOUDINARY_API_KEY")
    api_secret = os.environ.get("CLOUDINARY_API_SECRET")
    
    # Check if all credentials are present
    if not all([cloud_name, api_key, api_secret]):
        print("Error: Missing Cloudinary credentials!")
        print("  - CLOUDINARY_CLOUD_NAME")
        print("  - CLOUDINARY_API_KEY")
        print("  - CLOUDINARY_API_SECRET")
        return False
    
    # Configure Cloudinary
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )
    
    # Test the connection
    try:
        response = cloudinary.api.ping()
        print("Cloudinary connection successful!")
        print(f"Connected to cloud: {cloud_name}")
        
        # Create the pothole_detection folder if it doesn't exist
        try:
            cloudinary.api.create_folder("pothole_detection")
            print("Created 'pothole_detection' folder")
        except Exception:
            print("'pothole_detection' folder already exists")
            
        return True
    except Exception as e:
        print(f"Error connecting to Cloudinary: {e}")
        return False

if __name__ == "__main__":
    print("Testing Cloudinary configuration...")
    test_cloudinary_config()
