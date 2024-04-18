
function Click()    {
    const peso = parseFloat(document.getElementById('peso').value)
    const altezza=parseFloat(document.getElementById('altezza').value)
    const imc= peso / (altezza * altezza)
    let img;
    console.log(imc)
    console.log(peso)
    console.log(altezza)
    document.getElementById('dai').innerHTML= 'Il tuo IMC è '+ imc
    if (imc<18.5) {
        document.getElementById('imc').innerHTML= 'Sei sottopeso'
        img= static/images/carne.jpg
    }
    else if ( 18.5 < imc < 25) {
        document.getElementById('imc').innerHTML= 'Sei normopeso'
        img=static/images/riso.jpg
        

    }
    else if (imc>25) {
        document.getElementById('imc').innerHTML= 'Sei sovrappeso'
        img=static/images/insalata.jpg
        

    }
    document.getElementById('img').src= img
}