# -*- coding: latin-1 -*-

#import mysql.connector as sqldb
import pymysql  as sqldb
#import MySQLdb  as sqldb
import os
import random
from datacp import mot_clef_list
from datetime import datetime
import multiprocessing

#db = sqldb.connect(user='root', password='', host='localhost', database='woxup', charset="latin1")
db = sqldb.connect(user='root', passwd='', host='localhost', db='woxup')
cursor = db.cursor()
cursor_rues = db.cursor()
cursor_artisans = db.cursor()
cursor_conc = db.cursor()
cursor_conc2 = db.cursor()
cursor_meteo = db.cursor()

def head(ville_nom, cp, cc, dpt, hab, lng, latt, tel,region_nom):
	head_html="""
	<head>
		<title>{0} {1} météo {0}, artisans {1}</title>
		<meta name = "description " content = "Informations {0}, ville du {3} de la region {8} au code postal {1}, info météo {0} avec sélections plombiers {0}, serruriers {0} et autres artisans {0}"/>
			<meta name = "keyword" content = "{1} {0}, météo {0}, traffic {0}, Wikipedia {0}, plombier {0}, serrurier {0}, chauffagiste {0}, electricien {0}, vitrier {0}, volets roulant {0}" />
		<meta name="robots" content="index,follow">
        <meta name="geo.region" content="FR" />
        <meta name="geo.placement" content="France" />
        <meta name="geo.position"  content="latitude: {5} ; longitude:{6}">


		<meta charset="utf-8"/>
		<meta name="viewport" content="width=device-width, initial-scale=1"/>
		<!--[if lte IE 8]><script src="../../assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="../../assets/css/main.css"/>
		<!--[if lte IE 8]><link rel="stylesheet" href="../../assets/css/ie8.css" /><![endif]-->
		<link rel="stylesheet" type="text/css" href="../../assets/css/jqcloud.css"/>

	</head>
	""".format(ville_nom.title(), cp, cc, dpt, hab, lng, latt, tel,region_nom.encode("utf-8").decode("latin1"))

	return head_html


def footer(latt,lng):
	f_html = """<!-- Footer -->
				<div id="footer-wrapper">
					<footer id="footer" class="container">
						<div class="row">
							<div class="12u">
								<div id="copyright">
									<ul class="menu">
										<li>© 2015 <a href="http://www.woxup.com/">Woxup</a></li>
									</ul>
								</div>
							</div>
						</div>
					</footer>
					
				</div>
		<!-- Scripts -->
			<script src="../../assets/js/jquery.min.js"></script>
			<script src="https://maps.googleapis.com/maps/api/js?v=3"></script>
			<script src="../../assets/js/jquery.dropotron.min.js"></script>
			<script src="../../assets/js/jquery-ui.js" ></script>
			<script src="../../assets/js/jqcloud-1.0.0.min.js" type="text/javascript" ></script>
			<script src="../../assets/js/cloudtext.js" type="text/javascript"></script>
			<script src="../../assets/js/skel.min.js"></script>
			<script src="../../assets/js/util.js"></script>
			<!--[if lte IE 8]><script src="../../assets/js/ie/respond.min.js"></script><![endif]-->
			<script src="../../assets/js/main.js"></script>
			<script src="../../assets/js/json1.js"></script>
			
		<script type="text/javascript"> 
		function initialize() {

  var mapOptions = {
    zoom: 13,
	   scrollwheel: false,
    center: new google.maps.LatLng(%s, %s)
  };
  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  // Create a marker and set its position.
  var marker = new google.maps.Marker({
    map: map,
    position: new google.maps.LatLng(%s, %s),
 });

  var trafficLayer = new google.maps.TrafficLayer();


 google.maps.event.addDomListener(document.getElementById("traficToggle"), 'click', function() {
        if ( trafficLayer.getMap() != null ) {
            trafficLayer.setMap(null);
        }
        else {
            trafficLayer.setMap(map);
        }
    });



};
  var panorama = new google.maps.StreetViewPanorama(
    document.getElementById('street-view-canvas'),
    {
      position: { lat:%s, lng:%s },
      pov :{heading:165, pitch:0},
      zoom:1
    });

google.maps.event.addDomListener(window, 'load', initialize);</script>
		"""%(latt,lng,latt,lng,latt,lng)

	return f_html


def nav(ville_nom, tel):
	nav_html="""
	<!-- Header -->
				<div id="header-wrapper">
					<header id="header" class="container">

						<!-- Logo -->
							<div id="logo">
								<h1><a href="#">{0}</a></h1>
								<span>Toutes les infos de votre ville en temps réel</span>
							</div>

						<!-- Nav -->
		<nav id="nav">
								<ul>
									<li class="current"><a href="../../">Accueil</a></li>
										<li><a href="./">Departement</a></li>
									<li>
										<a href="#">Artisans</a>
										<ul class="selection-artisans">
												<li><a href="#Plombier"><h1>Pomblier {0} {1}</h1></a></li>			
												<li><a href="#Chauffagiste"><h1>Chauffagiste {0} {1}</h1></a></li>
												<li><a href="#Electricien"><h1>Electricien {0} {1}</h1></a></li>
												<li><a href="#Vitrier"><h1>Vitrier {0} {1}</h1></a></li>
												<li><a href="#Serrurier"><h1>Serrurier  {0} {1}</h1></a></li>
												<li><a href="#Volets Roulants"><h1>Volets Roulants {0} {1}1</h1></a></li>
												
										</ul>
									</li>
								
								</ul>
							</nav>
								</header>
				</div>
							""".format(ville_nom.title(),tel)
	return nav_html




def widget_meteo_map(ville_nom,cc):
	query_meteo = """SELECT ville_nom from villes_france Where ville_nom LIKE "%s" LIMIT 2 """%(ville_nom)
	#cursor_meteo.execute(query_meteo)
	#no_villes = len(cursor_meteo.fetchall())
	meteo_code = ''.join([i for i in ville_nom if not i.isdigit()])
	#if no_villes > 1:
	#	meteo_code = (''.join([i for i in ville_nom if not i.isdigit()]))+cc[:2]
	wm_html = """<!-- Trafic et meteo -->	
			<div id="trafic-wrapper" >
				<div class="container">
					<div class="row">
						<div class="10u 12u(medium)">
							<div id="map-canvas"></div>			
						</div>
						<div class="2u 12u(medium)">
							<div class="map-control">
								<a id="traficToggle" class="button lien">Afficher info trafic</a>
							</div>
		<div class="info-meteo">
												<!-- widget meteo -->
							<div style="width:100%;height:220px;color:#000;border:1px solid #F2F2F2;">
<iframe height="190" frameborder="0" width="100%" scrolling="no" src="http://www.prevision-meteo.ch/services/html/{2}/square" allowtransparency="true"></iframe>
<a style="text-decoration:none;font-size:0.75em;" title="Prévisions complètes pour {2}" href="http://www.prevision-meteo.ch/meteo/localite/{2}">Prévisions complètes pour {2}</a>
</div>
						</div>
					</div>
				</div>
			</div>
		</div>
						""".format(ville_nom,cc,meteo_code)

	return wm_html


def recherche():
	r_html = """
	<!-- Recherche ville -->	
					<div id="search-wrapper">
						<div class="container">
							<div class="row">
								<div class="12u 12u(medium)">
										<div class="search big ">
	  										<input id="tags" placeholder="Tapez votre code postal" class="fa-search"></input>
	  										<span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span>
	  									</div>
	  							</div>
							</div>
						</div>
				</div>
	"""
	return r_html

def widgets_wrapper(cp,cc,hab,latt,lng):
	ww_html = """
			<div id="widgets-wrapper">
					<div class="box container info-ville">
						<div class="row">
							<div class="3u 12u(medium)">
								<h1>Code Postal<br><span class="highlight"> {0}</span></h1>					
							</div>
							<div class="3u 12u(medium)">
								<h1>Code Commune<br><span class="highlight "> {1}</span></h1>
			

							</div> 
							<div class="3u 12u(medium)">
								<h1>Nombre d'habitants <br><span class="highlight">{2}</span></h1>
	
							</div> 

								<div class="3u 12u(medium)">
									<h1>GPS<br><span class="highlight">{3}, {4}</span></h1>
	

								</div> 
							
						</div>
					</div>
				</div>
				""".format(cp,cc,hab,latt,lng)
	return ww_html

def features_wrapper(ville_nom):
	fw_html = """<div id="features-wrapper">
					<div class="container">
						<div class="row">
							<div class="4u 12u(medium)">
								<!-- Box -->
									<section class="box feature">
										<a href="http://france-webcams.fr/site/search/?phrase={0}&amp;go=+Rechercher+sur+l'annuaire+&amp;isNewSearch=true"><div class="webcam-ville"></div></a>
										<div class="inner">
											<header>
												<h2>Webcams</h2>
											</header>
										</div>
									</section>

							</div>
							<div class="4u 12u(medium)">

								<!-- Box -->
									<section class="box feature">
											<div id="street-view-canvas"></div>
										<div class="inner">
											<header>
												<h2>Prise de vue</h2>
											</header>
										</div>
									</section>

							</div>
							<div class="4u 12u(medium)">

								<!-- Box -->
									<section class="box feature ">
										<a href="https://www.youtube.com/results?search_query={0}">
										<div class="youtube-video"></div></a>
										<div class="inner">
											<header>
												<h2>Vidéo de la ville</h2>
												</header>
										</div>
									</section>

							</div>
						</div>
					</div>
				</div>
	""".format(ville_nom)
	return fw_html

def links_wrapper(ville_nom):
	links_html = """
	<div id="links-wrapper">
					<div class="box container">
						<div class="row">
							<div class="6u 12u(medium) ">
							<a href="https://fr.wikipedia.org/wiki/{1}" class="button  alt big icon fa-search lien">Wikipedia</a>
							</div>
							<div class="6u 12u(medium)">
									<a href="https://www.google.fr/#q={0}" class="button big icon fa-search lien">Google</a>
							
							</div>
						</div>
					</div>
				</div>
	""".format(ville_nom,''.join([i for i in ville_nom.title() if not i.isdigit()]))

	return links_html

def rues(cc,cp):
	query_rues = """SELECT nom FROM rues WHERE code_insee = "%s" """%cc
	cursor_rues.execute(query_rues)
	rues_links = cursor_rues.fetchall()
	if not rues_links:
		query_rues2 = 'SELECT nom FROM rues WHERE code_insee = "%s"'%cp
		cursor_rues.execute(query_rues2)
		rues_links = cursor_rues.fetchall()
	rues_list=""
	for rn in rues_links:
		rues_list+="<li>%s</li>"%rn

	rues_html = """<div id="rues-wrapper">
					<div class="box container">
						<h1 title="rues">Liste des rues de la ville</h1> 
						<div class="rues-liste">
							<ul>{0}</ul>
						</div>
					</div>
				</div>
	""".format(rues_list)

	return rues_html

def artisans_wrapper(ville_nom,cp,tel,dpt, region_nom):
	conc_list = concurrents(cp,ville_nom)
	artisans_list = artisan_blinks(cp,ville_nom,dpt,region_nom)
	mot_clef = ""
	metiers = ["plombier","chauffagiste","electricien","vitrier", "serrurier","voletiste"]
	nom_metier = {"plombier":"plomberie","chauffagiste":"chauffage","electricien":"electrique","vitrier":"vitrerie", "serrurier":"serrurerie","voletiste":"volets roulants"}
	artisans_html = ""

	count=1
	for m in metiers:
		sh_list = mot_clef_list[m].split("\n")
		random.shuffle(sh_list)
		bourrage = "<li>{}</li>".format(" {}</li><li>".format(ville_nom.title()).join(sh_list[:19]))
		profession = nom_metier[m]
		current_conc = "".join(conc_list[m])
		current_artisans = "".join(artisans_list[m])
		if m == "voletiste":
			m = "volets roulants"
			artisans_html+="""<div id="main-wrapper">
						<div id="{0}" class="container">

						<div class="artisan-feature-image">
							<img src="../../images/{0}.jpg" width="100%">
							<div class="caption-pic">
								<h1 title="{0} {3} tel">{0} {3}<span class="tel">{4}</span></h1>
								</div>
							</div>

							<div class="row">							
								<div class="4u 12u(medium) ">
									<!-- Sidebar -->
									<div class="sidebar">							
									<div id="wordcloud{8}"></div>
									<a href="https://www.google.fr/#q={0}+{3}" class="button icon fa-search lien">Recherche {0} {3}</a>	
									</div>
								</div>
								<div class="8u 12u(medium) important(medium)">

									<!-- Content -->
										<div class="concurrents">
										<h2> Liste de(s)  {0} de {3} ou à proximité</h2>
										<ul>
										{1}
										</ul>
										</div>
									<hr>
									<div class="liste-artisans">
									<h3> Nos sélections de(s) {0} à {3} :</h3>
											<ul>
											{2}
											<li><a title="{0} {3} {10}" href="http://www.pagesjaunes.fr/recherche/{3}-{9}/{0}" class="pagesjaune">{0} à proximité de {3}</a></li>
											</ul>
											</div>
												<hr>
											<div class="bmc">
	 											<h4> Spécialités en {6} :</h4>
												<ul>
												{7}
												</ul>
											</div>
								</div>
							</div>
						</div>
					</div>
		""".format(m.title(),current_conc,current_artisans.strip(),ville_nom.title(),tel, mot_clef.title(), profession,bourrage,count,dpt,cp)
		else:
			artisans_html+="""<div id="main-wrapper">
							<div id="{0}" class="container">

							<div class="artisan-feature-image">
								<img src="../../images/{0}.jpg" width="100%">
								<div class="caption-pic">
									<h1 title="{0} {3} tel">{0} {3}<span class="tel">{4}</span></h1>
									</div>
								</div>

								<div class="row">							
									<div class="4u 12u(medium) ">
										<!-- Sidebar -->
										<div class="sidebar">							
										<div id="wordcloud{8}"></div>
										<a href="https://www.google.fr/#q={0}+{3}" class="button icon fa-search lien">Recherche {0} {3}</a>	
										</div>
									</div>
									<div class="8u 12u(medium) important(medium)">

										<!-- Content -->
											<div class="concurrents">
											<h2> Liste de(s) {0}(s) de {3} ou à proximité</h2>
											<ul>
											{1}
											</ul>
											</div>
										<hr>
										<div class="liste-artisans">
										<h3> Nos sélections de(s) {0}(s) à {3} :</h3>
												<ul>{2}
												<li><a title="{0} {3} {10}" href="http://www.pagesjaunes.fr/recherche/{3}-{9}/{0}" class="pagesjaune">{0} à proximité de {3}</a></li>
												</ul>
													
												</div>
													<hr>
												<div class="bmc">
		 											<h4> Spécialités en {6} :</h4>
													<ul>
													{7}
													</ul>
												</div>
									</div>
								</div>
							</div>
						</div>
			""".format(m.title(),current_conc,current_artisans,ville_nom.title(),tel, mot_clef.title(), profession,bourrage,count,dpt,cp)
		count+=1

	#print(artisans_html)
	return artisans_html


def concurrents(ccp,v):
	metiers = ["plombier","chauffagiste","electricien","vitrier", "serrurier","voletiste"]
	html = {"plombier":[],"chauffagiste":[],"electricien":[],"vitrier":[], "serrurier":[],"voletiste":[]}
	for m in metiers:
		query_conc = """SELECT nom, adr FROM concurrents WHERE metier =%s AND code_postal=%s AND dpt=%s AND ville=%s LIMIT 50"""
		query_data = (m,ccp,ccp[:2],v)
		cursor_conc.execute(query_conc,query_data)
		conc_list = cursor_conc.fetchall()
		if len(conc_list) >= 1:
			for (nom, adr) in conc_list:
				mv = m
				if m == "voletiste":
					mv = "volets roulants"		
				html[m].append('<li><p title="{3} - {0} {1} {2}">{3} - {4} ({1} {2})</p></li>'.format(mv.title(),v.title(),ccp,nom.title(),adr.title()))
			if len(conc_list) < 50:
				fill_in = 50-len(conc_list)				
				query_conc2 = """SELECT nom, adr, ville, code_postal FROM concurrents WHERE metier=%s AND dpt=%s ORDER BY RAND() LIMIT %s"""
				query_data2 = (m,ccp[:2], fill_in)
				cursor_conc2.execute(query_conc2,query_data2)
				conc_list = cursor_conc2.fetchall()
				for (nom, adr, ville, vcp) in conc_list:
					mv = m
					if m == "voletiste":
						mv = "volets roulants"
					html[m].append('<li><p title="{3} - {0} {1} {2}">{3} - {4} ({1} {2})</p></li>'.format(mv.title(),ville.title(),vcp,nom.title(),adr.title()))


		else:
			query_conc2 = """SELECT nom, adr, ville, code_postal FROM concurrents WHERE metier=%s AND dpt=%s ORDER BY RAND() LIMIT 50"""
			query_data3 = (m,ccp[:2])
			cursor_conc2.execute(query_conc2,query_data3)
			conc_list = cursor_conc2.fetchall()
			for (nom, adr, ville, vcp) in conc_list:
				mv = m
				if m == "voletiste":
					mv = "volets roulants"
				html[m].append('<li><p title="{3} - {0} {1} {2}">{3} - {4} ({1} {2})</p></li>'.format(mv.title(),ville.title(),vcp,nom.title(),adr.title()))

	return html


def artisan_blinks(acp,v,dpt,region_nom):
	metiers = ["plombier","chauffagiste","electricien","vitrier", "serrurier","voletiste"]

	html = {"plombier":[],"chauffagiste":[],"electricien":[],"vitrier":[], "serrurier":[],"voletiste":[]}
	#print(region_nom, "=-===========")
	for m in metiers:
		query_artisans = """SELECT mot_clef, url FROM artisans WHERE metier =%s AND code_postal=%s AND departement=%s  ORDER BY RAND() LIMIT 9"""
		query_data = (m,acp,dpt)
		cursor_artisans.execute(query_artisans,query_data)
		links= cursor_artisans.fetchall()		
		t="""
		if len(links) < 9:
			query_artisans2 = 'SELECT mot_clef, url FROM artisans WHERE metier=%s AND departement=%s ORDER BY RAND() LIMIT 9'
			query_data2 = (m,dpt)
			cursor_artisans.execute(query_artisans2,query_data2)
			links = cursor_artisans.fetchall()
			if len(links) < 1:
				query_artisans4 = 'SELECT dpt from tel WHERE region_nom LIKE "%s" '%(region_nom)
				
				cursor_artisans.execute(query_artisans4)
				dpt_list= "".join("'{}',".format(i[0]) for i in cursor_artisans)
				newlist = "(%s)"%dpt_list
				#print(newlist)
				query_artisans5 = 'SELECT mot_clef, url FROM artisans WHERE departement IN %s AND metier="%s" ORDER BY RAND() LIMIT 9'%(newlist.replace(",)",")"),m)
				cursor_artisans.execute(query_artisans5)
				links = cursor_artisans.fetchall()
				"""

		for (mot_clef, url) in links:
			#print(url)
			if m == "voletiste":
				mv = "volets roulants" 
				html[m].append('<li><a title="{4} {2}" href="{3}">{4}</a></li>'.format(mv,v,acp,url,mot_clef.title()))
			else:
				html[m].append('<li><a title="{4} {2}" href="{3}">{4}</a></li>'.format(m,v,acp,url,mot_clef.title()))


	return html


def infogen(ville_nom, cp, cc, dpt, hab, lng, latt, slug, tel, region_nom):
	filename = "c:/xampp/htdocs/departement/%s/%s-%s.html"%(dpt,ville_nom.replace(" ", ""),cp)
	print(filename)
	header = head(ville_nom, cp, cc, dpt, hab, lng, latt, tel,region_nom)
	logo_nav = nav(ville_nom,tel)
	widget_mm = widget_meteo_map(ville_nom, cc)
	features_w = features_wrapper(ville_nom)
	info_box = widgets_wrapper(cp,cc,hab,latt,lng)
	rues_w = rues(cc,cp)
	links_w = links_wrapper(ville_nom)
	artisans_w = artisans_wrapper(ville_nom,cp,tel,dpt,region_nom)
	footer_w = footer(latt,lng)
	recherche_w = recherche()


	source_html = """<html lang="fr">
		{0}
		<body class="homepage">
		<div id="page-wrapper">
		{1}
		{2}{3}{4}{5}{6}{7}{8}
		{9}
		</div>
		</body>
		</html>
		""".format(header,logo_nav, recherche_w, widget_mm,info_box, features_w, links_w, rues_w, artisans_w,footer_w)
	
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename,"w") as f:
		f.write(source_html)
	#for i in conc:
	#	print(i, conc[i])


if __name__ == '__main__':
	#startTime = datetime.now()
	#dept = 75
	code_postal=75001
	query = """SELECT 		villes_france.ville_nom, 
							villes_france.ville_code_postal,
							villes_france.ville_code_commune,
							villes_france.ville_departement,
							villes_france.ville_population_2010,
							villes_france.ville_longitude_deg,
							villes_france.ville_latitude_deg,
							villes_france.ville_slug,
							tel.tel,
							tel.region_nom
					FROM villes_france 
					LEFT JOIN tel ON villes_france.ville_departement = tel.dpt WHERE villes_france.ville_departement >39 ORDER BY villes_france.ville_departement 
					"""
					#WHERE villes_france.ville_departement = %s
					#"""
					#%dept

	cursor.execute(query)
	pool = multiprocessing.Pool(6) #use all available cores, otherwise specify the number you want as an argument

	for (ville_nom, cp, cc, dpt, hab, lng, latt, slug, tel,region_nom) in cursor:
		pool.apply_async(infogen, args=(ville_nom, cp, cc, dpt, hab, lng, latt,slug, tel,region_nom))
	pool.close()
	pool.join()

	#print(datetime.now() - startTime)