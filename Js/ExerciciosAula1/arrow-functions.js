// 1)
const ask = (question, yes, no) => (confirm(question)) ? yes() : no();

ask(
    "Você aceita?",
    () => alert("Você aceitou."),
    () => alert("Você cancelou a execução.")
);