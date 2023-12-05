import random
from pathlib import Path
import logging
from importlib import import_module
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Form, Request, BackgroundTasks, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
# from apscheduler.schedulers.background import BackgroundScheduler
from typing import Optional

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

output_dir = Path("output")
output_dir.mkdir(parents=True, exist_ok=True)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/run_script/")
async def run_script(request: Request, background_tasks: BackgroundTasks, 
                     number_of_variation: Optional[int] = Form(None),
                     percentage_of_video_cut: Optional[int] = Form(None),
                     badbunny: bool = Form(False), tuileries: bool = Form(False), sardinia: bool = Form(False), 
                     berlin: bool = Form(False), dolce: bool = Form(False), humble: bool = Form(False), 
                     clear: bool = Form(False), vibrant_ii: bool = Form(False), vibrant_i: bool = Form(False), 
                     copper: bool = Form(False), plum: bool = Form(False), urbanoid: bool = Form(False), 
                     life_i: bool = Form(False), life_ii: bool = Form(False), robust: bool = Form(False), 
                     salt: bool = Form(False), metal: bool = Form(False), gray: bool = Form(False), shadow: bool = Form(False), 
                     milky_green: bool = Form(False), taro: bool = Form(False), red_tea: bool = Form(False), mistletoe: bool = Form(False), 
                     jingle_bells: bool = Form(False), conifer_cone: bool = Form(False), pine: bool = Form(False), 
                     gingerbread: bool = Form(False), nature: bool = Form(False), autumn: bool = Form(False), cold: bool = Form(False), 
                     tan: bool = Form(False), umber: bool = Form(False), holiday: bool = Form(False), gourmet_i: bool = Form(False), 
                     gourmet_ii: bool = Form(False), candy_cane: bool = Form(False), snack: bool = Form(False), french: bool = Form(False), 
                     bake: bool = Form(False), cuisine: bool = Form(False), western: bool = Form(False), eclipse: bool = Form(False), 
                     white_tea : bool = Form(False), peach : bool = Form(False), cold_brew : bool = Form(False), latte : bool = Form(False), 
                     veggie : bool = Form(False), comfort_food : bool = Form(False), fling : bool = Form(False), hope : bool = Form(False), 
                     freedom : bool = Form(False), barbie : bool = Form(False), oppenheimer : bool = Form(False), budapest : bool = Form(False), 
                     dispatch : bool = Form(False), black_panther : bool = Form(False), flipped : bool = Form(False), 
                     high_saturation : bool = Form(False), green_orange : bool = Form(False), blue_grey : bool = Form(False), 
                     dark_brown : bool = Form(False), green_yellow : bool = Form(False), scent : bool = Form(False), 
                     inception : bool = Form(False), one_day : bool = Form(False), oasis : bool = Form(False), dunkirk : bool = Form(False), 
                     winter_snow : bool = Form(False), love_letter : bool = Form(False), ocean_road : bool = Form(False), 
                     woodland : bool = Form(False), maple : bool = Form(False), nighty_night : bool = Form(False), warm_natural : bool = Form(False), 
                     orange_blue : bool = Form(False), greenish_grey : bool = Form(False), cold_blue : bool = Form(False), 
                     radiance : bool = Form(False), las_vegas : bool = Form(False), hawaii : bool = Form(False), san_francisco : bool = Form(False), 
                     voyage : bool = Form(False), clear_ll : bool = Form(False), maldives : bool = Form(False), hiking : bool = Form(False), 
                     green_lake : bool = Form(False), gold_coast : bool = Form(False), nightfall : bool = Form(False), garden : bool = Form(False), 
                     ice_city : bool = Form(False), december : bool = Form(False), picnic : bool = Form(False), dusk : bool = Form(False), 
                     hasselblad : bool = Form(False), fuji : bool = Form(False), shade : bool = Form(False), remote : bool = Form(False), 
                     spring_chorus : bool = Form(False), light_green : bool = Form(False), oshima_cherry : bool = Form(False), 
                     provia_100 : bool = Form(False), agfa_400 : bool = Form(False), gold_200 : bool = Form(False), retro_iv : bool = Form(False), 
                     retro_i : bool = Form(False), retro_ii : bool = Form(False), retro_iii : bool = Form(False), friends : bool = Form(False), 
                     miami : bool = Form(False), beverly : bool = Form(False), princeton : bool = Form(False), photo_booth : bool = Form(False), 
                     vhs_i : bool = Form(False), vhs_ii : bool = Form(False), vhs_iii : bool = Form(False), film : bool = Form(False), 
                     roman_holiday : bool = Form(False), tunnel : bool = Form(False), fade : bool = Form(False), black_forest : bool = Form(False), 
                     warlock : bool = Form(False), jazz : bool = Form(False), brown : bool = Form(False), bw_1 : bool = Form(False), 
                     bw_2 : bool = Form(False), bw_3 : bool = Form(False), weird : bool = Form(False), yandere : bool = Form(False), 
                     negative : bool = Form(False), night_vision : bool = Form(False), dope : bool = Form(False), sunset : bool = Form(False), 
                     burgundy : bool = Form(False), lost_forest : bool = Form(False), secluded_blue : bool = Form(False), 
                     purple_limbo : bool = Form(False), ghost : bool = Form(False), pumpkin : bool = Form(False), red_devil : bool = Form(False), 
                     blue_devil : bool = Form(False), vaporwave : bool = Form(False), cyber_light : bool = Form(False), 
                     sepia: bool = Form(False), red: bool = Form(False)
                    ):

    try:
        crawler_module = import_module("capcut")
        start_parse = crawler_module.start_parse
    except (ImportError, AttributeError) as e:
        logging.error(f"Failed to import capcut.start_parse: {e}")
        raise HTTPException(status_code=500, detail="Failed to import crawler")

    background_tasks.add_task(start_parse, number_of_variation, percentage_of_video_cut)

    result_message = "Scraper is running in the background"

    return templates.TemplateResponse("result.html", {"request": request, "result_message": result_message})


# scheduler = BackgroundScheduler()
# scheduler.start()
