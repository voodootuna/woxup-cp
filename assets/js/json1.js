		$.getJSON('../../assets/js/autocomplete.json',function(data){
      var source = data;
      $("input#tags").autocomplete({ source: source,
	select:function(E,A){
		var N=A.item.label.split("-").pop().substring(0,2);
		var NM =A.item.label.split("-").pop().substring(0,3);
		if(NM == '201'|| NM == '200'){
			window.location.href="../../departement/"+"2A"+"/"+A.item.label+".html";
		}else if(NM == "202"){
			window.location.href="../../departement/"+"2B"+"/"+A.item.label+".html";
		}else{
		window.location.href="../../departement/"+N+"/"+A.item.label+".html"
	}},max:10,minLength:3 });

		});