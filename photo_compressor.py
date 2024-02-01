# photo_compressor.py

from PIL import Image


def photo_compressor(input_path, output_path, quality=85):
    """
    Compresses a photo.

    Parameters:
    - input_path (str): Path to the input photo file.
    - output_path (str): Path to save the compressed photo.
    - quality (int): Compression quality (0 to 100, where 100 is the best). Default is 85.
    """
    try:
        img = Image.open(input_path)
        img.save(output_path, quality=quality)
        print(f"Photo compressed successfully. Saved at: {output_path}")
    except Exception as e:
        print(f"Error compressing photo: {e}")


# Example usage:
if __name__ == "__main__":
    input_photo_path = "path/to/input/photo.jpg"
    output_photo_path = "path/to/output/compressed_photo.jpg"
    photo_compressor(input_photo_path, output_photo_path)
