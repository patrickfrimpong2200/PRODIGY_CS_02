import numpy as np
from PIL import Image
import argparse

# Encrypt an image using XOR operation and a random mask
def custom_encrypt(input_image_path, output_image_path, encryption_key):
    try:
        image = Image.open(input_image_path)
        image_array = np.array(image)

        np.random.seed(encryption_key)  # Set seed for reproducibility
        random_mask = np.random.randint(0, 256, image_array.shape, dtype=np.uint8)

        encrypted_array = np.bitwise_xor(image_array, random_mask)
        encrypted_image = Image.fromarray(encrypted_array)
        encrypted_image.save(output_image_path)
        print(f"Image successfully encrypted and saved as {output_image_path}")

    except Exception as e:
        print(f"Error during encryption: {e}")

# Decrypt an image by applying XOR operation again with the same key
def custom_decrypt(input_image_path, output_image_path, decryption_key):
    try:
        custom_encrypt(input_image_path, output_image_path, decryption_key)  # XOR again to decrypt
        print(f"Image successfully decrypted and saved as {output_image_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")

# Main function to handle the script execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom Image Encryption/Decryption Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Select mode: encrypt or decrypt")
    parser.add_argument("input", help="Path to the input image file")
    parser.add_argument("output", help="Path to save the output image")
    parser.add_argument("key", type=int, help="Key for encryption/decryption (integer)")

    args = parser.parse_args()

    # Execute the appropriate action based on user input
    if args.mode == "encrypt":
        custom_encrypt(args.input, args.output, args.key)
    elif args.mode == "decrypt":
        custom_decrypt(args.input, args.output, args.key)
