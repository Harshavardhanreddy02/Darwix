from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

# Updated import to match your new engine.py refactor
from engine import synthesize_vocal_output  

app = FastAPI(title="VocalSync AI")
templates = Jinja2Templates(directory="templates")

# Enable CORS for security and browser compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# CORE ROUTES
# -----------------------------

@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    """Renders the main VocalSync interface."""
    return templates.TemplateResponse(
        request,             # <--- Must be the first argument
        "index.html", 
        {"request": request}
    )

@app.post("/analyze", response_class=HTMLResponse)
async def process_voice_request(request: Request, text: str = Form(...)):
    """Handles text submission and returns modulated audio parameters."""
    vocal_data = synthesize_vocal_output(text)
    
    return templates.TemplateResponse(
        request,             # <--- Must be the first argument
        "index.html", 
        {
            "request": request,
            "emotion": vocal_data["emotion"],
            "intensity": vocal_data["intensity"],
            "params": vocal_data["voice_params"],
            "text": text
        }
    )

@app.get("/audio")
async def stream_vocal_output():
    """Serves the generated MP3 file to the browser."""
    return FileResponse("output.mp3", media_type="audio/mpeg")

@app.get("/favicon.ico", include_in_schema=False)
async def stop_favicon_error():
    """Silences the common browser favicon 404 error."""
    return Response(status_code=204)