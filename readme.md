<h1>Giffy</h1>

This project takes a set of images in a folder and outputs a looping gif in that folder containing all images. 

<h2>Installation</h2>

1. Get Python (tested on 3.11.10 on Linux Mint)
2. Install required packages with `pip install -r requirements.txt`
3. Run giffy.py with `python giffy.py --help` to see all parameters and test if install was a success (if the help message shows with no errors)

<h2>Usage</h2>

1. Run `python giffy.py` with desired parameters
    - For example, `python giffy.py --input "home/morris/example_dir/output" --dur 400`

<h3>Parameters</h3>

**--input:** The folder containing the images. Must pass it as a string if it contains spaces

**--dur:** (Optional) The amount of milliseconds to show each frame. The default duration is 400.