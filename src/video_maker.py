from moviepy.editor import ImageClip, concatenate_videoclips
from PIL import Image, ImageDraw
import os, random


def create_slide_image(title, content, path):
    """
    Create an image slide with Canva-style background and layout.
    """
    colors = [(255, 255, 255), (240, 248, 255), (245, 245, 255), (250, 250, 250)]
    color = random.choice(colors)

    img = Image.new("RGB", (1280, 720), color=color)
    draw = ImageDraw.Draw(img)

    draw.rectangle([(0, 0), (1280, 100)], fill=(100, 149, 237))  # header bar
    draw.text((40, 30), title, fill=(255, 255, 255))  # title text
    draw.text((60, 150), content[:1000], fill=(50, 50, 50))  # content text

    img.save(path)


def make_video(slides, outdir="outputs"):
    os.makedirs(outdir, exist_ok=True)
    temp_images = []

    print("🎬 Generating video frames...")
    for i, s in enumerate(slides, start=1):
        img_path = os.path.join(outdir, f"frame_{i}.png")
        create_slide_image(s.get("title", f"Slide {i}"), s.get("content", ""), img_path)
        temp_images.append(img_path)

    print("🎞️ Building video...")
    clips = [ImageClip(img).set_duration(3) for img in temp_images]
    final = concatenate_videoclips(clips, method='compose')

    outpath = os.path.join(outdir, "video.mp4")
    final.write_videofile(outpath, fps=24, codec="libx264")
    print(f"🎥 Video generated successfully → {outpath}")
