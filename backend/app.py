# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request

# creating a Flask app 
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})

    # A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

@app.route('/siemens', methods=['GET'])
def getsiemensdata():
    return jsonify({'new': 5,
                    'technology': 10,
                    'marketTrend': 15})

@app.route('/abb', methods=['GET'])
def getabbdata():
    return jsonify({'new': 5,
                    'technology': 10,
                    'marketTrend': 15})
@app.route('/schinder', methods=['GET'])
def getschinderdata():
    return jsonify({'new': 5,
                    'technology': 10,
                    'marketTrend': 15})

@app.route('/rockwell', methods=['GET'])
def getrockwelldata():
    return jsonify({'new': 5,
                    'technology': 10,
                    'marketTrend': 15})

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

# driver function
if __name__ == '__main__':
    app.run(debug=True)