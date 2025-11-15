#!/usr/bin/env python3
"""
Extract paragraphs from images in OCR_BW folder using LLM vision model.
Outputs the extracted text in markdown format.
"""

import asyncio
from pathlib import Path
from pydantic_ai import Agent, BinaryContent
from langfuse import get_client
from dotenv import load_dotenv

load_dotenv()

langfuse = get_client()

# Verify connection
if langfuse.auth_check():
    print("Langfuse client is authenticated and ready!")
    Agent.instrument_all()
else:
    print("Authentication failed. Please check your credentials and host.")

# OCR Vision Agent (using the same model as sample agent.py)
ocr_vision_agent = Agent(
    'openrouter:google/gemini-2.5-flash-lite',
    system_prompt="""You are an OCR (Optical Character Recognition) specialist. 
Your task is to extract all text content from images, preserving the structure and formatting as much as possible.

When extracting text:
- Maintain paragraph breaks and structure
- Preserve headings, subheadings, and titles
- Keep lists and bullet points intact
- Maintain numerical data and tables structure where possible
- Output the text in clean, readable markdown format

Return the extracted text as markdown, organizing it with proper headings and paragraphs."""
)


async def extract_text_from_image(image_path: Path) -> str:
    """
    Extract text from a single image using the OCR vision agent.
    
    Args:
        image_path: Path to the image file
    
    Returns:
        Extracted text in markdown format
    """
    if not image_path.exists():
        raise ValueError(f"Image file not found: {image_path}")
    
    # Read image data
    image_data = image_path.read_bytes()
    
    # Run the OCR agent with the image
    result = await ocr_vision_agent.run(
        [
            "Extract all text content from this image. Format it as clean markdown with proper paragraphs, headings, and structure. Preserve the original formatting and organization as much as possible.",
            BinaryContent(data=image_data, media_type='image/png'),
        ],
    )
    
    return result.output


async def process_all_images(input_dir: str, output_dir: str = None):
    """
    Process all PNG images in the input directory and extract text.
    
    Args:
        input_dir: Directory containing input images
        output_dir: Optional directory to save markdown output files
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' not found!")
        return
    
    # Get all PNG files from input directory
    png_files = sorted(input_path.glob("*.png"))
    
    if not png_files:
        print(f"Warning: No PNG files found in '{input_dir}'")
        return
    
    print(f"Found {len(png_files)} PNG image(s) in '{input_dir}'")
    print(f"Processing images with OCR vision agent...\n")
    
    # Create output directory if specified
    output_path = None
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        print(f"Output directory: {output_path.absolute()}\n")
    
    # Process each image
    for img_path in png_files:
        print(f"Processing: {img_path.name}...")
        try:
            # Extract text from image
            extracted_text = await extract_text_from_image(img_path)
            
            # Create markdown header with image name
            markdown_content = f"# {img_path.stem}\n\n"
            markdown_content += f"**Source Image:** `{img_path.name}`\n\n"
            markdown_content += "---\n\n"
            markdown_content += extracted_text
            markdown_content += "\n\n"
            
            # Save to file if output directory is specified
            if output_path:
                output_file = output_path / f"{img_path.stem}.md"
                output_file.write_text(markdown_content, encoding='utf-8')
                print(f"  ✓ Saved to: {output_file.name}")
            else:
                # Print to console
                print(f"  ✓ Extracted text:")
                print("-" * 80)
                print(markdown_content)
                print("-" * 80)
                print()
            
        except Exception as e:
            print(f"  ✗ Error processing {img_path.name}: {e}\n")
    
    print(f"\nOCR processing complete!")
    if output_path:
        print(f"All markdown files saved to: {output_path.absolute()}")


async def main():
    """Main function to process images."""
    # Input and output directories
    input_directory = "OCR_BW"
    output_directory = "OCR_MD"  # Optional: set to None to print to console only
    
    # Process all images
    await process_all_images(input_directory, output_directory)


if __name__ == "__main__":
    asyncio.run(main())

