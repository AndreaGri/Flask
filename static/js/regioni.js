function getElenco() {
    fetch('https://3246-andreagri-flask-7c4tmmus9jh.ws-eu110.gitpod.io/elenco')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        for (let regione in data) {
            document.getElementById('elenco').innerHTML += '<a href=https://3246-andreagri-flask-7c4tmmus9jh.ws-eu110.gitpod.io/info/'+data[regione]+'>'+ data[regione] + '<br />'
        }
    })
}


