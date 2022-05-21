
function resetujGreske(){
	document.getElementById("naslovGreska").innerHTML="";
	document.getElementById("textGreska").innerHTML="";
	document.getElementById("kategorijeGreska").innerHTML="";


}

$(document).ready(function(){


	kategorije=[];

	$("#kraj").click(function(){



		resetujGreske();
		$("input:checkbox[name=type]:checked").each(function(){
				kategorije.push($(this).val());
		});




		let plainText = $($("#summernote").summernote("code")).text()
		let naslov=$("#naslov").val()

		if(naslov.length==0){
			document.getElementById("naslovGreska").innerHTML="Niste uneli naslov";

		}
		if(!plainText){

			document.getElementById("textGreska").innerHTML="Niste uneli tekst";
		}
		if(kategorije.length==0){
			document.getElementById("kategorijeGreska").innerHTML="Niste izabrali kategoriju";
		}
		else{


			$.ajax({
				type: 'POST',
				url: '/create_article/',
				data: {'kategorije[]': kategorije,
					   'tekst_artikla':plainText,
						'naslov':naslov,
						'flag':1,
						'add_questions':1



				},
			});
			$("[name='pitanje']").prop('disabled', false);

		}







	});

	$("[name='pitanje']").click(function (){

		resetujGreske();
		//let url = "{% url 'makequestion' last_id %}";

		var id = $(this).attr('id');

		let plainText = $($("#summernote").summernote("code")).text()
		let naslov=$("#naslov").val()

		if(naslov.length==0){
			document.getElementById("naslovGreska").innerHTML="Niste uneli naslov";

		}
		if(!plainText){

			document.getElementById("textGreska").innerHTML="Niste uneli tekst";
		}
		if(kategorije.length==0){
			document.getElementById("kategorijeGreska").innerHTML="Niste izabrali kategoriju";
		}
		else {
			//window.location.pathname = 'makequestions' + "/" + id;
		}


	});







});