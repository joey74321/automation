# image_to_pdf.py

from fpdf import FPDF


class ImageToPdf:
    def __init__(self, input_images, output_pdf):
        """
        Initialize the ImageToPdf class.

        Parameters:
        - input_images (list): List of paths to input image files.
        - output_pdf (str): Path to the output PDF file.
        """
        self.input_images = input_images
        self.output_pdf = output_pdf

    def convert_images_to_pdf(self):
        """
        Convert a list of input images to a single PDF file.

        The method uses the FPDF library to create a PDF file and adds each image as a page.

        Note: Assumes A4 page size (adjust as needed).
        """
        pdf = FPDF()
        for image_path in self.input_images:
            pdf.add_page()
            pdf.image(image_path, 0, 0, 210, 297)  # Assuming A4 page size (adjust as needed)
        pdf.output(self.output_pdf)
