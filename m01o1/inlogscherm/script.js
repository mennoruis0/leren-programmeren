let naamIngelogd = "";

function handlelogin(){
    let naam = document.getElementById('inputNaam').value;
    console.log("U heeft op de button geklikt");
    if (naamIngelogd === ""){
        naamIngelogd = naam;
        console.log('U bent ingelogd: ' + naam);
        document.getElementById('inputNaam').value = '';
    }
}