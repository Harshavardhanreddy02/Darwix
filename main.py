from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from visualizer import get_storyboard_content
from engine import synthesize_vocal_output  

app = FastAPI(title="VocalSync AI & Pitch Visualizer")
templates = Jinja2Templates(directory="templates")

# Enable CORS for browser compatibility [cite: 89]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"request": request}
    )

@app.post("/analyze", response_class=HTMLResponse)
async def process_voice_request(request: Request, text: str = Form(...)):
    """Challenge 1: The Empathy Engine [cite: 11]"""
    vocal_data = synthesize_vocal_output(text)
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "emotion": vocal_data["emotion"],
            "intensity": vocal_data["intensity"],
            "params": vocal_data["params"], 
            "text": text
        }
    )
@app.post("/visualize")
async def visualize_pitch(request: Request, story_text: str = Form(...)):
    # Now generates real AI images based on the story sentences
    storyboard = get_storyboard_content(story_text)
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"storyboard": storyboard, "story_text": story_text}
    )

@app.get("/audio")
async def stream_vocal_output():
    """Final Audio Output Requirement [cite: 25]"""
    return FileResponse("output.mp3", media_type="audio/mpeg")

@app.get("/favicon.ico", include_in_schema=False)
async def stop_favicon_error():
    return Response(status_code=204)