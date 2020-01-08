$(document).ready(function() {
    $('.imageGallery').lightSlider({
        adaptiveHeight:true,
        item:1,
        slideMargin:0,
        loop:true
    });  

 
    $('.tap-target').tapTarget();

  

    function animateCss(element, animationName, callback) {
    const node = document.querySelector(element)
    node.classList.add('animated', animationName)

    function handleAnimationEnd() {
        node.classList.remove('animated', animationName)
        node.removeEventListener('animationend', handleAnimationEnd)

        if (typeof callback === 'function') callback()
    }

    node.addEventListener('animationend', handleAnimationEnd)
	}

    $('.dropdown-trigger').dropdown({constrainWidth:false,coverTrigger:false});

    $("#cadastrar").click(function(){
    	
    	if ($("#id_email").val() != '' && $("#id_senha").val() !='' && $("#id_nome").val() != '') {

	    		if($("#id_latitude,#id_longitude").val() == ''){
			    		$("#step1,.stap1_titulo")
			    		.addClass("animated fadeOutLeft faster")    		
			    		.on('animationend', function() { 
			    			   $(this).addClass("hidden");
			    			   $("#step2").addClass("animated fadeIn faster").removeClass("hidden fadeOut").unbind( "animationend" );
			    		});
			    		

			    		$(".step_back").click(function(){

			    			$("#step2")
				    		.addClass("fadeOut") 
				    		.removeClass("fadeIn")		
				    		.on('animationend', function() { 
				    			   $(this).addClass("hidden");
				    			   $("#step1,.stap1_titulo").removeClass("hidden fadeOutLeft").addClass("fadeInLeft").unbind( "animationend" );
				    			   $("#cadastrar").text("Continuar");
			    			 });

			    		});

			    		$('.tap-target').tapTarget('open');

			    		if (navigator.geolocation){
						    navigator.geolocation.getCurrentPosition(showPosition,showError);
						 }else{
						 	x.innerHTML="Seu browser não suporta Geolocalização.";
						 }
						 

						function showPosition(position){
						
						    $.ajax({
							        url: 'https://api.opencagedata.com/geocode/v1/json',
							        method: 'GET',
							        data: {
							          'key': '6940adf71cd14d6697323d05946d7388',
							          'q': ''+position.coords.latitude+','+position.coords.longitude+'',
							          'no_annotations': 1
							          // see other optional params:
							          // https://opencagedata.com/api#forward-opt
							        },
							        dataType: 'json',
							        statusCode: {
							          200: function(response){  // success
							           
							            $(".cidade_name").text(response.results[0].components.city)
							            $(".pulse_icon").addClass("animateStop");
							            $('.tap-target').tapTarget('close');
							            $("#cadastrar").addClass("pulse");
							            $("#id_latitude").val(position.coords.latitude);
							            $("#id_longitude").val(position.coords.longitude);
							           
							          },
							          402: function(){
							            console.log('hit free-trial daily limit');
							            console.log('become a customer: https://opencagedata.com/pricing');
							          }
							          // other possible response codes:
							          // https://opencagedata.com/api#codes
							        }
						     });
						}
						function showError(error){
						  switch(error.code){
							    case error.PERMISSION_DENIED:
							      x.innerHTML="Usuário rejeitou a solicitação de Geolocalização."
							      break;
							    case error.POSITION_UNAVAILABLE:
							      x.innerHTML="Localização indisponível."
							      break;
							    case error.TIMEOUT:
							      x.innerHTML="A requisição expirou."
							      break;
							    case error.UNKNOWN_ERROR:
							      x.innerHTML="Algum erro desconhecido aconteceu."
							      break;
						    }
						}



			    		$(this).text("Finalizar cadastro");

			    		return false;
	    		}else{

	    			return true;
	    		}
    	}else{
    	

    		if($("#id_email").val() == ''){

    			animateCss("#id_email","shake",null);

    		}else if ($("#id_senha").val() =='') {

    			animateCss("#id_senha","shake",null);

    		}else if ($("#id_nome").val() == '') {

				animateCss("#id_nome","shake",null);
    		}

    		return false;
   
    	}

    	
    	

    });
  });