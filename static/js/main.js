function show_form_search() {
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
 function prevSlide(obj) {
      $(obj).carousel('prev');
  }

  function nextSlide(obj) {
      $(obj).carousel('next');
  }


function activate_photo(id) {
    console.log(id);
    element = document.getElementById(id);
    const elements = document.querySelectorAll('.big_photo');
    elements.forEach(element => {
      element.classList.remove('active');
    });
    element.classList.add('active');
}
