from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - employeecollection-coll-4af80c20c5764b099f36b0504b29c9a6',debug=False,docs_url='/affectionate-meitner-6902d5fcc9a211ef81390242ac12000491/docs',openapi_url='/affectionate-meitner-6902d5fcc9a211ef81390242ac12000491/openapi.json')

app.include_router(router, prefix='/affectionate-meitner-6902d5fcc9a211ef81390242ac12000491/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()