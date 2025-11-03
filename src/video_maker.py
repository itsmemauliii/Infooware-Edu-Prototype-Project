from moviepy.editor import ImageClip, concatenate_videoclips

def make_video(slides, outdir='outputs'):
    clips = []
    for s in slides:
        clip = ImageClip(s['image_path']).set_duration(2)
        clips.append(clip)
    final = concatenate_videoclips(clips, method='compose')
    final.write_videofile(f"{outdir}/video.mp4", fps=24)
