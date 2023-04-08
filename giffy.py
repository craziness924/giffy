from PIL import Image
import argparse
import os



def make_gif(input, duration):
    output = f"{input}\output.gif"
    
    start_image = None
    images = []

    for i, file in enumerate(os.scandir(input), start=0):
        file_type = os.path.splitext(file.path)[1]
        
        if file_type not in [".png", ".jpeg"] or file_type == ".gif":
            continue

        img = Image.open(file.path)

        if i == 0:
            start_image = img
        else:
            images.append(img)
        

        
    start_image.save(output, save_all=True, append_images=images, duration=float(duration), loop=0)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Giffy", description="Makes gif from list of images")
    parser.add_argument("--input", help="Folder containing images")
    parser.add_argument("--dur", required=False, help="Time (in milliseconds) to display each frame")

    args = parser.parse_args()

    make_gif(args.input, args.dur)    
