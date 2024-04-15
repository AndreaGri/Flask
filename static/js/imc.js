
function Click()    {
    let peso = parseFloat(document.getElementById('peso'))
    let altezza=parseFloat(document.getElementById('altezza'))
    let imc= peso / (altezza * altezza)

}

alert ( 'ecco'+ imc )