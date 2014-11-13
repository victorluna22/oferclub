if(document.querySelector("#propagandas")){

		for (key in json) {
			var secao = document.createElement("section");
			secao.setAttribute("class","box-content sixteen columns carrosel");

			secao.innerHTML = '<header>'+
				'<h3>'+json[key].titulo_bloco+'</h3>'+
				'<button class="prev"></button>'+
				'<button class="next" data-bloco="'+json[key].titulo_bloco+'"></button>'+
				'<a href="'+json[key].link+'" class="ver-carrosel">Ver todos</a>'+
			'</header>'+
			
			'<div>'+
			'</div>';
			document.querySelector("#json").appendChild(secao);
			
			for(var i = 0; i < 3; i++){
				if (json[key].ofertas[i]){
				secao.querySelector("div").innerHTML += '<article>'+
						'<figure>'+
							'<a href="'+json[key].ofertas[i].link+'"><img src="'+json[key].ofertas[i].imagem+'" alt=""></a>'+
							'<figcaption>'+
'								<a href="'+json[key].ofertas[i].link+'"><div class="desconto">'+json[key].ofertas[i].discount+'% OFF</div></a>'+
								'<a href="'+json[key].ofertas[i].link+'"><div class="compras">'+json[key].ofertas[i].quantity+' compraram</div></a>'+
								'<a href="'+json[key].ofertas[i].link+'"><div class="volta">'+Math.floor(json[key].ofertas[i].cashback)+'% de volta</div></a>'+
								'<a href="'+json[key].ofertas[i].link+'"><div class="dias">'+json[key].ofertas[i].remaining+'</div></a>'+
							'</figcaption>'+
						'</figure>'+
					'<header>'+
						'<h4>'+json[key].ofertas[i].title+'</h4>'+
						'<a href="#"><h5>'+json[key].ofertas[i].partner+'</h5></a>'+
						'<a href="#"><span class="localidade-box">'+json[key].ofertas[i].city+'</span></a>'+
						'<p class="riscado">De '+json[key].ofertas[i].before_price+'</p>'+
						'<p class="color-destaque">Por  '+json[key].ofertas[i].new_price+'</p>'+
					'</header>'+
				'</article>';
				}
			}

		};

	//quando girar o tablet ou celular
	window.addEventListener("resize",function(){
		var carroseis =  document.querySelectorAll(".carrosel");
		Array.prototype.forEach.call(carroseis,function(element){
			element.querySelector("div").style.left = 0;
		});
	});

	var prev = document.querySelectorAll(".prev"), next = document.querySelectorAll(".next");

	//proximo
	Array.prototype.forEach.call(next,function(element){

		//adicionando evento clique
		element.addEventListener("click",function(){

			var bloco = this.dataset.bloco, content = this.parentNode.parentNode, n_itens = content.querySelectorAll("article").length;


				if(content.querySelector("div").style.left.split("px")[0]){
					var width = parseInt((-(content.querySelector("article").offsetWidth + 19))) + parseInt((content.querySelector("div").style.left.split("px")[0]));
				}else{
					var width = parseInt((-(content.querySelector("article").offsetWidth + 19)));
				}
				
				if((n_itens <= 8)){
					for(key in json){
						if(json[key].titulo_bloco == bloco){
							var new_iten = document.createElement("article");
							new_iten.innerHTML = '<figure>'+
									'<a href="'+json[key].ofertas[n_itens].link+'"><img src="'+json[key].ofertas[n_itens].imagem+'" alt=""></a>'+
									'<figcaption>'+
		'								<a href="'+json[key].ofertas[n_itens].link+'"><div class="desconto">'+json[key].ofertas[n_itens].discount+'% OFF</div></a>'+
										'<a href="'+json[key].ofertas[n_itens].link+'"><div class="compras">'+json[key].ofertas[n_itens].quantity+' compraram</div></a>'+
										'<a href="'+json[key].ofertas[n_itens].link+'"><div class="volta">'+Math.floor(json[key].ofertas[n_itens].cashback)+'% de volta</div></a>'+
										'<a href="'+json[key].ofertas[n_itens].link+'"><div class="dias">'+json[key].ofertas[n_itens].remaining+'</div></a>'+
									'</figcaption>'+
								'</figure>'+
							'<header>'+
								'<h4>'+json[key].ofertas[n_itens].title+'</h4>'+
								'<a href="#"><h5>'+json[key].ofertas[n_itens].partner+'</h5></a>'+
								'<a href="#"><span class="localidade-box">'+json[key].ofertas[n_itens].city+'</span></a>'+
								'<p class="riscado">De R$:'+json[key].ofertas[n_itens].before_price+'</p>'+
								'<p class="color-destaque">Por R$ '+json[key].ofertas[n_itens].new_price+'</p>'+
							'</header>';

							content.querySelector("div").appendChild(new_iten);
						}
					}
				}

				content.querySelector("div").style.left = width+"px";

		});
	});

	//anterior
	Array.prototype.forEach.call(prev,function(element){

		//adicionando evento clique
		element.addEventListener("click",function(){

			var content = this.parentNode.parentNode,left = content.querySelector("div").style.left.split("px")[0];
			
			if(left!=0){

				if(left){
					var width = parseInt(((content.querySelector("article").offsetWidth + 19))) + parseInt((content.querySelector("div").style.left.split("px")[0]));
				}else{
					var width = parseInt(((content.querySelector("article").offsetWidth + 19)));
				}
				
				content.querySelector("div").style.left = width+"px";
			}


		});
	});
}

if(document.querySelector("#slider")){
	var primeiro = document.querySelectorAll("#slider figure")[0];
	primeiro.style.display = "block";
	primeiro.style.opacity = 0;

	setTimeout(function (argument) {
		primeiro.classList.add("ativo");

		var bullets = document.querySelectorAll("#slider figure");
		Array.prototype.forEach.call(bullets,function(element,i){
			var li = document.createElement("li");
			li.dataset.index = i;

			//clique dos bullets
			li.addEventListener("click",function(){
				clearInterval(intervalo);
				var ativo = document.querySelector(".ativo"),proximo = document.querySelectorAll("#slider figure")[this.dataset.index];

				ativo.classList.remove("ativo");
				
				setTimeout(function(){
					ativo.style.display = "none";
				},1000,ativo);

				proximo.style.display = "block";
				proximo.style.opacity = 0;

				setTimeout(function(){
					arguments[0].classList.add("ativo");
				},1,proximo);

				document.querySelector(".ativo-thumb").classList.remove("ativo-thumb");
				this.classList.add("ativo-thumb");

				intervalo = setInterval(slide,5000,primeiro);
			});

			if(i == 0){
				li.classList.add("ativo-thumb");
			}
			document.querySelector("#slider ul").appendChild(li);
		});
	},1);

	var intervalo = setInterval(slide,5000,primeiro);

	function slide(){
		var ativo = document.querySelector(".ativo"), bullets_ativo = document.querySelector(".ativo-thumb");
		ativo.classList.remove("ativo");
		bullets_ativo.classList.remove("ativo-thumb");

		if(ativo.nextElementSibling){
			ativo.nextElementSibling.style.display = "block";
			ativo.nextElementSibling.style.opacity = 0;

			setTimeout(function(){
				arguments[0].style.display = "none";
			},1000,ativo);
			
			setTimeout(function (argument) {
				arguments[0].classList.add("ativo");
				arguments[1].nextElementSibling.classList.add("ativo-thumb");
			},1,ativo.nextElementSibling,bullets_ativo);
		}else{
			arguments[0].style.display = "block";
			arguments[0].style.opacity = 0;
			
			setTimeout(function (argument) {
				arguments[0].classList.add("ativo");
				document.querySelectorAll("#slider li")[0].classList.add("ativo-thumb");
			},1,arguments[0]);
		}
	}
}

if(document.querySelector(".produto")){
	var pdt_img = document.querySelectorAll(".produto img"), html = "";
	
	setTimeout(function(){
		pdt_img[0].classList.add("atv-produto")
	},100);

	Array.prototype.forEach.call(pdt_img,function(obj){
		var src = obj.src;
		html += '<img src="'+src+'" alt="" widt="50px" height="50px">';
	});

	document.querySelector(".produto figure").innerHTML = html;

	var sld_int = setInterval(function(){
		var ativo = document.querySelector(".atv-produto");

		ativo.classList.remove("atv-produto");

		if(ativo.nextElementSibling){
			ativo.nextElementSibling.classList.add("atv-produto");
		}else{
			pdt_img[0].classList.add("atv-produto");
		}
	},4000);
}

if(document.querySelector(".box-filtro div")){
	document.querySelector(".box-filtro div").addEventListener("click",function(){
		if(this.classList.contains("hovered")){
			this.classList.remove("hovered");
		}else{
			this.classList.add("hovered");
		}
	});
}

//seleciona as classes
var itens_nav = document.querySelectorAll(".itens_nav"), pagina = 1, itens_ordem = document.querySelectorAll(".box-filtro li");
var subcategorias = "&subcategory",interesses = "&interesses",ordem = "&order=mais-recentes";

//pecorre as classes do menu de categorias
Array.prototype.forEach.call(itens_nav, function(obj){
	obj.addEventListener("click",function(e){
		e.preventDefault();

		navegacao.setURL(this.dataset.slug,this,false);
	});
});

//pecorre as classes do menu de ordens
Array.prototype.forEach.call(itens_ordem, function(obj){
	obj.querySelector("a").addEventListener("click",function(e){
		e.preventDefault();

		navegacao.setURL(this.dataset.slug,this,false);
	});
});

if(document.querySelector("#carregar")){
	
document.querySelector("#carregar").addEventListener("click",function(e){
	e.preventDefault();

	pagina += 1;
	navegacao.setURL(false,false,"mais")
});

var navegacao = {
	getSubcategory : function(slug,obj){
		//chama o metódo 'checarCampos'
		this.checaCampos(obj);

		return this.getSlug(slug,"&subcategory=",".subcategorias");
	},



	getInteresses : function(slug,obj){
		//chama o metódo 'checarCampos'
		this.checaCampos(obj);

		return this.getSlug(slug,"&interesses=",".interesses_itens");
	},

	getSlug : function(slug,opcao,classe){
		var html = opcao, subcat = document.querySelectorAll(classe),i=0;


		Array.prototype.forEach.call(subcat,function(element){
			if(element.classList.contains("checado")){
				html += i!= document.querySelectorAll(classe+".checado").length-1?element.dataset.slug+",":element.dataset.slug;
				i++;
			}
		});

		return html;
	},

	getOrdem : function(slug){
		return "&order="+slug;
	},

	checaCampos: function(obj){
		//manipulando a opção de checar o conteudo
		if(obj.classList.contains("checado")){
			obj.querySelector("input").checked = false;
			obj.classList.remove("checado");
		}else{
			obj.querySelector("input").checked = true;
			obj.classList.add("checado");
		}
	},

	setURL : function (slug,obj,type){
		if(type != "mais"){
			if(obj.classList.contains("subcategorias")){
				subcategorias = this.getSubcategory(slug,obj);

			}else if(obj.classList.contains("interesses_itens")){
				interesses = this.getInteresses(slug,obj);
			}else {
				//ordem
				ordem = this.getOrdem(slug);
			}
		}


		if(type == "mais"){
			var url_concatenada = cat+subcategorias+interesses+ordem+"&page="+pagina;
			$.ajax({
					type: "get",
					dataType: "json",
					url: url_concatenada,
					success: function(data){
						for(i=0; i<= data.length - 1; i++){
							$("#lista-div").append('<section class="box-content listagem-produtos esconde-lista">'+
							'<article>'+
									'<figure>'+
										'<a href="'+data[i].link+'"><img src="'+data[i].imagem+'" alt=""></a>'+
										'<figcaption>'+
			'								<a href="'+data[i].link+'"><div class="desconto">'+data[i].discount+'% OFF</div></a>'+
											'<a href="'+data[i].link+'"><div class="compras">'+data[i].quantity+' compraram</div></a>'+
											'<a href="'+data[i].link+'"><div class="volta">'+Math.floor(data[i].cashback)+'% de volta</div></a>'+
											'<a href="'+data[i].link+'"><div class="dias">'+data[i].day+' dias '+data[i].hours+'</div></a>'+
										'</figcaption>'+
									'</figure>'+
								'<header>'+
									'<h4>'+data[i].title+'</h4>'+
									'<a href="#"><h5>'+data[i].partner+'</h5></a>'+
									'<a href="#"><span class="localidade-box">'+data[i].city+'</span></a>'+
									'<p class="riscado">De R$:'+data[i].before_price+'</p>'+
									'<p class="color-destaque">Por R$ '+data[i].new_price+'</p>'+
								'</header>'+
							'</article>'+
					'</section>');
						}
						
						$(".esconde-lista").slideDown("slow");


					}
				});

		}else{
			var url_concatenada = cat+subcategorias+interesses+ordem+"&page=1";

			$("#lista-div").slideUp("slow",function(){
				$.ajax({
					type: "get",
					dataType: "json",
					url: url_concatenada,
					success: function(data){
						$(".box-content").remove();
						var marcadores = [];

						for(i=0; i<= data.length - 1; i++){
							$("#lista-div").append('<section class="box-content listagem-produtos">'+
							'<article>'+
									'<figure>'+
										'<a href="produto.php"><img src="'+data[i].imagem+'" alt=""></a>'+
										'<figcaption>'+
			'								<a href="produto.php"><div class="desconto">'+data[i].discount+'% OFF</div></a>'+
											'<a href="produto.php"><div class="compras">'+data[i].quantity+' compraram</div></a>'+
											'<a href="produto.php"><div class="volta">'+Math.floor(data[i].cashback)+'% de volta</div></a>'+
											'<a href="produto.php"><div class="dias">'+data[i].day+' dias '+data[i].hours+'</div></a>'+
										'</figcaption>'+
									'</figure>'+
								'<header>'+
									'<h4>'+data[i].title+'</h4>'+
									'<a href="#"><h5>'+data[i].partner+'</h5></a>'+
									'<a href="#"><span class="localidade-box">'+data[i].city+'</span></a>'+
									'<p class="riscado">De R$:'+data[i].before_price+'</p>'+
									'<p class="color-destaque">Por R$ '+data[i].new_price+'</p>'+
								'</header>'+
							'</article>'+
					'</section>');

							marcadores[0] = {
						      lat:data[i].latitude,
						      lng: data[i].longitude,
						      nome: data[i].title,
						      morada1:data[i].partner,
						      morada2: data[i].city
							}
						}

						$("#lista-div").slideDown(2000);

						initialize(marcadores);

						pagina = 1;
						
					}
				});
			});
			//fimdofadeOut

		}

		window.history.replaceState('Object','Listar Produtos',url_concatenada);
	}//fim do setUrl
}
}

var markersData = [];

// Esta função vai percorrer a informação contida na variável markersData
// e cria os marcadores através da função createMarker
function displayMarkers(markersData){

   // esta variável vai definir a área de mapa a abranger e o nível do zoom
   // de acordo com as posições dos marcadores
   var bounds = new google.maps.LatLngBounds();

   // Loop que vai percorrer a informação contida em markersData 
   // para que a função createMarker possa criar os marcadores 
   for (var i = 0; i < markersData.length; i++){

      var latlng = new google.maps.LatLng(markersData[i].lat, markersData[i].lng);
      var nome = markersData[i].nome;
      var morada1 = markersData[i].morada1;
      var morada2 = markersData[i].morada2;

      createMarker(latlng, nome, morada1, morada2);

      // Os valores de latitude e longitude do marcador são adicionados à
      // variável bounds
      bounds.extend(latlng); 
   }

   // Depois de criados todos os marcadores,
   // a API, através da sua função fitBounds, vai redefinir o nível do zoom
   // e consequentemente a área do mapa abrangida de acordo com
   // as posições dos marcadores
   map.fitBounds(bounds);
}

// Função que cria os marcadores e define o conteúdo de cada Info Window.
function createMarker(latlng, nome, morada1, morada2){
   var marker = new google.maps.Marker({
      map: map,
      position: latlng,
      title: nome
   });

   // Evento que dá instrução à API para estar alerta ao click no marcador.
   // Define o conteúdo e abre a Info Window.
   google.maps.event.addListener(marker, 'click', function() {
      
      // Variável que define a estrutura do HTML a inserir na Info Window.
      var iwContent = '<div id="iw_container">' +
      '<div class="iw_title">' + nome + '</div>' +
      '<div class="iw_content">' + morada1 + '<br />' +
      morada2;
      
      // O conteúdo da variável iwContent é inserido na Info Window.
      infoWindow.setContent(iwContent);

      // A Info Window é aberta com um click no marcador.
      infoWindow.open(map, marker);
   });
}

function initialize(markersData) {
   var mapOptions = {
      center: new google.maps.LatLng(-19.212355602107472, -44.20234468749999),
      zoom: 3,
      mapTypeId: 'roadmap',
   };

   map = new google.maps.Map(document.getElementById('mapa-listar'), mapOptions);

   // Cria a nova Info Window com referência à variável infoWindow.
   // O conteúdo da Info Window é criado na função createMarker.
   infoWindow = new google.maps.InfoWindow();

   // Evento que fecha a infoWindow com click no mapa.
   google.maps.event.addListener(map, 'click', function() {
      infoWindow.close();
   });

   // Chamada para a função que vai percorrer a informação
   // contida na variável markersData e criar os marcadores a mostrar no mapa
   displayMarkers(markersData);
}

  // {
  //     lat: 40.6386333,
  //     lng: -8.745,
  //     nome: "oferta 2",
  //     morada1:"walmart",
  //     morada2: "Recife"
  //  }


if(document.querySelector(".link")){
	document.querySelector(".link").addEventListener("click",function(e){
	    mostrarCad(this,e);
	});

	function mostrarCad(obj,e){
	    e.preventDefault();
	    
	    obj.parentNode.innerHTML = "Já é cadastrado? Massa, <a href='#' class='login-form'>entre com sua conta.</a>" 
	    document.querySelector(".login-form").addEventListener('click',function(e){
	        mostrarLogin(this,e);
	    });

	    var recolhe = document.querySelector(".recolhe");
	    recolhe.previousElementSibling.classList.add("recolhe");

	    setTimeout(function(){
	        recolhe.classList.remove("recolhe");
	    },1000);
	}

	function mostrarLogin(obj,e){
	    e.preventDefault();

	    obj.parentNode.innerHTML = "<a href='#' class='link'>Cadastre-se</a>, é rapidinho";

	    document.querySelector(".link").addEventListener('click',function(e){
	        mostrarCad(this,e);
	    });


	    var recolhe = document.querySelector(".recolhe");
	    recolhe.nextElementSibling.classList.add("recolhe");

	    setTimeout(function(){
	        recolhe.classList.remove("recolhe");
	    },1000);
	}
}

$(document).ready(function(){
	$("#cupon-div input[type='text']").focus(function(){
		if($(this).val() == "Digite o código"){
			$(this).val("");
			
		}
	});
	$("#cupon-div input[type='text']").blur(function(){
		if($(this).val() == ""){
			$(this).val("Digite o código");
		}
	});

	$("#cupon-div input[type='submit']").click(function(){
		var $obj = $(this);
		$.ajax({
			type: "get",
			url: "/verifica-codigo/"+$obj.prev().val()+"/",
			success: function(data){
				if(data.error){
					mensagem("#cupom-info","Código inválido!","alert-danger");
				}else {
					$obj.next().next().text("- R$ "+data.discount.toFixed(2).replace(".",","));
					setTotal(document.querySelectorAll("#cupon > .bd-bottom")[0].querySelectorAll(".bold-price"));
				}
			},
		});
		return false;
	});

	$("#cupon-div .cancel").click(function(){
		var preco_desconto = parseFloat(document.querySelector("#cupon-div").querySelector(".bold-price").textContent.substr(4).replace(",",".")),
		total = parseFloat(document.querySelector("#total-price").textContent.substr(3).replace(",",".")),
		calculo = total + preco_desconto;

		document.querySelector("#total-price").textContent = "R$ "+calculo.toFixed(2).replace(".",",");

		$("#cupon-div input[type='text']").val("Digite o código");
		return false;
	});
});

var itens_topo = document.querySelectorAll("#header label ~ ul li");

Array.prototype.forEach.call(itens_topo,function(element){
	element.addEventListener("click", function(){
		this.parentNode.style.display = "none";
		this.parentNode.parentNode.querySelector("select").value = this.dataset.id;
		document.querySelector("#form-change-city").submit();
	});
})
