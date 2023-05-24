#  IMPORT THE SERVER (UVICORN)
import uvicorn 

# RUN THE SERVER IN THE APPLICATION PATH (APP FILE, INSIDE THE APP FOLDER)
if __name__ == "__main__": 
    # development: reload = True
    # deploy: reaload = False
    uvicorn.run("app.app:app", port = 8000, reload = True)
