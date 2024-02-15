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
        let url = "/search/posts/"+query;
        // $.get(url, function(data, status){
        //     if(data.length){
        //         let elem = document.getElementById("news_search");
        //         data.forEach(function(item, index, array){
        //             let clone = tmpl.content.cloneNode(true);
        //                 let h5 = clone.querySelectorAll("h5");
        //                 h5[0].textContent = item['title'];
        //                 let a = clone.querySelectorAll("a");
        //                 a[0].href ='/news/'+item['slug'];
        //                 let p = clone.querySelectorAll("p");
        //                 p[0].textContent = item['created_at'];
        //                 let img = clone.querySelectorAll("img");
        //                 img[0].src = item['picture_url'];
        //                 elem.append(clone);
        //    });
        //     }
        // });
        // // получение от es данных по поиску о важной информации
//         url = "/search/importantinfo/"+query;
//         $.get(url, function(data, status){

//             if(data.length){
//                 let elem = document.getElementById("news_search");
//                 data.forEach(function(item, index, array){
// //                    console.log(data);
//                     let clone = tmpl.content.cloneNode(true);
//                         let h5 = clone.querySelectorAll("h5");
//                         h5[0].textContent = item['title'];
//                         let a = clone.querySelectorAll("a");
//                         a[0].href ='/news/'+item['slug'];
//                         let p = clone.querySelectorAll("p");
//                         p[0].textContent = item['created_at'];
//                         let img = clone.querySelectorAll("img");
//                         img[0].src = item['picture_url'];
//                         elem.append(clone);
//            });
//             }
//         });
        // получение от es данных по поиску о Техники
        url = "/search/machine/"+query;
        $.get(url, function(data, status){
         
            if(data.length){
                let elem = document.getElementById("news_search");
                data.forEach(function(item, index, array){
                    let clone = tmpl.content.cloneNode(true);
                        let h5 = clone.querySelectorAll("h5");
                        h5[0].textContent = item['name'];
                        let a = clone.querySelectorAll("a");
                        a[0].href ='/category/machine/'+item['slug'];
                        let p = clone.querySelectorAll("p");
                        p[0].textContent = item['created_at'];
                        let img = clone.querySelectorAll("img");
                        img[0].src = item['picture_url'];
                        elem.append(clone);
           });
            }
        });

        // получение от es данных по поиску о акциях
        url = "/search/akcii/"+query;
        $.get(url, function(data, status){
            
            if(data.length){
                let elem = document.getElementById("news_search");
                data.forEach(function(item, index, array){
                    let clone = tmpl.content.cloneNode(true);
                        let h5 = clone.querySelectorAll("h5");
                        h5[0].textContent = item['title'];
                        let a = clone.querySelectorAll("a");
                        a[0].href ='/akcii/'+item['slug'];
                        let p = clone.querySelectorAll("p");
                        p[0].textContent = item['created_at'];
                        let img = clone.querySelectorAll("img");
                        img[0].src = item['picture_url'];
                        elem.append(clone);
           });
            }
        });
        // получение от es данных по поиску о категориях акций
        url = "/search/akciicategories/"+query;
        $.get(url, function(data, status){
            
            if(data.length){
                let elem = document.getElementById("news_search");
                data.forEach(function(item, index, array){
                    let clone = tmpl.content.cloneNode(true);
                        let h5 = clone.querySelectorAll("h5");
                        h5[0].textContent = item['title'];
                        let a = clone.querySelectorAll("a");
                        a[0].href ='/akciicategories/'+item['slug'];
                        let p = clone.querySelectorAll("p");
                        p[0].textContent = item['created_at'];
                        let img = clone.querySelectorAll("img");
                        img[0].src = item['picture_url'];
                        elem.append(clone);
           });
            }
        });

        // получение от es данных по поиску о альбомах
        // url = "/search/albom/"+query;
        // $.get(url, function(data, status){
         
        //     if(data.length){
        //         let elem = document.getElementById("news_search");
        //         data.forEach(function(item, index, array){
        //             let clone = tmpl.content.cloneNode(true);
        //                 let h5 = clone.querySelectorAll("h5");
        //                 h5[0].textContent = item['name'];
        //                 let a = clone.querySelectorAll("a");
        //                 a[0].href ='/albom/'+item['slug'];
        //                 let p = clone.querySelectorAll("p");
        //                 p[0].textContent = item['date'];
        //                 let img = clone.querySelectorAll("img");
        //                 img[0].src = item['picture_url'];
        //                 elem.append(clone);
        //    });
        //     }
        // });

         // получение от es данных по поиску о Баннерах
         // url = "/search/banneraakcii/"+query;
         // $.get(url, function(data, status){
            
         //     if(data.length){
         //         let elem = document.getElementById("news_search");
         //         data.forEach(function(item, index, array){
         //             let clone = tmpl.content.cloneNode(true);
         //                 let h5 = clone.querySelectorAll("h5");
         //                 h5[0].textContent = item['title'];
         //                 let a = clone.querySelectorAll("a");
         //                 a[0].href ='/'+item['href'];
         //                 let img = clone.querySelectorAll("img");
         //                 img[0].src = item['picture_url'];
         //                 elem.append(clone);
         //    });
         //     }
         // });
        
         // получение от es данных по поиску о Категориях
         url = "/search/categories/"+query;
         $.get(url, function(data, status){
             
             if(data.length){
                 let elem = document.getElementById("news_search");
                 data.forEach(function(item, index, array){
                     let clone = tmpl.content.cloneNode(true);
                         let h5 = clone.querySelectorAll("h5");
                         h5[0].textContent = item['name'];
                         let a = clone.querySelectorAll("a");
                         a[0].href ='/category/'+item['slug'];
                         
                         let img = clone.querySelectorAll("img");
                         img[0].src = item['picture_url'];
                         elem.append(clone);
            });
             }
         });
        // // получение от es данных по поиску о Контенте страниц
        // url = "/search/pagecontent/"+query;
        // $.get(url, function(data, status){
            
        //     if(data.length){
        //         let elem = document.getElementById("news_search");
        //         data.forEach(function(item, index, array){
        //             let clone = tmpl.content.cloneNode(true);
        //                 let h5 = clone.querySelectorAll("h5");
        //                 h5[0].textContent = item['title'];
        //                 let a = clone.querySelectorAll("a");
        //                 if(item['href']){
        //                     a[0].href ='/'+item['href'];
        //                 }
        //                 else{
        //                     a[0].href ='/content/'+item['slug'];
        //                 }
                        
                        
        //                 let p = clone.querySelectorAll("p");
        //                 p[0].textContent = item['created_at'];
        //                 let img = clone.querySelectorAll("img");
        //                 img[0].src = item['picture_url'];
        //                 elem.append(clone);
        //    });
        //     }
        // });
    
       



    }
}


function get_full_text(el){
    el.children[0].hidden = true;
    el.children[1].hidden = false;
}

function get_short_text(el){
    el.children[0].hidden = false;
    el.children[1].hidden = true;
}
