// Criar um novo objeto Date com a data atual
const hoje = new Date();

// Obter o dia, mês e ano
const dia = hoje.getDate();
const mes = hoje.toLocaleString('pt-br', { month: 'long' });
const ano = hoje.getFullYear();

// Formatar a data como "dia de mês, ano"
const dataFormatada = `${dia} de ${mes}, ${ano}`;

// Mostrar a data no elemento com o id="data-hoje"
document.getElementById("data-hoje").textContent = dataFormatada;