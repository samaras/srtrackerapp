from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context, RequestContext

import json 
from pprint import pprint
import urllib2
# from srmap.models import Targets
from xml.dom import minidom

def index(request):
    # Context from HttpResponse
    context = RequestContext(request)
    template_name = 'srmap/index.html'
    # get the list of points to set
    target_packs = "OpenStreetMap" # Targets.objects.all()
    context_dict = { 'targets': target_packs }
    
    return render_to_response('srmap/index.html', context_dict, context)


def parse_xml():
	doc = loadSource()

	root_elem = doc.getElementsByTagName("MTI")
	height   = root_elem[0].getAttribute('frameHeight')
	width    = root_elem[0].getAttribute('frameWidth')
	num_targets = root_elem[0].getAttribute('numTargets')

	frames = {}
	frames['height'] = height
	frames['width'] = width

	targets  = []

	# iterate over and get all target packs
	num_targets = int(num_targets)

	for i in range(num_targets):
		target_pack = root_elem[0].getElementsByTagName("TargetPack")[i]
		tid = target_pack.getAttribute('id') # get targetpack id

		# centroid
		centroid = target_pack.getElementsByTagName("centroid")
		pixel = centroid[0].getAttribute("pixel")
		
		# bounds
		bounds = target_pack.getElementsByTagName("bounds")
		b_top_left = bounds[0].getAttribute("topLeft")
		b_btm_right = bounds[0].getAttribute("bottomRight")
		
		# geoLocation
		geo_location = target_pack.getElementsByTagName("geoLocation")
		lat = geo_location[0].getAttribute("lat")
		lon = geo_location[0].getAttribute("lon")

		# geoBounds 
		geo_bounds = target_pack.getElementsByTagName("geoBounds")
		top_left_lat = geo_bounds[0].getAttribute("topLeftLat")
		top_left_lon = geo_bounds[0].getAttribute("topLeftLon")
		bottom_right_lat = geo_bounds[0].getAttribute("bottomRightLat")
		bottom_right_lon = geo_bounds[0].getAttribute("bottomRightLon")

		# just return latitude  and the longitude values
		targets.append([lat, lon]) 
	
	return json.dumps({'frames': frames, 'targets': targets})

def loadSource():
	# read the xml files from trmapper
	host = "127.0.0.1"
	port = "8090"
	url = host +":"+ port

	try:
		# source = urllib2.urlopen(url).read()
		source = "/home/samuelk/Work/srtrack/srtrack/static/example.xml"
		doc = minidom.parse(source)
		return doc
	except:
		return None

def tracker(request):
	""" AJAX GET method that returns the coordinates from the files """
	values = parse_xml()
	return HttpResponse(values, content_type = "application/json")