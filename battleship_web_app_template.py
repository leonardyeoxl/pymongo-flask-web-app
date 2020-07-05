from flask import *
from battleship import *
import random
from pymongo import *

app = Flask(__name__)
client = MongoClient('192.168.150.133', 27017)
db = client['ship_database']
coordinates = db['coordinates']

def RandomShip():
       global ship_X, ship_Y, won
       ship_X = random.randint(0,4)
       ship_Y = random.randint(0,5)
       won = False
       print("ship_X: ",ship_X)
       print("ship_Y: ",ship_Y)

@app.route('/') #decorator
def root():
       global grid

       ################
       #your code here#
       ################
       
       RandomShip()
       grid = initialiseGrid()
       coordinates.remove({})

       return render_template('main.html', grid=grid)
 
@app.route('/calculate', methods = ["POST"])
def calculate():
       global won       
       data = request.form

       ################
       #your code here#
       ################
       X = data['X']
       Y = data['Y']
       if validateRow(X) and validateCol(Y):

              xy_coord = { "X": X, "Y": Y }
              coordinates.insert_one(xy_coord)
              won = checkResult(grid, int(X), int(Y), ship_X, ship_Y, won)

              if won:
                     return render_template('won.html', coords=list(coordinates.find({})))

       return render_template('main.html', grid=grid) 
       
         
if __name__ == '__main__':
       app.run(port = 6789, debug = True)


