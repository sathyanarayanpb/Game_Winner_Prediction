from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("PUBG.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("index1.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":


        Id = int(request.form["Id"])

        assists = int(request.form["assists"])

        # Course

        boosts= int(request.form["boosts"])



        damageDealt= int(request.form["damageDealt"])

        DBNOs = int(request.form['DBNOs'])
        headshotKills = int(request.form['headshotKills'])
        heals = int(request.form['heals'])
        killpoints = int(request.form['killpoints'])
        kills = int(request.form['kills'])
        revives = int(request.form['revives'])
        walkDistance = int(request.form['walkDistance'])
        matchDuration = int(request.form['matchDuration'])
        teamKills = int(request.form['teamKills'])


        matchType = request.form['matchType']
        if(matchType == 'crashtpp'):
            crashtpp = 1
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif(matchType == 'duo'):
            crashtpp = 0
            duo = 1
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo= 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'duo - fpp'):
            crashtpp = 0
            duo = 0
            duofpp = 1
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'flarefpp'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 1
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'flaretpp'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 1
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'normal - duo'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 1
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'normal - duo - fpp'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 1
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'normal - solo'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 1
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'normal - solo - fpp'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 1
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'normal - squad'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 1
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'normal - squad - fpp'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 1
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'solo'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 1
            solofpp = 0
            squad = 0
            squadfpp = 0

        elif (matchType == 'solo - fpp'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 1
            squad = 0
            squadfpp = 0

        elif (matchType == 'squad'):
            crashtpp = 0
            duo = 0
            duofpp = 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 1
            squadfpp = 0

        else:
            crashtpp = 0
            duo = 0
            duofpp= 0
            flarefpp = 0
            flaretpp = 0
            normalduo = 0
            normalduofpp = 0
            normalsolo = 0
            normalsolofpp = 0
            normalsquad = 0
            normalsquadfpp = 0
            solo = 0
            solofpp = 0
            squad = 0
            squadfpp = 1


        prediction = model.predict([[
            Id,
            assists,
            boosts,
            DBNOs,
            damageDealt,
            headshotKills,
            heals,
            killpoints,
            matchDuration,
            kills,
            revives,
            walkDistance,
            teamKills,
            matchType

        ]])

        output = round(prediction[0],3)

        return render_template('index1.html', prediction_text="Player Performance :- {}".format(output))

    return render_template("index1.html")


if __name__ == "__main__":
    app.run(debug=True)

