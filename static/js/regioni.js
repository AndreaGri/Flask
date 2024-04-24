
function getElenco(){
    fetch('https://3248-andreagri-flask-fbtk26ncc4d.ws-eu110.gitpod.io/elenco')
    .then(response => response.json())
    .then(data=> {
        console.log(data)
        
        for ( let regione in data )
        {
            document.getElementById('elenco').innerHTML += data[regione]
        }
    })
}
