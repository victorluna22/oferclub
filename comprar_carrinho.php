<?php include "include/header.php" ?>
<form action="" id="form-carrinho">

	<section class="container internas" id="area-compra">
		<article class="sixteen columns">
			<header>
				<h2 class="sixteen columns">Sua compra</h2>	
			</header>

			<ul id="lista-compra">
				<li>
					<figure>
						<div class="three columns omega">
							<img src="img/thumbnail.png" alt="">
						</div>

						<figcaption class="ten columns omega ">
							<p>Duas diárias para casal em Porto de Galinhas com café da manhã</p>
							<a href="">Detalhes</a>
						</figcaption>
					</figure>

					<div class="three columns"> 
						<p class="color-destaque">R$ 200,50</p>
						<img src="img/off.png" alt="">
						<span>50% OFF</span>
					</div>
				</li>

				<li>
					<figure>
						<div class="three columns omega">
							<img src="img/thumbnail.png" alt="">
						</div>

						<figcaption class="ten columns omega">
							<p>Duas diárias para casal em Porto de Galinhas com café da manhã</p>
							<a href="">Detalhes da oferta</a>
						</figcaption>
					</figure>

					<div class="three columns"> 
						<p class="color-destaque">R$ 200,50</p>
						<img src="img/off.png" alt="">
						<span>50% OFF</span>
					</div>
				</li>
			</ul>
		</article>
	</section>

	<aside class="container internas mg" id="cupon">
		<div class="bd-bottom">
			<div>
				<div>
					<div class="five columns">
						<p>Nome de quem vai usar o cupon</p>
						<input type="text" value="Augusto Andrade" class="bg-area-clara">
					</div>

					<div class="four columns">
						<p>Outras opções</p>
						<ul id="list-opcoes">
							<li class="current-opcoes preco-valor-atual bg-area-clara">1 - R$ 199,90</li>
							<li>
								<ul>
									<li class="bg-area-clara sub-itens preco-itens"><a href="#" data-valor="1" data-texto="1 - R$ 199,90"><p>1 - R$ 199,90 - Três diárias para casal em Porto de Galinhas</p></a></li>
									<li class="bg-area-clara sub-itens preco-itens"><a href="#" data-valor="2" data-texto="2 - R$ 299,90"><p>2 - R$ 299,90 - Três diárias para casal em Porto de Galinhas</p></a></li>
									<li class="bg-area-clara sub-itens preco-itens"><a href="#" data-valor="3" data-texto="3 - R$ 399,90"><p>3 - R$ 399,90 - Três diárias para casal em Porto de Galinhas</p></a></li>
								</ul>
							</li>
						</ul>
						<select name="preco" class="esconde-select">
							<option value="1">1</option>
							<option value="2">2</option>
							<option value="3">3</option>
						</select>


						<a href="#" class="presente"></a>
					</div>

					<div class="four columns">
						<p>Quantos ein?</p>
						<ul id="list-qtd">
							<li class="current-opcoes bg-area-clara qtd-valor-atual">1
							</li>

							<li>
								<ul>
									<li class="bg-area-clara sub-itens"><a href="#" data-valor="1" data-texto="1"><p>1</p></a></li>
									<li class="bg-area-clara sub-itens"><a href="#" data-valor="2" data-texto="2"><p>2</p></a></li>
									<li class="bg-area-clara sub-itens"><a href="#" data-valor="3" data-texto="3"><p>3</p></a></li>
								</ul>
							</li>
						</ul>
						<select name="preco" class="esconde-select">
							<option value="1">1</option>
							<option value="2">2</option>
							<option value="3">3</option>
						</select>

						 <p class="vezes">x R$ 199,90</p>

					</div>

					<div class="two columns">
						<p class="center-text">Subtotal(zinho)</p>
						<p class="bold-price">R$ 199,90</p>
					</div>
				</div>
			</div>
			
			<a href="#" id="new-cupon">Clique aqui é para adicionar outro cupom , visse.</a>
		</div>
		<!-- END BD-BOTTOM -->

		<div class="bd-bottom">
			<div class="sixteen columns">
				<a href="#" class="sb-line mostrar">Cupom de desconto</a>
				
				<div class="esconde-compra" id="cupon-div">
					<input type="text" class="input-claro" value="Digite o código">
					<input type="submit" class="btn" value="Verificar código">
					<span class="cancel">Cancelar</span>
					<p class="bold-price">- R$ 49,90</p>
				</div>
				<br>
				<p>Clique se você tem aquele cupom (código) que deixa mais baratinho ainda</p>
				
			</div>
		</div>
		<!-- END BD-BOTTOM -->

		<div class="bd-bottom">
			<div class="five columns omega">
				<p>Calcule o frete</p>
				<input type="text" id="calcular-frete" class="bg-area-clara" placeholder="Informe o seu cep">
				<a href="#" id="frete">Calcular</a>
			</div>
			
			<div class="eleven columns alpha">
				<p class="bold-price" id="frete-price" data-price="49.90">R$ 49,90</p>
			</div>
		</div>

		<div class="sixteen columns">
			<p class="total">Total</p>
			<p class="color-destaque" id="total-price">R$ 200,50</p>
		</div>
	</aside>	
	<!-- END BOX -->

	<aside class="container internas" id="endereco-entrega">
		<div class="sixteen columns">
			<p id="p-end">Endereço de entrega</p>

			<div class="esconde-endereco">
				<div class="seven columns omega">
					<p class="subtitle">Últimos cadastrados</p>
					
					<input type="radio" name="endereco-radio" id="endereco1">
					<label for="endereco1">
						Rua das Pedras - N 17
						<br>
						Aldeia - Camaragibe - PE
						<br>
						CEP: 54 753 155
					</label>

					<input type="radio" name="endereco-radio" id="endereco2">
					<label for="endereco2">
						Rua das Pedras - N 17
						<br>
						Aldeia - Camaragibe - PE
						<br>
						CEP: 54 753 155
					</label>

					<input type="radio" name="endereco-radio" id="endereco3">
					<label for="endereco3">
						Rua das Pedras - N 17
						<br>
						Aldeia - Camaragibe - PE
						<br>
						CEP: 54 753 155
					</label>
				</div>

				<div class="four columns">
					<p class="subtitle">Novo Endereço</p>

					<label for="cpf-endereco">CPF</label>
					<input type="text" id="cpf-endereco" class="bg-area-clara mg">

					<label for="rua-endereco">Nome da rua</label>
					<input type="text" id="rua-endereco" class="bg-area-clara mg">

					<label for="numero-endereco">Número da casa</label>
					<input type="text" id="numero-endereco" class="bg-area-clara mg">

					<label for="complemento-endereco">Complemento</label>
					<input type="text" id="complemento-endereco" class="bg-area-clara mg">
				</div>

				<div class="four columns">
					<label for="cep-endereco">CEP</label>
					<input type="text" id="cep-endereco" class="bg-area-clara mg">

					<label for="bairro-endereco">Bairro</label>
					<input type="text" id="bairro-endereco" class="bg-area-clara mg">

					<label for="cidade-endereco">Cidade</label>
					<input type="text" id="cidade-endereco" class="bg-area-clara mg">

					<label for="estado-endereco">Estado</label>
					<input type="text" id="estado-endereco" class="bg-area-clara mg">

					<a href="#" class="salvar">Salvar</a>
				</div>
			</div>
			<!-- FIM DO BOX ESCONDIDO -->
		</div>
	</aside>
	<!-- END BOX -->

	<aside class="container internas pd">
		<div class="sixteen columns">
			<p class="pagamento">Pagamento</p>
			<br>
			<img src="img/pagseguro.gif" alt="">
		</div>
	</aside>

	<script type="text/javascript" src="js/handlebars-v2.0.0.js"></script>
	<!-- END TEMPLATE ENGINE -->

	<script id="entry-template" type="text/x-handlebars-template">
	<div>
		<div class="container internas" >
			<article class="eight columns">
				<header>
					<h2>Dados do cupom presente</h2>
				</header>

				<label for="nome-ps">Seu nome</label>
				<input type="text" name="nome[{{index}}]" id="nome-ps">

				<label for="pessoa-ps">Nome da pessoa bacana presenteada</label>
				<input type="text" name="pessoa[{{index}}]" id="pessoa-ps">

				<label for="mensagem-ps">Capriche no texto viu!</label>
				<textarea id="mensagem-ps" name="mensagem[{{index}}]"></textarea>

			</article>

			<article class="eight columns">
				<header>
					<h2>Escolha como deseja enviar</h2>
				</header>

				<label for="email-ps">Email do presenteado</label>
				<input type="text" id="email-ps" name="email[{{index}}]">
				<br>
				<p>Em que data você deseja que o e-mail com o cupom  seja enviado?</p>


				<label for="data-ps">Data do envio</label>
				<input type="date" id="data-ps" name="data[{{index}}]">

				<div>
					<input type="checkbox" id="copia" name="copia[{{index}}]"> <label for="copia">Óa, quero receber uma cópia</label>
				</div>
			</article>
		</div>

		<div class="container internas">
			<a href="" class="prontinho">Prontinho</a>
			<p class="cancel-ps">Cancelar</p>
		</div>
	</div>
	</script>

	<script type="text/javascript">

		document.querySelector(".salvar").addEventListener("click",function(e){
			e.preventDefault();
		});

		var opc = document.querySelectorAll(".current-opcoes"),
		presente_item = document.querySelectorAll(".presente");

		clickPresente(presente_item);
		abrirOpcoes(opc);

		document.querySelector("#new-cupon").addEventListener("click",function(e){
			e.preventDefault();
			
			var html = this.previousElementSibling.querySelectorAll("div")[0].cloneNode(true);
			var new_opc = html.querySelectorAll(".current-opcoes");
			
			abrirOpcoes(new_opc);

			this.parentNode.querySelectorAll("div")[0].appendChild(html);
			
			clickPresente(document.querySelectorAll(".presente"));
			valoresCupon(document.querySelector("#cupon").querySelectorAll("li"));
			setTotal(this.parentNode.querySelectorAll(".bold-price"));


		});

		function abrirOpcoes(opc){
			Array.prototype.forEach.call(opc,function(obj){
				obj.addEventListener("click",function(){
					if(this.classList.contains("aberto")){
						this.classList.remove("aberto");
						this.nextElementSibling.querySelector("ul").style.display = "none";
					}else{
						this.classList.add("aberto");
						this.nextElementSibling.querySelector("ul").style.display = "block";
					}
				});
			});
		}

		document.querySelector(".mostrar").addEventListener("click",function(e){
			e.preventDefault();
			this.nextElementSibling.style.display = "block";
		});

		document.querySelector(".cancel").addEventListener("click",function(e){
			e.preventDefault();
			this.parentNode.style.display = "none";
		});

		function clickPresente(obj){
			Array.prototype.forEach.call(obj,function(element,index){
				element.addEventListener("click",function(e){
					e.preventDefault();
					presente(index);
				})
			});
		}

		var presente = function(i){
			if(document.querySelectorAll(".presente-box")[i]){
				document.querySelectorAll(".presente-box")[i].classList.add("ativo-presente");
				document.querySelector("html").classList.add("show-presente");
			}else{
				var source = document.querySelector("#entry-template").innerHTML, 
				template = Handlebars.compile(source), 
				html = template({index:i});

				var secao = document.createElement("section");
				secao.classList.add("presente-box");
				secao.innerHTML = html;

				secao.querySelector(".cancel-ps").addEventListener("click",function(e){
					e.preventDefault();
					fecharPresente(this);
				});

				secao.querySelector(".prontinho").addEventListener("click",function(e){
					e.preventDefault();
					fecharPresente(this);
				});

				document.querySelector("#form-carrinho").appendChild(secao);
				var new_present = document.querySelectorAll(".presente-box ")[i];

				setTimeout(function(){
					new_present.classList.add("ativo-presente");
					document.querySelector("html").classList.add("show-presente");
				},300);

			}
		}

		var fecharPresente = function(element){
			element.parentNode.parentNode.parentNode.classList.remove("ativo-presente");
			document.querySelector(".show-presente").classList.remove("show-presente");
		}

		valoresCupon(document.querySelector("#cupon").querySelectorAll("li"));

		function valoresCupon(obj){
			Array.prototype.forEach.call(obj,function(element,index){	
				if(element.classList.contains("sub-itens")){
					element.querySelector("a").addEventListener("click",function(e){
						e.preventDefault();
						
						var texto = this.dataset.texto;
						this.parentNode.parentNode.parentNode.previousElementSibling.textContent = texto;
						this.parentNode.parentNode.style.display = "none";

						this.parentNode.parentNode.parentNode.parentNode.nextElementSibling.value = this.dataset.valor;
						var pai = this.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode;

						if(this.parentNode.classList.contains("preco-itens")){
							pai.querySelector(".vezes").textContent = "x "+texto.substr(3);
						}
						
						var preco = pai.querySelector(".preco-valor-atual").textContent.substr(7).replace(",","."), quantidade = pai.querySelector(".qtd-valor-atual").textContent;
						pai.querySelector(".bold-price").textContent = "R$ "+(parseFloat(preco*quantidade).toFixed(2)).replace(".",",");

						setTotal(pai.parentNode.querySelectorAll(".bold-price"));
					});
				}

			});
		}

		function setTotal(obj){
			var valorTotal = 0;
			Array.prototype.forEach.call(obj,function(element,i){
				valorTotal += parseFloat(element.textContent.substr(3).replace(",","."));
			});

			valorTotal += parseFloat(document.querySelector("#frete-price").dataset.price);

			document.querySelector("#total-price").textContent = "R$ "+valorTotal.toFixed(2).replace(".",",");
		}	
	</script>

	<footer id="footer-secundario">
		© 2014 Groupon, Inc. Todos os direitos reservados Ofer.Club - CNPJ 20.529.816/00001-14 | Estrada de Aldeia, Camaragibe/PE
	</footer>
	</form>
</body>
</html>