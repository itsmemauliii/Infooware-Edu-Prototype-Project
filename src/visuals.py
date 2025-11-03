from PIL import Image, ImageDraw

def make_visuals(slides, outdir='outputs'):
    for i, s in enumerate(slides):
        img = Image.new('RGB', (1280, 720), color=(240, 240, 240))
        d = ImageDraw.Draw(img)
        d.text((100, 100), s['title'], fill=(0, 0, 0))
        path = f"{outdir}/slide_{i+1:02d}.png"
        img.save(path)
        s['image_path'] = path
