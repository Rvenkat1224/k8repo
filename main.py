from fastapi import fastapi, Request, form
from fastapi.templating import Jinja2Templates

app = FastApi()
templates = Jinja2Templates(directory="/code")

@api.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})
