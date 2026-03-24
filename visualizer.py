import urllib.parse

def get_storyboard_content(full_text: str):
    """
    Requirement #2: Segmentation.
    Maintains full text integrity for short inputs while 
    creating 3 distinct visual moments.
    """
    text = full_text.strip()
    
    # Try to split by sentences first
    scenes = [s.strip() for s in text.split('.') if len(s.strip()) > 5]
    
    # NEW LOGIC: If input is short, DON'T split the words.
    # Instead, create 3 visual "beats" for the same text.
    if len(scenes) < 3:
        scenes = [
            f"{text} ",
            f"{text} ",
            f"{text} "
        ]

    storyboard = []
    
    # Camera angles to ensure Requirement #3 (Intelligent Prompting)
    angles = [
        "wide angle establishing shot, epic scale",
        "medium shot, character focused, dynamic",
        "extreme close up, detailed textures, dramatic depth of field"
    ]

    for i, scene in enumerate(scenes[:3]):
        # We use a specific angle for each panel to ensure they look different
        angle = angles[i] if i < len(angles) else angles[1]
        
        # Requirement #3: Intelligent Prompt Engineering
        v_prompt = f"Masterpiece cinematic digital art: {scene}. {angle}, 8k, professional lighting, vibrant colors"
        
        # URL ENCODING (Stable Endpoint)
        encoded_prompt = urllib.parse.quote(v_prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=576&seed={i+999}&nologo=true"
        
        storyboard.append({
            "scene_number": i + 1,
            "original_text": scene,
            "visual_prompt": v_prompt,
            "image_url": image_url
        })
        
    return storyboard