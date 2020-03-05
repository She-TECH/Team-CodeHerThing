# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request
from flask_cors import CORS
import processing
import technologyprocess
import market
from flask_script import Manager, Server

# creating a Flask app 
app = Flask(__name__)
CORS(app)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods=['GET', 'POST'])
def home():
    init()

    # A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

@app.route('/initialize', methods=['GET'])
def init():
    processing.segregateCompanyData()
    processing.processnewproductdata()
    processing.newdomaindrill()
    technologyprocess.segregatetechnology()
    market.markettrendprocessing()


@app.route('/siemens', methods=['GET'])
def getsiemensdata():
    newdata = processing.getNumberOfRows("..//new/NewKeywords.xls", "Siemens.csv");
    techdata1 = processing.getNumberOfRows("..//technologyCompany/Siemens.xls", "SiemensCyber security")
    techdata2 = processing.getNumberOfRows("..//technologyCompany/Siemens.xls", "SiemensDigital Twin")
    techdata3 = processing.getNumberOfRows("..//technologyCompany/Siemens.xls", "SiemensData Analytics and AI")
    techdata4 = processing.getNumberOfRows("..//technologyCompany/Siemens.xls", "SiemensConnectivityEdge")
    techdata5 = processing.getNumberOfRows("..//technologyCompany/Siemens.xls", "Siemensblockchain")
    techdata6 = processing.getNumberOfRows("..//technologyCompany/Siemens.xls", "SiemensAutonomous Robots")
    techdata7 = processing.getNumberOfRows("..//technologyCompany/Siemens.xls", "SiemensAdditive manufacturing")
    techdata = techdata1 + techdata2 + techdata3 + techdata4 + techdata5 + techdata6 + techdata7;
    markettrend1 = processing.getNumberOfRows("..//market/Siemens.xls", "Siemenssecurity")
    markettrend2 = processing.getNumberOfRows("..//market/Siemens.xls", "SiemensCollaboration")
    markettrend = markettrend1 + markettrend2

    return jsonify({'new': newdata,
                    'technology': techdata,
                    'marketTrend': markettrend})

@app.route('/abb', methods=['GET'])
def getabbdata():
    newdata = processing.getNumberOfRows("..//new/NewKeywords.xls", "ABB.csv");
    techdata1 = processing.getNumberOfRows("..//technologyCompany/ABB.xls", "ABBCyber security")
    techdata2 = processing.getNumberOfRows("..//technologyCompany/ABB.xls", "ABBDigital Twin")
    techdata3 = processing.getNumberOfRows("..//technologyCompany/ABB.xls", "ABBData Analytics and AI")
    techdata4 = processing.getNumberOfRows("..//technologyCompany/ABB.xls", "ABBConnectivityEdge")
    techdata5 = processing.getNumberOfRows("..//technologyCompany/ABB.xls", "ABBblockchain")
    techdata6 = processing.getNumberOfRows("..//technologyCompany/ABB.xls", "ABBAutonomous Robots")
    techdata7 = processing.getNumberOfRows("..//technologyCompany/ABB.xls", "ABBAdditive manufacturing")
    techdata = techdata1 + techdata2 + techdata3 + techdata4 + techdata5 + techdata6 + techdata7;
    markettrend1 = processing.getNumberOfRows("..//market/ABB.xls", "ABBsecurity")
    markettrend2 = processing.getNumberOfRows("..//market/ABB.xls", "ABBCollaboration")
    markettrend = markettrend1 + markettrend2

    return jsonify({'new': newdata,
                    'technology': techdata,
                    'marketTrend': markettrend})
@app.route('/schinder', methods=['GET'])
def getschinderdata():
    newdata = processing.getNumberOfRows("..//new/NewKeywords.xls", "Schneider.csv");
    techdata1 = processing.getNumberOfRows("..//technologyCompany/Schneider.xls", "SchneiderCyber security")
    techdata2 = processing.getNumberOfRows("..//technologyCompany/Schneider.xls", "SchneiderDigital Twin")
    techdata3 = processing.getNumberOfRows("..//technologyCompany/Schneider.xls", "SchneiderData Analytics and AI")
    techdata4 = processing.getNumberOfRows("..//technologyCompany/Schneider.xls", "SchneiderConnectivityEdge")
    techdata5 = processing.getNumberOfRows("..//technologyCompany/Schneider.xls", "Schneiderblockchain")
    techdata6 = processing.getNumberOfRows("..//technologyCompany/Schneider.xls", "SchneiderAutonomous Robots")
    techdata7 = processing.getNumberOfRows("..//technologyCompany/Schneider.xls", "SchneiderAdditive manufacturing")
    techdata = techdata1 + techdata2 + techdata3 + techdata4 + techdata5 + techdata6 + techdata7;
    markettrend1 = processing.getNumberOfRows("..//market/Schneider.xls", "Schneidersecurity")
    markettrend2 = processing.getNumberOfRows("..//market/Schneider.xls", "SchneiderCollaboration")
    markettrend = markettrend1 + markettrend2

    return jsonify({'new': newdata,
                    'technology': techdata,
                    'marketTrend': markettrend})

@app.route('/rockwell', methods=['GET'])
def getrockwelldata():
    newdata = processing.getNumberOfRows("..//new/NewKeywords.xls", "Rockwell.csv");
    techdata1 = processing.getNumberOfRows("..//technologyCompany/Rockwell.xls", "RockwellCyber security")
    techdata2 = processing.getNumberOfRows("..//technologyCompany/Rockwell.xls", "RockwellDigital Twin")
    techdata3 = processing.getNumberOfRows("..//technologyCompany/Rockwell.xls", "RockwellData Analytics and AI")
    techdata4 = processing.getNumberOfRows("..//technologyCompany/Rockwell.xls", "RockwellConnectivityEdge")
    techdata5 = processing.getNumberOfRows("..//technologyCompany/Rockwell.xls", "Rockwellblockchain")
    techdata6 = processing.getNumberOfRows("..//technologyCompany/Rockwell.xls", "RockwellAutonomous Robots")
    techdata7 = processing.getNumberOfRows("..//technologyCompany/Rockwell.xls", "RockwellAdditive manufacturing")
    techdata = techdata1 + techdata2 + techdata3 + techdata4 + techdata5 + techdata6 + techdata7;
    markettrend1 = processing.getNumberOfRows("..//market/Rockwell.xls", "Rockwellsecurity")
    markettrend2 = processing.getNumberOfRows("..//market/Rockwell.xls", "RockwellCollaboration")
    markettrend = markettrend1 + markettrend2

    return jsonify({'new': newdata,
                    'technology': techdata,
                    'marketTrend': markettrend})

@app.route('/siemensdetails', methods=['GET'])
def getsiemensdetaildata():
    return jsonify({'domain': 5,
                    'technology': 10,
                    'marketTrend': 15})

@app.route('/abbdetails', methods=['GET'])
def getabbdetaildata():
    return jsonify({'domain': 5,
                    'technology': 10,
                    'marketTrend': 15})

@app.route('/schinderdetails', methods=['GET'])
def getschinderdetaildata():
    return jsonify({'domain': 5,
                    'technology': 10,
                    'marketTrend': 15})

@app.route('/rockwelldetails', methods=['GET'])
def getrockwelldetaildata():
    return jsonify({'domain': 5,
                    'technology': 10,
                    'marketTrend': 15})


@app.route('/siemensallnews', methods=['GET'])
def getsiemensallnews():
    processing.getCSV("..//company/Siemens.csv")

    return jsonify({'news': [
    {'summary': "Siemens Implements an Efficient Power Supply System for KMRCL", 'url': "https://www.arcweb.com/blog/siemens-implements-efficient-power-supply-system-kmrcl"},
    {'summary': "Claroty and Siemens Mobility Integration Increases Cybersecurity for OT and IT Networks", 'url': "https://www.arcweb.com/blog/claroty-siemens-mobility-integration-increases-cybersecurity-ot-it-networks"}
  ]})

@app.route('/abballnews', methods=['GET'])
def getabballnews():
    return jsonify({'news': [
    {'summary': "ABB Launches New Performance Optimization Service for Long Product Rolling Mills", 'url': "https://www.arcweb.com/blog/abb-launches-new-performance-optimization-service-long-product-rolling-mills"},
    {'summary': "ABB Launches IoT Dashboard for Mid-Sized Commercial Building Automation Solutions", 'url': "https://www.arcweb.com/blog/abb-launches-iot-dashboard-mid-sized-commercial-building-automation-solutions"}
  ]})

@app.route('/schniderallnews', methods=['GET'])
def getschniderallnews():
    return jsonify({'news': [
    {'summary': "Schneider Electric to Launch Offer for Construction Software Provider, RIB Software", 'url': "https://www.arcweb.com/blog/schneider-electric-launch-offer-construction-software-provider-rib-software"},
    {'summary': "Schneider Electric Unveils Next Generation of Intelligent Enclosures at Innovation Days 2019, Foxboro and Triconex User Groups", 'url': "https://www.arcweb.com/blog/schneider-electric-unveils-next-generation-intelligent-enclosures-innovation-days-2019-foxboro"}
  ]})

@app.route('/rockwellallnews', methods=['GET'])
def getrockwellallnews():
    return jsonify({'news': [
    {'summary': "Rockwell Automation, Inc. Signs Agreements to Acquire ASEM, S.p.A. and Kalypso, LP", 'url': "https://www.arcweb.com/blog/rockwell-automation-inc-signs-agreements-acquire-asem-spa-kalypso-lp"},
    {'summary': "Rockwell Automation to Acquire Avnet to Expand Cybersecurity Expertise and Services", 'url': "https://www.arcweb.com/blog/rockwell-automation-acquire-avnet-expand-cybersecurity-expertise-services"}
  ]})

@app.route('/siemensnewnews', methods=['GET'])
def getsiemensnewnews():
    return jsonify({'news': [
    {'summary': "Siemens Implements an Efficient Power Supply System for KMRCL", 'url': "https://www.arcweb.com/blog/siemens-implements-efficient-power-supply-system-kmrcl"},
    {'summary': "Claroty and Siemens Mobility Integration Increases Cybersecurity for OT and IT Networks", 'url': "https://www.arcweb.com/blog/claroty-siemens-mobility-integration-increases-cybersecurity-ot-it-networks"}
  ]})

@app.route('/abbnewnews', methods=['GET'])
def getabbnewnews():
    return jsonify({'news': [
    {'summary': "ABB Launches New Performance Optimization Service for Long Product Rolling Mills", 'url': "https://www.arcweb.com/blog/abb-launches-new-performance-optimization-service-long-product-rolling-mills"},
    {'summary': "ABB Launches IoT Dashboard for Mid-Sized Commercial Building Automation Solutions", 'url': "https://www.arcweb.com/blog/abb-launches-iot-dashboard-mid-sized-commercial-building-automation-solutions"}
  ]})

@app.route('/schnidernewnews', methods=['GET'])
def getschnidernewnews():
    return jsonify({'news': [
    {'summary': "Schneider Electric to Launch Offer for Construction Software Provider, RIB Software", 'url': "https://www.arcweb.com/blog/schneider-electric-launch-offer-construction-software-provider-rib-software"},
    {'summary': "Schneider Electric Unveils Next Generation of Intelligent Enclosures at Innovation Days 2019, Foxboro and Triconex User Groups", 'url': "https://www.arcweb.com/blog/schneider-electric-unveils-next-generation-intelligent-enclosures-innovation-days-2019-foxboro"}
  ]})

@app.route('/rockwellnewnews', methods=['GET'])
def getrockwellnewnews():
    return jsonify({'news': [
    {'summary': "Rockwell Automation, Inc. Signs Agreements to Acquire ASEM, S.p.A. and Kalypso, LP", 'url': "https://www.arcweb.com/blog/rockwell-automation-inc-signs-agreements-acquire-asem-spa-kalypso-lp"},
    {'summary': "Rockwell Automation to Acquire Avnet to Expand Cybersecurity Expertise and Services", 'url': "https://www.arcweb.com/blog/rockwell-automation-acquire-avnet-expand-cybersecurity-expertise-services"}
  ]})

@app.route('/siemenstechnews', methods=['GET'])
def getsiemenstechnews():
    return jsonify({'news': [
    {'summary': "Siemens Implements an Efficient Power Supply System for KMRCL", 'url': "https://www.arcweb.com/blog/siemens-implements-efficient-power-supply-system-kmrcl"},
    {'summary': "Claroty and Siemens Mobility Integration Increases Cybersecurity for OT and IT Networks", 'url': "https://www.arcweb.com/blog/claroty-siemens-mobility-integration-increases-cybersecurity-ot-it-networks"}
  ]})

@app.route('/abbtechnews', methods=['GET'])
def getabbtechnews():
    return jsonify({'news': [
    {'summary': "ABB Launches New Performance Optimization Service for Long Product Rolling Mills", 'url': "https://www.arcweb.com/blog/abb-launches-new-performance-optimization-service-long-product-rolling-mills"},
    {'summary': "ABB Launches IoT Dashboard for Mid-Sized Commercial Building Automation Solutions", 'url': "https://www.arcweb.com/blog/abb-launches-iot-dashboard-mid-sized-commercial-building-automation-solutions"}
  ]})

@app.route('/schnidertechnews', methods=['GET'])
def getschnidertechnews():
    return jsonify({'news': [
    {'summary': "Schneider Electric to Launch Offer for Construction Software Provider, RIB Software", 'url': "https://www.arcweb.com/blog/schneider-electric-launch-offer-construction-software-provider-rib-software"},
    {'summary': "Schneider Electric Unveils Next Generation of Intelligent Enclosures at Innovation Days 2019, Foxboro and Triconex User Groups", 'url': "https://www.arcweb.com/blog/schneider-electric-unveils-next-generation-intelligent-enclosures-innovation-days-2019-foxboro"}
  ]})

@app.route('/rockwelltechnews', methods=['GET'])
def getrockwelltechnews():
    return jsonify({'news': [
    {'summary': "Rockwell Automation, Inc. Signs Agreements to Acquire ASEM, S.p.A. and Kalypso, LP", 'url': "https://www.arcweb.com/blog/rockwell-automation-inc-signs-agreements-acquire-asem-spa-kalypso-lp"},
    {'summary': "Rockwell Automation to Acquire Avnet to Expand Cybersecurity Expertise and Services", 'url': "https://www.arcweb.com/blog/rockwell-automation-acquire-avnet-expand-cybersecurity-expertise-services"}
  ]})

@app.route('/siemensmarkettrendnews', methods=['GET'])
def getsiemensmarkettrendnews():
    return jsonify({'news': [
    {'summary': "Siemens Implements an Efficient Power Supply System for KMRCL", 'url': "https://www.arcweb.com/blog/siemens-implements-efficient-power-supply-system-kmrcl"},
    {'summary': "Claroty and Siemens Mobility Integration Increases Cybersecurity for OT and IT Networks", 'url': "https://www.arcweb.com/blog/claroty-siemens-mobility-integration-increases-cybersecurity-ot-it-networks"}
  ]})

@app.route('/abbmarkettrendnews', methods=['GET'])
def getabbmarkettrendnews():
    return jsonify({'news': [
    {'summary': "ABB Launches New Performance Optimization Service for Long Product Rolling Mills", 'url': "https://www.arcweb.com/blog/abb-launches-new-performance-optimization-service-long-product-rolling-mills"},
    {'summary': "ABB Launches IoT Dashboard for Mid-Sized Commercial Building Automation Solutions", 'url': "https://www.arcweb.com/blog/abb-launches-iot-dashboard-mid-sized-commercial-building-automation-solutions"}
  ]})

@app.route('/schnidermarkettrendnews', methods=['GET'])
def getschnidermarkettrendnews():
    return jsonify({'news': [
    {'summary': "Schneider Electric to Launch Offer for Construction Software Provider, RIB Software", 'url': "https://www.arcweb.com/blog/schneider-electric-launch-offer-construction-software-provider-rib-software"},
    {'summary': "Schneider Electric Unveils Next Generation of Intelligent Enclosures at Innovation Days 2019, Foxboro and Triconex User Groups", 'url': "https://www.arcweb.com/blog/schneider-electric-unveils-next-generation-intelligent-enclosures-innovation-days-2019-foxboro"}
  ]})

@app.route('/rockwellmarkettrendnews', methods=['GET'])
def getrockwellmarkettrendnews():
    return jsonify({'news': [
    {'summary': "Rockwell Automation, Inc. Signs Agreements to Acquire ASEM, S.p.A. and Kalypso, LP", 'url': "https://www.arcweb.com/blog/rockwell-automation-inc-signs-agreements-acquire-asem-spa-kalypso-lp"},
    {'summary': "Rockwell Automation to Acquire Avnet to Expand Cybersecurity Expertise and Services", 'url': "https://www.arcweb.com/blog/rockwell-automation-acquire-avnet-expand-cybersecurity-expertise-services"}
  ]})

class CustomServer(Server):
    def __call__(self, app, *args, **kwargs):
        init()
        app.run()
        #Hint: Here you could manipulate app
        return Server.__call__(self, app, *args, **kwargs)

manager = Manager(app)

# Remeber to add the command to your Manager instance
manager.add_command('runserver', CustomServer())


# driver function
if __name__ == '__main__':
   app.run(debug=True)
