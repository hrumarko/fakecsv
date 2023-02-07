add_column = document.querySelector('.add-column')
type = add_column.querySelector('#id_type')
var cols = document.querySelector('.cols')
order = 0 
Array.from(cols.children).forEach(function(col){
  order++
})
add_column.querySelector('#id_order').value = order


///////////////
type.addEventListener('click', function(){
  add_column = document.querySelector('.add-column')
  type = add_column.querySelector('#id_type')
  val = type.value
  a = add_column.querySelector('.body-from-to')
  if (val == 'Integer' | val == 'Text'){
    a.querySelector('#id_from_int').value = ''
    a.querySelector('#id_to_int').value = ''
    a.classList.remove("hide")
  }else{
    a.querySelector('#id_to_int').value = ''
   a.querySelector('#id_from_int').value = ''
    a.classList.add("hide")
  }
})


// check on start for from-to
val = type.value
a = add_column.querySelector('.body-from-to')
if (val == 'Integer' | val == 'Text'){
  a.classList.remove("hide")
  a.querySelector('#id_from_int').value = ''
    a.querySelector('#id_to_int').value = ''
}else{
  a.classList.add("hide")
  a.querySelector('#id_to_int').value = ''
  a.querySelector('#id_from_int').value = ''
}

Array.from(cols.children).forEach(function(col){
  type = col.querySelector('#id_type')
  val = type.value
  if (val == 'Integer' | val == 'Text'){
    col.querySelector('.body-from-to').classList.remove('hide')
  }
  
})


// show/hide from-to

Array.from(cols.children).forEach(function(c){
    console.log(c)
    c.querySelector("#id_type").addEventListener('click', function(){
      console.log("HELLLO")
      val = c.querySelector("#id_type").value
      a = c.querySelector('.body-from-to')
      if (val == 'Integer' | val == 'Text'){
        a.querySelector('#id_from_int').value = ''
        a.querySelector('#id_to_int').value = ''
        a.classList.remove("hide")
      }else{
        a.querySelector('#id_to_int').value = ''
        a.querySelector('#id_from_int').value = ''
        a.classList.add("hide")
      }
    })

})


//add column
button_add_column = add_column.querySelector('.btn-add-column')
button_add_column.addEventListener('click', function(){
  column = add_column.querySelector('.row')
  col = column.cloneNode(true);
  col.querySelector('#id_type').value = val
  cols.append(col)
  order++;
  add_column.querySelector('#id_order').value = order
  
  Array.from(cols.children).forEach(function(c){
    del_but = c.querySelector('.btn-outline-danger')
    del_but.addEventListener('click', function(){
      order = Array.from(cols.children).length
      add_column.querySelector('#id_order').value = order
      c.remove()

  })
    
  c.querySelector("#id_type").addEventListener('click', function(){
      console.log("HELLLO")
      val = c.querySelector("#id_type").value
      a = c.querySelector('.body-from-to')
      if (val == 'Integer' | val == 'Text'){
        a.querySelector('#id_from_int').value = ''
        a.querySelector('#id_to_int').value = ''
        a.classList.remove("hide")
      }else{
        a.querySelector('#id_to_int').value = ''
        a.querySelector('#id_from_int').value = ''
        a.classList.add("hide")
      }
    })
})
})


//send columns to server 
btn_subimt = document.querySelector('.submit') 
btn_subimt.addEventListener('click', function(){
  schema = {
    name: document.querySelector('#id_name').value,
    column_separator: document.querySelector('#id_column_separator').value,
    string_character: document.querySelector('#id_string_character').value,
  }

  dct_cols = {}
  let i = 0
  cols = document.querySelector('.cols')
  cols = Array.from(cols.children)
  cols.forEach(function(col){
    dct_cols['column'+ i] = {
      column_name: col.querySelector('#id_name_column').value,
      type: col.querySelector('#id_type').value,
      from_int: col.querySelector('#id_from_int').value,
      to_int: col.querySelector('#id_to_int').value,
      order: col.querySelector('#id_order').value,
    }
    i++;
  })

  schema['cols'] = dct_cols
  try{
      pk = document.location.pathname.match(/\d/g).join("")
      schema['pk'] = pk
      json_schema = JSON.stringify(schema) 
      $.post("http://127.0.0.1:8000/create-schema/",
        {
          "csrfmiddlewaretoken": getCookie("csrftoken"),
          json_schema,
        },
        console.log(json_schema)
      );
      window.location.replace("/data-schemas/");
  }catch{
    console.log('hello')
    json_schema = JSON.stringify(schema) 
    $.post("create-schema/",
      {
        "csrfmiddlewaretoken": getCookie("csrftoken"),
        json_schema,
      },
      console.log(json_schema)
    );
    window.location.replace("/data-schemas/");
  }
  
})


function getCookie(name) {
    // get csrftoken
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


//button "Generate data"
gen_data = document.querySelector('.gen-data')
gen_data.addEventListener('click', function(){
  console.log('hello ebat')
})
