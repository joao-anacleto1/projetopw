const botao = document.getElementById("botao");
const inputNome = document.getElementById("nome");
const greeting = document.getElementById("greeting");
const alerta = document.getElementById("alerta");
const alerta2 = document.getElementById("alerta2");

// Adicionando um ouvinte de eventos ao botão de envio
botao.addEventListener("click", function() {
  // Obtendo o nome inserido pelo usuário
  const nome = inputNome.value;

  // Exibindo a mensagem de boas-vindas
  console.log("Bem-vindo, " + nome + "!");
  greeting.innerHTML = "Olá, " + nome + "!";
  alert("Olá, " + nome + "! Como estás?");
  alerta.innerHTML = "Bem-vindo ao meu portfólio digital, " + nome + "!";
  alerta2.innerHTML = "Espero que gostes desta pagina, " + nome + "!";
});