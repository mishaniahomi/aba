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


function get_posts(query){
    if (query){
        // получение от es данных по поиску о новостях
        let url = "/search/posts/"+query;
        $.get(url, function(data, status){
            console.log(data);
            if(data['results'].length){
                let elem = document.getElementById("news_search");
                data['results'].forEach(function(item, index, array){
                    let clone = tmpl.content.cloneNode(true);
                        let h5 = clone.querySelectorAll("h5");
                        h5[0].textContent = item['title'];
                        let a = clone.querySelectorAll("a");
                        a[0].href ='/news/'+item['slug'];
                        let p = clone.querySelectorAll("p");
                        p[0].textContent = item['created_at'];
                        let img = clone.querySelectorAll("img");
                        img[0].src = item['picture_url'];
                        elem.append(clone);
           });
            }
        });
        // получение от es данных по поиску о важной информации
        url = "/search/importantinfo/"+query;
        $.get(url, function(data, status){
            console.log(data);
            if(data['results'].length){
                let elem = document.getElementById("important_news_search");
                data['results'].forEach(function(item, index, array){
                    let clone = tmpl.content.cloneNode(true);
                        let h5 = clone.querySelectorAll("h5");
                        h5[0].textContent = item['title'];
                        let a = clone.querySelectorAll("a");
                        a[0].href ='/news/'+item['slug'];
                        let p = clone.querySelectorAll("p");
                        p[0].textContent = item['created_at'];
                        let img = clone.querySelectorAll("img");
                        img[0].src = item['picture_url'];
                        elem.append(clone);
           });
            }
        });
        



    }
}
