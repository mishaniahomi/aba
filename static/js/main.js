function show_form_search() {
console.log('1111');
    console.log(document.getElementById('search').style.display);
    if(document.getElementById('search').style.display == 'block')
    document.getElementById('search').style.display = '';
    else if(document.getElementById('search').style.display == '')
    document.getElementById('search').style.display = 'block';
    }
function show_form() {
    console.log(document.getElementById('machine').style.display);
    if(document.getElementById('machine').style.display == 'block')
    document.getElementById('machine').style.display = '';
    else if(document.getElementById('machine').style.display == '')
    document.getElementById('machine').style.display = 'block';
    }

