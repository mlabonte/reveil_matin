import asyncio
#from flask import Flask
print("import what the fuck??")

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

async def start():
    await app.run(debug=True, host='0.0.0.0', port=80)

if __name__ == '__main__':
    asyncio.run(start())
    
