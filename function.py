# def fun():
#     print("I am a function")
# fun()

# def sum(x,y):
#     return x + y #The exist point in function

# print(sum(10, 20))
from PIL import Image, ImageDraw, ImageFont

# Define the size of the banner
width = 1584
height = 396
banner = Image.new('RGB', (width, height), color=(25, 118, 210))  # Dark blue background

# Create a draw object
draw = ImageDraw.Draw(banner)

# Define fonts and sizes
title_font_size = 60
subtitle_font_size = 30
try:
    # Attempt to use a nicer font if available
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    title_font = ImageFont.truetype(font_path, title_font_size)
    subtitle_font = ImageFont.truetype(font_path, subtitle_font_size)
except IOError:
    # Fallback to default font if custom font is not available
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# Title and subtitle text
title_text = "Prabuddha Chunchekar"
subtitle_text = "Aspiring Web Developer | Front-End Enthusiast | Lifelong Learner"

# Calculate text width and height to position it in the center
title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_height = title_bbox[3] - title_bbox[1]

subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
subtitle_height = subtitle_bbox[3] - subtitle_bbox[1]

# Positioning text in the center
title_x = (width - title_width) / 2
title_y = (height - title_height) / 2 - 20
subtitle_x = (width - subtitle_width) / 2
subtitle_y = title_y + title_height + 10

# Add text to image
draw.text((title_x, title_y), title_text, font=title_font, fill=(255, 255, 255))  # White text
draw.text((subtitle_x, subtitle_y), subtitle_text, font=subtitle_font, fill=(255, 255, 255))  # White text

# Save the banner
banner_path = "Prabuddha_Chunchekar_LinkedIn_Banner.png"
banner.save(banner_path)

banner_path
