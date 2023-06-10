const body = document.querySelector("body"),
  nav = document.querySelector("nav"),
  modeToggle = document.querySelector(".dark-light"),
  searchToggle = document.querySelector(".searchToggle"),
  siderbarOpen = document.querySelector(".siderbarOpen"),
  siderbarClose = document.querySelector(".siderbarClose");

// Verificar se há uma entrada "darkmode" no LocalStorage
let darkmodeData = localStorage.getItem("darkmode");
if (darkmodeData === null) {
  darkmodeData = true;
} else {
  darkmodeData = JSON.parse(darkmodeData);
}

// Definir o modo escuro com base no valor do LocalStorage
if (darkmodeData) {
  body.classList.add("dark");
  modeToggle.classList.add("active");
} else {
  body.classList.remove("dark");
}

// Adicionar um event listener para o botão de alternar o modo escuro
modeToggle.addEventListener("click", () => {
  modeToggle.classList.toggle("active");

  // Alternar o valor da variável darkmodeData
  darkmodeData = !darkmodeData;

  // Atualizar a classe do body com base no novo valor de darkmodeData
  if (darkmodeData) {
    body.classList.add("dark");
  } else {
    body.classList.remove("dark");
  }

  // Armazenar o novo valor de darkmodeData no LocalStorage
  localStorage.setItem("darkmode", JSON.stringify(darkmodeData));
});

// Adicionar um event listener para o botão de alternar a caixa de pesquisa
searchToggle.addEventListener("click", () => {
  searchToggle.classList.toggle("active");
});

// Adicionar um event listener para o botão de alternar a barra lateral
siderbarOpen.addEventListener("click", () => {
  nav.classList.add("active");
});

// Adicionar um event listener para o body para fechar a barra lateral ao clicar fora dela
body.addEventListener("click", (e) => {
  let clickedElm = e.target;

  if (
    !clickedElm.classList.contains("siderbarOpen") &&
    !clickedElm.classList.contains("menu")
  ) {
    nav.classList.remove("active");
  }
});
