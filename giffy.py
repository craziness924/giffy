from PIL import Image
import argparse
import os

def make_gif(input, duration):
    output = os.path.join(input, "output.gif")
    
    start_image = None
    images = []

    for file in sorted(os.listdir(input)):
        file_path = os.path.join(input, file)
        file_type = os.path.splitext(file_path)[1]
        
        if file_type not in [".png", ".jpg", ".jpeg", ".gif"] or file_path == output:
            continue

        img = Image.open(file_path)

        images.append(img)
        
    start_image: Image = images[0]

    start_image.save(output, save_all=True, append_images=images, duration=float(duration), loop=0)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Giffy", description="Makes gif from list of images")
    parser.add_argument("--input", help="Folder containing images")
    parser.add_argument("--dur", required=False, default=400, help="Time (in milliseconds) to display each frame (default: 400ms)")

    args = parser.parse_args()

    make_gif(args.input, args.dur)