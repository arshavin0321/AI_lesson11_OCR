#!/usr/bin/env python3
"""
Extract specific pages from AR2024_C.pdf as PNG images.
Extracts pages 1-5 and 14, saves them to OCR_PNG folder.
"""

import pymupdf  # PyMuPDF
import os
from pathlib import Path


def extract_pdf_pages_to_images(pdf_path: str, output_dir: str, pages: list[int]):
    """
    Extract specified pages from PDF and save as PNG images.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the PNG images
        pages: List of page numbers (1-indexed, user-facing)
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Open the PDF document
    doc = pymupdf.open(pdf_path)
    
    print(f"PDF opened: {pdf_path}")
    print(f"Total pages in PDF: {len(doc)}")
    print(f"Extracting pages: {pages}")
    
    # Extract each specified page
    for page_num in pages:
        # Convert 1-indexed page number to 0-indexed
        page_index = page_num - 1
        
        # Check if page exists
        if page_index >= len(doc):
            print(f"Warning: Page {page_num} does not exist in PDF (max page: {len(doc)})")
            continue
        
        # Get the page
        page = doc[page_index]
        
        # Render page to a pixmap (image)
        # Using zoom factor of 2.0 for better quality (300 DPI equivalent)
        zoom = 2.0
        mat = pymupdf.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        
        # Save as PNG
        output_filename = output_path / f"page_{page_num:03d}.png"
        pix.save(str(output_filename))
        
        print(f"Saved: {output_filename} (size: {pix.width}x{pix.height})")
    
    # Close the document
    doc.close()
    print(f"\nExtraction complete! Images saved to: {output_path.absolute()}")


def main():
    """Main function to extract PDF pages."""
    # PDF file path
    pdf_file = "AR2024_C.pdf"
    
    # Output directory
    output_directory = "OCR_PNG"
    
    # Pages to extract (1-indexed: pages 1-5 and 14)
    pages_to_extract = [1, 2, 3, 4, 5, 14]
    
    # Check if PDF file exists
    if not os.path.exists(pdf_file):
        print(f"Error: PDF file '{pdf_file}' not found!")
        return
    
    # Extract pages
    extract_pdf_pages_to_images(pdf_file, output_directory, pages_to_extract)


if __name__ == "__main__":
    main()

