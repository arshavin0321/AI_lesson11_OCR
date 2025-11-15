#!/usr/bin/env python3
"""
Convert images from OCR_PNG folder to grayscale and enhance contrast.
Saves processed images to OCR_BW folder for better OCR readability.
"""

import os
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps


def enhance_image_contrast(image: Image.Image, contrast_factor: float = 2.0) -> Image.Image:
    """
    Enhance the contrast of an image.
    
    Args:
        image: PIL Image object
        contrast_factor: Factor to enhance contrast (1.0 = no change, >1.0 = more contrast)
    
    Returns:
        Enhanced PIL Image object
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(contrast_factor)


def process_image(input_path: Path, output_path: Path, contrast_factor: float = 2.0):
    """
    Process a single image: convert to grayscale and enhance contrast.
    
    Args:
        input_path: Path to input image
        output_path: Path to save processed image
        contrast_factor: Factor to enhance contrast
    """
    # Open the image
    img = Image.open(input_path)
    
    # Convert to grayscale (L mode)
    gray_img = img.convert("L")
    
    # Enhance contrast
    enhanced_img = enhance_image_contrast(gray_img, contrast_factor)
    
    # Optionally apply autocontrast for additional enhancement
    # This normalizes the image to use the full intensity range
    final_img = ImageOps.autocontrast(enhanced_img, cutoff=2)
    
    # Save the processed image
    final_img.save(output_path, "PNG", optimize=True)
    
    print(f"Processed: {input_path.name} -> {output_path.name}")


def process_all_images(input_dir: str, output_dir: str, contrast_factor: float = 2.0):
    """
    Process all PNG images in the input directory.
    
    Args:
        input_dir: Directory containing input images
        output_dir: Directory to save processed images
        contrast_factor: Factor to enhance contrast (default: 2.0)
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(exist_ok=True)
    
    # Check if input directory exists
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' not found!")
        return
    
    # Get all PNG files from input directory
    png_files = list(input_path.glob("*.png"))
    
    if not png_files:
        print(f"Warning: No PNG files found in '{input_dir}'")
        return
    
    print(f"Found {len(png_files)} PNG image(s) in '{input_dir}'")
    print(f"Processing images with contrast factor: {contrast_factor}")
    print(f"Output directory: {output_path.absolute()}\n")
    
    # Process each image
    for img_path in sorted(png_files):
        output_file = output_path / img_path.name
        process_image(img_path, output_file, contrast_factor)
    
    print(f"\nProcessing complete! Processed images saved to: {output_path.absolute()}")


def main():
    """Main function to process images."""
    # Input and output directories
    input_directory = "OCR_PNG"
    output_directory = "OCR_BW"
    
    # Contrast enhancement factor (1.0 = no change, 2.0 = double contrast)
    contrast_factor = 2.0
    
    # Process all images
    process_all_images(input_directory, output_directory, contrast_factor)


if __name__ == "__main__":
    main()

