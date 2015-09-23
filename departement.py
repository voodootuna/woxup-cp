# coding: latin-1

#import mysql.connector
import pymysql  as sqldb
import os
import codecs



#db = mysql.connector.connect(user='root', password='', host='localhost', database='woxup', charset="latin1", pool_size=32)
db = sqldb.connect(user='root', passwd='', host='localhost', db='woxup')
cursor = db.cursor()
cursor2 = db.cursor()


def head(dpt_code, dpt_name, region):
	head_html="""
	<head>
		<title>Departement {0}-{1}, de la région {2}</title>
		<meta name = "description " content = "Informations du departement {1}, info météo {1} avec sélections plombiers {1}, serruriers {1} et autres artisans {1}"/>
			<meta name = "keyword" content = "{1} {1}, météo {1}, traffic {1}, Wikipedia {1}, plombier {1}, serrurier {1}, chauffagiste {1}, electricien {1}, vitrier {1}, volets roulant {1}" />
		<meta name="robots" content="index,follow">
        <meta name="geo.region" content="FR" />
        <meta name="geo.placement" content="France" />


		<link href="../../assets/css/jqvmap.css" media="screen" rel="stylesheet" type="text/css" />

		<meta charset="utf-8"/>
		<meta name="viewport" content="width=device-width, initial-scale=1"/>
		<!--[if lte IE 8]><script src="../../assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="../../assets/css/main.css"/>
		<!--[if lte IE 8]><link rel="stylesheet" href="../../assets/css/ie8.css" /><![endif]-->

	</head>
	""".format(dpt_code, (dpt_name.encode("utf-8").decode("latin1")).strip(), region)

	return head_html

def footer(dpt_code):
	f_html = """<!-- Footer -->
				<div id="footer-wrapper">
					<footer id="footer" class="container">
						<div class="row">
							<div class="12u">
								<div id="copyright">
									<ul class="menu">
										<li>©2015 Woxup</li>
									</ul>
								</div>
							</div>
						</div>
					</footer>
					
				</div>

		<!-- Scripts -->
		    <script src="../../assets/js/jquery.min.js" type="text/javascript" ></script>
			<script src="../../assets/js/jquery-ui.js "type="text/javascript"  ></script>
			<script src="../../assets/js/jquery.dropotron.min.js" type="text/javascript" ></script>
		    <script src="../../assets/js/jquery.vmap.min.js" type="text/javascript"></script>
		    <script src="../../assets/js/jquery.vmap.france.js" type="text/javascript"></script>
		    <script src="../../assets/js/skel.min.js" type="text/javascript" ></script>
			<script src="../../assets/js/util.js" type="text/javascript" ></script>
		    <script src="../../assets/js/main.js" type="text/javascript" ></script>
		      <script type="text/javascript">


			$.getJSON('../../assets/js/autocomplete.json',function(data){
      var source = data;
      $("input#tags").autocomplete({ source: source,
	select:function(E,A){
		var N=A.item.label.split("-").pop().substring(0,2);
		var NM =A.item.label.split("-").pop().substring(0,3);
		if(NM == '201'|| NM == '200'){
			window.location.href="../"+"2A"+"/"+A.item.label+".html";
		}else if(NM == "202"){
			window.location.href="../"+"2B"+"/"+A.item.label+".html";
		}else{
		window.location.href="../"+N+"/"+A.item.label+".html"
	}},max:10,minLength:3 });

		});

	jQuery(document).ready(function() {
	jQuery('#vmap').vectorMap({
	    map: 'france_fr',
	    backgroundColor: 'transparent',
	    borderColor: '#FFF',
	    borderOpacity: 0.25,
	    borderWidth: 1,
	    color: '#0090c5',
	    enableZoom: false,
	    hoverColor: '#ff4486',
	    hoverOpacity: null,
	    normalizeFunction: 'linear',
	    scaleColors: ['#b6d6ff', '#005ace'],
	    selectedColor: '#ff4486',
	    selectedRegion: 'FR-%s',
	    showTooltip: true,
    onRegionClick: function(element, code, region)
    {
        var url = "/departement/" + code.substring(3,5);

        window.location = url;
    },
    onLabelShow:function(event,label,code)
    {
    
    	document.getElementById("logo-title").innerHTML = code.substring(3,5) +" - "+ label.text();
    	
    }

});

	});
	</script>
		"""%dpt_code

	return f_html

def nav(dpt_code,dpt_name, region):
	n_html = """
	<div id="header-wrapper">
					<header id="header" class="container">

						<!-- Logo -->
							<div id="logo">
								<h1 ><a href="#" id="logo-title">{0} - {1}</a></h1>
								<span>{2}</span>
							</div>

						<!-- Nav -->
		<nav id="nav">
								<ul>
									<li class="current"><a href="../../">Accueil</a></li>								
								</ul>
							</nav>
								</header>
				</div>

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
	""".format(dpt_code, dpt_name.encode("utf-8").decode("latin1"),region)
	return n_html


def villes(dpt_code, dpt_name):
		query="""SELECT villes_france.ville_nom, villes_france.ville_code_postal FROM villes_france  WHERE villes_france.ville_departement = '%s' """%dpt_code
		cursor.execute(query)
		villes_list =""
		for (vn, vc) in cursor:
			villes_list += '<li><a class="hilight" href="./{3}-{2}.html">{1} - {2}</a></li>'.format(dpt_code,vn,vc, vn.replace(" ",""))

		return '<div class="liste-ville"><h3>Liste des villes du département {0}</h3><ul>{1}</ul></div>'.format(dpt_code, villes_list)

def infogen(dpt_code, dpt_name):
	query2 = """SELECT region_nom FROM tel  WHERE dpt = '%s' """%dpt_code
	cursor2.execute(query2)
	region = (cursor2.fetchone()[0]).encode("utf-8").decode("latin1")
	filename = "./departement/%s/index.html"%(dpt_code)
	header_h = head(dpt_code, dpt_name, region)	
	footer_h = footer(dpt_code)
	villes_h =villes(dpt_code, dpt_name)
	nav_h = nav(dpt_code, dpt_name, region)

	source_html = """
	<html lang="fr">
	{0}
	<body>
	<div id="page-wrapper">
		{1}
			<div id="vmap" style="width: auto; height: 520px;"></div>
		<div class="box container">
		{2}
		</div>
		{3}
	</div>
	<body>
	</html>
	""".format(header_h, nav_h, villes_h, footer_h)
	
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename,"w") as f:
		f.write(source_html)
		f.close()
	#for i in conc:
	#	print(i, conc[i])


with open("wawa.txt","r") as f:
	data = f.readlines()
	for i in data:
		dpt = i.split(";")
		dpt_code = dpt[0]
		dpt_name = dpt[1]
		infogen(dpt_code,dpt_name)

