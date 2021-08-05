from flask import Flask,jsonify,request
import csv

movie_list= []
with open("movies.csv",encoding = "utf-8")as f:
    reader          = csv.reader(f)
    data            = list(reader)
    movie_list      = data[1:]

like        =[]
unlike      =[]
not_watch   =[]

app = Flask(__name__)
@app.route("/getmovie")

def getmovie():
    return jsonify({
        "data"      : movie_list[0],
        "status"    :"success"
    })

@app.route("/likemovie",methods=["POST"])
def likemovie():
    movie          = movie_list[0]
    movies_list     = movie_list[1:]
    like.append(movie)
    return jsonify({
        "status"    :"success",
        
    }),201

@app.route("/unlikemovie",methods=["POST"])
def unlikemovie():
    movie       =movie_list[0]
    movieslist  =movie_list[1:]
    unlike.append(movie)
    return jsonify({
        "status":"success",

    }),201

@app.route("/notwatchedtmovie",methods=["POST"])
def nwatmovie():
    movie = movie_list[0]
    movieslist = movie_list[1:]
    not_watch.append(movie)
    return jsonify({
         "status":"success",
    }),201
if __name__ == "__main__":
    app.run()

