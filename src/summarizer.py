def make_slide_data(sections):
    slides = []
    for i, s in enumerate(sections):
        slides.append({
            'id': i+1,
            'title': s.get('title', f'Slide {i+1}'),
            'bullets': [s['text'][:80] + '...'],
            'image_path': 'assets/icons/default.png'
        })
    return slides
