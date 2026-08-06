import base64
import os
from PIL import Image, ImageDraw

def generate_halftone(img, grid_size=4, bg_color=(9, 9, 11), dot_color=(56, 189, 248)):
    img_gray = img.convert('L')
    width, height = img_gray.size
    halftone = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(halftone)
    
    pixels = img_gray.load()
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            avg = 0
            count = 0
            for i in range(grid_size):
                for j in range(grid_size):
                    if x+i < width and y+j < height:
                        avg += pixels[x+i, y+j]
                        count += 1
            if count > 0:
                avg = avg / count
            
            radius = (avg / 255.0) * (grid_size / 2)
            if radius > 0.5:
                cx, cy = x + grid_size/2, y + grid_size/2
                draw.ellipse((cx-radius, cy-radius, cx+radius, cy+radius), fill=dot_color)
                
    return halftone

from rembg import remove

def process_portrait(image_path, bg_color, dot_color):
    # Load original and remove background
    input_img = Image.open(image_path).convert("RGB")
    no_bg_img = remove(input_img).convert("RGBA")
    
    # Square crop based on the isolated subject (using the center)
    w, h = no_bg_img.size
    min_dim = min(w, h)
    left = (w - min_dim) / 2
    top = (h - min_dim) / 2
    right = (w + min_dim) / 2
    bottom = (h + min_dim) / 2
    
    cropped = no_bg_img.crop((left, top, right, bottom))
    cropped = cropped.resize((400, 400), Image.Resampling.LANCZOS)
    
    # Composite over solid background color
    bg = Image.new("RGBA", (400, 400), bg_color + (255,))
    blended = Image.alpha_composite(bg, cropped).convert("RGB")
    
    return generate_halftone(blended, grid_size=4, bg_color=bg_color, dot_color=dot_color)

def to_base64(img):
    import io
    buffered = io.BytesIO()
    img.save(buffered, format="PNG", optimize=True)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def main():
    input_path = "Photo.jpeg"
    assets_dir = r"assets"
    os.makedirs(assets_dir, exist_ok=True)
    
    print("Processing Dark Theme Portrait...")
    # Dark Theme: #09090B background, #38BDF8 cyan dots
    dark_img = process_portrait(input_path, bg_color=(9, 9, 11), dot_color=(56, 189, 248))
    dark_b64 = to_base64(dark_img)
    with open(os.path.join(assets_dir, "portrait_dark.b64"), "w") as f:
        f.write(dark_b64)
        
    print("Processing Light Theme Portrait...")
    # Light Theme: #FAFAFA background, #0F172A slate dots
    light_img = process_portrait(input_path, bg_color=(250, 250, 250), dot_color=(15, 23, 42))
    light_b64 = to_base64(light_img)
    with open(os.path.join(assets_dir, "portrait_light.b64"), "w") as f:
        f.write(light_b64)

    print("Success! Base64 assets saved to assets directory.")

if __name__ == "__main__":
    main()
